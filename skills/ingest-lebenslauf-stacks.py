#!/usr/bin/env python3
"""Ingest attested lebenslauf stacks into pedagogy/universe.graph.md.

Only names from self/identity/skill.toon.md and experience claims.
Does not invent Kafka or other unsourced tools.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GRAPH = ROOT / "pedagogy" / "universe.graph.md"
BODY_DIR = ROOT / "pedagogy" / "computation" / "stack"
SRC = "self/identity/skill.toon.md"
EXP = "self/identity/experience.toon.md"

# id, gloss, edges[(LABEL, target)], extra claim or None, extra source or None
STACKS: list[tuple[str, str, list[tuple[str, str]], str | None, str | None]] = [
    ("JavaScript", "language-of-the-web-runtime", [("APPLIES", "Computation")], "Implied via React in the skill family. Not a separate cert.", None),
    ("TypeScript", "javascript-plus-types", [("APPLIES", "TypeSystem"), ("INFORMS", "JavaScript")], "Role line: Next.js · TypeScript · KI.", "self/lebenslauf.toon.md"),
    ("GoLang", "compiled-language-for-servers", [("APPLIES", "Computation")], "Attested at RITS with Fiber.", EXP),
    ("Python", "language-for-scripts-and-models", [("APPLIES", "Computation")], None, None),
    ("Java", "language-of-the-jvm", [("APPLIES", "Computation")], None, None),
    ("NodeJS", "javascript-on-the-server", [("APPLIES", "JavaScript"), ("APPLIES", "Computation")], None, None),
    ("React", "component-ui-on-javascript", [("APPLIES", "JavaScript")], None, None),
    ("NextJS", "react-with-server-routes", [("APPLIES", "React")], "Role line names Next.js.", "self/lebenslauf.toon.md"),
    ("Vue", "component-ui-on-javascript", [("APPLIES", "JavaScript")], "Attested at MORIMATSU with MES.", EXP),
    ("TailwindCSS", "utility-css-for-layout", [("APPLIES", "Computation")], None, None),
    ("Redux", "ui-state-as-a-store", [("APPLIES", "React")], None, None),
    ("Figma", "drawing-of-interface-form", [("APPLIES", "SpatialGraphics")], "Attested at Avature UX.", EXP),
    ("MicroFrontend", "ui-split-across-deployable-parts", [("APPLIES", "Computation")], None, None),
    ("SpringBoot", "java-server-framework", [("APPLIES", "Java")], None, None),
    ("FastAPI", "python-http-framework", [("APPLIES", "Python")], "Attested GIS-Chat FastAPI at RITS.", EXP),
    ("NestJS", "node-server-framework", [("APPLIES", "NodeJS")], None, None),
    ("REST", "http-as-resource-verbs", [("APPLIES", "Computation")], None, None),
    ("WebSocket", "bidirectional-bytes-over-http", [("APPLIES", "Computation")], None, None),
    ("Redis", "in-memory-store", [("APPLIES", "Computation")], None, None),
    ("Redisson", "java-client-for-redis", [("APPLIES", "Redis"), ("APPLIES", "Java")], None, None),
    ("GoFiber", "go-http-framework", [("APPLIES", "GoLang")], "Attested at RITS.", EXP),
    ("PostgreSQL", "relational-store", [("APPLIES", "Computation")], None, None),
    ("MongoDB", "document-store", [("APPLIES", "Computation")], "Attested at Legrand SLEC.", EXP),
    ("MySQL", "relational-store", [("APPLIES", "Computation")], None, None),
    ("Supabase", "postgres-as-a-backend", [("APPLIES", "PostgreSQL")], None, None),
    ("DynamoDB", "managed-key-value-store", [("APPLIES", "AWS")], None, None),
    ("PostGIS", "geometry-inside-postgres", [("APPLIES", "PostgreSQL"), ("APPLIES", "GeographicInformation")], "Attested 15+ layers at RITS.", EXP),
    ("AWS", "amazon-cloud-as-one-computer", [("APPLIES", "CloudRuntime")], "Developer Associate Nov 2021. SysOps Associate Sep 2022.", "self/identity/credential.toon.md"),
    ("Azure", "microsoft-cloud-as-one-computer", [("APPLIES", "CloudRuntime")], None, None),
    ("ECS", "aws-container-service", [("APPLIES", "AWS"), ("APPLIES", "Docker")], "Fictio / NovelMonkey.", EXP),
    ("EKS", "aws-managed-kubernetes", [("APPLIES", "AWS"), ("APPLIES", "Kubernetes")], "Fictio / NovelMonkey.", EXP),
    ("Fargate", "aws-serverless-containers", [("APPLIES", "AWS"), ("APPLIES", "ECS")], "Fictio / NovelMonkey.", EXP),
    ("Bedrock", "aws-hosted-models", [("APPLIES", "AWS"), ("INFORMS", "Agent")], "Fictio / NovelMonkey.", EXP),
    ("SQS", "aws-queue", [("APPLIES", "AWS")], "Fictio / NovelMonkey. Kafka is not in the skill toon. Do not add Kafka until sourced.", EXP),
    ("CDK", "aws-infra-as-typescript", [("APPLIES", "AWS"), ("APPLIES", "TypeScript")], "Fictio / NovelMonkey.", EXP),
    ("CloudFormation", "aws-infra-as-templates", [("APPLIES", "AWS")], None, None),
    ("MapLibre", "vector-maps-in-the-browser", [("APPLIES", "GeographicInformation"), ("APPLIES", "WebGL")], "Attested at RITS.", EXP),
    ("DeckGL", "gpu-layers-on-a-map", [("APPLIES", "GeographicInformation"), ("APPLIES", "WebGL")], "Attested at RITS.", EXP),
    ("GeoJSON", "place-as-json", [("APPLIES", "GeographicInformation"), ("APPLIES", "JavaScript")], None, None),
    ("MCP", "tool-protocol-for-models", [("INFORMS", "Agent"), ("APPLIES", "GeographicInformation")], "GIS-Chat MCP at RITS. Also in the AI family.", EXP),
    ("OSM", "open-street-map-as-place-data", [("APPLIES", "GeographicInformation")], "Attested layer source at RITS.", EXP),
    ("ALKIS", "german-cadastre-as-place-data", [("APPLIES", "GeographicInformation")], "Attested layer source at RITS.", EXP),
    ("MaStR", "german-energy-register-as-place-data", [("APPLIES", "GeographicInformation")], "Attested layer source at RITS.", EXP),
    ("BKG", "german-geodata-authority-feeds", [("APPLIES", "GeographicInformation")], "Attested layer source at RITS.", EXP),
    ("LargeLanguageModel", "learned-weights-as-a-reasoner", [("INFORMS", "Agent"), ("APPLIES", "Computation")], "Skill family OpenAI/LLM.", None),
    ("Kiro", "aws-agent-ide", [("APPLIES", "AWS"), ("PARTICIPATES", "CursorSkill")], "Named with Cursor / Claude Code on worldquant-miner evidence.", None),
    ("ClaudeCode", "cli-agent", [("PARTICIPATES", "AgentLoop")], "Named with Cursor / Kiro on worldquant-miner evidence.", None),
    ("SemanticKernel", "orchestration-sdk-for-models", [("INFORMS", "Agent"), ("APPLIES", "Computation")], None, None),
    ("ThreeJS", "scene-graph-in-the-browser", [("APPLIES", "WebGL"), ("APPLIES", "SpatialGraphics")], "MORIMATSU and Inkdeeps.", EXP),
    ("D3", "data-as-svg", [("APPLIES", "SpatialGraphics"), ("APPLIES", "JavaScript")], "MORIMATSU MES.", EXP),
    ("BIMFACE", "building-mesh-in-the-browser", [("APPLIES", "SpatialGraphics")], "MORIMATSU mesh compression LOD.", EXP),
    ("WebGL", "gpu-in-the-browser", [("APPLIES", "SpatialGraphics")], "Inkdeeps Unity WebGL.", EXP),
    ("Unity", "realtime-3d-engine", [("APPLIES", "SpatialGraphics")], "Inkdeeps virtual exhibition.", EXP),
    ("Docker", "process-plus-filesystem-as-an-image", [("APPLIES", "Computation")], None, None),
    ("Kubernetes", "schedule-of-containers", [("APPLIES", "Docker")], None, None),
    ("GitHubCI", "tests-on-git-push", [("APPLIES", "Computation")], None, None),
    ("Playwright", "browser-as-a-test", [("APPLIES", "Computation")], None, None),
    ("Sentry", "runtime-error-as-a-feed", [("APPLIES", "Computation")], None, None),
    ("LabVIEW", "graphical-automation", [("APPLIES", "Computation")], "Legrand SLEC with Node.js MongoDB.", EXP),
    ("MetaTrader", "retail-trade-runtime", [("APPLIES", "Computation")], "WorldQuant MT5. profitable-expert-advisor. No invented profit metric.", "self/identity/project.toon.md"),
    ("Bandit", "explore-or-exploit-allocation", [("APPLIES", "SearchHarness"), ("GROUNDS_IN", "Mathematics")], "worldquant-miner.", "self/identity/project.toon.md"),
    ("GeneticSearch", "search-by-variation-and-select", [("APPLIES", "SearchHarness"), ("GROUNDS_IN", "Mathematics")], "worldquant-miner.", "self/identity/project.toon.md"),
    ("AST", "program-as-a-tree", [("STUDIES", "Form"), ("APPLIES", "TypeSystem")], "worldquant-miner AST harness.", "self/identity/project.toon.md"),
    ("InAppPurchase", "payment-inside-a-phone-app", [("APPLIES", "MobileRuntime"), ("APPLIES", "Payment")], "Skill family mobile.", None),
    ("AzureCosmosGremlin", "hosted-property-graph", [("APPLIES", "Azure"), ("APPLIES", "GraphTraversal")], "Skill family Azure CosmosDB Gremlin.", None),
]


def body_text(vid: str, gloss: str, claim: str | None, extra_src: str | None) -> str:
    lines = [
        f"- VERTEX {vid}",
        "- KIND techne",
        f"- GLOSS {gloss}",
        "- STORE PATH pedagogy/universe.graph.md",
        f"- CLAIM Attested in {SRC}. Particular job stays in self/identity/experience.toon.md.",
    ]
    if claim:
        lines.append(f"- CLAIM {claim}")
    lines.append(f"- SOURCE {SRC}")
    if extra_src and extra_src != SRC:
        lines.append(f"- SOURCE {extra_src}")
    return "\n".join(lines) + "\n"


def v_line(vid: str, gloss: str) -> str:
    body = f"pedagogy/computation/stack/{vid}.fu.md"
    return f"V {vid:<22} kind=techne gloss={gloss} body={body}"


def e_line(src: str, label: str, dst: str, extra_src: str | None) -> str:
    source = extra_src or SRC
    return f"E {src:<22} {label:<12} {dst} SOURCE={source}"


def main() -> None:
    BODY_DIR.mkdir(parents=True, exist_ok=True)
    text = GRAPH.read_text(encoding="utf-8")
    existing = {line.split()[1] for line in text.splitlines() if line.startswith("V ")}
    v_add: list[str] = []
    e_add: list[str] = []
    for vid, gloss, edges, claim, extra_src in STACKS:
        (BODY_DIR / f"{vid}.fu.md").write_text(
            body_text(vid, gloss, claim, extra_src), encoding="utf-8"
        )
        if vid not in existing:
            v_add.append(v_line(vid, gloss))
        for label, dst in edges:
            e_add.append(e_line(vid, label, dst, extra_src))
    if "V JavaScript" not in text:
        # insert new V before first E
        first_e = text.index("\nE ")
        text = text[:first_e] + "\n" + "\n".join(v_add) + "\n" + text[first_e:]
    marker = "E SlashCommand         PARTICIPATES CursorSkill SOURCE=mezzanine/cursor-slash.toon.md\n"
    if marker in text and "E JavaScript" not in text:
        text = text.replace(marker, marker + "\n" + "\n".join(e_add) + "\n")
    elif "E JavaScript" not in text:
        text = text.rstrip() + "\n\n" + "\n".join(e_add) + "\n"
    GRAPH.write_text(text, encoding="utf-8")
    print(f"bodies={len(STACKS)} newV={len(v_add)} newE={len(e_add)}")


if __name__ == "__main__":
    main()
