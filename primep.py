'''
    This script was written in python 3.x.
    In order to run this script, please make sure your python version is 3.x or above.
    How to run:
        python primep.py
    or if it doesn't work use this one:
        python3 primep.py
    Author: Pedja <pedja.terzic@hotmail.com>
'''

from random import *
from tkinter import *
import tkinter.messagebox
from tkinter.ttk import Frame, Label, Entry , Button ,Style,Scale




class PRIMEP(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("PRIMEP")
        self.pack(fill=BOTH, expand=True)
        global value
        value = 0
        global var
        var=IntVar()
        global num
        num = StringVar()
        global res
        res = StringVar()
		
   
		
	


    

        

        frame1 = Frame(self,style='My.TFrame')
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text="Enter a number :", width=16,background='orange')
        lbl1.pack(side=LEFT, padx=5, pady=5)

        entry1 = Entry(frame1,textvariable=num,style='My.TEntry')
        entry1.pack(fill=X, padx=5, expand=True)
		
        frame2 = Frame(self,style='My.TFrame')
        frame2.pack(fill=X)

        lbl2 = Label(frame2, text="Set certainty :", width=16,background='orange')
        lbl2.pack(side=LEFT, padx=5, pady=5)

        #entry2 = Entry(frame2,textvariable=cer,style='My.TEntry')
        #entry2.pack(fill=X, padx=5, expand=True)
		
        scale = Scale(frame2, from_=1, to=25,orient=HORIZONTAL,command=self.onScale)
        scale.pack(side=LEFT, padx=5)
		
        #var = IntVar()
        label = Label(frame2, text=1, textvariable=var)
        label.pack(side=LEFT,padx=5)

        
        frame3 = Frame(self,style='My.TFrame')
        frame3.pack(fill=X)

        result = Label(frame3, textvariable=res, width=28,background='orange')
        result.pack(side=LEFT, padx=60, pady=5)

		
        frame4 = Frame(self,style='My.TFrame')
        frame4.pack(fill=X)

        btntest = Button(frame4, text="Test", width=10, command=self.test,style='My.TButton')
        btntest.pack(side=LEFT, anchor=N, padx=5, pady=5)
		
        btnclear = Button(frame4, text="Clear", width=10, command=self.clear,style='My.TButton')
        btnclear.pack(side=LEFT, anchor=N, padx=5, pady=5)
		
        btnclose = Button(frame4, text="Close", width=10, command=self.quit,style='My.TButton')
        btnclose.pack(side=LEFT, anchor=N, padx=5, pady=5)

    def errorMsg(self,msg):
        if msg == 'error':
            tkinter.messagebox.showerror('Error!', 'Something went wrong! Maybe invalid entries')
			
   
    def onScale(self,val):
        v = int(float(val))
        var.set(v)  
    

    def test(self):
        try:
            n = int(num.get())
            k = int(var.get())
            def polynomial(m,b,x):
                p0=1
                p1=x
                l=2
                while l<=m:
                    p=2*x*p1+b*p0
                    p0=p1
                    p1=p
                    l=l+1
                return p
            j=0
            for i in range(1,k+1):
                a=randint(-100,100)
                c=randint(2,n-2)
                if polynomial(n,a,c)%n !=c:
                    value=str(n) + " is composite"
                    res.set(self.makeAsItIs(value))
                    j=j+1
                    break
            if j==0:
                value=str(n) + " is probably prime"
                res.set(self.makeAsItIs(value))

          
        except:
            self.errorMsg('error')
			
    def clear(self):
        try:
            res.set('')
            num.set('')
            
            
        except:
            self.errorMsg('error')
			
    
    def makeAsItIs(self, value):
        return value
	
   
	

	


def main():
	

    root = Tk()
    root.resizable(0,0)
    s = Style()
    s.configure('My.TFrame', background='orange')
    s.configure('My.TButton', background='light gray')
    s.configure('My.TEntry', fieldbackground='light gray')
    root.geometry("300x112")
    primep = PRIMEP(root)
    root.mainloop()

if __name__ == '__main__':
    main()
