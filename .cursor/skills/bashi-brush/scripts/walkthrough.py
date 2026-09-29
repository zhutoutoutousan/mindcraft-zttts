# 巴氏刷牙法全量解说 · 正常恒牙列
# 上颌 14 + 下颌 14（不含智齿），上颌稍宽，轻张口。
# 步骤：45° → 短颤 → 拂刷 → 上颊 → 上腭（前牙竖刷）→ 下颊 → 下舌 → 咬合面。
#
# 预览关键帧（先出静帧，再决定要不要出片）:
#   blender --background --factory-startup --python .cursor/skills/bashi-brush/scripts/walkthrough.py
# 出片（约 2 分 30 秒，约 20 分钟）:
#   同上，末尾加 -- --anim
# 输出在 tmp/bashi-brush/，不写到技能目录。

import math
import os
import sys

import bpy
from mathutils import Vector

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
import build_scene as B

REPO = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", "..", ".."))
ROOT = os.path.join(REPO, "tmp", "bashi-brush")
RENDER_DIR = os.path.join(ROOT, "renders")
BLEND_PATH = os.path.join(ROOT, "bashi-walkthrough.blend")
MP4_PATH = os.path.join(RENDER_DIR, "bashi-walkthrough.mp4")
os.makedirs(RENDER_DIR, exist_ok=True)

FPS = 24
UPPER = dict(half_w=7.15, depth=5.85, front_y=-1.05, z=1.35, name="upper")
LOWER = dict(half_w=6.55, depth=5.25, front_y=-0.42, z=-1.35, name="lower")
KINDS = ["M2", "M1", "PM2", "PM1", "C", "LI", "CI", "CI", "LI", "C", "PM1", "PM2", "M1", "M2"]
KIND_SCALE = {"M2": 0.96, "M1": 1.06, "PM2": 0.84, "PM1": 0.82, "C": 0.90, "LI": 0.72, "CI": 0.78}
BASE_SCALE = 0.56

# seconds. Total ~150s ≈ 2:30
STEPS = [
    ("title", 6.0, "巴氏刷牙法\n软毛小刷头 · 轻张口", "park", "upper", "hero"),
    ("arch", 7.0, "正常牙列\n上下各 14 颗 · 上颌稍宽", "park", "upper", "orbit"),
    ("angle", 9.0, "第1步  刷毛对准龈沟\n与牙长轴约成 45°", "hold", "upper", "buccal"),
    ("vib", 11.0, "第2步  水平短距离颤动\n每次 2 到 3 颗 · 约 10 次", "vib", "upper", "buccal"),
    ("sweep", 8.0, "第3步  颤动后再向牙冠拂刷", "sweep", "upper", "buccal"),
    ("ub", 22.0, "第4步  上颌颊侧\n从一侧后牙刷到另一侧", "travel", "upper", "buccal"),
    ("up", 20.0, "第5步  上颌腭侧\n前牙改为竖刷", "travel", "upper", "lingual"),
    ("lb", 18.0, "第6步  下颌颊侧\n刷毛改指向下牙龈", "travel", "lower", "buccal"),
    ("ll", 18.0, "第7步  下颌舌侧\n前牙用刷头前部竖刷", "travel", "lower", "lingual"),
    ("uo", 13.0, "第8步  上颌咬合面\n来回轻刷", "occlusal", "upper", "occlusal"),
    ("lo", 12.0, "第9步  下颌咬合面\n来回轻刷", "occlusal", "lower", "occlusal"),
    ("end", 8.0, "每区重叠着刷 · 力度要轻\n刷毛进入龈沟就可以", "park", "upper", "hero"),
]

argv = sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else []
DO_ANIM = "--anim" in argv


def spec_of(name):
    return UPPER if name == "upper" else LOWER


def arch_point(s, spec):
    u = (max(0.0, min(1.0, s)) - 0.5) * 2.0
    x = u * spec["half_w"]
    y = spec["front_y"] + spec["depth"] * (abs(u) ** 1.45)
    return Vector((x, y, spec["z"]))


