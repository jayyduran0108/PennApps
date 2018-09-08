### the floor is fucking lava 

import random
from tkinter import *
'''
model, view, control 

init 

different environments (class/oop)

mousePressed

mouseMoved
keyPressed 
timerFired

personWalking

redrawAll

drawstart 

loadImage(data, filename): 

loadGif(data): 
   '''
   
def init(data): 
    data.mode = 'start'
    data.personx = 0
    data.persony = data.height
    data.level = 'game'
    data.debrispos = []
    loadGif(data)
    data.count = 0
    
def loadGif(data):
    data.starGif = dict()
    for i in range(48):
        data.starGif[i] = PhotoImage(file="stars.gif", format="gif -index "+str(i))

def drawDebris(canvas, data):
    for item in data.debrispos: 
        size = 5
        x = item[0]
        y = item[1]
        canvas.create_rectangle(x, y, x+size, y+size)

def move(data):
    data.personx += 1
    for item in data.debrispos:
        if (data.personx, data.persony) == item:
            data.mode = 'dead'
    if data.personx > data.width: 
        data.level = 'fin'        

def mousePressed(event,data):
    pass

def keyPressed(event, data):
    if data.mode == 'start':
        data.mode = "play"
    pass

def timerFired(data):
    move(data)

def redrawAll(canvas, data):
    if data.mode == 'start':
        canvas.create_text(data.width//2, data.height//2, text="hello world press any key to play")
    elif data.mode == "play":
        
        yawn = data.starGif[0]
        
        data.count += 1 
        starbg =  data.starGif[data.count%48] 
        
        canvas.create_image(0, 0, image=starbg) 
        
        canvas.create_oval(data.personx, data.persony, data.personx+10, data.persony+10) 
        drawDebris(canvas,data)
    

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)
        
    def mouseMovedWrapper(event, canvas, data):
        mouseMovedWrapper(event, data)
        redrawAllWrapper(canvas,data)    

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
        
    
    root = Tk()
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    root.bind("<Motion>", lambda event: mouseMovedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")
    
def main():
    run(500,500)
    
if __name__ == '__main__':
    main()