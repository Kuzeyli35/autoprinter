from cgitb import text
import os
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter.tix import COLUMN
import time

#Kullanıcının gireceği değişkenler
path = 'C:\\Users\\pc\\Desktop\\printerrrrr\\printing'
süre = 32  #zaman (saniye)

#Program değişkenleri

l_files = os.listdir(path)
lenght = len(l_files)
root = Tk()
root.title("Printer")
root.geometry("400x260")
root.resizable(False, False)
c = 0
z = 0
def step(y):
    global c
    c+=y/2
    my_progress["value"] += y/2
    percentage.config(text = f"%{c}")
    root.update_idletasks()

def err(z):
    error.config(text=f"⨻={z}")
    root.update_idletasks()


def start():
    global z
    for i, file in zip(range(lenght), l_files):
        
        # Instantiating the path of the file
        file_path = f'{path}\\{file}'
        y = 100/lenght
        x = (i+1)*y
        step(y)
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)

        # Checking whether the given file is a directory or not
        if os.path.isfile(file_path):
            try:
                # Printing the file pertaining to file_path
                
                print(f'{x}/100 Printing {file}.')
                #os.startfile(file_path, 'print')         
                progress.insert(0,f'{current_time}-{i}-Printing {file}.')
                time.sleep(süre/2)    
                step(y)
                time.sleep(süre/2)
                continue

            except:
                z += 1    
                step(y)
                progress.insert(0,f'{current_time}-{i}-⨻- File failed to print: {file}.')
                err(z)
                #Catching if any error occurs and alerting the user
                with open("error.txt", "a") as error_file:
                    error_file.write(f"{current_time}-{file} cannot be printed.\n")
                #print(f'ALERT: {file} could not be printed! Please check the associated softwares, or the file type.')
        z += 1
        step(y)
        progress.insert(0,f'{current_time}-{i}-⨻- File failed to print: {file}.')
        err(z)
        with open("error.txt", "a") as error_file:
                error_file.write(f"{current_time}-{file} is not a file, so can not be printed!\n")
        #print(f'ALERT: {file} is not a file, so can not be printed!')
    my_progress["value"] = 100
    percentage.config(text = "%100")
    root.update_idletasks()

        


#---widgets---

#progres bar
my_progress = ttk.Progressbar(root, orient=HORIZONTAL, length=320, mode="determinate")
my_progress.grid(row=0, column=0, sticky=NE,padx=20, pady=10)

#start button
start_button = Button(root, text="Başlat", command=start)
start_button.place(x=335,y=210,in_=root)

#list box for the log of printed orcan not printed files
progress = Listbox(root, height=10, width=33, bg="grey", font="Helvetica", selectmode='extended')
progress.grid(padx= 20, sticky=W ,row=1, column=0)
scrollbar = ttk.Scrollbar(root, orient='vertical', command=progress.yview)
progress['yscrollcommand'] = scrollbar.set
scrollbar.grid(column=0, row=1, sticky='nes', padx=41)

#labe of the percentage
percentage = Label(root, text="%0")
percentage.grid(row=0, column=1)

#error massage
error = Label(root, text="⨻=0", font="Helvetica 12")
error.place(x=335,y=115,in_=root)


root.mainloop()