import cadquery as cq

result = (
        cq.Workplane("front").box(20.0, 10.0, 0.25)
     .faces('>Z')
          .pushPoints([(8, -4), (-8, -4)])
      .circle(0.25).cutThruAll()         
        
        .faces(">Y").workplane()
     .transformed(offset=cq.Vector(0, 0, -0.1), rotate=cq.Vector(170, 0, 0))     
     .moveTo(0, 5 - 0.1)
     .box(20.0, 10.0, 0.25)
     .faces('>Y')
     .pushPoints([(1, 1), (-1, 1)])
     .circle(0.25).cutThruAll()
     
)