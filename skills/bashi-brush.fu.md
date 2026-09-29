# SKILL bashi-brush

TESTED satisfied 2026-09-29. Human accepted the photo-card walkthrough, then asked to archive the skill and delete the media.

## Contract

- Bass brushing explainer in Blender 5.2. Normal 14+14 arch. Every tooth is a camera-facing card of the character still the human supplies. Q-elastic is a scale spring.
- Distinct from metaball heads. `build_scene.py` `main()` is the rejected short demo. Deliverable is `walkthrough.py`.
- Cutout floods white from the border only (threshold 230). Eye whites stay.
- Preview `walk_arch.png` and `walk_angle.png` before `--anim` (~20 min, 3648 frames, ~2:32).
- MEDIA stays in `tmp/bashi-brush/`. Do not commit png, blend, or mp4. Human may delete that folder; the skill is the archive.

## Commands

```powershell
python .cursor/skills/bashi-brush/scripts/cutout.py --src <photo>
& "D:\Program Files\Blender Foundation\Blender 5.2\blender.exe" --background --factory-startup --python ".cursor/skills/bashi-brush/scripts/walkthrough.py"
& "D:\Program Files\Blender Foundation\Blender 5.2\blender.exe" --background --factory-startup --python ".cursor/skills/bashi-brush/scripts/walkthrough.py" -- --anim
python cron/janitor.py --touch
```

OUTPUT tmp/bashi-brush/renders/bashi-walkthrough.mp4
HARD: missing `roo.png` → stop and run cutout. Do not GenerateImage a stand-in.

## Explain card (human)

When the human asks 怎么弄 / how this skill works: read `.cursor/skills/bashi-brush/SKILL.md`. Numbers and the failed stills: `.cursor/skills/bashi-brush/reference.md`.