def axes(s, spec):
    p = arch_point(s, spec)
    p0 = arch_point(max(0.0, s - 0.012), spec)
    p1 = arch_point(min(1.0, s + 0.012), spec)
    tan = p1 - p0
    tan.z = 0.0
    if tan.length < 1e-6:
        tan = Vector((1.0, 0.0, 0.0))
    else:
        tan.normalize()
    center = Vector((0.0, spec["front_y"] + spec["depth"] * 0.38, spec["z"]))
    out = p - center
    out.z = 0.0
    if out.length < 1e-6:
        out = Vector((0.0, -1.0, 0.0))
    else:
        out.normalize()
    return p, tan, out


def yaw_of(out):
    return math.atan2(out.x, -out.y)


def ranges():
    out = []
    frame = 1
    for name, sec, caption, action, arch, cam in STEPS:
        n = max(1, int(round(sec * FPS)))
        out.append(
            dict(name=name, caption=caption, action=action, arch=arch, cam=cam, f0=frame, f1=frame + n - 1)
        )
        frame += n
    return out, frame - 1


def step_at(frame, items):
    for item in items:
        if item["f0"] <= frame <= item["f1"]:
            span = max(1, item["f1"] - item["f0"])
            return item, (frame - item["f0"]) / span
    return items[-1], 1.0


def travel_s(u, stations=6):
    """Returns s, local 0..1 inside the dwell, sliding flag."""
    u = max(0.0, min(0.999, u))
    span = 1.0 / stations
    i = min(stations - 1, int(u / span))
    local = (u - i * span) / span
    s0 = 0.05 + (0.90 * i / stations)
    s1 = 0.05 + (0.90 * (i + 1) / stations)
    if local < 0.74:
        return s0, local / 0.74, False
    k = B.smoother((local - 0.74) / 0.26)
    return s0 * (1.0 - k) + s1 * k, 1.0, True


def mode_for(step, s):
    if step["action"] == "occlusal":
        return "occlusal"
    if step["cam"] == "lingual" and 0.40 <= s <= 0.60:
        return "vertical"
    if step["cam"] == "lingual":
        return "lingual"
    if step["action"] == "park":
        return "buccal"
    return "buccal"


def brush_pose(spec, s, mode, vib, press, sweep):
    p, tan, out = axes(s, spec)
    gum = Vector((0.0, 0.0, 1.0 if spec["name"] == "upper" else -1.0))
    crown = Vector((0.0, 0.0, -1.0 if spec["name"] == "upper" else 1.0))
    if mode == "buccal":
        bristle = (gum * 0.74 - out * 0.58).normalized()
        tip = p + out * 0.22 + crown * 0.20
    elif mode == "lingual":
        bristle = (gum * 0.80 + out * 0.42).normalized()
        tip = p - out * 0.18 + crown * 0.16
    elif mode == "vertical":
        bristle = (gum * 0.90 + out * 0.28).normalized()
        tip = p - out * 0.12 + crown * 0.10
    else:
        if spec["name"] == "upper":
            bristle = Vector((0.0, 0.0, 1.0))
            tip = p + Vector((0.0, 0.06, -0.72))
        else:
            bristle = Vector((0.0, 0.0, -1.0))
            tip = p + Vector((0.0, 0.06, 0.72))
    if mode in ("buccal", "lingual") and sweep > 0.0:
        crown = -gum
        rolled = (crown * 0.25 - out * 0.92).normalized() if mode == "buccal" else (crown * 0.25 + out * 0.90).normalized()
        bristle = (bristle * (1.0 - sweep) + rolled * sweep).normalized()
        tip = tip + crown * (0.26 * sweep)
    tip = tip + tan * vib + bristle * (0.10 * press)
    rot = B.aim_euler(-bristle, tan if mode != "vertical" else Vector((1.0, 0.0, 0.0)))
    return tip, rot, p, out


