# Helper library for the Bass walkthrough (brush, springs, materials, aim).
# Photo-card teeth live in walkthrough.py. Do not ship this file's metaball main() as the tooth.
# Output stays in tmp/bashi-brush/, not next to this script.

import math
import os
import random
import sys
import traceback

import bpy
from mathutils import Matrix, Vector

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", "..", ".."))
ROOT = os.path.join(REPO, "tmp", "bashi-brush")
BLEND_PATH = os.path.join(ROOT, "bashi.blend")
RENDER_DIR = os.path.join(ROOT, "renders")
os.makedirs(RENDER_DIR, exist_ok=True)

# --- timeline (24 fps, ~9 s) ---
FPS = 24
INTRO = 32
DWELL = 30
SLIDE = 10
STATIONS = (0.18, 0.38, 0.58, 0.78)
OUTRO_START = INTRO + (len(STATIONS) - 1) * (DWELL + SLIDE) + DWELL
END = OUTRO_START + 36  # 218

UPPER_N = 8
LOWER_N = 6
UPPER_W, UPPER_D, UPPER_Y = 13.2, 2.4, -0.2
LOWER_W, LOWER_D, LOWER_Y = 11.2, 2.0, 0.15

argv = sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else []
DO_ANIM = "--anim" in argv
DO_STILL = "--no-still" not in argv


def srgb(r, g, b, a=1.0):
    def f(u):
        return u / 12.92 if u <= 0.04045 else ((u + 0.055) / 1.055) ** 2.4

    return (f(r), f(g), f(b), a)


def clamp01(t):
    return 0.0 if t < 0.0 else 1.0 if t > 1.0 else t


def smoother(t):
    t = clamp01(t)
    return t * t * t * (t * (t * 6.0 - 15.0) + 10.0)


def link(obj, col=None):
    (col or bpy.context.scene.collection).objects.link(obj)
    return obj


def smooth(obj):
    bpy.ops.object.select_all(action="DESELECT")
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    try:
        bpy.ops.object.shade_smooth()
    except Exception as exc:
        print("shade_smooth skipped", exc)


class Spring:
    def __init__(self, x):
        self.x = float(x)
        self.v = 0.0

    def step(self, target, k, damp):
        self.v = (self.v + (target - self.x) * k) * (1.0 - damp)
        self.x += self.v
        return self.x


def reset_scene():
    bpy.ops.wm.read_factory_settings(use_empty=False)
    for obj in list(bpy.data.objects):
        bpy.data.objects.remove(obj, do_unlink=True)
    scene = bpy.context.scene
    scene.name = "Bashi"
    scene.render.fps = FPS
    scene.frame_start = 1
    scene.frame_end = END
    scene.render.resolution_x = 1280
    scene.render.resolution_y = 720
    scene.render.resolution_percentage = 100
    scene.render.engine = "BLENDER_EEVEE"
    ee = scene.eevee
    if hasattr(ee, "taa_render_samples"):
        ee.taa_render_samples = 32
    if hasattr(ee, "taa_samples"):
        ee.taa_samples = 16
    if hasattr(ee, "use_raytracing"):
        ee.use_raytracing = True
    if hasattr(ee, "use_shadows"):
        ee.use_shadows = True
    if hasattr(ee, "use_gtao"):
        ee.use_gtao = True
    try:
        scene.view_settings.view_transform = "AgX"
    except Exception:
        pass
    for look in ("AgX - Medium High Contrast", "AgX - Punchy"):
        try:
            scene.view_settings.look = look
            break
        except Exception:
            continue
    scene.render.image_settings.media_type = "VIDEO"
    scene.render.ffmpeg.format = "MPEG4"
    scene.render.ffmpeg.codec = "H264"
    scene.render.ffmpeg.constant_rate_factor = "MEDIUM"
    scene.render.ffmpeg.ffmpeg_preset = "GOOD"
    scene.render.ffmpeg.audio_codec = "NONE"
    scene.render.image_settings.file_format = "FFMPEG"
    scene.render.filepath = os.path.join(RENDER_DIR, "bashi.mp4")
    scene.render.use_file_extension = True
    return scene


