from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title("Text Editor")
root.iconbitmap("C:/Users/Erik/Desktop/GUI_Final_Project/Icon/Logo.ico")
root.geometry("1200x800")

#New File Function Creation
def new_file():
	#This delete the previous text
	The_text.delete("1.0", END)
	#The update of the status 
	root.title("New Text")
	status_bar.config(text="New File        ")

#Open File Function Creation
def open_file():
	#Delete text
	The_text.delete("1.0", END)
	#Get filename
	text_file = filedialog.askopenfilename(title="Open File", filetypes=(("Text File", "*.txt"), ("HTML File", "*.html"), ("Python File", "*.py"), ("All Files", "*.*")))
	#Update of the status bar
	name = text_file
	status_bar.config(text=f'{name}'        )
	#Open The File 
	text_file = open(text_file, "r")
	stuff = text_file.read()
	#Add file to the textbox
	The_text.insert(END, stuff)
	#Close the file opened
	text_file.close()

#Save as the File 
def save_as_file():
	text_file = filedialog.asksaveasfilename(defaultextension=".*", title="Save File", filetypes=(("Text File", "*.txt"), ("HTML File", "*.html"), ("Python File", "*.py"), ("All Files", "*.*")))
	if text_file:
		#The update of the status bar
		name = text_file
		status_bar.config(text=f'Saved: {name}'        )
		#Save the File
		text_file = open(text_file, 'w')
		text_file.write(The_text.get(1.0, END))

		#Close The File
		text_file.close()


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

#Creation of the menu
myMenu = Menu(root)
root.config(menu=myMenu)

#Add file 
file_menu = Menu(myMenu)
myMenu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save")
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_command(label="New", command = new_file)
file_menu.add_separator()
file_menu.add_command(label="Exit")

#Add an edit menu
edit_menu = Menu(myMenu)
myMenu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")

#Status bar to Botto of the GUI
status_bar = Label(root, text="Ready        ", anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)



root.mainloop()