def camera_pose(step, u, focus, out):
    name = step["cam"]
    if name == "hero":
        loc = Vector((-6.4, -16.5, 2.6))
        lens = 28
        tgt = Vector((0.0, 0.8, 0.0))
    elif name == "orbit":
        ang = -0.35 + u * 0.7
        loc = Vector((math.sin(ang) * 13.6, -math.cos(ang) * 15.2, 3.0))
        lens = 28
        tgt = Vector((0.0, 0.7, 0.0))
    elif name == "occlusal" and step["arch"] == "upper":
        loc = Vector((focus.x * 0.25, focus.y - 5.2, 0.05))
        lens = 34
        tgt = focus + Vector((0.0, 0.15, -0.45))
    elif name == "occlusal":
        loc = Vector((focus.x * 0.25, focus.y - 5.0, 0.72))
        lens = 34
        tgt = focus + Vector((0.0, 0.1, 0.35))
    elif name == "lingual":
        loc = focus + Vector((0.15, -6.6, 0.15 if step["arch"] == "upper" else -0.05))
        lens = 42
        tgt = focus
    else:
        loc = focus + out * 3.1 + Vector((0.5, -7.0, 1.15 if step["arch"] == "upper" else 0.85))
        lens = 38
        tgt = focus + Vector((0.0, 0.0, 0.05))
    return loc, tgt, lens


def pose(frame, items):
    step, u = step_at(frame, items)
    spec = spec_of(step["arch"])
    action = step["action"]
    if action == "park":
        s, vib, press, sweep, slide = 0.5, 0.0, 0.0, 0.0, True
    elif action == "hold":
        s, vib, press, sweep, slide = 0.10, 0.0, 1.0, 0.0, False
    elif action == "vib":
        ph = u
        bell = math.sin(math.pi * min(1.0, ph * 1.05))
        vib = math.sin(u * 11.0 * math.tau) * 0.20 * bell
        s, press, sweep, slide = 0.10, 1.0, 0.0, False
    elif action == "sweep":
        if u < 0.62:
            vib = math.sin((u / 0.62) * 6.0 * math.tau) * 0.16
            sweep = 0.0
        else:
            vib = 0.0
            sweep = B.smoother((u - 0.62) / 0.38)
        s, press, slide = 0.10, 1.0 - 0.35 * sweep, False
    elif action == "occlusal":
        s, local, slide = travel_s(u, stations=5)
        vib = 0.0 if slide else math.sin(local * 4.0 * math.tau) * 0.38
        press, sweep = (0.35 if slide else 1.0), 0.0
    else:
        s, local, slide = travel_s(u, stations=6)
        if slide:
            vib, press, sweep = 0.0, 0.4, 0.0
        else:
            vib = math.sin(local * 5.0 * math.tau) * 0.18 * math.sin(math.pi * local)
            sweep = B.smoother((local - 0.78) / 0.22) if local > 0.78 else 0.0
            press = 1.0
    mode = mode_for(step, s)
    if mode == "vertical":
        vib_vec_scale = 0.55
        vib = vib * vib_vec_scale
    tip, rot, focus, out = brush_pose(spec, s, mode, vib, press, sweep)
    if action == "park":
        tip = tip + Vector((-9.0, -3.0, 2.5))
        press = 0.0
    enter = 0.0
    if step["name"] == "angle":
        enter = 1.0 - B.smoother(min(1.0, u / 0.28))
        tip = tip + Vector((-6.5 * enter, -2.0 * enter, 1.4 * enter))
    cam_loc, cam_tgt, lens = camera_pose(step, u, focus, out)
    return dict(
        step=step, tip=tip, rot=rot, press=press, focus=focus, out=out,
        cam_loc=cam_loc, cam_tgt=cam_tgt, lens=lens, mode=mode, s=s, spec=spec,
    )


def curve_through(name, points, thick, mat):
    curve = bpy.data.curves.new(name, type="CURVE")
    curve.dimensions = "3D"
    curve.resolution_u = 12
    curve.bevel_depth = thick
    curve.bevel_resolution = 6
    curve.use_fill_caps = True
    spline = curve.splines.new("NURBS")
    spline.points.add(len(points) - 1)
    spline.order_u = 4
    spline.use_endpoint_u = True
    for i, p in enumerate(points):
        spline.points[i].co = (p.x, p.y, p.z, 1.0)
    obj = bpy.data.objects.new(name, curve)
    obj.data.materials.append(mat)
    B.link(obj)
    return obj


def gum_points(spec, z_off, lateral):
    pts = []
    for i in range(24):
        s = i / 23
        p, _tan, out = axes(s, spec)
        pts.append(p + out * lateral + Vector((0.0, 0.0, z_off)))
    return pts


