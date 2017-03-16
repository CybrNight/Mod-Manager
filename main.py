import tkinter as tk
from tkinter import filedialog as tkFile
import shutil, os, sys
import delete_window as delWin

LARGE_FONT = ("Verdana",12)

class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.menu = tk.Menu(self, tearoff=0)
        self.menu.add_command(label="Undo", command=self.hello)
        self.menu.add_command(label="Redo", command=self.hello)

        self.frames = {}
        self.frameList = [StartPage]

        for F in self.frameList:
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def hello(self):
        print("Hello")

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, cont):
        LARGE_FONT = ("Verdana",12)
        TITLE_FONT = ("Verdana",16)

        self.mod = ""
        self.validPath = False
        self.selectedItem = tk.StringVar()

        tk.Frame.__init__(self,parent)

        title = tk.Label(self,text="Universal Mod Manager",font=TITLE_FONT)
        title.grid(row=0,column=2)
        title = tk.Label(self,text="Manager for all your mods",font=LARGE_FONT)
        title.grid(row=1,column=2)

        label = tk.Label(self, text="Mods Folder",font=LARGE_FONT)
        label.grid(row=3,column=1)

        label1 = tk.Label(self, text="Mods List",font=LARGE_FONT)
        label1.grid(row=4,column=2)

        self.modDir = tk.Entry(self,width=45)
        self.modDir.grid(row=3,column=2)
        self.modDir.bind("<Return>",lambda x:self.buildList())

        self.modList = tk.Listbox(self,width=45,height=20)
        self.modList.grid(row=5,column=2)
        self.modList.bind("<Delete>",lambda x:self.deleteWindow())
        self.modList.bind("<Button-1>",lambda x:self.setSelected())
        self.modList.bind("<Return>", lambda x:self.deleteWindow())

        dirBrowse = tk.Button(self,text="Browse...",command=lambda :self.openDirectory())
        dirBrowse.grid(column=3,row=3)

    def deleteWindow(self):
        file_path = self.mod+"/"+self.selectedItem.get()

        self.newWindow = tk.Toplevel(self)
        self.app = delWin.DeleteWindow(self.newWindow,self.modList,file_path)



    def addButtons(self):
        self.addBtn = tk.Button(self,text="Add File(s)",command=lambda :self.copyFile())
        self.addBtn.grid(row=5,column=3,sticky="NW")

        self.addFolder = tk.Button(self,text="Add Folder",command=lambda :self.copyFolder())
        self.addFolder.grid(row=5,column=3,pady=40,sticky="NW")

        self.delBtn = tk.Button(self,text="Delete Selected",command=lambda :self.deleteFile())
        self.delBtn.grid(row=5,column=3,pady=80,sticky="NW")

    def deleteButtons(self):
        self.addBtn.destroy()
        self.addFolder.destroy()
        self.delBtn.destroy()

    def openDirectory(self):
        directory = tkFile.askdirectory()
        if (directory == "" and self.mod is not "" and self.validPath):
            directory = self.mod

        try:
            self.modDir.delete(0,tk.END)
        except SyntaxError:
            print("None")

        self.modDir.insert(0,directory)
        self.mod = self.modDir.get()
        print(self.mod)
        self.buildList()

    def copyFile(self):
        if (self.validPath is not True): return

        filesPaths = tkFile.askopenfilenames()

        for filePath in filesPaths:
            shutil.copy2(filePath,self.mod)

        self.buildList()

    def copyFolder(self):
        if (self.validPath is not True): return

        filePath = tkFile.askdirectory()

        shutil.copytree(filePath,self.mod+"/"+os.path.basename(filePath))

        self.buildList()

    def setSelected(self):
        self.selectedItem.set(self.modList.get(tk.ACTIVE))

    def deleteFile(self):
        if (self.validPath is not True): return

        file = self.mod+"/"+self.selectedItem.get()

        if (os.path.isfile(file)):
            os.remove(file)
        else:
            shutil.rmtree(file)

        selected = self.modList.curselection()
        for select in selected:
            self.modList.delete(select)

    def buildList(self):
        try:
            self.mod = self.modDir.get()
            self.modList.delete(0,self.modList.size())

            all = os.listdir(self.mod)
            for file in all:
                self.modList.insert(tk.END,file+os.path.commonpath(file))
                print(os.path.commonpath(file).upper())
            self.validPath = True
            self.addButtons()
        except FileNotFoundError:
            self.validPath = False
            self.modList.delete(0,self.modList.size())
            self.modList.insert(0,"Invalid Path!")
            self.deleteButtons()

app = Application()
app.geometry("640x480")
app.title("Universal Mod Manager")
app.resizable(width=False,height=False)
app.mainloop()