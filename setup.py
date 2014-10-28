from cx_Freeze import setup, Executable

setup(
name = "Hash Generator",
version = "1.0",
description = "Hashing your files",
executables = [Executable("hash_gen.py", base="Win32GUI")],

)