def constant_interp(obj):
    ad = obj.animation_data
    if not ad or not ad.action:
        return
    action = ad.action
    fcurves = []
    if hasattr(action, "fcurves"):
        try:
            fcurves.extend(list(action.fcurves))
        except Exception:
            pass
    slot = getattr(ad, "action_slot", None)
    if hasattr(action, "layers"):
        for layer in action.layers:
            for strip in getattr(layer, "strips", []):
                bag = None
                try:
                    bag = strip.channelbag(slot) if slot is not None else None
                except Exception:
                    bag = None
                if bag is not None and hasattr(bag, "fcurves"):
                    fcurves.extend(list(bag.fcurves))
    for fc in fcurves:
        for kp in fc.keyframe_points:
            kp.interpolation = "CONSTANT"


def add_caption(cam, text, mat, font):
    curve = bpy.data.curves.new("Cap_" + str(abs(hash(text)) % 10000), type="FONT")
    curve.body = text
    curve.align_x = "CENTER"
    curve.align_y = "CENTER"
    curve.size = 0.125
    curve.extrude = 0.008
    curve.resolution_u = 4
    if font:
        curve.font = font
    obj = bpy.data.objects.new("Caption", curve)
    obj.data.materials.append(mat)
    obj.parent = cam
    obj.location = (0.0, -0.70, -3.35)
    B.link(obj)
    return obj


def load_font():
    for path in (r"C:\Windows\Fonts\msyh.ttc", r"C:\Windows\Fonts\simhei.ttf", r"C:\Windows\Fonts\arial.ttf"):
        if os.path.exists(path):
            try:
                font = bpy.data.fonts.load(path)
                print("font", path)
                return font
            except Exception as exc:
                print("font fail", path, exc)
    return None


def influence(dist):
    inner, outer = 0.72, 1.85
    if dist >= outer:
        return 0.0
    if dist <= inner:
        return 1.0
    t = (outer - dist) / (outer - inner)
    return t * t * (3.0 - 2.0 * t)


