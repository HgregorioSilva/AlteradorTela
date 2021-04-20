import sys
from cx_Freeze import setup, Executable
import pyautogui
import time


base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable("alterador.py", base=base)
]

buildOptions = dict(
        packages = [],
        includes = [],
        include_files = [],
        excludes = []
)

setup(
    name = "NomeDoPrograma",
    version = "1.0",
    description = "Descrição do programa",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