def make_mat(name, color, rough=0.34, sub=0.28, trans=0.08, coat=0.22, radius=0.12):
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    mat.diffuse_color = srgb(*color)
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = srgb(*color)
    bsdf.inputs["Roughness"].default_value = rough
    bsdf.inputs["Specular IOR Level"].default_value = 0.48
    bsdf.inputs["IOR"].default_value = 1.36
    bsdf.inputs["Subsurface Weight"].default_value = sub
    bsdf.inputs["Subsurface Radius"].default_value = (1.0, 0.42, 0.12)
    bsdf.inputs["Subsurface Scale"].default_value = radius
    bsdf.inputs["Transmission Weight"].default_value = trans
    bsdf.inputs["Coat Weight"].default_value = coat
    bsdf.inputs["Coat Roughness"].default_value = 0.16
    return mat


def new_mesh(op, name, mat, **kw):
    op(**kw)
    obj = bpy.context.active_object
    obj.name = name
    smooth(obj)
    obj.data.materials.append(mat)
    return obj


def build_body(mat_body, mat_belly):
    bpy.ops.object.metaball_add(type="BALL", location=(0, 0, 0))
    obj = bpy.context.active_object
    obj.name = "BodyProto"
    mb = obj.data
    mb.resolution = 0.038
    mb.render_resolution = 0.026
    mb.threshold = 0.18
    # Round chubby head. Threshold is low so the blobs fuse into one mass.
    specs = [
        ("ELLIPSOID", (0.00, 0.00, 0.15), (1.15, 1.05, 1.05), 1.0),
        ("ELLIPSOID", (0.00, -0.20, -0.05), (1.25, 1.00, 0.95), 1.0),
        ("ELLIPSOID", (0.00, -0.55, -0.08), (0.62, 0.55, 0.48), 1.0),
        ("ELLIPSOID", (-0.42, 0.00, 0.95), (0.22, 0.16, 0.28), 1.0),
        ("ELLIPSOID", (0.48, -0.02, 1.00), (0.24, 0.18, 0.30), 1.0),
        ("ELLIPSOID", (0.00, 0.05, -0.78), (0.95, 0.85, 0.62), 1.0),
    ]
    first = mb.elements[0]
    kind, co, size, stiff = specs[0]
    first.type = kind
    first.co = co
    first.radius = 1.0
    first.size_x, first.size_y, first.size_z = size
    first.stiffness = stiff
    for kind, co, size, stiff in specs[1:]:
        try:
            el = mb.elements.new(type=kind)
        except TypeError:
            el = mb.elements.new()
            el.type = kind
        el.co = co
        el.radius = size[0] if kind == "BALL" else 1.0
        el.size_x, el.size_y, el.size_z = size
        el.stiffness = stiff
    bpy.context.view_layer.update()
    bpy.ops.object.convert(target="MESH")
    body = bpy.context.active_object
    body.name = "BodyMesh"
    smooth(body)
    me = body.data
    me.materials.append(mat_body)
    zs = [v.co.z for v in me.vertices]
    xs = [v.co.x for v in me.vertices]
    print(f"body bounds x {min(xs):.2f}..{max(xs):.2f}  z {min(zs):.2f}..{max(zs):.2f}")
    return body, min(zs), max(zs)


def unit_sphere(name, mat, segments=32):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segments, ring_count=16, radius=1.0, location=(0, 0, 0))
    obj = bpy.context.active_object
    obj.name = name
    smooth(obj)
    obj.data.materials.append(mat)
    return obj


def hide_proto(objs):
    col = bpy.data.collections.new("PROTO")
    bpy.context.scene.collection.children.link(col)
    for obj in objs:
        for c in list(obj.users_collection):
            c.objects.unlink(obj)
        col.objects.link(obj)
    col.hide_render = True

    def walk(layer):
        if layer.collection == col:
            layer.exclude = True
            return True
        return any(walk(ch) for ch in layer.children)

    walk(bpy.context.view_layer.layer_collection)


def spawn(mesh, name, parent, loc, scale, rot=(0, 0, 0)):
    obj = bpy.data.objects.new(name, mesh)
    obj.parent = parent
    obj.location = loc
    obj.scale = scale
    obj.rotation_euler = rot
    link(obj)
    return obj


