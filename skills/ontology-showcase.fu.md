- STORE PATH pedagogy/universe.graph.md
- STORE PATH pedagogy/ontology.fu.md
- STORE PATH tmp/ttl.toon.md
- RUN python skills/ontology-showcase.py
- TMP PATH tmp/_work/showcase
- OUTPUT PATH tmp/pedagogy/universe.png
- OUTPUT PATH tmp/pedagogy/universe.stack.png
- OUTPUT PATH tmp/pedagogy/universe.html
- OUTPUT PATH tmp/pedagogy/universe.mp4

- ASK on deliver
  - If $output unset, ASK image or video. Do not render both unless the human says both.
  - Default image. Image is three files: core PNG, stack-family PNG, pan-zoom HTML. Video is the core tree only.

- AGENT $id=ontology-showcase-image $input=pedagogy/universe.graph.md $output=tmp/pedagogy/universe.png $prompt=python skills/ontology-showcase.py --mode image --deliver. Core PNG uses networkx multipartite so nodes do not share a cell. Stack tools go to labeled family panels. Full graph is tmp/pedagogy/universe.html. Delete tmp/_work/showcase after deliver. python cron/janitor.py --touch.

- AGENT $id=ontology-showcase-video $input=pedagogy/universe.graph.md $output=tmp/pedagogy/universe.mp4 $prompt=python skills/ontology-showcase.py --mode video --deliver. Layer reveal stills then ffmpeg. After mp4 exists, delete tmp/_work/showcase. Keep tmp/pedagogy/universe.mp4 until TTL. python cron/janitor.py --touch.

- AGENT $id=ontology-viz-puml $input=pedagogy/universe.graph.md $output=tmp/pedagogy/universe.puml $prompt=Compile V/E into PlantUML. Dark bg #0a0e14. Arrows #69f0ae. Group by kind. Alias of showcase for text puml only. No tmp PNG unless --deliver image.

- AGENT $id=ontology-viz-gremlin $input=pedagogy/universe.graph.md $when=user asks traversal $prompt=Answer with gremlin-lite only: g.V(id).out(LABEL) style. Compact. No essay.

- RULE never write Nature figure bytes. MEDIA stays URL on vertex bodies.
- RULE deliverable PNG html or mp4 lives in tmp/pedagogy/. It is a render, not a claim. pedagogy/universe.graph.md stays.
- RULE delete _work after the delivered file is on disk and readable. If deliver failed, keep _work for debug.
- RULE janitor --ttl deletes tmp siblings 5 days after last_run. Do not KEEP these renders in pedagogy/.
