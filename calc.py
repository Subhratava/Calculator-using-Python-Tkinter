from tkinter import E, W, Tk,Entry,END,Toplevel,Text,Button,Grid,Scrollbar
from turtle import width
from support_fx import *
#import matplotlib.pyplot as plt

global resu
global Ans
Ans = "#"
resu = False
global hist
hist = []

root = Tk()
root.title("Calculator")
root.iconbitmap("calc.ico")
scrollbar_entry = Scrollbar(orient="horizontal")
scrollbar_ans = Scrollbar(orient="horizontal")
e = Entry(root, font=('Arial 18'),xscrollcommand=scrollbar_entry.set,width=20)
e.focus()
scrollbar_entry.config(command=e.xview)
ans_op = Entry(root, font=('Arial 18'),xscrollcommand=scrollbar_ans.set,width=15)
scrollbar_ans.config(command=ans_op.xview)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="we")
ans_op.grid(row=0, column=4, columnspan=1, padx=10, pady=10, sticky="we")
scrollbar_entry.grid(row=7, column=0, columnspan=3, padx=10, pady=10, sticky="we")
scrollbar_ans.grid(row=7, column=3, columnspan=2, padx=10, pady=10, sticky="we")


def button_add(number):
    global resu
    if resu == True:
        clr()
        resu = False
    e.insert(END, number)


def button_answer():
    global Ans
    global resu
    if Ans != "#":
        e.insert(END, Ans)
        resu = False
    else:
        return


def clr():
    e.delete(0, END)
    ans_op.delete(0,END)
    global var1
    var1 = 0


def evaluate(event=None):
    try:
        if ans_op.get() != "":
            ans_op.delete(0,END)
        global resu
        global hist
        temp = auto_complete(e.get())
        #print(temp)
        #temp = e.get()
        hist.append(temp)
        temp = temp.replace(" ", "")
        e.delete(0, END)
        e.insert(END,temp)
        # print(temp)
        x = float(eval(vulneribilty_check(iter(temp))))
        #clr()
        ans_op.insert(0, x)
        global Ans
        Ans = x
        hist.append(x)
        resu = True
    except:
        #global resu
        clr()
        e.insert(END,"ERROR")
        resu = True


def back():
    e.delete(len(e.get())-1, END)

def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb  


e.bind('<Return>', evaluate)


#def fx():
    #return
""" temp = e.get().split("=")
    gfx = Toplevel()
    gfx.title("Grapher")
    gfx.iconbitmap("calc.ico")
    lbl = Label(
        gfx, text="Enter range a,b,p where (a,b ~ I) , Precision", anchor=W)
    lbl = lbl.grid(row=0, column=0)
    rng = Entry(gfx)
    rng.grid(sticky=W+E, row=1, column=0)

    def ca():
        r = rng.get()
        inp = r.split(",")
        a = int(inp[0])
        b = int(inp[1])
        p = int(inp[2])
        d = expn(10, -1*p)
        bins = int((b-a)/d)
        arr = list(linspace(a, b, bins))
        y = [0]*len(arr)
        sol = temp[1]

        for i in range(len(arr)):
            x = arr[i]
            y[i] = eval(sol)
        fig = plt.figure(figsize=(10, 5))
        plt.axhline(0, color='red')
        plt.axvline(0, color='red')
        plt.plot(arr, y)
        plt.show()

    ok = Button(gfx, text="Ok", command=lambda: ca())
    ok.grid(row=2, column=0, sticky=W+E) """


def hst():
    global hist
    history = Toplevel()
    history.title("History")
    history.iconbitmap("calc.ico")
    for i in range(len(hist)):
        w = Text(history, height=1, borderwidth=0,font=('Arial 12'))
        w.insert(1.0, hist[i])
        w.pack()


# numbers
button1 = Button(root, text="1", padx=40, pady=20,
                 command=lambda: button_add(1))
button2 = Button(root, text="2", padx=40, pady=20,
                 command=lambda: button_add(2))
button3 = Button(root, text="3", padx=40, pady=20,
                 command=lambda: button_add(3))
button4 = Button(root, text="4", padx=40, pady=20,
                 command=lambda: button_add(4))
button5 = Button(root, text="5", padx=40, pady=20,
                 command=lambda: button_add(5))
button6 = Button(root, text="6", padx=40, pady=20,
                 command=lambda: button_add(6))
button7 = Button(root, text="7", padx=40, pady=20,
                 command=lambda: button_add(7))
button8 = Button(root, text="8", padx=40, pady=20,
                 command=lambda: button_add(8))
button9 = Button(root, text="9", padx=40, pady=20,
                 command=lambda: button_add(9))
button0 = Button(root, text="0", padx=40, pady=20,
                 command=lambda: button_add(0))

