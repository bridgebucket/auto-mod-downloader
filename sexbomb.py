import tkinter as tk
from tkinter import filedialog as fd
import zipfile
import os
from pyunpack import Archive
import shutil

root = tk.Tk()
root.geometry('900x800')
root.config(bg='#191819')
root.title("Humping a Taxidermified Rat")
root.resizable(True, False)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


mainframe = tk.Frame(root)
mainframe.grid(column=0, row=0)
mainframe.config(bg="#0a0b0b")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

dirframe = tk.Frame(mainframe)
dirframe.grid(column=0, row=1, padx=(50, 50), pady=(50, 50))
dirframe.config(bg="#202020")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


def targetCommand():
    global target
    target = fd.askdirectory()
    if not target:
        dildoknife.set("No Directory Selected")
    else:
        target = target.replace("/", "\\")
        print(target)
        dildoknife.set(target)

dildoknife = tk.StringVar()
dildoknife.set("No Directory Selected")
targetlbl = tk.Label(dirframe,
                     textvariable=dildoknife,
                     bg="#202020",
                     fg="#fefeff",
                     relief="flat",
                     highlightthickness="0",
                     font=('Arial', 11)
                     )
targetlbl.grid(column=2, row=1, padx=(5, 50), pady=(40, 40))

targetbtn = tk.Button(dirframe,
                      bg="#202020",
                      fg="#fefeff",
                      relief="flat",
                      highlightthickness="1",
                      highlightcolor="#cc1918",
                      default="active",
                      text="Mod Dir",
                      command=targetCommand
                      )
targetbtn.grid(column=1, row=1, padx=(50, 5), pady=(40, 40))

def originCommand():
    global origin
    origin = fd.askdirectory()
    if not origin:
        doorstuck.set("No Directory Selected")
    else:
        origin = origin.replace("/", "\\")
        print(origin)
        doorstuck.set(origin)

doorstuck = tk.StringVar()
doorstuck.set("No Directory Selected")
originlbl = tk.Label(dirframe,
                     textvariable=doorstuck,
                     bg="#202020",
                     fg="#fefeff",
                     relief="flat",
                     highlightthickness="0",
                     font=('Arial', 11)
                     )
originlbl.grid(column=2, row=2, padx=(5, 50), pady=(40, 40))

originbtn = tk.Button(dirframe,
                      bg="#202020",
                      fg="#fefeff",
                      relief="flat",
                      highlightthickness="1",
                      highlightcolor="#cc1918",
                      default="active",
                      text="Origin Dir",
                      command=originCommand
                      )
originbtn.grid(column=1, row=2, padx=(50, 5), pady=(40, 40))

transframe = tk.Frame(mainframe)
transframe.grid(column=0, row=2, padx=(50, 50), pady=(50, 50))
transframe.config(bg="#202020")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

warninglbl = tk.Label(transframe,
                     text="make sure that no other files are in the origin directory.\nim serious like double triple check so that no other files\nthat you may need get deleted",
                     bg="#202020",
                     fg="#fefeff",
                     relief="flat",
                     highlightthickness="0",
                     font=('Arial', 15, 'bold')
                     )
warninglbl.grid(column=2, row=3, padx=(50, 50), pady=(50, 10))

listen2sewerslvt = tk.StringVar()
listen2sewerslvt.set("Make sure origin/target directories are set, and press the transfer button.")

def transfercmd(downloadspath, target):
    for i in os.listdir(downloadspath):
        listen2sewerslvt.set(f"Transferring {i} to target...")
        print(i)
        fil = os.path.join(downloadspath, i)
        if os.path.isfile(fil):
            if fil.lower().endswith('.zip'):
                with zipfile.ZipFile(fil, 'r') as zip_ref:
                    zip_ref.extractall(target)
                os.remove(fil)
            elif fil.lower().endswith('.7z'):
                Archive(fil).extractall(target)
                os.remove(fil)
            elif fil.lower().endswith('rar'):
                Archive(fil).extractall(target)
                os.remove(fil)
            else:
                shutil.move(fil, target)
                os.remove(fil)
        listen2sewerslvt.set(f"Transferred!")
    listen2sewerslvt.set(f"Successfully transferred all files from origin to target.")
        


def freerobux():
    #ignore this please its literally just calling transfercmd because i cant call it with a button command

    transfercmd(origin, target)

transferbtn = tk.Button(transframe,
                      bg="#202020",
                      fg="#fefeff",
                      relief="flat",
                      highlightthickness="1",
                      highlightcolor="#cc1918",
                      default="active",
                      text="Transfer",
                      command=freerobux,
                      )
transferbtn.grid(column=2, row=4, padx=(50, 50), pady=(10, 30))


resultlbl = tk.Label(mainframe,
                     textvariable=listen2sewerslvt,
                     bg="#0a0b0b",
                     fg="#fefeff",
                     relief="flat",
                     font=('Arial', 15, 'bold')
                     )
resultlbl.grid(column=0, row=5, padx=(50, 50), pady=(2, 50))

root.mainloop()
