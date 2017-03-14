application_title = "Mod Manager"
main_python_file = "main.py"

import sys

from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

includes = ["atexit","re"]

setup(
    name = application_title,
    version = "1.1",
    description = "Sample cx_Freeze PyQt4 script",
    options = {
        "build_exe" : {
            "includes" : includes,
            "excludes": ['tcl', 'ttk', 'tkinter', 'Tkinter'],
        }
    },
    executables = [
        Executable(main_python_file, base = base)
    ]
)