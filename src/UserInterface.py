from tkinter import *
import re
from tkinter import messagebox
from tkinter.ttk import *
from time import strftime
global textdata


textdata=""

global flag,flag1,flag2,vlist
vlist=[]
flag=0
flag1=0
flag2=0

global count
count=0
keywordlist=['readnumber','display','add','sub',"multiply","divide","loop upto"]
keywordmap=["int(input(%))","print(%)","%+%","%-%","%*%","%/%","for i in range(%):"]


def checkceriable(txt):
    global vlist
    lst=txt.split('"')[0]
    list=lst.split('=')
    if len(list)>1:
        vlist.append(list[0])


def refn_readnumber(txt):
    global vlist
    lst=txt.split('readnumber')

    if len(lst)>1:
    #     return "error0"
    # else:
        txt=lst[1]
        vtxt=lst[0].split("=")

        for i in vtxt:
            if i != "" or i!=" ":
                print(i,"==========")
                x=re.split(r"\s+", i)
                print(x,"=x")
                vvlst=[]
                for ix in x:
                    if ix!="":
                        vvlst.append(ix)
                if len(vvlst)>1:
                    return "Error : Invalid Variable!"
                elif len(vvlst)==1:



                    if (bool(re.search('^[a-zA-Z0-9_]+$',vvlst[0])) == True):
                        print("valid")
                    else:
                        print(vvlst[0],"error special")
                        return "Error : Invalid Variable!"


                    if re.match('[a-zA-Z_]',vvlst[0][0]):
                        print(vvlst[0],"ok")
                    else:
                        return "Error : Invalid Variable !"
                    vlist.append(vvlst[0])


        # lst=txt.split("")
        return "ok"
def refn_display(txt):
    global vlist
    lst=txt.split('display')

    if len(lst)>1:

        vtxt=lst[-1].split('"')
        print(vtxt,"===========")
        aa=[]
        for i in range(0,len(vtxt),2):
            aa.append(vtxt[i])
        vtxt=''.join(aa)
        aa=vtxt.split(',')
        for i in aa:
            aaa=i.split(" ")
            a3=[]
            print(aaa,"aaa")
            for ai in aaa:
                if ai!="":
                    a3.append(ai)
            print(a3,"a3")
            if len(a3)>1:
                return "Syntax Error!"
            print(vlist,"=============")
            for i in a3:
                if i!="":
                    if i not in vlist:
                        return "Syntax Error"





        return "ok"


#Create an instance of tkinter frame
win= Tk()
w = Label(win,text="keywords")
w.place(relx=0.035,y=20)
w2 = Label (win, text="Terminal")
w2.place(relx=0.45,y=20)
w3 = Label(win,text="Expressions")
w3.place(relx=0.91,y=20)
#Set the geometry
win.geometry("880x620")
win.configure(background='#27325a')
win.resizable(0,0)
photo = PhotoImage(file = "E+.png")
win.iconphoto(False, photo)
win.title('SnapCode')
menubar = Menu(win)



canvas = Canvas(
    win,
    height=540,
    width=84,
    bg="#4a5679"
)
canvas.place(x=10,y=42)

win.config(menu = menubar)

canvas2 = Canvas(
    win,
    height=540,
    width=84,
    bg="#4a5679"
)
canvas2.place(x=788,y=42)

def divc():
    global textdata
    INPUT = t.get("1.0", "end-1c")
    INPUT += "\n" + "divide"
    t.delete("1.0", "end")
    textdata = "divide"
    t.insert('1.0', INPUT)

def area():
    global textdata
    t.delete("1.0", "end")
    textdata='''
display "enter height"
a=readnumber
display "enter base length"
b=readnumber
area=(a*b)/2
display area'''
    t.insert('1.0',textdata)

def display():
    global textdata
    INPUT = t.get("1.0", "end-1c")
    INPUT+="\n"+"display"
    t.delete("1.0", "end")
    textdata= "display"
    t.insert('1.0',INPUT)

def readnumber():
    global textdata
    INPUT = t.get("1.0", "end-1c")
    t.delete("1.0","end")
    INPUT=INPUT+"\n"+ "%=readnumber"
    textdata= INPUT
    t.insert('1.0',textdata)

