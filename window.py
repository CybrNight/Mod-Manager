import tkinter as tk
from tkinter import filedialog as tkFile
import shutil, os, sys

class StartPage(tk.Frame):

    def __init__(self, parent, cont):
        LARGE_FONT = ("Verdana",12)
        TITLE_FONT = ("Verdana",16)

        self.mod = ""
        self.validPath = False

        tk.Frame.__init__(self,parent)

        title = tk.Label(self,text="Universal Mod Manager",font=TITLE_FONT)
        title.pack(side="top")
        title = tk.Label(self,text="Manager for all your mods",font=LARGE_FONT)
        title.pack(side="top")

        label = tk.Label(self, text="Mods Folder",font=LARGE_FONT)
        label.place(x=32,y=96)

        self.modDir = tk.Entry(self,width=35)
        self.modDir.place(x=192,y=96)
        self.modDir.bind("<Return>",lambda x:self.buildList())

        self.modList = tk.Listbox(self,width=50,height=20)
        self.modList.place(x=32,y=128)

        #scrollbar = tk.Scrollbar(self.modList,orient=tk.VERTICAL)
        #scrollbar.pack(side=tk.RIGHT,fill=tk.Y)

        #self.modList.config(yscrollcommand=scrollbar.set)
        #scrollbar.config(command=self.modList.yview)

        dirBrowse = tk.Button(self,text="Browse...",command=lambda :self.openDirectory())
        dirBrowse.place(x=520,y=94)

    def addButtons(self):
        addBtn = tk.Button(self,text="Add File(s)",command=lambda :self.copyFile())
        addBtn.place(x=520,y=128)

        addFolder = tk.Button(self,text="Add Folder",command=lambda :self.copyFolder())
        addFolder.place(x=520,y=160)

        delBtn = tk.Button(self,text="Delete Selected",command=lambda :self.deleteFile())
        delBtn.place(x=520,y=192)

    def openDirectory(self):
        directory = tkFile.askdirectory()

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



    def deleteFile(self):
        if (self.validPath is not True): return

        file = self.mod+"/"+self.modList.get(tk.ACTIVE)

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