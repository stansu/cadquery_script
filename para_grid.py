import cadquery
import Part

x_length = 40.0
y_length = 40.0
z_length = 3.0
outer_gap = 5.0
inner_gap = 5.0
x_count = 7
y_count = 2

if (outer_gap*2)+((x_count-1)*inner_gap) >= x_length:
    x_length = ((outer_gap*2)+((x_count-1)*inner_gap))+1
    inner_gap = 1

if (outer_gap*2)+((y_count-1)*inner_gap) >= y_length:
    y_length = ((outer_gap*2)+((y_count-1)*inner_gap))+1
    inner_gap = 1

x_cell = x_length-(outer_gap*2)
x_cell = x_cell-((x_count-1)*inner_gap)
x_cell = x_cell/x_count
array_x = x_cell+inner_gap

y_cell = y_length-(outer_gap*2)
y_cell = y_cell-((y_count-1)*inner_gap)
y_cell = y_cell/y_count
array_y = y_cell+inner_gap

result = cadquery.Workplane('XY')
result = result.rect(x_length, y_length)
result = result.workplane()
result = result.rarray(array_x, array_y, x_count, y_count)
result = result.rect(x_cell, y_cell)
result = result.extrude(z_length)

Part.show(result.toFreecad())
