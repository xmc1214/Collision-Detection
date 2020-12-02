cx,cy,r = 0,0,30

x1,y1,x2,y2 = 200,400,800,100

def setup():
    size(1000,800)
    strokeWeight(5)

def draw():
    background(255)
    
    cx,cy = mouseX,mouseY
    
    hit = lineCircle(x1,y1,x2,y2,cx,cy,r)
    if hit:
        stroke(255,150,0,150)
    else:
        stroke(0,150,255,150)
    line(x1,y1,x2,y2)
    
    fill(0,150,255,150)
    noStroke()
    ellipse(cx,cy,r * 2,r * 2)

def lineCircle(x1,y1,x2,y2,cx,cy,r):
    inside1 = pointCircle(x1,y1,cx,cy,r)
    inside2 = pointCircle(x2,y2,cx,cy,r)
    
    
    if inside1 or inside2:
        return True
    distX = x1 - x2
    distY = y1 - y2
    lineLen = sqrt( (distX*distX) + (distY*distY) )
    
    dot = ((cx - x1) * (x2 - x1) + (cy - y1) * (y2 - y1)) / pow(lineLen,2)
    
    closestX = x1 + (dot * (x2 - x1))
    closestY = y1 + (dot * (y2 - y1))
    
    onSegment = linePoint(x1,y1,x2,y2,closestX,closestY)
    if not onSegment:
        return False
    fill(255,0,0)
    noStroke()
    ellipse(closestX,closestY,20,20)
    
    
    distX = closestX - cx
    distY = closestY - cy
    distance = sqrt( (distX*distX) + (distY*distY) )
    if distance <= r:
        return True
    return False

def pointCircle(px,py,cx,cy,r):
    
    distX = px - cx
    distY = py - cy
    distance = sqrt( (distX*distX) + (distY*distY) )
    if distance <= r:
        return True
    return False


def linePoint(x1,y1,x2,y2,px,py):
    d1 = dist(x1,y1,px,py)
    d2 = dist(x2,y2,px,py)
    
    lineLen = dist(x1,y1,x2,y2)
    
    buffer = 0.1
    
    if lineLen - buffer <= d1 + d2 <= lineLen + buffer:
        return True
    return False
