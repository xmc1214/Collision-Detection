x1,y1,r1,x2,y2,r2 = 0,0,25,200,200,40

def setup():
    size(600,400)
    noCursor()

def draw():
    background(255)
    x1,y1 = mouseX,mouseY
    hit = circle_circle(x1,y1,r1,x2,y2,r2)
    if hit:
        fill(255,150,0)
    else:
        fill(0,150,255)
    noStroke()
    ellipse(x2,y2,r2 * 2,r2 * 2)
    fill(0,150)
    noStroke()
    ellipse(x1,y1,r1 * 2,r1 * 2)
    
def circle_circle(x1,y1,r1,x2,y2,r2):
    distX = x1 - x2
    distY = y1 - y2
    distance = sqrt((distX * distX) + (distY * distY))
    if distance <= r1 + r2:
        print(distance)
        return True
    return False
