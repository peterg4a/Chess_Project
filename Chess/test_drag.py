import os
import tkinter as tk

APP_TITLE = "Drag & Drop Tk Canvas Images"
APP_XPOS = 100
APP_YPOS = 100
APP_WIDTH = 300
APP_HEIGHT = 200

class CreateCanvasObject(object):    

    def __init__(self, canvas, block_name):
        self.canvas = canvas

        self.block_width = 250
        self.block_height = 250

        self.name = block_name

        self.max_speed = 30

        self.win_width = self.canvas.winfo_width()
        self.win_height = self.canvas.winfo_height()

        self.block_main = tk.Frame(self.canvas, bd=10, relief=tk.RAISED)
        self.block_main.pack(side=tk.TOP, fill=tk.BOTH, expand=False, padx=0, pady=0)

        self.block_name = tk.Label(self.block_main, text=block_name, anchor=tk.CENTER, font='Helvetica 10 bold', cursor='fleur')
        self.block_name.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.image_obj = self.canvas.create_window( (0, 0), window=self.block_main, anchor="nw", width=self.block_width, height=self.block_height)

        self.block_name.bind( '<Button1-Motion>', self.move)
        self.block_name.bind( '<ButtonRelease-1>', self.release)
        self.move_flag = False    

        self.canvas.bind("<Configure>", self.configure)


    def configure(self, event):
        self.win_width = event.width
        self.win_height = event.height        


    def move(self, event):

        print('Moving [%s]'%self.name)
        print(event)

        if self.move_flag:

            dx, dy = event.x, event.y

            abs_coord_x, abs_coord_y = self.canvas.coords( self.image_obj )

            cond_1 = abs_coord_x + dx >= 0
            cond_2 = abs_coord_y + dy >= 0
            cond_3 = (abs_coord_x + self.block_width + dx) <= self.win_width
            cond_4 = (abs_coord_y + self.block_height + dy) <= self.win_height

            print('abs_coord_x = %3.2f ; abs_coord_y = %3.2f'%(abs_coord_x, abs_coord_y))
            print('dx = %3.2f ; dy = %3.2f'%(dx, dy))
            print('self.block_width = %3.2f'%(self.block_width))
            print('self.block_height = %3.2f'%(self.block_height))
            print('Cond 1 = %s; Cond 2 = %s; Cond 3 = %s; Cond 4 = %s\n\n'%(cond_1, cond_2, cond_3, cond_4))

            if cond_1 and cond_2 and cond_3 and cond_4:
                self.canvas.move(self.image_obj, dx, dy)

        else:
            self.move_flag = True
            self.canvas.tag_raise(self.image_obj)


    def release(self, event):
        self.move_flag = False



class Application(tk.Frame):

    def __init__(self, master):
        self.master = master
        self.master.protocol("WM_DELETE_WINDOW", self.close)
        tk.Frame.__init__(self, master)

        self.canvas = tk.Canvas(self, width=800, height=800, bg='steelblue', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.block_1 = CreateCanvasObject(canvas=self.canvas, block_name='Thing 1')
        self.block_2 = CreateCanvasObject(canvas=self.canvas, block_name='Thing 2')

    def close(self):
        print("Application-Shutdown")
        self.master.destroy()

def main():
    app_win = tk.Tk()
    app_win.title(APP_TITLE)
    app_win.geometry("+{}+{}".format(APP_XPOS, APP_YPOS))

    Application(app_win).pack(fill='both', expand=True)

    app_win.mainloop()

if __name__ == '__main__':
    main()