def loopc():
    global textdata
    INPUT = t.get("1.0", "end-1c")
    t.delete("1.0", "end")
    INPUT = INPUT + "\n" + "loop upto "
    textdata = INPUT
    t.insert('1.0', textdata)

def addcd():
    global textdata
    INPUT = t.get("1.0", "end-1c")
    t.delete("1.0", "end")
    INPUT = INPUT + "\n" + "add"
    textdata = INPUT
    t.insert('1.0', textdata)

def subcd():
    global textdata
    INPUT = t.get("1.0", "end-1c")
    t.delete("1.0", "end")
    INPUT = INPUT + "\n" + "sub"
    textdata = INPUT
    t.insert('1.0', textdata)

def multiplyc():
    global textdata
    INPUT = t.get("1.0", "end-1c")
    t.delete("1.0", "end")
    INPUT = INPUT + "\n" + "multiply"
    textdata = INPUT
    t.insert('1.0', textdata)



def eqc():
    global textdata
    INPUT = t.get("1.0", "end-1c")
    if '%' in INPUT:
        inp=INPUT.split('%')
        print(inp,"++++++++++++++1")
        inp[0]=inp[0]+ "( % = %)"
        print(inp, "++++++++++++++2")
        inp='%'.join(inp)
        print(inp, "++++++++++++++3")
        inp=inp.replace('%)%','%)')
        print(inp, "++++++++++++++4")
        t.delete("1.0", "end")
        t.insert('1.0', inp)
    else:
        t.delete("1.0","end")
        textdata= "(% = %)"
        t.insert('1.0',textdata)


def andc():
    global textdata
    INPUT = t.get("1.0", "end-1c")
    if '%' in INPUT:
        inp=INPUT.split('%')
        print(inp,"++++++++++++++1")
        inp[0]=inp[0]+ "( % and %)"
        print(inp, "++++++++++++++2")
        inp='%'.join(inp)
        print(inp, "++++++++++++++3")
        inp=inp.replace('%)%','%)')
        print(inp, "++++++++++++++4")
        t.delete("1.0", "end")
        t.insert('1.0', inp)
    else:
        t.delete("1.0","end")
        textdata= "(% and %)"
        t.insert('1.0',textdata)

def noteqcd():
    global textdata
    INPUT = t.get("1.0", "end-1c")
    if '%' in INPUT:
        inp=INPUT.split('%')
        print(inp,"++++++++++++++1")
        inp[0]=inp[0]+ "( %!=%)"
        print(inp, "++++++++++++++2")
        inp='%'.join(inp)
        print(inp, "++++++++++++++3")
        inp=inp.replace('%)%','%)')
        print(inp, "++++++++++++++4")
        t.delete("1.0", "end")
        t.insert('1.0', inp)
    else:
        t.delete("1.0","end")
        textdata= "(%!=%)"
        t.insert('1.0',textdata)

def orcdd():
    global textdata
    INPUT = t.get("1.0", "end-1c")
    print(INPUT,"============")
    if '%' in INPUT:
        inp=INPUT.split('%')
        print(inp,"++++++++++++++1")
        inp[0]=inp[0]+ " (% or %)"
        print(inp, "++++++++++++++2")
        inp='%'.join(inp)
        print(inp, "++++++++++++++3")
        inp=inp.replace('%)%','%)')
        print(inp, "++++++++++++++4")
        t.delete("1.0", "end")
        t.insert('1.0', inp)
    else:
        t.delete("1.0","end")
        textdata= "(% or %)"
        t.insert('1.0',textdata)



def motion(event):
    global flag, flag1, flag2
    global count
    x, y = event.x, event.y
    if flag2!=0 and flag1==0:
        print("drop===========")
        print(flag2)
        if flag2==1:
            divc()
        elif flag2==2:
            area()
        elif flag2==3:
            display()
        elif flag2==4:
             readnumber()
        elif flag2==5:
            andc()
        elif flag2==6:
            orcdd()
        elif flag2==7:
            eqc()
        elif flag2==8:
            noteqcd()
        elif flag2==9:
            loopc()
        elif flag2==10:
            addcd()
        elif flag2==11:
            subcd()
        elif flag2==12:
            multiplyc()
        flag2=0

    flag1=0