def main():
    items, end = ranges()
    print(f"walkthrough frames 1..{end}  ({end / FPS:.1f}s)")
    scene = B.reset_scene()
    scene.frame_start = 1
    scene.frame_end = end
    scene.render.filepath = MP4_PATH
    if hasattr(scene.eevee, "taa_render_samples"):
        scene.eevee.taa_render_samples = 16

    mats = {
        "body": B.make_mat("GummyYellow", (1.00, 0.78, 0.12), rough=0.30, sub=0.42, trans=0.10, coat=0.38, radius=0.10),
        "belly": B.make_mat("Belly", (1.00, 0.90, 0.58), rough=0.38, sub=0.35, trans=0.06, coat=0.20, radius=0.08),
        "eye": B.make_mat("EyeWhite", (0.97, 0.97, 0.95), rough=0.22, sub=0.05, trans=0.02, coat=0.45, radius=0.01),
        "iris": B.make_mat("Iris", (0.45, 0.24, 0.10), rough=0.35, sub=0.15, trans=0.0, coat=0.25, radius=0.02),
        "pupil": B.make_mat("Pupil", (0.08, 0.04, 0.02), rough=0.25, sub=0.0, trans=0.0, coat=0.4, radius=0.0),
        "glint": B.make_mat("Glint", (1, 1, 1), rough=0.1, sub=0.0, trans=0.0, coat=0.8, radius=0.0),
        "nose": B.make_mat("Nose", (0.72, 0.38, 0.16), rough=0.42, sub=0.30, trans=0.04, coat=0.18, radius=0.06),
        "gum": B.make_mat("Gum", (0.93, 0.48, 0.52), rough=0.48, sub=0.45, trans=0.05, coat=0.12, radius=0.12),
        "palate": B.make_mat("Palate", (0.78, 0.36, 0.40), rough=0.62, sub=0.3, trans=0.0, coat=0.05, radius=0.08),
        "bone": B.make_mat("Bone", (0.90, 0.62, 0.58), rough=0.55, sub=0.2, trans=0.0, coat=0.08, radius=0.05),
        "white": B.make_mat("PlasticWhite", (0.95, 0.95, 0.96), rough=0.28, sub=0.0, trans=0.0, coat=0.35, radius=0.0),
        "coral": B.make_mat("Coral", (0.95, 0.28, 0.32), rough=0.32, sub=0.05, trans=0.0, coat=0.30, radius=0.0),
        "bristle": B.make_mat("Bristle", (0.62, 0.82, 0.98), rough=0.35, sub=0.0, trans=0.15, coat=0.2, radius=0.0),
        "cove": B.make_mat("Cove", (0.58, 0.84, 0.86), rough=0.85, sub=0.0, trans=0.0, coat=0.0, radius=0.0),
        "floor": B.make_mat("Floor", (0.45, 0.72, 0.74), rough=0.7, sub=0.0, trans=0.0, coat=0.05, radius=0.0),
        "guide": B.make_mat("Guide", (0.95, 0.85, 0.2), rough=0.4, sub=0.0, trans=0.0, coat=0.2, radius=0.0),
        "text": B.make_mat("Text", (0.10, 0.13, 0.16), rough=0.55, sub=0.0, trans=0.0, coat=0.0, radius=0.0),
    }
    glint = mats["glint"].node_tree.nodes.get("Principled BSDF")
    glint.inputs["Emission Color"].default_value = (1, 1, 1, 1)
    glint.inputs["Emission Strength"].default_value = 1.5

    print("portrait...")
    roo_path = os.path.join(ROOT, "roo.png")
    if not os.path.isfile(roo_path):
        raise SystemExit("missing tmp/bashi-brush/roo.png — run scripts/cutout.py --src <photo> first")
    roo_img = bpy.data.images.load(roo_path)
    roo_img.pack()
    roo_mat = bpy.data.materials.new("RooTex")
    roo_mat.use_nodes = True
    if hasattr(roo_mat, "surface_render_method"):
        roo_mat.surface_render_method = "BLENDED"
    try:
        roo_mat.blend_method = "BLEND"
    except Exception:
        pass
    roo_mat.use_backface_culling = True
    nt = roo_mat.node_tree
    tex = nt.nodes.new("ShaderNodeTexImage")
    tex.image = roo_img
    tex.interpolation = "Linear"
    emit = nt.nodes.new("ShaderNodeEmission")
    emit.inputs["Strength"].default_value = 1.15
    trans = nt.nodes.new("ShaderNodeBsdfTransparent")
    mix = nt.nodes.new("ShaderNodeMixShader")
    out_node = nt.nodes.get("Material Output")
    nt.links.new(tex.outputs["Color"], emit.inputs["Color"])
    nt.links.new(tex.outputs["Alpha"], mix.inputs["Fac"])
    nt.links.new(trans.outputs["BSDF"], mix.inputs[1])
    nt.links.new(emit.outputs["Emission"], mix.inputs[2])
    nt.links.new(mix.outputs["Shader"], out_node.inputs["Surface"])
    aspect = roo_img.size[0] / roo_img.size[1]
    card_h = 1.02
    card_w = card_h * aspect
    bpy.ops.mesh.primitive_plane_add(size=1.0, location=(0, 0, 0))
    card_proto = bpy.context.active_object
    card_proto.scale = (card_w, card_h, 1.0)
    bpy.ops.object.transform_apply(scale=True)
    card_proto.data.materials.append(roo_mat)
    print(f"card {card_w:.2f} x {card_h:.2f}")

    teeth = []
    for arch_name, spec in (("Upper", UPPER), ("Lower", LOWER)):
        for i, kind in enumerate(KINDS):
            s = (i + 0.5) / len(KINDS)
            p, _tan, out = axes(s, spec)
            sc = KIND_SCALE[kind]
            yaw = yaw_of(out)
            root = B.empty(f"{arch_name}.{i:02d}", p, sc, yaw, 0.0)
            # local +Z is world up (parent yaw is around Z). Shift the card
            # toward the bite so the gum tube sits above the ears, not through the face.
            gum_sign = 1.0 if spec["name"] == "upper" else -1.0
            card = B.spawn(
                card_proto.data,
                f"{arch_name}.{i:02d}.card",
                root,
                (0.0, 0.0, -0.42 * gum_sign),
                (1, 1, 1),
            )
            card.visible_shadow = False
            teeth.append(
                dict(
                    root=root,
                    card=card,
                    looks=[],
                    rest=p.copy(),
                    yaw=yaw,
                    scale=sc,
                    s=s,
                    arch=spec["name"],
                    phase=i * 0.55,
                )
            )
    B.hide_proto([card_proto])

    for spec, sign in ((UPPER, 1.0), (LOWER, -1.0)):
        tag = spec["name"]
        curve_through(f"GumOuter_{tag}", gum_points(spec, 0.55 * sign, 0.05), 0.18, mats["gum"])
        curve_through(f"GumInner_{tag}", gum_points(spec, 0.42 * sign, -0.22), 0.14, mats["gum"])
        curve_through(f"Jaw_{tag}", gum_points(spec, 0.95 * sign, 0.0), 0.40 if tag == "lower" else 0.32, mats["bone"])

    bpy.ops.mesh.primitive_uv_sphere_add(segments=48, ring_count=24, radius=1.0, location=(0.0, 1.25, 3.05))
    palate = bpy.context.active_object
    palate.name = "Palate"
    palate.scale = (4.5, 3.7, 0.72)
    B.smooth(palate)
    palate.data.materials.append(mats["palate"])

    B.setup_world(scene, mats)
    brush = B.build_brush(mats)
    brush.scale = (1.02, 1.02, 1.02)

    axis = B.new_mesh(bpy.ops.mesh.primitive_cylinder_add, "ToothAxis", mats["guide"], vertices=12, radius=0.025, depth=1.7, location=(0, 0, 0))
    br_axis = B.new_mesh(bpy.ops.mesh.primitive_cylinder_add, "BristleAxis", mats["coral"], vertices=12, radius=0.02, depth=1.5, location=(0, 0, 0))

    tgt = B.empty("CamTarget", (0.0, 0.4, 0.0))
    cam_data = bpy.data.cameras.new("CAM")
    cam_data.lens = 32
    cam_data.clip_end = 200
    cam = bpy.data.objects.new("CAM", cam_data)
    cam.location = (-4.6, -12.2, 2.4)
    B.link(cam)
    B.track_to(cam, tgt)
    scene.camera = cam
    for tooth in teeth:
        con = tooth["card"].constraints.new("TRACK_TO")
        con.target = cam
        con.track_axis = "TRACK_Z"
        con.up_axis = "UP_Y"
    B.add_lights(tgt)
    # under-light so the upper occlusal shot is not black
    under = bpy.data.lights.new("Under", "AREA")
    under.energy = 180
    under.size = 8
    under.color = B.srgb(1.0, 0.92, 0.88)[:3]
    under_ob = bpy.data.objects.new("Under", under)
    under_ob.location = (0.0, -2.0, -4.5)
    B.link(under_ob)
    B.track_to(under_ob, tgt)

    font = load_font()
    captions = []
    for item in items:
        cap = add_caption(cam, item["caption"], mats["text"], font)
        captions.append(cap)

    springs = [{"sx": B.Spring(1), "sy": B.Spring(1), "sz": B.Spring(1), "rx": B.Spring(0), "look": B.Spring(0)} for _ in teeth]
    print("keying...")
    for frame in range(1, end + 1):
        st = pose(frame, items)
        brush.location = st["tip"]
        brush.rotation_euler = st["rot"]
        brush.keyframe_insert("location", frame=frame)
        brush.keyframe_insert("rotation_euler", frame=frame)
        show_guide = st["step"]["name"] == "angle" and st["step"]["f0"] + 10 <= frame
        axis.hide_render = not show_guide
        br_axis.hide_render = not show_guide
        if show_guide:
            p, _tan, _out = axes(0.10, UPPER)
            axis.location = p + Vector((0, 0, 0.15))
            axis.rotation_euler = (0.0, 0.0, 0.0)
            br_axis.location = st["tip"]
            bristle_dir = -(st["rot"].to_matrix() @ Vector((0.0, 0.0, 1.0)))
            br_axis.rotation_euler = B.aim_euler(bristle_dir, Vector((1.0, 0.0, 0.0)))
        if frame == 1 or frame % 3 == 0 or frame == end:
            axis.keyframe_insert("location", frame=frame)
            axis.keyframe_insert("rotation_euler", frame=frame)
            axis.keyframe_insert("hide_render", frame=frame)
            br_axis.keyframe_insert("location", frame=frame)
            br_axis.keyframe_insert("rotation_euler", frame=frame)
            br_axis.keyframe_insert("hide_render", frame=frame)
        tgt.location = st["cam_tgt"]
        cam.location = st["cam_loc"]
        cam_data.lens = st["lens"]
        if frame == 1 or frame % 4 == 0 or frame == end:
            tgt.keyframe_insert("location", frame=frame)
            cam.keyframe_insert("location", frame=frame)
            cam_data.keyframe_insert("lens", frame=frame)
        for cap, item in zip(captions, items):
            cap.hide_render = not (item["f0"] <= frame <= item["f1"])
            marks = {1, item["f0"], item["f1"], min(end, item["f1"] + 1)}
            if frame in marks:
                cap.keyframe_insert("hide_render", frame=frame)
        for tooth, sp in zip(teeth, springs):
            if st["step"]["action"] == "park" or tooth["arch"] != st["spec"]["name"]:
                pwr = 0.0
            else:
                pwr = influence((tooth["rest"] - st["tip"]).length) * st["press"]
            breath = 1.0 + 0.015 * math.sin(frame * 0.12 + tooth["phase"])
            wave = 0.0
            if st["step"]["name"] == "end":
                wave = max(0.0, math.sin((frame - st["step"]["f0"]) * 0.45 - tooth["rest"].x * 0.5))
            tsx = (1.0 + 0.34 * pwr + 0.08 * wave) * breath
            tsy = (1.0 - 0.12 * pwr) * breath
            tsz = (1.0 - 0.42 * pwr - 0.10 * wave) * breath
            sx = sp["sx"].step(tsx, 0.66, 0.30)
            sy = sp["sy"].step(tsy, 0.66, 0.30)
            sz = sp["sz"].step(tsz, 0.58, 0.26)
            rx = sp["rx"].step(-0.40 * pwr, 0.45, 0.32)
            squash = max(0.0, 1.0 - sz)
            gum_sign = 1.0 if tooth["arch"] == "upper" else -1.0
            tooth["root"].location = tooth["rest"] + Vector((0.0, 0.04 * squash, -0.12 * squash * gum_sign))
            tooth["root"].rotation_euler = (rx, 0.0, tooth["yaw"])
            bsc = tooth["scale"]
            tooth["root"].scale = (bsc * max(0.5, sx), bsc * max(0.5, sy), bsc * max(0.4, sz))
            if frame % 2 == 0 or frame == 1 or frame == end:
                tooth["root"].keyframe_insert("location", frame=frame)
                tooth["root"].keyframe_insert("rotation_euler", frame=frame)
                tooth["root"].keyframe_insert("scale", frame=frame)
            look_t = max(-0.1, min(0.1, (st["tip"].x - tooth["rest"].x) * 0.03))
            lx = sp["look"].step(look_t, 0.32, 0.42)
            for look in tooth["looks"]:
                look.location = (lx, 0.0, 0.0)
                if frame % 3 == 0 or frame == 1:
                    look.keyframe_insert("location", frame=frame)
        if frame % 120 == 0:
            print(f"  frame {frame}  {st['step']['name']}")

    for cap in captions:
        constant_interp(cap)
    constant_interp(axis)
    constant_interp(br_axis)

    scene.frame_set(items[2]["f0"] + int(4 * FPS))
    bpy.ops.wm.save_as_mainfile(filepath=BLEND_PATH)
    print("saved", BLEND_PATH)

    if not DO_ANIM:
        picks = ["arch", "angle"]
        for item in items:
            if item["name"] not in picks:
                continue
            frame = item["f0"] + int((item["f1"] - item["f0"]) * 0.55)
            B.render_png(scene, frame, os.path.join(RENDER_DIR, f"walk_{item['name']}.png"))
        scene.render.filepath = MP4_PATH
        bpy.ops.wm.save_as_mainfile(filepath=BLEND_PATH)
        return

    scene.camera = cam
    scene.render.image_settings.media_type = "VIDEO"
    scene.render.image_settings.file_format = "FFMPEG"
    scene.render.filepath = MP4_PATH
    bpy.ops.render.render(animation=True)
    print("anim", MP4_PATH)


if __name__ == "__main__":
    main()