# operators
button_adder = Button(root, text="+", padx=40, pady=20,
                      command=lambda: button_add("+"))
button_sub = Button(root, text="-", padx=40, pady=20,
                    command=lambda: button_add("-"))
button_mul = Button(root, text="*", padx=40, pady=20,
                    command=lambda: button_add("*"))
button_div = Button(root, text="/", padx=40, pady=20,
                    command=lambda: button_add("/"))
button_pr = Button(root, text="(", padx=40, pady=20,
                   command=lambda: button_add("("))
button_pl = Button(root, text=")", padx=40, pady=20,
                   command=lambda: button_add(")"))
button_com = Button(root, text=",", padx=40, pady=20,
                    command=lambda: button_add(","))
button_log = Button(root, text="log10", padx=40, pady=20,
                    command=lambda: button_add("log("))
button_decimal = Button(root, text=".", padx=40, pady=20,
                        command=lambda: button_add("."))
button_logx = Button(root, text="logn(n,m)", padx=40, pady=20,
                     command=lambda: button_add("logn("))  # used logx(base,arg) format
button_equal = Button(root, text="=", padx=40, pady=20,bg="#abcc8b",
                      command=lambda: evaluate())
button_clr = Button(root, text="Clr", padx=40, pady=20, command=lambda: clr())
button_del = Button(root, text="Del", padx=40, pady=20, command=lambda: back())
button_sin = Button(root, text="sin", padx=40, pady=20,
                    command=lambda: button_add("sin("))
button_cos = Button(root, text="cos", padx=40, pady=20,
                    command=lambda: button_add("cos("))
button_tan = Button(root, text="tan", padx=40, pady=20,
                    command=lambda: button_add("tan("))
button_ans = Button(root, text="Ans", padx=40, pady=20,
                    command=lambda: button_answer())
button_pow = Button(root, text="expn(n,m)", padx=40, pady=20,
                    command=lambda: button_add("expn("))
#button_fx = Button(root, text="fx", padx=40, pady=20, command=lambda: fx())
button_hist = Button(root, text="Hist", padx=40,
                     pady=20, command=lambda: hst())
button_sqrt = Button(root, text="Sqrt", padx=40,
                     pady=20, command=lambda: button_add("sqrt("))

# constants
# button_list = [button0, button1, button2, button3, button4, button5, button6, button7, button8, button9, button_adder, button_sub, button_mul, button_div, button_pr, button_pl,
#                button_com, button_log, button_decimal, button_logx, button_decimal, button_equal, button_clr, button_del, button_sin, button_cos, button_tan, button_ans,
#                button_pow, button_hist, button_sqrt]

#print(len(button_list))

for row_number in range(0,8):
    Grid.rowconfigure(root, row_number , weight = 2)

for col_number in range(0,5):
    Grid.columnconfigure(root, col_number , weight = 2)
    
# design
button1.grid(row=1, column=0, sticky="NSEW")
button2.grid(row=1, column=1, sticky="NSEW")
button3.grid(row=1, column=2, sticky="NSEW")
button_pl.grid(row=1, column=3, sticky="NSEW")
button_sin.grid(row=1, column=4, sticky="NSEW")

button4.grid(row=2, column=0, sticky="NSEW")
button5.grid(row=2, column=1, sticky="NSEW")
button6.grid(row=2, column=2, sticky="NSEW")
button_pr.grid(row=2, column=3, sticky="NSEW")
button_cos.grid(row=2, column=4, sticky="NSEW")

button7.grid(row=3, column=0, sticky="NSEW")
button8.grid(row=3, column=1, sticky="NSEW")
button9.grid(row=3, column=2, sticky="NSEW")
button_com.grid(row=3, column=3, sticky="NSEW")
button_tan.grid(row=3, column=4, sticky="NSEW")

button0.grid(row=4, column=0, sticky="NSEW")
button_adder.grid(row=4, column=1, sticky="NSEW")
button_sqrt.grid(row=4, column=2, sticky="NSEW")
button_del.grid(row=4, column=3, sticky="NSEW")
button_pow.grid(row=4, column=4, sticky="NSEW")

button_sub.grid(row=5, column=0, sticky="NSEW")
button_mul.grid(row=5, column=1, sticky="NSEW")
button_div.grid(row=5, column=2, sticky="NSEW")
button_ans.grid(row=5, column=3, sticky="NSEW")
button_hist.grid(row=5, column=4, sticky="NSEW")


button_log.grid(row=6, column=0, sticky="NSEW")
button_decimal.grid(row=6, column=1, sticky="NSEW")
button_logx.grid(row=6, column=2, sticky="NSEW")
#button_fx.grid(row=6, column=3, sticky="NSEW")
button_clr.grid(row=6, column=3, sticky="NSEW")
button_equal.grid(row=6, column=4, sticky="NSEW")

root.mainloop()
