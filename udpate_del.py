from tkinter import *
from tkinter import messagebox
from pattern import search
import math
from database_importing import dict_create
from del_fn import delet

def delete():
        def continue_setup():
                txt.delete('end')
                sel_can,sel_dish = dft_val.get().split(" : ")
                delet(sel_can, sel_dish)
                messagebox.showinfo("Title", sel_dish + " in " + sel_can + " deleted successfully")
                root.destroy()
                from intro import mainfile
                mainfile()


                


        di = dict_create()
        def quit_tk():
                root.destroy()
                from intro import mainfile
                mainfile()
        root = Tk()
        root.geometry ("900x700")

        background_image = PhotoImage(file = "images/Webp.net-resizeimage.png")
        background_label = Label(root, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        dishlist = []
        for i in range(0,len(di)):
                appendable_str = di[i]["Canteen"] + " : " + di[i]["Dish"]
                dishlist.append(appendable_str)

        dft_val = StringVar(root)
        dft_val.set(sorted(dishlist)[0]) # default value

        canvas = Canvas(root, bg = 'white', height=100, width=70)

        entry1 = OptionMenu(canvas, dft_val, *sorted(dishlist))


        title_line = Label(canvas, text = "Search by Canteen")
        line1 = Label(canvas, text = "Search Canteen")


        title_line.grid(row=49, column=1, columnspan=2)
        line1.grid (row=50, column=1)
        entry1.grid (row=50, column=2)

        #quitbtn = Button(root, image="exitbtn.png", command=root.quit).grid(row=4, column=0)
        txt = Text(canvas, width=70, height=10, wrap=WORD)
        txt.grid(row=52, column=1, columnspan=2, sticky=W)
            
        btn = Button(canvas, text="Delete This Dish", bg ="green", fg="black", command = continue_setup).grid(row=51, column=2)
        btn2 = Button(canvas, text="Quit", bg ="green", fg="black", command= quit_tk).grid(row=52, column=2)    
   
        canvas.place(x=200, y=200, anchor=NW)
        root.mainloop()
