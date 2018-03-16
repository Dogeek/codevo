import sys
import os
from cx_Freeze import setup, Executable
import pip

installed_packages = pip.get_installed_distributions()
installed_packages_list = sorted(["%s" % (i.key) for i in installed_packages])
os.environ['TCL_LIBRARY'] = r'D:\Softwares\python-362-x86\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'D:\Softwares\python-362-x86\tcl\tk8.6'

include_files = ["chipmunk.dll", "sprites", "levels", "config"]
required_packages = ["os", "sys", "pygame", "math", "yaml", "pymunk", "lib", "heapq", "collections", "random", "cffi", "pycparser"]
excludes = [i for i in installed_packages_list if i not in required_packages]

build_exe_options = {	"packages": required_packages,
						"excludes": excludes,
						"include_files": include_files,
 						"include_msvcr": True
						}


BASE = None
if sys.platform == "win32":
	BASE = "Win32GUI"

setup(
		name = "CodEvo",
		version = "0.1",
		options = {"build_exe": build_exe_options},
		description = "DevBuild for CodEvo",
		executables = [Executable("main.py", base=BASE)]
)
