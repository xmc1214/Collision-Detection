cx,cy,r = 0,0,30

vertices = []

def setup():
    size(600,400)
    noStroke()
    
    vertices.append(PVector(200,100))
    vertices.append(PVector(400,100))
    vertices.append(PVector(350,300))
    vertices.append(PVector(250,300))

def draw():
    background(255)
    
    cx,cy = mouseX,mouseY
    
    hit = polyCircle(vertices,cx,cy,r)
    if hit:
        fill(255,150,0)
    else:
        fill(0,150,255)
    noStroke()
    beginShape()
    for v in vertices:
        vertex(v.x,v.y)
    endShape()
    
    fill(0,150)
    ellipse(cx,cy,r * 2,r * 2)

def polyCircle(vertices,cx,cy,r):
    next = 0
    
    for index in range(len(vertices)):
        next = index + 1
        if next == len(vertices):
            next = 0
        vc = vertices[index]
        vn = vertices[next]
        
        collision = lineCircle(vc.x,vc.y,vn.x,vn.y,cx,cy,r)
        if collision:
            return True
    centerInside = polygonPoint(cx,cy,vertices)
    if centerInside:
        return True
    return False

def polygonPoint(px,py,vertices):
    collision = False
    next = 0
    
    for index in range(len(vertices)):
        next = index + 1
        if next == len(vertices):
            next = 0
        vc = vertices[index]
        vn = vertices[next]
        
        if (((vc.y > py and vn.y < py) or (vc.y < py and vn.y > py)) and
         (px < (vn.x-vc.x)*(py-vc.y) / (vn.y-vc.y)+vc.x)):
            collision = not collision
    return collision
    
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
