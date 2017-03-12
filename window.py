import tkinter as tk
from tkinter import filedialog as tkFile
import shutil, os, sys

class StartPage(tk.Frame):

    def __init__(self, parent, cont):
        LARGE_FONT = ("Verdana",12)
        TITLE_FONT = ("Verdana",16)

        self.mod = ""

        tk.Frame.__init__(self,parent)

        title = tk.Label(self,text="Universal Mod Manager",font=TITLE_FONT)
        title.pack(side="top")
        title = tk.Label(self,text="Manager for all your mods",font=LARGE_FONT)
        title.pack(side="top")

        label = tk.Label(self, text="Mods Folder",font=LARGE_FONT)
        label.place(x=32,y=96)

        self.modDir = tk.Text(self,width=40,height=1)
        self.modDir.place(x=192,y=96)

        self.modList = tk.Listbox(self,width=75,height=20)
        self.modList.place(x=32,y=128)

        #scrollbar = tk.Scrollbar(self.modList,orient=tk.VERTICAL)
        #scrollbar.pack(side=tk.RIGHT,fill=tk.Y)

        #self.modList.config(yscrollcommand=scrollbar.set)
        #scrollbar.config(command=self.modList.yview)

        addBtn = tk.Button(self,text="Add File(s)",command=lambda :self.copyFile())
        addBtn.place(x=520,y=128)

        delBtn = tk.Button(self,text="Delete Selected",command=lambda :self.deleteFile())
        delBtn.place(x=520,y=160)

        dirBrowse = tk.Button(self,text="...",command=lambda :self.openDirectory())
        dirBrowse.place(x=520,y=94)

    def openDirectory(self):
        directory = tkFile.askdirectory()
        self.modDir.insert('1.0', directory)
        self.mod = directory
        print(self.mod)
        self.buildList()

    def copyFile(self):
        if (self.mod == ""): return

        filesPaths = tkFile.askopenfilenames(filetypes=[("All Files","*")])

        for filePath in filesPaths:
            shutil.copy2(filePath,self.mod)

        self.buildList()


    def deleteFile(self):
        if (self.mod == ""): return

        os.remove(self.mod+"/"+self.modList.get(tk.ACTIVE))

        selected = self.modList.curselection()
        for select in selected:
            self.modList.delete(select)

    def buildList(self):
        self.modList.delete(0,self.modList.size())

        all = os.listdir(self.mod)
        for file in all:
            self.modList.insert(tk.END,file+os.path.commonpath(file))
            print(os.path.commonpath(file).upper())