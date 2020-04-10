from Spirograph import TriangleSpirograph 

def reset():
    global spiro
    
    # Go up by one multiplication on reset
    spiro.next_setup()
    
    background(255)
    stroke(0)
    spiro.draw_triangle()
    
    stroke(0, 0, 0, 100)

def setup():
    global spiro, p1, p2, p3, TO_MOVE
    size(700, 700)
    
    # Global point currently being moved
    TO_MOVE = None 
    
    x, n = 2, 300
    
    dx, dy = width / 4.0, height/3.0
    p1, p2, p3 = PVector(dx, 2*dy), PVector(2*dx, 2*dy - tan(PI/3)*dx), PVector(width-dx, 2*dy)
    
    spiro = TriangleSpirograph(p1, p2, p3, n, x)
    
    background(255)
    stroke(0)
    spiro.draw_triangle()
    
    stroke(0, 0, 0, 100)
    
def draw():
    global spiro, TO_MOVE, p1, p2, p3
    
    if TO_MOVE is not None:
        TO_MOVE.x = mouseX
        TO_MOVE.y = mouseY
        
        background(255)
        triangle(p1.x, p1.y, p2.x, p2.y, p3.x, p3.y)
        
        return
    
    try:
        spiro.draw_next_line()
    except IndexError:
        reset()

def keyPressed():
    global spiro
    
    if key == ' ':
        spiro.PAUSED = not spiro.PAUSED

def mouseClicked():
    global spiro, p1, p2, p3
    """Allows dragging of spirograph vertices upon click"""
    
    diag = sqrt(width ** 2 + height ** 2)
    
    if TO_MOVE is not None:
        TO_MOVE = None
        reset()
        return
    
    if dist(mouseX, mouseY, p1.x, p1.y) <= diag/150.0:
        TO_MOVE = p1
    elif dist(mouseX, mouseY, p2.x, p2.y) <= diag/150.0:
        TO_MOVE = p2
    elif dist(mouseX, mouseY, p3.x, p3.y) <= diag/150.0:
        TO_MOVE = p3
    
