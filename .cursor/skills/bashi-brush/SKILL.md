---
name: bashi-brush
description: >-
  Builds a Bass brushing (巴氏刷牙法) explainer in Blender 5.2: a normal 14+14
  permanent arch whose every tooth is a photo card of the chubby character
  the human supplies, with Q-elastic squash and Chinese step captions.
  Use when the human names 巴氏刷牙, 巴氏刷牙法, Bass brushing, 刷牙讲解,
  肥嘟嘟, 牙齿必须一模一样, or asks to rebuild that Blender walkthrough.
---

# Bass brush walkthrough

Teeth are the **reference photo**, one card per tooth, always facing the camera. Not metaballs. Not a sculpt.

Output stays in `tmp/bashi-brush/`. Do not commit png, blend, or mp4. Stamp TTL after a render.

Blender on this machine: `D:\Program Files\Blender Foundation\Blender 5.2\blender.exe` (5.2.2 LTS).

## Pipeline

```
- [ ] Human supplied the character still (white background)
- [ ] cutout.py wrote tmp/bashi-brush/roo.png (leftover_white is only eye whites)
- [ ] walkthrough.py stills: arch shows the whole character, angle shows bristles on the head
- [ ] --anim only after those stills
- [ ] python cron/janitor.py --touch
```

```
python .cursor/skills/bashi-brush/scripts/cutout.py --src <photo>
& "D:\Program Files\Blender Foundation\Blender 5.2\blender.exe" --background --factory-startup --python ".cursor/skills/bashi-brush/scripts/walkthrough.py"
& "D:\Program Files\Blender Foundation\Blender 5.2\blender.exe" --background --factory-startup --python ".cursor/skills/bashi-brush/scripts/walkthrough.py" -- --anim
python cron/janitor.py --touch
```

Preview stills land in `tmp/bashi-brush/renders/walk_arch.png` and `walk_angle.png`. The film is `tmp/bashi-brush/renders/bashi-walkthrough.mp4` (~2:32, 3648 frames, ~20 min).

## What the film does

14 upper + 14 lower, no wisdom teeth. Upper arch slightly wider. Steps: 45° into the sulcus, short horizontal vibration (2–3 teeth), roll toward the crown, upper buccal, upper palatal (anterior vertical), lower buccal, lower lingual (anterior vertical), upper occlusal, lower occlusal. Chinese captions, one block at a time.

Q-elastic is a per-tooth spring on the card root's scale, not a soft-body sim.

## Hard

- Likeness is the photo. Cards billboard to the camera (`TRACK_Z`, `UP_Y`). A side-on shard is a failed tooth.
- Cutout floods from the image border at RGB > 230. Do not threshold the whole image or the eye whites disappear. Do not blur the mask. Cleared pixels are `(0,0,0,0)`.
- Card material is Emission mixed by the image alpha, `surface_render_method = BLENDED`. `DITHERED` punches holes.
- Shift each card toward the bite so the gum tube sits above the ears. Bristle tips meet the head, not the gum cylinder.
- Occlusal cameras stay in the open mouth, in front of the arches. Floor is `z = -3.15`. A camera under the floor is a teal frame. A camera inside the palate is a burgundy frame.
- Caption `hide_render` is keyed at frame 1, `f0`, `f1`, and `f1+1`, then CONSTANT. A key only inside the step leaves the last line up forever.
- Set `image_settings.media_type = VIDEO` before `file_format = FFMPEG`.
- `build_scene.py` is the helper (brush, spring, aim). Its `main()` still builds the rejected metaball heads. Do not render that as the deliverable.
- Do not `GenerateImage` a stand-in character. Use the still the human attached.
- MEDIA stays in `tmp/`. The human may delete that folder after watching; the skill is the archive.

Blender 5.2 traps and the arch numbers: [reference.md](reference.md).
