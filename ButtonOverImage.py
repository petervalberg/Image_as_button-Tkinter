from tkinter import *

count = 0

def shiftImage(event):
    if count % 2 == 0:
        canvas1.itemconfig(button, image=stopImage)

    else:
        canvas1.itemconfig(button, image=playImage)
    globals()['count'] += 1

root = Tk()
root.title('Button over image tkinter canvas')
root.resizable(width=False, height=False)
root.geometry('+750+150')
root.geometry('400x400')
root.configure(bg='SystemButtonFace')

playImage = PhotoImage(file='playButton.png')
stopImage = PhotoImage(file='stopButton.png')
blankImage = PhotoImage(file='blankButton.png')

canvas1 = Canvas(root, width=400, height=400)
button = canvas1.create_image(100, 100, anchor=NW, image=playImage)
blank = canvas1.create_image(100, 100, anchor=NW, image=blankImage, state=NORMAL)
canvas1.tag_bind(blank, "<Button-1>", shiftImage)
canvas1.pack()
      
root.mainloop()



#root.update_idletasks()
#root.update()
#canvas1.itemconfig(blank, state=DISABLED) ...makes blank-button inactive
