import cadquery as cq
from models import *

mill = encoder_mill(
    external_radius=10,
    support_radius=4,
    hole_radius=2.5,
    blade_height=3,
    support_height=5,
    fillet_radius=3
)

mount = encoder_mount(
    base_height=20,
    base_depth=2,
    hole_distance=21,
    hole_radius=1.5,
    hole_padding=6,
    cut_width=14.5,
    cut_height=6.5
)

left_bracket = hull_bracket(
    angle=173,
    width=50,
    thickness=2,
    top_height=14,
    side_height=12,
    top_hole_radius=2,
    top_hole_distance=40,
    top_hole_margin=9,
    side_hole_radius=1.5,
    side_hole_distance=31,
    side_hole_margin=8
)

right_bracket = hull_bracket(
    angle=180,
    width=50,
    thickness=2,
    top_height=14,
    side_height=12,
    top_hole_radius=2,
    top_hole_distance=40,
    top_hole_margin=9,
    side_hole_radius=1.5,
    side_hole_distance=28,
    side_hole_margin=8
)

cq.exporters.export(mill, "out/encoder_mill.stl")
cq.exporters.export(mount, "out/encoder_mount.stl")
cq.exporters.export(left_bracket, "out/left_bracket.stl")
cq.exporters.export(right_bracket, "out/right_bracket.stl")