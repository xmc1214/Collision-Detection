x1,y1,w1,h1,x2,y2,w2,h2 = 0,0,200,100,300,200,300,200

def setup():
    size(1000,600)
    noCursor()

def draw():
    background(255)
    x1,y1 = mouseX,mouseY
    hit = rectangle_rectangle(x1,y1,w1,h1,x2,y2,w2,h2)
    if hit:
        fill(255,150,0)
    else:
        fill(0,150,255)
    noStroke()
    rect(x2,y2,w2,h2)
    fill(0,150)
    noStroke()
    rect(x1,y1,w1,h1)

def rectangle_rectangle(x1,y1,w1,h1,x2,y2,w2,h2):
    maxX,maxY = max(x1,x2),max(y1,y2)
    if maxX == x1:
        if maxX > x2 + w2:
            return False
    if maxX == x2:
        if maxX > x1 + w1:
            return False
    if maxY == y1:
        if maxY > y2 + h2:
            return False
    if maxY == y2:
        if maxY > y1 + h1:
            return False
    return True
