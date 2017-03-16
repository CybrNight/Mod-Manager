import tkinter as tk
import os, shutil

class DeleteWindow():
    def __init__(self, master, modList, filePath):
        self.modList = modList
        self.master = master
        self.frame = tk.Frame(self.master)

        self.label = tk.Label(self.master,text="Do you want to delete this?")
        self.label.grid(row=0,column=0,sticky="WE")

        self.yesButton = tk.Button(self.master, text='Yes', width=25, command=lambda :self.delete_file(filePath))
        self.yesButton.grid(row=1,column=0)

        self.noButton = tk.Button(self.master, text='No', width=25, command=lambda: self.master.destroy())
        self.noButton.grid(row=1, column=1)

    def delete_file(self, file_path):

        if (os.path.isfile(file_path)):
            os.remove(file_path)
        else:
            shutil.rmtree(file_path)

        selected = self.modList.curselection()
        for select in selected:
            self.modList.delete(select)
        self.master.destroy()