
sx,sy,sw,sh = 0,0,30,30

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
    
    sx,sy = mouseX,mouseY
    
    hit = polyRect(vertices,sx,sy,sw,sh)
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
    rect(sx,sy,sw,sh)
    
def polyRect(vertices,sx,sy,sw,sh):
    next = 0
    
    for index in range(len(vertices)):
        next = index + 1
        if next == len(vertices):
            next = 0
        vc = vertices[index]
        vn = vertices[next]
        
        collision = lineRect(vc.x,vc.y,vn.x,vn.y,sx,sy,sw,sh)
        if collision:
            return True
    # centerInside = polygonPoint(sx,sy,vertices)
    # if centerInside:
    #     return True
    return False

def lineRect(x1,y1,x2,y2,rx,ry,rw,rh):
   left = lineLine(x1,y1,x2,y2, rx,ry,rx, ry+rh)
   right = lineLine(x1,y1,x2,y2, rx+rw,ry, rx+rw,ry+rh)
   top = lineLine(x1,y1,x2,y2, rx,ry, rx+rw,ry)
   bottom = lineLine(x1,y1,x2,y2, rx,ry+rh, rx+rw,ry+rh)
   
   if left or right or bottom or top:
       return True
   return False


def lineLine( x1,  y1,  x2,  y2,  x3,  y3,  x4,  y4):
   if ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1)) == 0:
    if ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) == 0 and ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)):
        return True
    else:
        return False
   uA = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1))
   uB = ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1))

   if 0 <= uA <= 1 and 0 <= uB <= 1:
     intersectionX = x1 + (uA * (x2-x1))
     intersectionY = y1 + (uA * (y2-y1))
     fill(255,0,0)
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
