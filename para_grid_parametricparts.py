UOM = 'mm'
# These parameters can be manipulated by end users
p_x_length = FloatParam(min=0.0,presets={'default':40.0},group='volumn', desc='Length of x')
p_y_length = FloatParam(min=0.0,presets={'default':40.0},group='volumn', desc='Length of y')
p_z_length = FloatParam(min=0.0,presets={'default':3.0},group='volumn', desc='Length of z')
p_outer_gap = FloatParam(min=0.0,presets={'default':5.0},group='gaps', desc='Length of outer gap')
p_inner_gap = FloatParam(min=0.0,presets={'default':5.0},group='gaps', desc='Length of inner gap')
p_x_count = IntegerParam(min=1,presets={'default':2},group='counts', desc='number of x')
p_y_count = IntegerParam(min=1,presets={'default':2},group='counts', desc='number of y')

# Your build method. It must return a solid object
def build():
    
    x_length = p_x_length.value
    y_length = p_y_length.value
    z_length = p_z_length.value
    outer_gap = p_outer_gap.value
    inner_gap = p_inner_gap.value
    x_count = p_x_count.value
    y_count = p_y_count.value
    
    if (outer_gap*2)+((x_count-1)*inner_gap) >= p_x_length.value:
        x_length = ((outer_gap*2)+((x_count-1)*inner_gap))+1

    if (outer_gap*2)+((y_count-1)*inner_gap) >= p_y_length.value:
        y_length = ((outer_gap*2)+((y_count-1)*inner_gap))+1

    x_cell = x_length-(outer_gap*2)
    x_cell = x_cell-((x_count-1)*inner_gap)
    x_cell = x_cell/x_count
    array_x = x_cell+inner_gap

    y_cell = y_length-(outer_gap*2)
    y_cell = y_cell-((y_count-1)*inner_gap)
    y_cell = y_cell/y_count
    array_y = y_cell+inner_gap

    final = Workplane('XY'). \
        rect(x_length,y_length). \
        workplane(). \
        rarray(array_x,array_y,x_count,y_count). \
        rect(x_cell,y_cell). \
        extrude(z_length)

    return final