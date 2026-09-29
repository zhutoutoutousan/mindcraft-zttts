# MinSec · zero-to-operator curriculum

source: https://github.com/cgx9/minsec
kind: product + infosec vocabulary · not a paper
deliverables: tmp/minsec-ladder/tree.html · tmp/minsec-ladder/tree.puml
paradigm_skill: .cursor/skills/paper-muscle/
hub: SecretSurface
updated: 2026-09-14

## Why this ladder
The human named unfamiliarity with the whole Gebiet (ZK slogans, wrangler login, spawn vs kernel, leftover .env, agent TTY). Graph already had fragments. This file is the **order** to walk them: shallow workspace leak → process env → the CLI → crypto words you must not mix → Cloudflare credentials → rotate vs leftover.

Do not invent ANSWER. Grasp unknown until the human writes under PROBE.

## Ladder (six rungs)

1. EnvFile + SecretSurface — where a secret can sit before any crypto
2. ProcessEnvironment + SpawnEnv + JavaProcessEnv + AgentTty — disk vs RAM vs model context
3. MinSec + MinSecBinding — VARIABLE vs SECRET, `minsec run`, three filenames
4. HonestButCurious + ClientHeldSecret + ZeroKnowledgeProof + EnvelopeEncryption + AuthenticatedEncryption — slogans vs GMR
5. ApiToken + OAuthAuthorization + Wrangler + CloudflareWorkers + WorkerBinding — three different credentials
6. SecretRotation + leftover EnvFile + leftover AgentTty — rotate ≠ revoke ≠ leftover

## Bounds (what this ladder is not)
- Not a crypto audit of MinSec nonces
- Not a completed `wrangler login` or `npm i -g`
- Not permission to paste live tokens, `.env`, or `minsec list` output into chat
- License remains Non-Commercial; commercial use needs the author

## Graph walk
g.V(SecretSurface).out()
g.V(MinSec).out()
g.V(ClientHeldSecret).out()
g.V(EnvFile).out()
g.V(ProcessEnvironment).out()
g.V(ApiToken).out()

## Agent
pedagogy-cpu AGENT $id=minsec-ladder — one PROBE per unfinished rung; wait ANSWER; do not lecture all six; fog ≤1 rung; do not paste secrets.
