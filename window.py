import tkinter as tk
from tkinter import filedialog as tkFile
import shutil, os, sys

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

        self.modDir = tk.Entry(self,width=60)
        self.modDir.grid(row=3,column=2,sticky="E")
        self.modDir.bind("<Return>",lambda x:self.buildList())

        self.modList = tk.Listbox(self,width=60,height=20)
        self.modList.grid(row=5,column=2)
        self.modList.bind("<Delete>",lambda x:self.deleteFile())
        self.modList.bind("<Button-1>",lambda x:self.setSelected())

        #scrollbar = tk.Scrollbar(self.modList,orient=tk.VERTICAL)
        #scrollbar.pack(side=tk.RIGHT,fill=tk.Y)

        #self.modList.config(yscrollcommand=scrollbar.set)
        #scrollbar.config(command=self.modList.yview)

        dirBrowse = tk.Button(self,text="Browse...",command=lambda :self.openDirectory())
        dirBrowse.grid(column=3,row=3,padx=10)

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