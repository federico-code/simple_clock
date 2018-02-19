def setup():
    global f
    size(500,500)
    f = createFont("Arial",16)
    
def draw():
    global f
    background(50)
    textFont(f,16)
    fill(255)
    s=second()
    m=minute()
    h=hour()
    
    strokeWeight(4)
    stroke(255, 153, 0)
    noFill()
    ellipse(width/2, width/2, s*6, s*6)
    
    stroke(0, 102, 255)
    noFill()
    ellipse(width/2, width/2, m*5, m*5)
    
    stroke(255, 51, 0)
    noFill()
    ellipse(width/2, width/2, h*4, h*4)
    
    fill(255, 51, 0)
    text(str(h),width/2-20,width-20)
    
    fill(0, 102, 255)
    text(str(m),width/2,width-20)
    
    fill(255, 153, 0)
    text(str(s),width/2+20,width-20)
    