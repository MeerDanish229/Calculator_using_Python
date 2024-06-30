from tkinter import *

def btnClick(number):
    global val
    val = val+str(number)
    data.set(val)

def btnClear():
    global val
    val = ""
    data.set("")

def btnEquals():
    global val
    try:
        result = eval(val)
        data.set(result)
    except Exception as e:
        data.set("Error")  


root=Tk()
root.title("Codexcue_Calculator")
root.geometry("361x381+500+100")
root.resizable(False,False)
val=""


data = StringVar()

resultBox= Entry(root, bd=29, bg="black", font=("ariel",20),justify="right",foreground="white",textvariable=data)
resultBox.grid(row=0 ,columnspan=4)

btn_add=Button(root,text="+",font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda :btnClick('+'))
btn_add.grid(row=1,column=3)
btn9=Button(root,text="9",font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda :btnClick('9'))
btn9.grid(row=1,column=2)
btn8=Button(root,text="8",font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda :btnClick('8'))
btn8.grid(row=1,column=1)
btn7=Button(root,text="7",font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda :btnClick('7'))
btn7.grid(row=1,column=0)

btn_subtract=Button(root,text="-",font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda :btnClick('-'))
btn_subtract.grid(row=2,column=3)
btn6=Button(root,text="6",font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda :btnClick('6'))
btn6.grid(row=2,column=2)
btn5=Button(root,text="5",font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda :btnClick('5'))
btn5.grid(row=2,column=1)
btn4=Button(root,text="4",font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda :btnClick('4'))
btn4.grid(row=2,column=0)

btn_multiply=Button(root,text="*",font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda :btnClick('*'))
btn_multiply.grid(row=3,column=3)
btn3=Button(root,text="3",font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda :btnClick('3'))
btn3.grid(row=3,column=2)
btn2=Button(root,text="2",font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda :btnClick('2'))
btn2.grid(row=3,column=1)
btn1=Button(root,text="1",font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda :btnClick('1'))
btn1.grid(row=3,column=0)

btn_divide=Button(root,text="÷",font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda :btnClick('/'))
btn_divide.grid(row=4,column=3)
btn_equal=Button(root,text="=",font=("ariel",12,"bold"),bd=12,height=2,width=6,command=btnEquals)
btn_equal.grid(row=4,column=2)
btn0=Button(root,text="0",font=("ariel",12,"bold"),bd=12,height=2,width=6,command=lambda: btnClick('0'))
btn0.grid(row=4,column=1)
btn_clear=Button(root,text="C",font=("ariel",12,"bold"),bd=12,height=2,width=6,command=btnClear)
btn_clear.grid(row=4,column=0)

root.mainloop()