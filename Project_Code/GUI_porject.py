from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title("Text Editor")
root.iconbitmap("C:/Users/Erik/Desktop/GUI_Final_Project/Icon/Logo.ico")
root.geometry("1200x800")

#Here I create a Main Frame
The_frame = Frame(root)
The_frame.pack(pady=5)

#Creation of the scrollbar for the text box
text_scroll = Scrollbar(The_frame)
text_scroll.pack(side=RIGHT, fill=Y)

#Here I create My Text Box 
The_text = Text(The_frame, width=97, height=25, font=("Helvetica", 16), selectbackground="green", selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
The_text.pack()

#Config of Scrollbar
text_scroll.config(command=The_text.yview)

root.mainloop()


