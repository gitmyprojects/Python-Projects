import shutil
import os
import datetime
from tkinter import *
from tkinter import filedialog as fd
from pathlib import Path
import time



#________________________________________________________CREATE GUI__________________________________________________________

win = Tk()

#create frame to contain the widgets
f = Frame(win)

# Create entry box to display the destination folder
v = StringVar()
e=Entry(win,textvariable = v, width=100)
e.pack(side=BOTTOM)

# create list box to list the files that will be moved
lb = Listbox(win, height=15)
lb.pack(side=RIGHT)
sb = Scrollbar(win,orient=VERTICAL)
sb.pack(side=RIGHT, fill=Y)

# connect scroll bar to list box
sb.configure(command=lb.yview)
lb.configure(yscrollcommand=sb.set)


# create button that allows user to choose which folder to review and then opens explorer window
choose_folder_button = Button(f,text="Choose Folder")
destination_folder_button = Button(f,text="Choose Destination")
send_files_button = Button(f, text="Send Files")

# place the created button
choose_folder_button.pack(pady=10)
destination_folder_button.pack(pady=10)
send_files_button.pack(pady=10,side=BOTTOM)

# label the button to instruct user
l = Label(win, text="Click below to choose a folder to review")
dest_l = Label(win, text="Choose the destination folder")
send_l = Label(win, text="Send files")

# position the lable above the button.
l.pack()
f.pack()
send_l.pack()
dest_l.pack()



#_________________________________________________FUNCTIONS TO BE ASSIGNED TO CREATED BUTTONS_____________________________________


def open_directory():
    global source_path
    source_path = fd.askdirectory() # this will store the file path in the variable as a string
    global source_path_dir
    source_path_dir = Path(source_path) # this will store the file path in the variable as a recognizable file path(/ wont be an escape character)
    for f_name in os.listdir(source_path):
        fp = (source_path + "/" + f_name)
        if f_name.endswith('.txt') and(time.time() - os.path.getmtime(fp)) < 86400: # 86400 is the number of seconds in 24 hours
            files = [f_name]
            lb.insert(END, files)
            
def destination_dir():
    global destination_path
    destination_path = fd.askdirectory() # this will store the file path in the variable as a string
    global destination_path_dir
    destination_path_dir = Path(destination_path)# this will store the file path in the variable as a recognizable file path(/ wont be an escape character)
    v.set(destination_path)


def move_files():
    for txt_files in os.listdir(source_path):
        fp = (source_path + "/" + txt_files)
        if txt_files.endswith('.txt') and(time.time() - os.path.getmtime(fp)) < 86400:
            full_path = source_path+"/"+txt_files
            shutil.move(full_path,destination_path_dir)
      
        



#_____________________________________________ASSIGN FUNCTIONS TO CREATED BUTTONS_____________________________________________________  

# assign functions to buttons
choose_folder_button.configure(command=open_directory)
destination_folder_button.configure(command=destination_dir)
send_files_button.configure(command=move_files)














#________________________________________________________SAND BOX__________________________________________________________

    #os.startfile(path) #this opens the explorer window with the file path stored in 'path' variable# # i removed thisfrom the open directory function because once the folder is chosen, the files will be added to list box
    # but i want to remember this function. It opens a new explorer window in the chosen folder

    #### move files #####
### set where the source of the files are
##source = 'C:\\Users\\bearf_000\\Desktop\\Folder A\\'
##
### set the destination path to Folder B
##destination = 'C:\\Users\\bearf_000\\Desktop\\Folder B\\'
##files = os.listdir(source)
##
##for i in files:
##    # we are saying move the files represented by 'i' to thier new destination
##    shutil.move(source+i, destination)


##        for i in new_files:
##        shutil.move(source_path_dir/new_files,destination_path_dir)  

