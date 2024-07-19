from tkinter import *
from tkinter import ttk
from pytube import YouTube
import os

def download(*args):
    #url input from user
    # url = YouTube(str(input("Enter the url of the video!\n")))
    value = YouTube(str(url.get()))

    #extract only audio
    video = value.streams.filter(only_audio=True).first()

    #check for destination to save file
    # print("Enter the destination(leave blank for current directory).")
    # destination = str(input(">> ")) or '.'

   

    #download the file 
    output_file = video.download(output_path="")

    #save the file
    base,ext = os.path.splitext(output_file)
    new_file = base + ".mp3"
    os.rename(output_file,new_file)

    #result
    # print(value.title + "File has been succesfully downloaded!")
    success_note.set("Successfully downloaded!")

###  CODE FOR GUI  ####
root = Tk()
root.title("Youtube to mp3 convertor.")

#making mainframe
mainframe = ttk.Frame(root,padding="80 80 80 80")
mainframe.grid(column=0,row=0,sticky=(N,W,E,S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#get url of the video
url = StringVar()
ttk.Label(mainframe,text="Enter the url of the video.").grid(column=1, row=1,sticky=(W))
url_entry = ttk.Entry(mainframe, width=50, textvariable=url)
url_entry.grid(column=2, row=1,sticky=(W,E))

#get the directory for saving the file
# destination = StringVar()
# ttk.Label(mainframe, text="Enter the destination to save the file.").grid(column=1, row=2, sticky=W)
# destination_entry = ttk.Entry(mainframe, width=10, textvariable=destination)
# destination_entry.grid(column=2, row=2, sticky=(W,E))

#populating success note
success_note = StringVar()
ttk.Label(mainframe, textvariable=success_note).grid(column=1, row=2,sticky=(W))

#creating convert button
ttk.Button(mainframe,text="Convert", command=download).grid(column=2, row=3,sticky=(E))

for child in mainframe.winfo_children():
    child.grid_configure(padx=15, pady=15)

url_entry.focus()
root.bind("<Return>", download)

root.mainloop()
