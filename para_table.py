# import modules.
import cadquery
import Part

# parameter(s).
xSize = 90.0
ySize = 180.0
zSize = 75.0
tableThickess = 5.0
legOffset = 5.0
legSize = 10.0
filletSize = 1.0

# build.
# start from XY plane.
result = cadquery.Workplane("XY")
# move to table height.
result = result.workplane(offset=zSize-tableThickess, invert=False)
# create table top.
result = result.box(xSize, ySize, tableThickess, centered=(True, True, False))
# move to table top's bottom.
result = result.faces("<Z")
# change direction to -Z.
result = result.workplane(offset=0, invert=False)
# defined table leg's position.
result = result.rect(
    xSize-legOffset-legSize, ySize-legOffset-legSize, forConstruction=True)
# collect 4 leg's position.
result = result.vertices()
# create legs.
result = result.box(
    legSize, legSize, zSize-tableThickess, centered=(True, True, False))
result = result.fillet(filletSize)

# show build result.
# create whole model.
Part.show(result.toFreecad())
