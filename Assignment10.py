import tkinter as tk
import webbrowser as wb
obj=tk.Tk()

#button
e=tk.Entry(obj,font=("Times New Roman",25),width=30)
e.grid(row=0,column=0)

def display():
    s=e.get()   
    wb.open(f"https://www.flipkart.com/search?q={s}") 
    print("Navigating to FlipKart the Search: ",(f"https://www.flipkart.com/search?q={s}"))

b1=tk.Button(obj,text="Search",font=("Times New Roman",25),command=display)
b1.grid(row=1,column=0)

b=tk.Button(obj,text="Close",font=("Times New Roman",30),command=obj.destroy)
b.grid(row=2,column=0)
obj.mainloop()