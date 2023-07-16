import tkinter as tk
import webbrowser

window = tk.Tk()
window.title("Course Inquiry Form")

name=tk.Label(window, text="Name:")
name.grid(row=0,column=0)
entry=tk.Entry(window)
entry.grid(row=0,column=1)
source=tk.Label(window, text="Where did you hear about us?")
source.grid(row=1,column=0)
list=tk.StringVar(window)
list.set("Select source")  
source_dropdown=tk.OptionMenu(window, list, "Instagram Ads", "YouTube Ads")
source_dropdown.grid(row=1,column=1)

def faq():
    source = list.get()
    if source =="Instagram Ads":
        webbrowser.open("https://help.instagram.com")
    elif source =="YouTube Ads":
        webbrowser.open("https://support.google.com/youtube")

submit_button=tk.Button(window, text="Submit",command=faq)
submit_button.grid(row=2, column=0)

window.mainloop()