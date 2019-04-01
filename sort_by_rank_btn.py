from tkinter import *
from pattern import search
import math
from database_importing import dict_create
import operator

def mainrank():
        di = dict_create()
        def sort_rank():
            distinct_can = []
            output_str = ""
            for i in range(0,len(di)):
                if di[i]["Canteen"] in distinct_can:
                    continue
                else:
                    distinct_can.append(di[i]["Canteen"])

            num_of_dishes = 0
            sum_of_rating = 0
            rate_avg = 0
            canlist = {}
            for i in range(0,len(distinct_can)):
                for j in range(0,len(di)-1):
                    if distinct_can[i] == di[j]["Canteen"]:
                        num_of_dishes += 1
                        sum_of_rating += di[j]["Rating"]
                        
                        if distinct_can[i] == di[j+1]["Canteen"]:
                            pass
                        else:
                            rate_avg = sum_of_rating/num_of_dishes
                            canlist[distinct_can[i]] = rate_avg
                            num_of_dishes = 0
                            sum_of_rating = 0
                            
            sorted_canlist = sorted(canlist.items(), key=operator.itemgetter(1))

            ordered_canlist = list(reversed(sorted_canlist))
            
            for i in range(0,len(ordered_canlist)):
                output_str += str(i+1)
                output_str += ") " 
                output_str += ordered_canlist[i][0]
                output_str += " with rating "
                output_str += str(round(ordered_canlist[i][1],2))
                output_str += "\n"
           

            txt.insert(0.0, output_str)
            txt.insert(0.0, "THe rankings are as follows: \n")

                
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

        title_line = Label(canvas, text = "Sort By Rank")

        btn = Button(canvas, text="Sort By Rank", bg ="green", fg="black", command= sort_rank).grid(row=56, column=1, columnspan = 2)
        btn = Button(canvas, text="Quit", bg ="green", fg="black", command= quit_tk).grid(row=57, column=1, columnspan = 2)
        
        txt = Text(canvas, width=70, height=10, wrap=WORD)
        txt.grid(row=58, column=1, columnspan=2, sticky=W)

        canvas.place(x=200, y=200, anchor=NW)
        root.mainloop()

