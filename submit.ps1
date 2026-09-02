<#
.SYNOPSIS
  Commit the working tree onto develop without PII, then open a PR to main.

.DESCRIPTION
  Staging respects .gitignore: tmp/ (except ttl.toon.md), .private, identity,
  lebenslauf, training logs, generated media, and calendar.ics stay local.
  Defense-in-depth unstages those paths if they appear in the index.

.PARAMETER Message
  Commit message. Required when there is something to commit.

.PARAMETER SkipPr
  Commit and push only. Do not create or print a pull request.

.PARAMETER DryRun
  Show branch and files that would be staged. Do not commit or push.

.EXAMPLE
  .\submit.ps1 -Message "Add schedule-view week PNGs to the harvest loop."
#>
[CmdletBinding()]
param(
    [string]$Message = "",
    [switch]$SkipPr,
    [switch]$DryRun
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Invoke-Git {
    param([Parameter(Mandatory = $true)][string[]]$GitArgs)
    & git @GitArgs
    if ($LASTEXITCODE -ne 0) {
        throw "git $($GitArgs -join ' ') failed with exit $LASTEXITCODE"
    }
}

function Convert-GitPath([string]$Path) {
    return ($Path -replace "\\", "/")
}

function Test-ForbiddenPath([string]$Path) {
    $n = Convert-GitPath $Path
    if ($n -eq "tmp/ttl.toon.md") { return $false }
    if ($n -like "self/identity/*") { return $true }
    if ($n -like "self/lebenslauf*") { return $true }
    if ($n -eq "self/training.toon.md") { return $true }
    if ($n -like ".private/*" -or $n -eq ".private") { return $true }
    if ($n -like "tmp/*") { return $true }
    if ($n -like "videos/*") { return $true }
    if ($n -eq "schedule/calendar.ics") { return $true }
    if ($n -like "*.pdf") { return $true }
    return $false
}

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $root

Invoke-Git @("fetch", "origin")

$current = (git branch --show-current).Trim()
if ($current -ne "develop") {
    git show-ref --verify --quiet refs/heads/develop | Out-Null
    if ($LASTEXITCODE -eq 0) {
        Invoke-Git @("checkout", "develop")
    }
    else {
        Invoke-Git @("checkout", "-b", "develop", "origin/develop")
    }
}

if ($DryRun) {
    git add -An
    git status --short
    Write-Host "Dry run. No commit, no push."
    exit 0
}

Invoke-Git @("add", "-A")

$staged = @(git diff --cached --name-only)
$forbidden = @($staged | Where-Object { Test-ForbiddenPath $_ })
if ($forbidden.Count -gt 0) {
    foreach ($path in $forbidden) {
        git reset -q HEAD -- $path
        Write-Warning "Unstaged PII or generated path: $path"
    }
    $staged = @(git diff --cached --name-only)
}

if ($staged.Count -eq 0) {
    Write-Host "Nothing to commit after PII filter."
}
else {
    if (-not $Message) {
        throw "Commit needs -Message. Example: .\submit.ps1 -Message 'Harvest Berlin AI events into schedule/.'"
    }
    Invoke-Git @("commit", "-m", $Message)
}

Invoke-Git @("push", "-u", "origin", "HEAD")

if ($SkipPr) {
    exit 0
}

$existing = gh pr view --json url --jq .url 2>$null
if ($LASTEXITCODE -eq 0 -and $existing) {
    Write-Host $existing
    exit 0
}

gh pr create --base main --head develop --title "Fu-language OS: ontology, study loop, and cron gatherers" --body @"
## Summary
- Personal operating system in Fu-language (``ROOT.md``, ``CPU.md``) with a Gremlin-lite ontology under ``pedagogy/``.
- Cron gatherers for study, interview titles, inflow news, schedule harvest, and janitor/TTL.
- Identity, CV, health logs, ``tmp/`` renders, and ``.private`` stay gitignored.

## Test plan
- [ ] ``python cron/janitor.py --dry-run`` does not list ``submit.ps1``
- [ ] ``.\submit.ps1 -DryRun`` does not stage ``self/identity/`` or ``tmp/`` siblings
"@
if ($LASTEXITCODE -ne 0) {
    throw "gh pr create failed with exit $LASTEXITCODE"
}