def empty(name, loc, scale=1.0, yaw=0.0, rot_x=0.0):
    obj = bpy.data.objects.new(name, None)
    obj.empty_display_type = "PLAIN_AXES"
    obj.empty_display_size = 0.02
    obj.location = loc
    obj.rotation_mode = "XYZ"
    obj.rotation_euler = (rot_x, 0.0, yaw)
    obj.scale = (scale, scale, scale)
    link(obj)
    return obj


def arch(s, z, width, depth, front_y):
    x = (s - 0.5) * width
    y = front_y + depth * (x / (width * 0.5)) ** 2
    return Vector((x, y, z))


def tangent_of(s, z, width, depth, front_y):
    a = arch(max(0.0, s - 0.012), z, width, depth, front_y)
    b = arch(min(1.0, s + 0.012), z, width, depth, front_y)
    t = b - a
    t.z = 0.0
    return t.normalized() if t.length > 1e-6 else Vector((1, 0, 0))


def scale_at(s, front):
    return front * (1.0 - 0.10 * abs(s - 0.5) * 2.0)


def add_eyes(root, name, meshes, sleepy, look0):
    """Big clay eyes. look empty slides the iris toward the brush."""
    z_eye = 0.16 if sleepy else 0.34
    for side, x, z in (("L", -0.34, 0.48), ("R", 0.36, 0.50)):
        spawn(meshes["eye"], f"{name}.eye{side}", root, (x, -1.02, z), (0.30, 0.15, z_eye))
        look = empty(f"{name}.look{side}", (0, 0, 0))
        look.parent = root
        look.location = (look0, 0.0, 0.0)
        iz = 0.18 if sleepy else 0.20
        spawn(meshes["iris"], f"{name}.iris{side}", look, (x, -1.16, z - 0.01), (0.17, 0.07, iz))
        spawn(meshes["pupil"], f"{name}.pupil{side}", look, (x, -1.22, z - 0.02), (0.075, 0.04, 0.085 if not sleepy else 0.05))
        spawn(
            meshes["glint"],
            f"{name}.glint{side}",
            look,
            (x - 0.07, -1.26, z + 0.07),
            (0.038, 0.02, 0.038),
        )
        if side == "L":
            left = look
    return left


def make_gum(name, z, y_shift, width, depth, front_y, thick, mat):
    curve = bpy.data.curves.new(name, type="CURVE")
    curve.dimensions = "3D"
    curve.resolution_u = 16
    curve.bevel_depth = thick
    curve.bevel_resolution = 7
    curve.use_fill_caps = True
    spline = curve.splines.new("NURBS")
    n = 18
    spline.points.add(n - 1)
    spline.order_u = 4
    spline.resolution_u = 8
    spline.use_endpoint_u = True
    for i in range(n):
        s = i / (n - 1)
        p = arch(s, z, width, depth, front_y)
        spline.points[i].co = (p.x, p.y + y_shift, p.z, 1.0)
    obj = bpy.data.objects.new(name, curve)
    obj.data.materials.append(mat)
    link(obj)
    return obj


