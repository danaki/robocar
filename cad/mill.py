import cadquery as cq


# result = cq.Workplane("XZ").threePointArc((1.0, 1.0), (0.0, 2.0)).close().extrude(0.5)


#result = cq.Workplane("XY") \
#    .circle(5.0).extrude(1).faces(">Z")\
#    .polarArray(4.5,0,360,6).rect(1.6,1.6).cutThruAll()

#b = cq.Workplane().box(10,10,1).faces('>Z').workplane()
#e = b.polarArray(3.2,0,360,8,rotate=True).ellipseArc(4, 4, 0, 30).lineTo(0, 0).close().cutThruAll()
#show_object(e.translate((12,0,0)))

#show_object(result)

external_radius = 10
support_radius = 5
hole_radius = 3
blade_height = 3
support_height = 5
fillet_radius = 2

blades = (
    cq.Workplane("XZ")
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

#result = cq.Workplane("XZ").union(blades).union(cylinder)

