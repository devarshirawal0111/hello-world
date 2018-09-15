import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from main import *
from tkinter import *
import re
import numpy as np


def plotFilled(canvas, data):
    # highest y = max_data_value * y_stretch
    y_stretch = 15
    # gap between lower canvas edge and x axis
    y_gap = 20
    # stretch enough to get all data items in
    x_stretch = 0
    x_width = 10
    # gap between left canvas edge and y axis
    x_gap = 20

    for x, y in enumerate(data):
        x0 = x * x_stretch + x * x_width + x_gap
        y0 = c_height - (y * y_stretch + y_gap)
        x1 = x * x_stretch + x * x_width + x_width + x_gap
        y1 = c_height - y_gap
        canvas.create_rectangle(x0, y0, x1, y1, fill="teal", outline="black")
        canvas.create_text(x0, y1, anchor=SW, text=str(y), fill="white")


def refreshAll():
    binSize = int(e1.get())
    num_array = [int(s) for s in re.findall(r'\b\d+\b', e2.get())]

    data = showFilled(nextFit(num_array, binSize))
    plotFilled(c1, data)

    data = showFilled(nextFit_dec(num_array, binSize))
    plotFilled(c2, data)

    data = showFilled(firstFit(num_array, binSize))
    plotFilled(c3, data)

    data = showFilled(firstFit_dec(num_array, binSize))
    plotFilled(c4, data)

    data = showFilled(firstLastFit(num_array, binSize))
    plotFilled(c5, data)

    data = showFilled(bestFit(num_array, binSize))
    plotFilled(c6, data)

    data = showFilled(worstFit(num_array, binSize))
    plotFilled(c7, data)

    #f = Figure()
    #a = f.add_subplot(111)
    #x = np.arange(len(data))
    #a.bar(x, data, width=1.0, facecolor='teal', edgecolor='white')

    #canvas = FigureCanvasTkAgg(f, f1)
    #canvas.draw()
    #canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

root = Tk()
root.title("Bin Packing")
c_width = 300
c_height = 200

topFrame = Frame(root, bg='white')
topFrame.pack(fill="both", expand=True)

bottomFrame = Frame(root, bg='white')
bottomFrame.pack(fill="both", expand=True, side=BOTTOM)

f1 = Frame(topFrame, bg='white')
f1.pack(fill="both", expand=True, side=LEFT)

f2 = Frame(topFrame, bg='white')
f2.pack(fill="both", expand=True, side=LEFT)

f3 = Frame(topFrame, bg='white')
f3.pack(fill="both", expand=True, side=LEFT)

f4 = Frame(topFrame, bg='white')
f4.pack(fill="both", expand=True, side=LEFT)

f5 = Frame(bottomFrame, bg='white')
f5.pack(fill="both", expand=True, side=LEFT)

f6 = Frame(bottomFrame, bg='white')
f6.pack(fill="both", expand=True, side=LEFT)

f7 = Frame(bottomFrame, bg='white')
f7.pack(fill="both", expand=True, side=LEFT)

f8 = Frame(bottomFrame, bg='white')
f8.pack(fill="both", expand=True, side=LEFT)

c1 = Canvas(f1, bg='white')
c1.pack(fill="both", expand=True)

c2 = Canvas(f2, bg='white')
c2.pack(fill="both", expand=True)

c3 = Canvas(f3, bg='white')
c3.pack(fill="both", expand=True)

c4 = Canvas(f4, bg='white')
c4.pack(fill="both", expand=True)

c5 = Canvas(f5, bg='white')
c5.pack(fill="both", expand=True)

c6 = Canvas(f6, bg='white')
c6.pack(fill="both", expand=True)

c7 = Canvas(f7, bg='white')
c7.pack(fill="both", expand=True)

c8 = Canvas(f8, bg='white')
c8.pack(fill="both", expand=True)

l1 = Label(c1, text='nextFit')
l1.grid(row=0, column=0, sticky=NW)

l2 = Label(c2, text='nextFit_dec')
l2.grid(row=0, column=1, sticky=NW)

l3 = Label(c3, text='firstFit')
l3.grid(row=0, column=2, sticky=NW)

l4 = Label(c4, text='firstFit_dec')
l4.grid(row=0, column=3, sticky=NW)

l5 = Label(c5, text='firstLastFit')
l5.grid(row=1, column=0, sticky=NW)

l6 = Label(c6, text='bestFit')
l6.grid(row=1, column=1, sticky=NW)

l7 = Label(c7, text='worstFit')
l7.grid(row=1, column=2, sticky=NW)

Label(c8, text="Bin size:").grid(row=0)
Label(c8, text=" Items:  ").grid(row=1)

e1 = Entry(c8)
e2 = Entry(c8)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(c8, text='Run', command=refreshAll).grid(row=3, column=1, sticky=W, pady=4)

root.mainloop()