def build_brush(mats):
    root = empty("Brush", (0, 0, 0))
    head = new_mesh(
        bpy.ops.mesh.primitive_cube_add,
        "BrushHead",
        mats["white"],
        size=1.0,
        location=(0, 0, 0.62),
    )
    head.scale = (2.05, 0.92, 0.30)
    bpy.context.view_layer.objects.active = head
    head.select_set(True)
    bpy.ops.object.transform_apply(scale=True)
    bev = head.modifiers.new("Bevel", "BEVEL")
    bev.width = 0.07
    bev.segments = 3
    bpy.ops.object.modifier_apply(modifier=bev.name)
    sub = head.modifiers.new("Sub", "SUBSURF")
    sub.levels = 1
    bpy.ops.object.modifier_apply(modifier=sub.name)
    smooth(head)

    neck = new_mesh(
        bpy.ops.mesh.primitive_cylinder_add,
        "BrushNeck",
        mats["white"],
        vertices=20,
        radius=0.11,
        depth=0.7,
        location=(0, 0, 1.15),
    )
    handle = new_mesh(
        bpy.ops.mesh.primitive_cylinder_add,
        "BrushHandle",
        mats["coral"],
        vertices=24,
        radius=0.18,
        depth=2.35,
        location=(0, 0, 2.35),
    )
    grip = new_mesh(
        bpy.ops.mesh.primitive_cylinder_add,
        "BrushGrip",
        mats["white"],
        vertices=24,
        radius=0.215,
        depth=0.55,
        location=(0, 0, 2.55),
    )
    # one bristle, then linked copies
    br = new_mesh(
        bpy.ops.mesh.primitive_cone_add,
        "Bristle",
        mats["bristle"],
        vertices=8,
        radius1=0.028,
        radius2=0.010,
        depth=0.26,
        location=(0, 0, 0.16),
        rotation=(math.pi, 0, 0),
    )
    xs = (-0.78, -0.52, -0.26, 0.0, 0.26, 0.52, 0.78)
    ys = (-0.28, 0.0, 0.28)
    bristles = [br]
    for i, x in enumerate(xs):
        for j, y in enumerate(ys):
            if i == 0 and j == 0:
                br.location = (x, y, 0.16)
                continue
            dup = br.copy()
            dup.data = br.data
            dup.location = (x, y, 0.16)
            dup.name = f"Bristle.{i}{j}"
            link(dup)
            bristles.append(dup)
    parts = [head, neck, handle, grip, *bristles]
    for p in parts:
        p.parent = root
    return root


def aim_euler(z_axis, x_hint):
    z = z_axis.normalized()
    x = x_hint - z * x_hint.dot(z)
    if x.length < 1e-6:
        x = Vector((1.0, 0.0, 0.0))
    x.normalize()
    y = z.cross(x).normalized()
    x = y.cross(z).normalized()
    return Matrix((x, y, z)).transposed().to_euler("XYZ")


