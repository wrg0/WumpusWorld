#!/usr/bin/env python
import Tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid().columnconfigure()
        self.createWidgets(4,3)

    def sayHello(self):
        print 'hello wumpus world'

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit',
            command= self.quit )
        self.quitButton.grid()
        self.startButton = tk.Button(self, text='start',
            command=self.sayHello )
        self.startButton.grid()

app = Application()
app.master.title('Wumpus World')
app.mainloop()
