from tkinter import *
from pattern import search
import math
from database_importing import dict_create


def search_food():
        di = dict_create()
        def search_data():
                txt.delete('end')
                foodname = entry1.get()
                foodnames = str(foodname)
                minrate = entry2.get()
                pricerange = entry3.get()
                minrates = str(minrate)
                priceranges = str(pricerange)
                veg_check = dft_val.get()
                halal_check = dft_val2.get()
                
                sentence = sentence = "\nSearching for " + foodnames + " that has a minimum rating of " + minrates + " and price range between " + priceranges + "\n"
                dishes = search(foodnames,minrates,priceranges, veg_check, halal_check, search_type = 'Dish')

                txt.insert(0.0, dishes)
                txt.insert(0.0, sentence)
        def quit_tk():
                root.destroy()
                from intro import mainfile
                mainfile()

        root = Tk()
        root.geometry ("900x700")

        background_image = PhotoImage(file = "images/Webp.net-resizeimage.png")
        background_label = Label(root, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        canvas = Canvas(root, bg = 'white', height=100, width=70)

        title_line = Label(canvas, text = "Search by Food")
        line1 = Label(canvas, text = "Search Food")
        line2 = Label(canvas, text = "Minimun Rating (inclusive)")
        line3 = Label(canvas, text = "Price Range (inclusive): format: min-max")
        line4 = Label(canvas, text = "Vegetarian")
        line5 = Label(canvas, text = "Halal")
        
        entry1 = Entry(canvas)
        entry2 = Entry(canvas)
        #entryy2 = str(entry2)
        entry3 = Entry(canvas)
        true_false_veg = ["True","False"]
        true_false_hal = ["True","False"]
        
        dft_val = StringVar(root)
        dft_val2 = StringVar(root)
        dft_val.set(true_false_veg[0])
        dft_val2.set(true_false_hal[0])
        
        entry4 = OptionMenu(canvas, dft_val, *true_false_veg)
        entry5 = OptionMenu(canvas, dft_val2, *true_false_hal)

        
        #entryy3 = str(entry3)

        title_line.grid(row=49, column=1, columnspan=2)
        line1.grid (row=50, column=1)
        line2.grid (row=51, column=1)
        line3.grid (row=52, column=1)
        line4.grid (row=53, column=1)
        line5.grid (row=54, column=1)
        entry1.grid (row=50, column=2)
        entry2.grid (row=51, column=2)
        entry3.grid (row=52, column=2)
        entry4.grid (row=53, column=2)
        entry5.grid (row=54, column=2)

        #quitbtn = Button(root, image="exitbtn.png", command=root.quit).grid(row=4, column=0)

            
        btn = Button(canvas, text="Search", bg ="green", fg="black", command= search_data).grid(row=56, column=2)
        btn2 = Button(canvas, text="Quit", bg ="green", fg="black", command= quit_tk).grid(row=57, column=2)
        txt = Text(canvas, width=70, height=10, wrap=WORD)
        txt.grid(row=58, column=1, columnspan=2, sticky=W)

        canvas.place(x=200, y=200, anchor=NW)
        root.mainloop()