def timeline(frame):
    """s, vib, press, intro, outro, sweep."""
    if frame <= INTRO:
        u = smoother(frame / INTRO)
        return STATIONS[0], 0.0, u, 1.0 - u, 0.0, 0.0
    if frame >= OUTRO_START:
        u = smoother((frame - OUTRO_START) / max(1, END - OUTRO_START))
        return STATIONS[-1], 0.0, 1.0 - u, 0.0, u, 0.0
    t = frame - INTRO
    span = DWELL + SLIDE
    i = min(len(STATIONS) - 1, t // span)
    local = t - i * span
    if i < len(STATIONS) - 1 and local >= DWELL:
        u = smoother((local - DWELL) / SLIDE)
        s = STATIONS[i] * (1.0 - u) + STATIONS[i + 1] * u
        return s, 0.0, 0.45, 0.0, 0.0, 0.0
    phase = float(local)
    sweep = 0.0
    if phase > DWELL - 8:
        sweep = smoother((phase - (DWELL - 8)) / 8.0)
    bell = math.sin(math.pi * min(phase, DWELL) / DWELL)
    vib = math.sin(phase * 1.15) * 0.32 * max(0.0, bell) * (1.0 - sweep)
    return STATIONS[i], vib, 1.0, 0.0, 0.0, sweep


def influence(dist):
    inner, outer = 0.95, 2.55
    if dist >= outer:
        return 0.0
    if dist <= inner:
        return 1.0
    t = (outer - dist) / (outer - inner)
    return t * t * (3.0 - 2.0 * t)


def brush_pose(frame, tip_off_y, tip_off_z, upper_z):
    s, vib, press, intro, outro, sweep = timeline(frame)
    base = arch(s, upper_z, UPPER_W, UPPER_D, UPPER_Y)
    tangent = tangent_of(s, upper_z, UPPER_W, UPPER_D, UPPER_Y)
    # Handle stays in the side plane so the 45° reads from a 3/4 camera.
    # sweep rotates the bristles down the crown (the Bass roll).
    into = 0.72
    up = 0.72 - 0.20 * sweep
    handle_dir = Vector((0.0, -into, -up))
    bristle = -handle_dir.normalized()
    tip = Vector((base.x, base.y + tip_off_y, base.z + tip_off_z))
    tip += tangent * vib
    tip += Vector((0.0, 0.04 * sweep, -0.18 * sweep))
    tip += bristle * (0.16 * press)
    tip += Vector((-7.5 * intro + 6.0 * outro, -2.2 * intro - 1.2 * outro, 1.6 * intro + 1.2 * outro))
    rot = aim_euler(handle_dir, Vector((1.0, 0.0, 0.0)))
    return tip, rot, press


def add_text(cam):
    font = None
    label = "45°"
    for path in (
        r"C:\Windows\Fonts\msyh.ttc",
        r"C:\Windows\Fonts\msyhbd.ttc",
        r"C:\Windows\Fonts\simhei.ttf",
        r"C:\Windows\Fonts\arial.ttf",
    ):
        if not os.path.exists(path):
            continue
        try:
            font = bpy.data.fonts.load(path)
            if path.lower().endswith((".ttc", ".ttf")) and "arial" not in path.lower():
                label = "巴氏刷牙法\n刷毛 45°  水平短颤"
            print("font", path)
            break
        except Exception as exc:
            print("font fail", path, exc)
    curve = bpy.data.curves.new("Label", type="FONT")
    curve.body = label
    curve.align_x = "CENTER"
    curve.align_y = "CENTER"
    curve.size = 0.17
    curve.extrude = 0.012
    curve.bevel_depth = 0.003
    curve.bevel_resolution = 2
    curve.resolution_u = 6
    if font:
        curve.font = font
    mat = make_mat("Text", (0.12, 0.16, 0.20), rough=0.6, sub=0.0, trans=0.0, coat=0.0, radius=0.0)
    obj = bpy.data.objects.new("Label", curve)
    obj.data.materials.append(mat)
    obj.parent = cam
    obj.location = (0.0, 0.82, -3.5)
    obj.rotation_euler = (0.0, 0.0, 0.0)
    link(obj)
    return obj


def setup_world(scene, mats):
    world = scene.world or bpy.data.worlds.new("World")
    scene.world = world
    world.use_nodes = True
    bg = world.node_tree.nodes.get("Background")
    bg.inputs["Color"].default_value = srgb(0.62, 0.86, 0.88)
    bg.inputs["Strength"].default_value = 0.45

    bpy.ops.mesh.primitive_cylinder_add(vertices=64, radius=26, depth=18, location=(0, 0, 1.2))
    cove = bpy.context.active_object
    cove.name = "Cove"
    smooth(cove)
    cove.data.materials.append(mats["cove"])
    bpy.ops.object.mode_set(mode="EDIT")
    bpy.ops.mesh.select_all(action="SELECT")
    bpy.ops.mesh.flip_normals()
    bpy.ops.object.mode_set(mode="OBJECT")

    bpy.ops.mesh.primitive_cylinder_add(vertices=64, radius=24, depth=0.2, location=(0, 0, -3.15))
    floor = bpy.context.active_object
    floor.name = "Floor"
    floor.data.materials.append(mats["floor"])
    smooth(floor)


def add_lights(target):
    specs = [
        ("Key", (7.2, -7.5, 9.2), 520, 6.5, srgb(1.0, 0.96, 0.90)),
        ("Fill", (-7.5, -6.0, 5.4), 160, 8.0, srgb(0.75, 0.88, 1.0)),
        ("Rim", (0.4, 8.5, 6.5), 240, 5.0, srgb(1.0, 0.86, 0.72)),
        ("Bounce", (0.0, -1.0, -1.6), 70, 8.0, srgb(1.0, 0.80, 0.70)),
    ]
    for name, loc, energy, size, color in specs:
        light = bpy.data.lights.new(name, "AREA")
        light.energy = energy
        light.shape = "RECTANGLE"
        light.size = size
        light.size_y = size * 0.8
        light.color = color[:3]
        obj = bpy.data.objects.new(name, light)
        obj.location = loc
        link(obj)
        con = obj.constraints.new("TRACK_TO")
        con.target = target
        con.track_axis = "TRACK_NEGATIVE_Z"
        con.up_axis = "UP_Y"


def track_to(obj, target):
    con = obj.constraints.new("TRACK_TO")
    con.target = target
    con.track_axis = "TRACK_NEGATIVE_Z"
    con.up_axis = "UP_Y"
    return con


def render_png(scene, frame, path):
    scene.frame_set(frame)
    im = scene.render.image_settings
    prev_media, prev_fmt = im.media_type, im.file_format
    im.media_type = "IMAGE"
    im.file_format = "PNG"
    scene.render.filepath = path
    bpy.ops.render.render(write_still=True)
    im.media_type = prev_media
    im.file_format = prev_fmt
    scene.render.filepath = os.path.join(RENDER_DIR, "bashi.mp4")
    print("rendered", path)


def main():
    scene = reset_scene()
    rng = random.Random(7)

    mats = {
        "body": make_mat("GummyYellow", (1.00, 0.78, 0.12), rough=0.30, sub=0.42, trans=0.10, coat=0.38, radius=0.10),
        "belly": make_mat("Belly", (1.00, 0.90, 0.58), rough=0.38, sub=0.35, trans=0.06, coat=0.20, radius=0.08),
        "eye": make_mat("EyeWhite", (0.97, 0.97, 0.95), rough=0.22, sub=0.05, trans=0.02, coat=0.45, radius=0.01),
        "iris": make_mat("Iris", (0.45, 0.24, 0.10), rough=0.35, sub=0.15, trans=0.0, coat=0.25, radius=0.02),
        "pupil": make_mat("Pupil", (0.08, 0.04, 0.02), rough=0.25, sub=0.0, trans=0.0, coat=0.4, radius=0.0),
        "glint": make_mat("Glint", (1, 1, 1), rough=0.1, sub=0.0, trans=0.0, coat=0.8, radius=0.0),
        "nose": make_mat("Nose", (0.72, 0.38, 0.16), rough=0.42, sub=0.30, trans=0.04, coat=0.18, radius=0.06),
        "gum": make_mat("Gum", (0.93, 0.48, 0.52), rough=0.48, sub=0.45, trans=0.05, coat=0.12, radius=0.15),
        "white": make_mat("PlasticWhite", (0.95, 0.95, 0.96), rough=0.28, sub=0.0, trans=0.0, coat=0.35, radius=0.0),
        "coral": make_mat("Coral", (0.95, 0.28, 0.32), rough=0.32, sub=0.05, trans=0.0, coat=0.30, radius=0.0),
        "bristle": make_mat("Bristle", (0.62, 0.82, 0.98), rough=0.35, sub=0.0, trans=0.15, coat=0.2, radius=0.0),
        "cove": make_mat("Cove", (0.58, 0.84, 0.86), rough=0.85, sub=0.0, trans=0.0, coat=0.0, radius=0.0),
        "floor": make_mat("Floor", (0.45, 0.72, 0.74), rough=0.7, sub=0.0, trans=0.0, coat=0.05, radius=0.0),
    }
    # glint reads as a wet highlight
    glint_bsdf = mats["glint"].node_tree.nodes.get("Principled BSDF")
    glint_bsdf.inputs["Emission Color"].default_value = (1, 1, 1, 1)
    glint_bsdf.inputs["Emission Strength"].default_value = 1.5

    print("metaball body...")
    body, zmin, zmax = build_body(mats["body"], mats["belly"])
    eye = unit_sphere("EyeProto", mats["eye"])
    iris = unit_sphere("IrisProto", mats["iris"], segments=24)
    pupil = unit_sphere("PupilProto", mats["pupil"], segments=16)
    glint = unit_sphere("GlintProto", mats["glint"], segments=12)
    nose = unit_sphere("NoseProto", mats["nose"], segments=24)
    belly = unit_sphere("BellyProto", mats["belly"], segments=24)
    meshes = {
        "body": body.data,
        "eye": eye.data,
        "iris": iris.data,
        "pupil": pupil.data,
        "glint": glint.data,
        "nose": nose.data,
        "belly": belly.data,
    }
    height = zmax - zmin
    front_scale = 1.72 / height
    print(f"front_scale {front_scale:.3f}  height {height:.2f}")

    upper_z = 1.05
    lower_z = upper_z + zmin * front_scale - 0.85 - (zmax * front_scale)
    print(f"upper_z {upper_z:.2f} lower_z {lower_z:.2f}")

    teeth = []

    def place_row(n, z, width, depth, front_y, prefix):
        for i in range(n):
            s = (i + 0.5) / n
            sc = scale_at(s, front_scale) * rng.uniform(0.96, 1.05)
            loc = arch(s, z, width, depth, front_y)
            loc.x += rng.uniform(-0.04, 0.04)
            yaw = (s - 0.5) * 1.05 + rng.uniform(-0.04, 0.04)
            tilt = rng.uniform(-0.06, 0.07)
            look0 = rng.choice((-0.07, -0.05, -0.02, 0.04))
            sleepy = prefix == "Upper" and i == 1
            root = empty(f"{prefix}.{i:02d}", loc, sc, yaw, tilt)
            spawn(meshes["body"], f"{prefix}.{i:02d}.body", root, (0, 0, 0), (1, 1, 1))
            spawn(meshes["belly"], f"{prefix}.{i:02d}.belly", root, (0.0, -0.78, -0.42), (0.46, 0.18, 0.40))
            spawn(meshes["nose"], f"{prefix}.{i:02d}.nose", root, (0.0, -1.05, -0.12), (0.26, 0.16, 0.20))
            looks = add_eyes(root, f"{prefix}.{i:02d}", meshes, sleepy, look0)
            teeth.append(
                {
                    "root": root,
                    "looks": [obj for obj in bpy.data.objects if obj.name.startswith(f"{prefix}.{i:02d}.look")],
                    "s": s,
                    "rest": loc.copy(),
                    "yaw": yaw,
                    "tilt": tilt,
                    "scale": sc,
                    "look0": look0,
                    "phase": i * 0.65 + (0.4 if prefix == "Lower" else 0.0),
                    "row": prefix,
                }
            )

    place_row(UPPER_N, upper_z, UPPER_W, UPPER_D, UPPER_Y, "Upper")
    place_row(LOWER_N, lower_z, LOWER_W, LOWER_D, LOWER_Y, "Lower")
    hide_proto([body, eye, iris, pupil, glint, nose, belly])

    gum_z_up = upper_z + zmax * front_scale * 0.55
    gum_z_lo = lower_z + zmin * front_scale * 0.50
    make_gum("GumUpper", gum_z_up, 0.70, UPPER_W + 0.8, UPPER_D, UPPER_Y, 0.20, mats["gum"])
    make_gum("GumLower", gum_z_lo, 0.58, LOWER_W + 0.6, LOWER_D, LOWER_Y, 0.18, mats["gum"])

    tip_off_y = -0.42
    tip_off_z = zmax * front_scale * 0.28
    print(f"brush tip offset y {tip_off_y:.2f} z {tip_off_z:.2f}")

    brush = build_brush(mats)
    brush.scale = (1.12, 1.12, 1.12)
    setup_world(scene, mats)

    tgt = empty("CamTarget", (0.2, 0.3, 0.35))
    cam_data = bpy.data.cameras.new("CAM")
    cam_data.lens = 38
    cam_data.clip_end = 200
    cam = bpy.data.objects.new("CAM", cam_data)
    cam.location = (4.8, -7.6, 2.6)
    link(cam)
    track_to(cam, tgt)
    scene.camera = cam
    add_lights(tgt)
    add_text(cam)

    face_data = bpy.data.cameras.new("CAM_FACE")
    face_data.lens = 50
    face_data.clip_end = 80
    face_cam = bpy.data.objects.new("CAM_FACE", face_data)
    hero = min((t for t in teeth if t["row"] == "Upper"), key=lambda t: abs(t["s"] - 0.5))
    face_cam.location = hero["rest"] + Vector((0.55, -2.55, 0.05))
    link(face_cam)
    face_tgt = empty("FaceTarget", hero["rest"] + Vector((0, 0, 0.15)))
    track_to(face_cam, face_tgt)

    print(f"keying {len(teeth)} teeth, frames 1..{END}")
    springs = [
        {
            "sx": Spring(1),
            "sy": Spring(1),
            "sz": Spring(1),
            "rx": Spring(t["tilt"]),
            "look": Spring(t["look0"]),
        }
        for t in teeth
    ]
    for frame in range(1, END + 1):
        tip, rot, press_amt = brush_pose(frame, tip_off_y, tip_off_z, upper_z)
        brush.location = tip
        brush.rotation_euler = rot
        brush.keyframe_insert("location", frame=frame)
        brush.keyframe_insert("rotation_euler", frame=frame)
        # gentle camera drift toward the active group
        s, _, _, intro, outro, _ = timeline(frame)
        focus = arch(s, upper_z, UPPER_W, UPPER_D, UPPER_Y)
        tgt.location = Vector((focus.x + 0.35, focus.y, 0.15))
        cam.location = tgt.location + Vector((-4.8, -8.6, 2.05))
        if frame == 1 or frame == END or frame % 4 == 0:
            tgt.keyframe_insert("location", frame=frame)
            cam.keyframe_insert("location", frame=frame)
        for t, sp in zip(teeth, springs):
            dist = (t["rest"] - tip).length
            p = influence(dist) * press_amt
            if frame >= OUTRO_START - 6:
                wave = max(0.0, math.sin((frame - OUTRO_START) * 0.48 - t["rest"].x * 0.55))
            else:
                wave = 0.0
            breath = 1.0 + 0.02 * math.sin(frame * 0.15 + t["phase"])
            tsx = (1.0 + 0.42 * p + 0.10 * wave) * breath
            tsy = (1.0 - 0.18 * p) * breath
            tsz = (1.0 - 0.50 * p - 0.14 * wave) * breath
            trx = t["tilt"] - 0.55 * p
            sx = sp["sx"].step(tsx, 0.72, 0.28)
            sy = sp["sy"].step(tsy, 0.72, 0.28)
            sz = sp["sz"].step(tsz, 0.64, 0.24)
            rx = sp["rx"].step(trx, 0.45, 0.32)
            root = t["root"]
            squash = max(0.0, 1.0 - sz)
            root.location = t["rest"] + Vector((0.0, 0.06 * squash, -0.22 * squash))
            root.rotation_euler = (rx, 0.0, t["yaw"])
            base = t["scale"]
            root.scale = (base * max(0.45, sx), base * max(0.45, sy), base * max(0.35, sz))
            root.keyframe_insert("location", frame=frame)
            root.keyframe_insert("rotation_euler", frame=frame)
            root.keyframe_insert("scale", frame=frame)
            look_target = max(-0.12, min(0.12, t["look0"] * 0.4 + (tip.x - t["rest"].x) * 0.035))
            lx = sp["look"].step(look_target, 0.35, 0.40)
            for look in t["looks"]:
                look.location = (lx, 0.0, 0.0)
                look.keyframe_insert("location", frame=frame)
        if frame % 40 == 0:
            print(f"  frame {frame}")

    # open on a squish frame: station 2, mid-dwell, vibration near a peak
    action_frame = INTRO + (DWELL + SLIDE) + 8
    scene.frame_set(action_frame)
    bpy.ops.wm.save_as_mainfile(filepath=BLEND_PATH)
    print("saved", BLEND_PATH, "action_frame", action_frame)

    if DO_STILL:
        try:
            scene.camera = face_cam
            render_png(scene, 1, os.path.join(RENDER_DIR, "preview_face.png"))
            scene.camera = cam
            render_png(scene, action_frame, os.path.join(RENDER_DIR, "preview_action.png"))
            sweep_frame = INTRO + DWELL - 2
            render_png(scene, sweep_frame, os.path.join(RENDER_DIR, "preview_sweep.png"))
        except Exception:
            traceback.print_exc()
        scene.camera = cam
        scene.frame_set(action_frame)
        bpy.ops.wm.save_as_mainfile(filepath=BLEND_PATH)

    if DO_ANIM:
        scene.camera = cam
        scene.render.image_settings.media_type = "VIDEO"
        scene.render.image_settings.file_format = "FFMPEG"
        scene.render.filepath = os.path.join(RENDER_DIR, "bashi.mp4")
        bpy.ops.render.render(animation=True)
        print("anim", scene.render.filepath)


if __name__ == "__main__":
    main()
