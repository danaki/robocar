import cadquery as cq

def encoder_mill(
        external_radius,
        support_radius,
        hole_radius,
        blade_height,
        support_height,
        fillet_radius
    ):

    return (cq
            .Workplane("XZ")
            .moveTo(0, 0)
            .ellipseArc(external_radius, external_radius, 0, 60, startAtCurrent=False)
            .lineTo(0, 0)
            .close()
            .moveTo(0,0)
            .ellipseArc(external_radius, external_radius, 120, 180, startAtCurrent=False)
            .lineTo(0, 0)
            .close()
            .moveTo(0, 0)
            .ellipseArc(external_radius, external_radius, 240, 300, startAtCurrent=False)
            .lineTo(0, 0)
            .close()
            .extrude(blade_height)
            .center(0, 0)
            .ellipseArc(support_radius, support_radius, 0, 300, startAtCurrent=False)
            .lineTo(0, 0)
            .close()
            .extrude(support_height)
            .center(0, 0)
            .circle(hole_radius)
            .cutThruAll()
            .edges('>Y[1]')
            .fillet(fillet_radius)
    )

def encoder_mount(
        base_height,
        base_depth,
        hole_distance,
        hole_radius,
        hole_padding,
        cut_width,
        cut_height
    ):

    base_width = hole_distance + 2 * hole_radius + hole_padding * 2

    return (cq
            .Workplane("front")
            .box(base_width, base_height, base_depth)
            .pushPoints([
                (hole_distance / 2, 0),
                (-hole_distance / 2, 0)
            ])
            .circle(hole_radius)
            .cutThruAll()
            .rect(cut_width, cut_height)
            .cutThruAll()
    )