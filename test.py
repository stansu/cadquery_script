import cadquery
import Part

cq = cadquery
origin = cq.Workplane("XY")
box1 = origin.box(1, 1, 1)
box1_vertices = box1.vertices()

dim = 0.5
box1_vertices.box(dim, dim, dim)

Part.show(box1.toFreecad())
