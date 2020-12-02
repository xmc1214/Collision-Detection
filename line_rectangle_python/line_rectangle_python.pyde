x1,y1,x2,y2,sx,sy,sw,sh = 0,0,0,0,200,100,200,200

def setup():
    size(600,400)
    strokeWeight(5)
    
def draw():
    background(255)
    x1,y1 = mouseX,mouseY
    hit = lineRect(x1,y1,x2,y2,sx,sy,sw,sh)
    if hit:
        fill(255,150,0)
    else:
        fill(0,150,255)
    noStroke()
    rect(sx,sy,sw,sh)
    stroke(0,150)
    line(x1,y1,x2,y2)

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
     noStroke()
     ellipse(intersectionX,intersectionY, 20,20)
     return True
  
   return False
