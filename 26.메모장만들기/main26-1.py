from tkinter import *
from tkinter.filedialog import *

def new_file():
    text_area.delete(1.0,END)

def save_file():
    f = asksaveasfile(mode="w",defaultextension=".txt", filetypes=[("Text files",'.txt')])
    text_save = str(text_area.get(1.0, END))
    f.write(text_save)
    f.close()

def maker():
    help_view = Toplevel(window)
    help_view.geometry("300x50+800+300")
    help_view.title("writer")
    lb= Label(help_view,text="making the text box")
    lb.pack()
    print("Writer functionality")

window = Tk()
window.title("메모장")
window.geometry("400x400+800+300")
window.resizable(False, False)

menu = Menu(window)
menu_1 = Menu(menu, tearoff=0) #tearoff는 절취선 모양의 메뉴 0이면 절취선 안보이게 하는 것
menu_1.add_command(label="New file", command=new_file)
menu_1.add_command(label="Save", command=save_file)
menu_1.add_separator()
menu_1.add_command(label="Terminate", command=window.destroy)
menu.add_cascade(label="File", menu=menu_1)

menu_2 = Menu(menu, tearoff=0)
menu_2.add_command(label="Writer", command=maker)
menu.add_cascade(label="Writer", menu=menu_2)

text_area = Text(window)
text_area.grid(row=0, column=0, sticky=N+E+S+W)

button_frame = Frame(window)
button_frame.grid(row=1, column=0, sticky=W)

button_new_file = Button(button_frame, text="New file", command=new_file)
button_new_file.pack(side=LEFT, padx=5)

button_save = Button(button_frame, text="Save", command=save_file)
button_save.pack(side=LEFT, padx=5)

button_terminate = Button(button_frame, text="Terminate", command=window.destroy)
button_terminate.pack(side=LEFT, padx=5)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

window.config(menu=menu)

window.mainloop()
