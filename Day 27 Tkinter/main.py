from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
#window.minsize(150,100)
window.config(padx=10,pady=10)

def miles_to_km():
    miles=float(Entry1.get())
    km=miles*1.609
    Label3.config(text="{:.2f}".format(km))

#Entry
Entry1=Entry(width=7)
Entry1.grid(row=1,column=1,padx=5,pady=5)
Entry1.get()

#Label
Label1=Label(text="Miles")
Label1.grid(row=1 ,column=2,padx=5,pady=5)

Label2=Label(text="is equal to")
Label2.grid(row=2 ,column=0,padx=5,pady=5)

Label3=Label(text=0)
Label3.grid(row=2 ,column=1,padx=5,pady=5)

Label4=Label(text="Km")
Label4.grid(row=2 ,column=2,padx=5,pady=5)

#Button
Button1=Button(text="Calculate",command=miles_to_km)
Button1.grid(row=3,column=1,padx=5,pady=5)

Exit=Button(text="  Exit  ",command=exit,width=7)
Exit.grid(row=3,column=2)




window.mainloop()