win.bind('<Motion>', motion)
#Create a canvas object
# canvas= Canvas(win, width= 700, height= 750, bg="SpringGreen2")
#
# #Add a text in Canvas
#
# canvas.create_text(300, 50, fill="black", font=('Helvetica 15 bold'))
# # canvas.pack()
# canvas.place(x=0, y=0)
t = Text(win, width=83, height=34, bg="wheat1")
t.place(x=105, y=40)

def pp():

    global textdata
    # Insert method inserts the text at
    # specified position, Here it is the
    # beginning
    t.delete("1.0", "end")
    textdata='''a=int(input("Enter a number"))
b=int(input("Enter a number"))
if a>b:
     print(a, "is big")
else:
     print (b ,"is big")'''
    t.insert('1.0',textdata)


# buttons####################


def clear():
    t.delete("1.0","end")
def div(x):
    global flag, flag1, flag2
    flag2=1

    flag1=1

    global count
    count=count+1
    # print("=================",x,"========",count)
def aread(x):
    global flag, flag1, flag2
    flag2=2

    flag1=1

    global count
    count=count+1
    # print("=================",x,"========",count)

def displayd(x):
    global flag, flag1, flag2
    flag2=3

    flag1=1

    global count
    count=count+1
    # print("=================",x,"========",count)

def readnumberd(x):
    global flag, flag1, flag2
    flag2=4

    flag1=1

    global count
    count=count+1
    # print("=================",x,"========",count)

def andcd(x):
    global flag, flag1, flag2
    flag2=5

    flag1=1

    global count
    count=count+1

    # print("=================",x,"========",count)

def orcd(x):
    global flag, flag1, flag2
    flag2=6

    flag1=1

    global count
    count=count+1

def eqcd(x):
    global flag, flag1, flag2
    flag2=7

    flag1=1

    global count
    count=count+1

def noteq(x):
    global flag, flag1, flag2
    flag2=8

    flag1=1

    global count
    count=count+1

def loop(x):
    global flag, flag1, flag2
    flag2=9

    flag1=1

    global count
    count=count+1

def addc(x):
    global flag, flag1, flag2
    flag2=10

    flag1=1

    global count
    count=count+1

def subc(x):
    global flag, flag1, flag2
    flag2=11

    flag1=1

    global count
    count=count+1

def multiply(x):
    global flag, flag1, flag2
    flag2=12

    flag1=1

    global count
    count=count+1




