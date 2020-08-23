from tkinter import *
from PIL import ImageTk,Image
window=Tk()
window.title("FLAMES")
img1=ImageTk.PhotoImage(Image.open("C:/Enter/the/filepath/file_name.jpeg"))
label=Label(image=img1)
l1=Label(window,text="Enter your name :",bg="#F94F60")
e1=Entry(window,width=40,borderwidth=5)
l2=Label(window,text="Enter your crush name :",bg="#F94F60")
e2=Entry(window,width=40,borderwidth=5)



label.grid(rowspan=10,columnspan=3)
l1.grid(row=0,column=0,columnspan=3)
e1.grid(row=1,column=0,columnspan=3)
l2.grid(row=2,column=0,columnspan=3)
e2.grid(row=3,column=0,columnspan=3)

def calc():

    s1=e1.get().strip().lower().split()
    s2=e2.get().strip().lower().split()
    l=['f','l','a','m','e','s']
    a=""
    b=""
    for i in s1:
        a+=i
    for i in s2:
        b+=i
    for i in a:
        if i in b:
            a=a.replace(i,"",1)
            b=b.replace(i,"",1)
    for i in b:
        if i in a:
            b=b.replace(i,'',1)
            a=a.replace(i,'',1)
    a+=b
    while len(l)!=1:
        l.pop((len(a)%len(l))-1)
    if l[0]=='f':
        label=Label(window,text="FRIEND")
    elif l[0]=='l':
        label=Label(window,text="LOVER")
    elif l[0]=='a':
        label=Label(window,text="AFFECTION")
    elif l[0]=='m':
        label=Label(window,text="MARRIAGE")
    elif l[0]=='e':
        label=Label(window,text="ENEMY")
    else:
        label=Label(window,text="SISTER")
    
    label.grid(row=5,column=0,columnspan=3)
    
    


bt=Button(window,text="Predict",command=lambda :calc())
bt.grid(row=4,column=0,padx=5,columnspan=3)



window.mainloop()
