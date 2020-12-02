x1 = 0
y1 = 0
x2 = 10
y2 = 10

x3 = 100   
y3 = 300
x4 = 500
y4 = 100


def setup():
  size(600,400)
  strokeWeight(5)


def draw():
  background(255)

  x1 = mouseX
  y1 = mouseY

  hit = lineLine(x1,y1,x2,y2, x3,y3,x4,y4)
  if hit:
     stroke(255,150,0, 150)
  else:
     stroke(0,150,255, 150)
  line(x3,y3, x4,y4)
  stroke(0, 150)
  line(x1,y1, x2,y2)


def lineLine( x1,  y1,  x2,  y2,  x3,  y3,  x4,  y4):

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
