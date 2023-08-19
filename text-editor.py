from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

filename = None

# creates a new file with the name untitled and deletes all text within the text box
def newFile():
    global filename
    filename = 'Untitled'
    text.delete(0.0, END)

# gets all text from the textbox and writes it to a file
def saveFile():
    global filename
    if filename is None:
        saveAs()
    else:
        t = text.get(0.0, END)
        try:
            with open(filename, 'w') as f:
                f.write(t)
        except Exception as e:
            messagebox.showerror(title='Error', message=f"An error occurred while saving the file: {str(e)}")



def saveAs():
    global filename
    f = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=[('Text Files', '*.txt')])
    if f is not None:
        filename = f.name
        t = text.get(0.0, END)
        try:
            f.write(t.rstrip())
        except:
            messagebox.showerror(title='Oops!', message='Unable to save file')
        finally:
            f.close()


def openFile():
    global filename
    f = filedialog.askopenfile(mode='r', filetypes=[('Text Files', '*.txt')])
    if f is not None:
        t = f.read()
        text.delete(0.0, END)
        text.insert(0.0, t)
        f.close()


root = Tk()
root.title("My Python Text Editor")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)

text = Text(root, width = 400, height = 400)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label='New', command=newFile)
filemenu.add_command(label='Open', command=openFile)
filemenu.add_command(label='Save', command=saveFile)
filemenu.add_command(label='Save As', command=saveAs)
filemenu.add_separator()
filemenu.add_command(label='Quit', command=root.quit)
menubar.add_cascade(label='File', menu=filemenu)

root.config(menu=menubar)
root.mainloop()


