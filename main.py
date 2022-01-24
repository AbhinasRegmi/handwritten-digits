#! /usr/bin/python3


#we will create gui window where we can draw our digits
#and let the model decide which digit is being drawn

from tkinter import *
import os
from tkinter import filedialog
from PIL import Image
import test as tt

#clear the console
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
clearConsole()

class main_:
    def __init__(self, main):
        self.main = main
        self.color_fg = 'black'
        self.color_bg = 'white'
        self.old_x = None
        self.old_y = None
        self.penwidth = 3
        self.drawWidgets()
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def paint(self, e):
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, e.x, e.y, width=self.penwidth, fill=self.color_fg, capstyle=ROUND, smooth=True)

        self.old_x = e.x
        self.old_y = e.y

    def reset(self, e):
        self.old_x = None
        self.old_y = None

    def clear(self):

        #save the image
        self.c.postscript(file='image.eps')
        img = Image.open('image.eps')
        img.save('image.png', 'png')

        #give path of image to the model
        #the path will always be image.png
        tt.locateImage('image.png')

        #clear the canvas to next drawing
        self.c.delete(ALL)

        #after the prediction delete the temp image
        os.remove('image.png')
        os.remove('image.eps')

    def openFile(self):
        self.file_path = filedialog.askopenfilename()

        #now pass the file path to the model
        if self.file_path:
            tt.locateImage(self.file_path)
        
    def drawWidgets(self):
        self.controls = Frame(self.main, padx = 5, pady = 5)
        
        self.c = Canvas(self.main, width = 125, height =125, bg=self.color_bg)
        self.c.pack(fill=BOTH, expand=True)

        #we need to extract data when the drawing is done
        menu = Menu(self.main)
        self.main.config(menu=menu)
        File = Menu(menu)
        menu.add_cascade(label='File', menu=File)
        File.add_command(label='Predict Number', command=self.clear)
        File.add_command(label='Upload', command=self.openFile)


if __name__ == '__main__':
    root = Tk()
    main_(root)
    root.title('Digit Classification')
    root.mainloop()

