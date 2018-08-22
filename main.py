# coding=<utf-8>
from tkinter import*
import matplotlib.pyplot as plt
from numpy import*

#Fuction_setting
def show():
    #print("SHOW")
    y1list = []
    y2list = []
    y3list = []
    color = "black"
    xf = int(x_from.get())
    xt = int(x_to.get())
    yf = int(y_from.get())
    yt = int(y_to.get())
    xlist = linspace(xf,xt,100*(xt-xf))
    
    plt.title("Graph")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.xlim([xf,xt])
    plt.ylim([yf,yt])
    if check1.get()==1:
        ex1 = expression1.get()
        for x in xlist:
            y1list.append(eval(ex1))
        plt.plot(xlist,y1list,color,linestyle=style1.get(),label=ex1)
    if check2.get()==1:
        ex2 = expression2.get()
        for x in xlist:
            y2list.append(eval(ex2))
        plt.plot(xlist,y2list,color,linestyle=style2.get(),label=ex2)
    if check3.get()==1:
        ex3 = expression3.get()
        for x in xlist:
            y3list.append(eval(ex3))
        plt.plot(xlist,y3list,color,linestyle=style3.get(),label=ex3)
    if grid_check.get()==1:
        plt.grid()
    if legend_check.get()==1:
        plt.legend()
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))
    plt.show()
        

#Variable_setting
y1list = []
y2list = []
y3list = []
line_styles = ["-","--","-.",":"]


#app_setting
app = Tk()
app.title("Plotting_program")

#app.geometry("400x275")

#Frame_setting
limit_frame = Frame(app)
limit_frame.pack(side=TOP,fill=BOTH,padx=3,pady=3)
expression_frame = Frame(app)
expression_frame.pack(side=TOP,fill=BOTH,padx=3,pady=3)
button_frame = Frame(app)
button_frame.pack(side=TOP,fil=BOTH,padx=3,pady=3)

#Range_setting
Label(limit_frame, text="x_시작").grid(row=0,column=0,sticky=W,padx=5,pady=3)
x_from = Entry(limit_frame)
x_from.grid(row=0,column=1,sticky=W)
Label(limit_frame, text="x_끝").grid(row=1,column=0,sticky=W,padx=5,pady=3)
x_to = Entry(limit_frame)
x_to.grid(row=1,column=1,sticky=W)
Label(limit_frame, text="y_시작").grid(row=2,column=0,sticky=W,padx=5,pady=3)
y_from = Entry(limit_frame)
y_from.grid(row=2,column=1,sticky=W)
Label(limit_frame, text="y_끝").grid(row=3,column=0,sticky=W,padx=5,pady=3)
y_to = Entry(limit_frame)
y_to.grid(row=3,column=1,sticky=W)

#Expression_setting
check1 = IntVar()
check1.set(1)
check2 = IntVar()
check2.set(0)
check3 = IntVar()
check3.set(0)
style1 = StringVar()
style1.set('-')
style2 = StringVar()
style2.set('-')
style3 = StringVar()
style3.set('-')

#수식1
Label(expression_frame, text="수식1").grid(row=4,column=1,sticky=W,padx=5,pady=3)
expression1 = Entry(expression_frame,width=30)
expression1.grid(row=5,column=1,sticky=W,padx=5,pady=3)
Checkbutton(expression_frame, variable = check1).grid(row=4,column=0,sticky=W,pady=3)
OptionMenu(expression_frame,style1,*line_styles).grid(row=5,column=2,sticky=W,pady=3)
#수식2
Label(expression_frame, text="수식2").grid(row=6,column=1,sticky=W,padx=5,pady=3)
expression2 = Entry(expression_frame,width=30)
expression2.grid(row=7,column=1,sticky=W,padx=5,pady=3)
Checkbutton(expression_frame, variable = check2).grid(row=6,column=0,sticky=W,pady=3)
OptionMenu(expression_frame,style2,*line_styles).grid(row=7,column=2,sticky=W,pady=3)
#수식3
Label(expression_frame, text="수식3").grid(row=8,column=1,sticky=W,padx=5,pady=3)
expression3 = Entry(expression_frame,width=30)
expression3.grid(row=9,column=1,sticky=W,padx=5,pady=3)
Checkbutton(expression_frame, variable = check3).grid(row=8,column=0,sticky=W,pady=3)
OptionMenu(expression_frame,style3,*line_styles).grid(row=9,column=2,sticky=W,pady=3)

#Button_setting
grid_check = IntVar()
grid_check.set(0)
legend_check = IntVar()
legend_check.set(0)
show_button = Button(button_frame,text="그래프보기",command=show)
show_button.pack(side=RIGHT,padx=5,pady=5)
Checkbutton(button_frame,text="Grid", variable = grid_check).pack(side=LEFT,padx=5,pady=5)
Checkbutton(button_frame,text="Legend", variable = legend_check).pack(side=LEFT,padx=5,pady=5)


app.mainloop()
