import sys
import os
from cx_Freeze import *

base = "Win32GUI"

os.environ['TCL_LIBRARY'] = "C:\\Users\\naest_000\\AppData\Local\Programs\\Python\\Python36\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\naest_000\\AppData\\Local\\Programs\\Python\\Python36\\tcl\\tk8.6"

includes      = []
include_files = ["C:\\Users\\naest_000\\AppData\\Local\\Programs\\Python\\Python36\\DLLs\\tcl86t.dll",
                 "C:\\Users\\naest_000\\AppData\\Local\\Programs\\Python\\Python36\\DLLs\\tk86t.dll"]

setup(
    name = "Mod Manager",
    version = "1.1",
    options = {"build_exe": {"includes": includes, "include_files": include_files}},
    executables = [Executable("main.py", base=base)]
)