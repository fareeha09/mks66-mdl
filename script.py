import mdl
from display import *
from matrix import *
from draw import *

def run(filename):
    """
    This function runs an mdl script
    """
    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
    else:
        print "Parsing failed."
        return

    view = [0,
            0,
            1];
    ambient = [50,
               50,
               50]
    light = [[0.5,
              0.75,
              1],
             [255,
              255,
              255]]

    color = [0, 0, 0]
    tmp = new_matrix()
    ident( tmp )

    stack = [ [x[:] for x in tmp] ]
    screen = new_screen()
    zbuffer = new_zbuffer()
    tmp = []
    step_3d = 100
    consts = ''
    coords = []
    coords1 = []
    symbols['.white'] = ['constants',
                         {'red': [0.2, 0.5, 0.5],
                          'green': [0.2, 0.5, 0.5],
                          'blue': [0.2, 0.5, 0.5]}]
    reflect = '.white'

    print symbols
    for command in commands:
        print command
        if command['op'] == 'push':
            stack.append( [x[:] for x in stack[-1]] )
        if command['op'] == 'pop':
            stack.pop()
        if command['op'] == 'sphere':
            add_sphere(tmp, float(command['args'][0]),
                           float(command['args'][1]),
                           float(command['args'][2]),
                           float(command['args'][3]),
                           step_3d)
            matrix_mult(stack[-1], tmp)
            #if constant variable is present, use those for lighting
            if command['constants'] != None
            draw_polygons(polygons, screen, zbuffer, view, ambient, light, areflect, dreflect, sreflect)
        if command['op'] == 'box':
            add_box(tmp, float(command['args'][0]),
                        float(command['args'][1]),
                        float(command['args'][2]),
                        float(command['args'][3]),
                        float(command['args'][4]),
                        float(command['args'][5]))
        if command['op'] == 'torus':
            add_torus(polygons, float(command['args'][0]),
                          float(command['args'][1]),
                          float(command['args'][2]),
                          float(command['args'][3]),
                          float(command['args'][4]),
                          step_3d)
            
