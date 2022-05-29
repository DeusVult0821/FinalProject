from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
import os, sys
import win32print
import win32api

root = Tk()
root.title("Text Editor")
root.iconbitmap("C:/Users/Erik/Desktop/GUI_Final_Project/Icon/Logo.ico")
root.geometry("1200x800")

global open_status_name
open_status_name = False

global selected
selected = False

#New File Function Creation
def new_file():
	#This delete the previous text
	The_text.delete("1.0", END)
	#The update of the status 
	root.title("New Text")
	status_bar.config(text="New File        ")

	global open_status_name
	open_status_name = False

#Open File Function Creation
def open_file():
	#Delete text
	The_text.delete("1.0", END)
	
	#Get filename
	text_file = filedialog.askopenfilename(title="Open File", filetypes=(("Text File", "*.txt"), ("HTML File", "*.html"), ("Python File", "*.py"), ("All Files", "*.*")))
	
	#Check if there is a file name
	if text_file:
		#Makening sure that works
		global open_status_name
		open_status_name = text_file

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

#Save file
def save_file():
	global open_status_name
	if open_status_name:
		#Save the File
		text_file = open(open_status_name, 'w')
		text_file.write(The_text.get(1.0, END))

		#Close The File
		text_file.close()
		
		#Status update
		status_bar.config(text=f'Saved: {open_status_name}'        )
	else:
		save_as_file()

#Cut Tool
def cut_text(e):
	global selected
	#Check keyboard shortcut
	if e:
		selected = root.clipboard_get()
	else:
		if The_text.selection_get():
			#Get selected text from the text box
			selected = The_text.selection_get()
			#deleted
			The_text.delete("sel.first", "sel.last")
			#CLear The board
			root.clipboard_get()
			root.clipboard_append(selected)


#Copy Tool
def copy_text(e):
	global selected
	#check keyboards shourtcut
	if e:
		selected = root.clipboard_get()
	else:
		if The_text.selection_get():
			#Gets the text selected
			selected = The_text.selection_get()
			#CLear The board
			root.clipboard_get()
			root.clipboard_append(selected)

#Paste Tool
def paste_text(e):
	global selected
	#Check shortcut
	if e:
		selected = root.clipboard_get()
	else:
		if selected:
			position = The_text.index(INSERT)
			The_text.insert(position, selected)

#Bold the text
def bold_it():
	#Creation of the font
	bold_font = font.Font(The_text, The_text.cget("font"))
	bold_font.configure(weight="bold")

	#The config of a tag
	The_text.tag_configure("bold", font=bold_font)

	current_tags = The_text.tag_names("sel.first")

	if "bold" in current_tags:
		The_text.tag_remove("bold", "sel.first", "sel.last")
	else:
		The_text.tag_add("bold", "sel.first", "sel.last")

#Italics the text
def italics_it():
	#Creation of the font
	italics_font = font.Font(The_text, The_text.cget("font"))
	italics_font.configure(slant="italic")

	#The config of a tag
	The_text.tag_configure("italic", font=italics_font)

	current_tags = The_text.tag_names("sel.first")

	if "italic" in current_tags:
		The_text.tag_remove("italic", "sel.first", "sel.last")
	else:
		The_text.tag_add("italic", "sel.first", "sel.last")

#Change color of the text
def text_color():
	#Chouse a color
	The_color = colorchooser.askcolor()[1]
	if The_color:
		#Creation of the font
		color_font = font.Font(The_text, The_text.cget("font"))

		#The config of a tag
		The_text.tag_configure("color_text", font=color_font, foreground=The_color)

		current_tags = The_text.tag_names("sel.first")

		if "color_text" in current_tags:
			The_text.tag_remove("color_text", "sel.first", "sel.last")
		else:
			The_text.tag_add("color_text", "sel.first", "sel.last")

#Chenge the background color
def bg_color():
	The_color = colorchooser.askcolor()[1]
	if The_color:
		The_text.config(bg=The_color)

#Change all the text color
def all_text_color():
	The_color = colorchooser.askcolor()[1]
	if The_color:
		The_text.config(fg=The_color)

