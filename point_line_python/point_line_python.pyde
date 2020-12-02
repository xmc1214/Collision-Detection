px,py = 0,0

x1,y1,x2,y2 = 100,300,500,100

def setup():
    size(600,400)
    noCursor()
    
    strokeWeight(10)

def draw():
    background(255)
    
    px = mouseX
    py = mouseY
    
    hit = linePoint(x1,y1,x2,y2,px,py)
    if hit:
        stroke(0,150,0,150)
    else:
        stroke(0,150,255,150)
    line(x1,y1,x2,y2)
    
    stroke(0,150)
    point(px,py)
    
def linePoint(x1,y1,x2,y2,px,py):
    d1 = dist(x1,y1,px,py)
    d2 = dist(x2,y2,px,py)
    
    lineLen = dist(x1,y1,x2,y2)
    
    buffer = 0.1
    
    if lineLen - buffer <= d1 + d2 <= lineLen + buffer:
        return True
    return False
