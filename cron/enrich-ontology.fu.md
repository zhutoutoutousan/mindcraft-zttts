- RECURRING on RESEARCH or DUMP or LEARNING_DUMP in CPU.md
- STORE PATH pedagogy/universe.graph.md
- STORE PATH pedagogy/ontology.fu.md

- AGENT $id=ontology-enrich $input=CPU.md $output=pedagogy/universe.graph.md $prompt=Scan RESEARCH DUMP LEARNING_DUMP in CPU.md and STUDY in pedagogy/pedagogy-cpu.fu.md and self/lebenslauf.toon.md self/training.toon.md. Add V and E to pedagogy/universe.graph.md. Every new E needs SOURCE=. Use only ROOT edge labels. Prefer attaching under Mathematics Physics Biology Computation Agent Language. Never delete Being Essence Form Matter. If two claims fight, add CONTRADICTS instead of overwrite. Write pedagogy/<branch>/<id>.fu.md with CLAIM MEDIA SOURCE. MEDIA is URL only, never bytes. Lebenslauf and training become domain vertices, never Person. After enrich, leave a STUDY stub with empty GAP on pedagogy-cpu.fu.md so internalization can start.

- AGENT $id=ontology-challenge $input=pedagogy/universe.graph.md $output=pedagogy/universe.graph.md $when=after ontology-enrich $prompt=Walk g.V().out(). If an edge has no SOURCE and is not in the seed set Being Essence Form Matter Mathematics Physics Computation Agent Language Pedagogy, mark it TODO or drop it.
