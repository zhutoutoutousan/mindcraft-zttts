# Bass brush reference

Read this when a still is wrong. The happy path is in SKILL.md.

## Arch

`walkthrough.py` constants that matched the photo cards:

- Upper: `half_w=7.15`, `depth=5.85`, `front_y=-1.05`, `z=1.35`
- Lower: `half_w=6.55`, `depth=5.25`, `front_y=-0.42`, `z=-1.35`
- Kinds, viewer's left to right: M2 M1 PM2 PM1 C LI CI | CI LI C PM1 PM2 M1 M2
- `s=0` is viewer-left / patient-right posterior. Front of the arch is −Y.
- Card about `1.37 × 1.02`. Child location `(0, 0, -0.42 * gum_sign)` with `gum_sign` +1 upper, −1 lower, so the body hangs into the bite.
- Gum tubes: outer `z_off=0.55 * sign`, lateral `0.05`, bevel `0.18`. Inner bevel `0.14`. Jaw bevel `0.32` upper / `0.40` lower at `z_off=0.95 * sign`.

## Brush

Local +X is head width along the arch, +Z is the handle, −Z is the bristles. `aim_euler` builds that rotation.

Buccal tip sits just outside the arch and crown-ward of the arch point (`out * 0.22 + crown * 0.20`) so the cones land on the forehead. Occlusal tips are about `0.72` toward the bite from the arch point. A tip near `±0.92` floated in the gap; a tip near `±0.48` sat in the belly when the cards were shorter.

## Camera

- Hero: `(-6.4, -16.5, 2.6)`, lens 28, look `(0, 0.8, 0)`
- Buccal: `focus + out * 3.1 + (0.5, -7.0, 1.15)` lens 38 (lower z offset `0.85`)
- Lingual: `focus + (0.15, -6.6, small z)` lens 42
- Upper occlusal: `(focus.x * 0.25, focus.y - 5.2, 0.05)` looking slightly down, lens 34
- Lower occlusal: `(focus.x * 0.25, focus.y - 5.0, 0.72)` looking slightly up, lens 34

## Render

EEVEE, AgX, 1280×720, TAA 16. About 0.3 s/frame. Keying the 3648-frame timeline is ~35 s and happens before either stills or `--anim`.

FFMPEG: MPEG4 / H264 / CRF MEDIUM / preset GOOD / audio NONE. PNG stills flip `media_type` to `IMAGE` and restore `VIDEO`.

Font: `C:\Windows\Fonts\msyh.ttc`. Caption object is parented to the camera at local `(0, -0.70, -3.35)`, size `0.125`.

## Cutout

Border flood, 8-connected, channels all above 230. Crop to the opaque box. A Gaussian-blurred mask plus `DITHERED` alpha made noisy holes. A threshold of 250 left a white rectangle (~14k near-white opaque samples). Interior eye whites are not connected to the border, so they survive 230.

Shader: TexImage → Emission strength 1.15; MixShader Fac = Alpha; input 1 Transparent, input 2 Emission. `use_backface_culling = True`. Plane child has no extra X rotation once the Track To constraint faces the camera. `visible_shadow = False`.

## Q-elastic

Critically springy scale on the root: pressed teeth widen in X and squash in Z, with a small X tilt. Influence radius about `0.72–1.85` so two or three neighbors move. Billboard constraint overrides the child's rotation; the squash still reads because it is on the parent scale.
