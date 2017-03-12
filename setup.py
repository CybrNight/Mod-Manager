import sys
import os
from cx_Freeze import *

base = "Win32GUI"

os.environ['TCL_LIBRARY'] = "C:\\Users\\naest_000\\AppData\Local\Programs\\Python\\Python36\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\naest_000\\AppData\\Local\\Programs\\Python\\Python36\\tcl\\tk8.6"

includes      = []
include_files = [r"C:\\Users\\naest_000\\AppData\\Local\\Programs\\Python\\Python36\\DLLs\\tcl86t.dll",
                 r"C:\\Users\\naest_000\\AppData\\Local\\Programs\\Python\\Python36\\DLLs\\tk86t.dll"]

setup(
    name = "Test",
    version = "1.0",
    options = {"build_app": {"includes": includes, "include_files": include_files}},
    executables = [Executable("main.py", base=base)]
)