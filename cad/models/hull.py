import cadquery as cq
from math import sin, cos, radians

def hull_bracket(
        angle,
        width,
        thickness,
        top_height,
        side_height,
        top_hole_radius,
        top_hole_distance,
        top_hole_margin,
        side_hole_radius,
        side_hole_distance,
        side_hole_margin
    ):
    
    thm = top_height / 2 - top_hole_margin
    
    return (cq
            .Workplane("front")
            .box(width, top_height, thickness)
            .faces('>Z')
            .pushPoints([
                (top_hole_distance / 2, thm),
                (-top_hole_distance / 2, thm)
            ])
            .circle(top_hole_radius)
            .cutThruAll()         
            .faces(">Y")
            .workplane()
            .transformed(
                offset=cq.Vector(0, thickness / 2 - sin(radians(angle)) * thickness / 2, cos(radians(angle)) * thickness / 2),
                rotate=cq.Vector(angle, 0, 0)
            )     
            .moveTo(0, side_height / 2)
            .box(width, side_height, thickness)
            .faces('>Y')
            .pushPoints([
                (side_hole_distance / 2, side_hole_margin),
                (-side_hole_distance / 2, side_hole_margin)
            ])
            .circle(side_hole_radius)
            .cutThruAll()
    )