#Primt function
def print_file():
	print_name = win32print.GetDefaultPrinter()
	status_bar.config(text=print_name)
	file_to_print = filedialog.askopenfilename(title="Open File", filetypes=(("Text File", "*.txt"), ("HTML File", "*.html"), ("Python File", "*.py"), ("All Files", "*.*")))
	if file_to_print:
		win32api.ShellExecute(0, "primt", file_to_print, None, ".", 0)

#Select all the text
def select_all(e):
	#Add sel tag to get all the tags of the text
	The_text.tag_add('sel', '1.0', 'end')

#Clear All the Text
def clear_all():
	The_text.delete(1.0, END)

#Here I put a toolbar frame 
toolbar_frame = Frame(root)
toolbar_frame.pack(fill=X)


#Here I create a Main Frame
The_frame = Frame(root)
The_frame.pack(pady=5)

#Creation of the scrollbar for the text box
text_scroll = Scrollbar(The_frame)
text_scroll.pack(side=RIGHT, fill=Y)

#Here is the creation of the scrollbar horizontal
hor_scroll = Scrollbar(The_frame, orient='horizontal')
hor_scroll.pack(side=BOTTOM, fill=X)

#Here I create My Text Box 
The_text = Text(The_frame, width=97, height=25, font=("Helvetica", 16), selectbackground="green", selectforeground="black", undo=True, yscrollcommand=text_scroll.set, wrap="none", xscrollcommand=hor_scroll.set)
The_text.pack()

#Config of Scrollbar
text_scroll.config(command=The_text.yview)
hor_scroll.config(command=The_text.xview)

#Creation of the menu
myMenu = Menu(root)
root.config(menu=myMenu)

#Add file 
file_menu = Menu(myMenu)
myMenu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_command(label="New", command = new_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
file_menu.add_separator()
file_menu.add_command(label="Print", command=print_file)



#Add an edit menu
edit_menu = Menu(myMenu)
myMenu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Copy", command=lambda: copy_text(False), accelerator="(Ctrl+c)")
edit_menu.add_command(label="Paste", command=lambda: paste_text(False), accelerator="(Ctrl+v)")
edit_menu.add_command(label="Cut", command=lambda: cut_text(False), accelerator="(Ctrl+x)")
edit_menu.add_command(label="Undo", command=The_text.edit_undo, accelerator="(Ctrl+z)")
edit_menu.add_command(label="Redo", command=The_text.edit_redo, accelerator="(Ctrl+y)")
file_menu.add_separator()
edit_menu.add_command(label="Select All", command=lambda: select_all(True), accelerator="(Ctrl+A)")
edit_menu.add_command(label="Clear", command=clear_all, accelerator="(Ctrl+a)")


#The color Menu
color_menu = Menu(myMenu)
myMenu.add_cascade(label="Colors", menu=color_menu)
color_menu.add_command(label="Change selected Text", command=text_color)
color_menu.add_command(label="Change all the text", command=all_text_color)
color_menu.add_command(label="Change background", command=bg_color)

#Status bar to Botto of the GUI
status_bar = Label(root, text="Ready        ", anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=12)

#Edit Bindings 
root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-v>', paste_text)
#Select Binding
root.bind('Control-A', select_all)
root.bind('Control-a', select_all)

#Create Buttons 
#Bold button
bold_button = Button(toolbar_frame, text="Bold", command=bold_it)
bold_button.grid(row=0, column=0, sticky=W, padx=5)
#Italics button
italics_button = Button(toolbar_frame, text="Italics", command=italics_it)
italics_button.grid(row=0, column=1, padx=5)

#Undo and Redo buttom
undo_button = Button(toolbar_frame, text="Undo", command=The_text.edit_undo)
undo_button.grid(row=0, column=2, padx=5)
redo_button = Button(toolbar_frame, text="Redo", command=The_text.edit_redo)
redo_button.grid(row=0, column=3, padx=5)

#Text Color
color_text_button = Button(toolbar_frame, text="Text Color", command=text_color)
color_text_button.grid(row=0, column=4, padx=5)

root.mainloop()