def execute():
    exflag=0
    global  vlist
    vlist=[]
    result=""
    INPUT = t.get("1.0", "end-1c").split("\n")
    for i in INPUT:
        print(i)
        print("==============================")
        for j in range(0,len(keywordlist)):
            if keywordlist[j] in i:
                if keywordlist[j]=="readnumber":
                    r=refn_readnumber(i)
                    if r!="ok":
                        print("read number")
                        exflag=1

                        messagebox.showinfo("Error information", r+" on line "+str(j+1))
                        break
                if keywordlist[j]=="display":
                    r=refn_display(i)
                    if r!="ok":
                        print("display")
                        exflag=1

                        messagebox.showinfo("Error information", r+" on line "+str(j+1))
                        break
                if keywordlist[j] == "add":
                    i = i.replace(keywordlist[j], keywordmap[j])
                    ii = i.split(keywordmap[j])[1].split(' ')
                    i = i.split(keywordmap[j])[0]+keywordmap[j]
                    iii=[]
                    for i2 in ii:
                        if i2!="":
                            iii.append(i2)

                    if len(iii)!=2:
                        exflag = 1

                        messagebox.showinfo("Error information", r + " on line " + str(j + 1))
                        break
                    else:

                        i = i.replace("%+", str(iii[0])+"+")
                        i = i.replace("%", str(iii[1]))
                elif keywordlist[j] == "sub":
                    i = i.replace(keywordlist[j], keywordmap[j])
                    ii = i.split(keywordmap[j])[1].split(' ')
                    i = i.split(keywordmap[j])[0]+keywordmap[j]
                    iii=[]
                    for i2 in ii:
                        if i2!="":
                            iii.append(i2)

                    if len(iii)!=2:
                        exflag = 1

                        messagebox.showinfo("Error information", r + " on line " + str(j + 1))
                        break
                    else:

                        i = i.replace("%-", str(iii[0])+"-")
                        i = i.replace("%", str(iii[1]))
                elif keywordlist[j] == "divide":
                    i = i.replace(keywordlist[j], keywordmap[j])
                    ii = i.split(keywordmap[j])[1].split(' ')
                    i = i.split(keywordmap[j])[0]+keywordmap[j]
                    iii=[]
                    for i2 in ii:
                        if i2!="":
                            iii.append(i2)

                    if len(iii)!=2:
                        exflag = 1

                        messagebox.showinfo("Error information", r + " on line " + str(j + 1))
                        break
                    else:

                        i = i.replace("%-", str(iii[0])+"-")
                        i = i.replace("%", str(iii[1]))
                elif keywordlist[j] == "multiply":
                    i = i.replace(keywordlist[j], keywordmap[j])
                    ii = i.split(keywordmap[j])[1].split(' ')
                    i = i.split(keywordmap[j])[0]+keywordmap[j]
                    iii=[]
                    for i2 in ii:
                        if i2!="":
                            iii.append(i2)

                    if len(iii)!=2:
                        exflag = 1

                        messagebox.showinfo("Error information", r + " on line " + str(j + 1))
                        break
                    else:

                        i = i.replace("%-", str(iii[0])+"-")
                        i = i.replace("%", str(iii[1]))
                else:
                    i=i.replace(keywordlist[j],keywordmap[j])
                    ii=i.split(keywordmap[j])[1]
                    i=i.replace(ii,"")
                    i=i.replace("%",ii)
        else:
            checkceriable(i)




        result=result+i+"\n"


    print(result)
    print(vlist,"vlist====")
    result = result + "\ninput()"
    if exflag==0:
        f = open("e.py", "w")
        f.write(result)

        f.close()

        import subprocess
        subprocess.run(['python', 'e.py'])


# keywords ####


B4 = Button(win, text ="display")
B4.bind('<B1-Motion>', displayd)
B4.place(x=16,y=45)

B5 = Button(win, text ="readnumber")
B5.bind('<B1-Motion>', readnumberd)
B5.place(x=16,y=80)

B11 = Button(win,text="loop upto")
B11.bind('<B1-Motion>', loop)
B11.place(x=16,y=115)

B12 = Button(win,text="add")
B12.bind('<B1-Motion>',addc)
B12.place(x=16,y=150)

B13 = Button(win,text="sub")
B13.bind('<B1-Motion>',subc)
B13.place(x=16,y=185)

B2 = Button(win, text ="divide")
B2.bind('<B1-Motion>', div)
B2.place(x=16,y=220)

B14 = Button(win,text="multiply")
B14.bind('<B1-Motion>',multiply)
B14.place(x=16,y=255)




# expressions #####


B7 = Button(win, text = "% and %")
B7.bind('<B1-Motion>', andcd)
B7.place(x=796,y=45)

B8 = Button(win, text="% or %")
B8.bind('<B1-Motion>', orcd)
B8.place(x=796,y=80)

B9 = Button(win, text="% = %")
B9.bind('<B1-Motion>', eqcd)
B9.place(x=796,y=115)

B10 = Button(win, text="% != %")
B10.bind('<B1-Motion>', noteq)
B10.place(x=796,y=150)



# predefined ######


#B = Button(win, text ="Hello", command=pp)
#B.place(x=796,y=485)

#B3 = Button(win, text ="area")
#B3.bind('<B1-Motion>', aread)
#B3.place(x=796,y=520)

# operations #####
# Adding File Menu and commands
file = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=file)
file.add_command(label='Clear', command=clear)

file.add_separator()
file.add_command(label='Exit', command=win.destroy)



edit = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Run', menu = edit)
edit.add_command(label ='Run Module', command = execute)




win.config(menu = menubar)

# B1 = Button(win, text ="Execute", command=execute)
# B1.place(relx=0.018,y=485)
#
# B6 = Button(win, text = "clear", command=clear)
# B6.place(relx=0.018,y=520)



win.mainloop()
