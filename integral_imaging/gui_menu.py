from tkinter import *
from tkinter import filedialog

def Load():
    filename = filedialog.askopenfilename(initialdir="d:/office_com_backup/mjcho/", title="Select file",
                                          filetypes=(("JPEG files", "*.jpg"),
                                          ("TIFF files", "*.tiff"),
                                          ("PNG files", "*.png"),
                                          ("all files", "*.*")))
    print(filename)

def Save():
    filename = filedialog.asksaveasfilename(initialdir="d:/office_com_backup/mjcho/", title="Select file",
                                          filetypes=(("JPEG files", "*.jpg"),
                                          ("TIFF files", "*.tiff"),
                                          ("PNG files", "*.png"),
                                          ("all files", "*.*")))
    print(filename)

def domenu():
    print("OK")

root = Tk()
root.title("Integral Imaging")
root.geometry("1920x1080")
root.resizable(False, False)    # x, y 크기 변경 불가
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=domenu)
filemenu.add_command(label="Open", command=Load)
filemenu.add_command(label="Save", command=Save)
filemenu.add_command(label="Save as...", command=Save)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Copy", command=domenu)
editmenu.add_command(label="Paste", command=domenu)
editmenu.add_separator()
editmenu.add_command(label="Delete", command=domenu)
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=domenu)

root.config(menu=menubar)
root.mainloop()



