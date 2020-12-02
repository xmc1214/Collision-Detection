cx = 0
cy = 0
r = 30
sx = 200
sy = 100
sw = 200
sh = 200

def setup():
  size(600,400)
  noStroke()
  
def draw():
  background(255)
  cx = mouseX
  cy = mouseY
  hit = circlerect(cx,cy,r,sx,sy,sw,sh)
  if hit:
    fill(255,150,0)
  else:
    fill(0,150,255)
  rect(sx,sy,sw,sh)
  fill(0,150)
  ellipse(cx,cy,r*2,r*2)

def circlerect(cx,cy,radius,rx,ry,rw,rh):
  testX = cx
  testY = cy
  if cx < rx:      
   testX = rx
  elif cx > rx+rw:
   testX = rx+rw
  if cy < ry:    
    testY = ry
  elif cy > ry+rh:
    testY = ry+rh
  distX = cx-testX
  distY = cy-testY
  distance = sqrt((distX*distX) + (distY*distY))
  if distance <= radius:
    return True
  return False
