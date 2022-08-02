#UNIcompiler
#YouTube Downloader
#Task-2

import tkinter as tk
import os
from tkinter import *
from pytube import YouTube
from tkinter import filedialog, messagebox

root = tk.Tk()
root.geometry("650x260")
root.resizable(False,False)
root.title("UNIcompiler-Youtube Video Downloader")
root.config(background="#98F5FF")

video_link = StringVar()
download_path = StringVar()

def createWidgets():
    link_label = Label(root, text="Youtube URL: ",bg="#E8D579", font="Times 12 italic bold")
    link_label.grid(row=1, column=0, pady=5, padx=5)

    root.link_text = Entry(root, width=60, textvariable=video_link)
    root.link_text.grid(row=1, column=1, pady=5, padx=5)

    destination_label = Label(root, text="Destination: ",bg="#E8D579", font="Times 12 italic bold")
    destination_label.grid(row=2, column=0, pady=5, padx=5)

    root.destination_text = Entry(root, width=45, textvariable=download_path)
    root.destination_text.grid(row=2, column=1, pady=3, padx=3)

    browse_but = Button(root, text="Browse", command=browse, width=10, bg="#05E8E0", font="Times 12 italic bold")
    browse_but.grid(row=2, column=2, pady=1, padx=1)

    download_but = Button(root, text="Download Video", command=download_video,width=25, bg="#05E8E0", font="Times 12 italic bold")
    download_but.grid(row=3, column=1, pady=3, padx=3)
    download_but.place(x=185, y=200)

def browse():

    download_dir = filedialog.askdirectory(initialdir="Your Directory Path")

    download_path.set(download_dir)

def download_video():

    url = YouTube(str(video_link.get()))
    folder = download_path.get()

    if var.get() == 1:
        if res.get() == 720:
            video = url.streams.filter(res="720p").first()
            out_file = video.download(output_path=folder)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp4'
            os.rename(out_file, new_file)
            messagebox.showinfo("Success!!", "Download Successful! You will find your video at\n" + folder)
        elif res.get() == 1080:
            video = url.streams.filter(res="1080p").first()
            out_file = video.download(output_path=folder)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp4'
            os.rename(out_file, new_file)
            messagebox.showinfo("Success!!", "Download Successful! You will find your video at\n" + folder)
    elif var.get() == 2:
        video = url.streams.filter(only_audio=True).first()
        out_file = video.download(output_path=folder)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        messagebox.showinfo("Success!!", "Download Successful! You will find your audio at\n" + folder)
    else:
        messagebox.showwarning("Warning!!","Download Failed! Please select any resolution\n")


def selection():
    selection1 = "YOUR SELECTED OPTION IS " + str(var.get())
    print(selection1)
    if (var.get() == 1):
        radio_button()


def radio_button():
    Label(root, text='Select the resolution of video: ', font='Times 12 italic bold', bg="#98F5FF").place(x=400, y=90)

    rad_but3 = Radiobutton(root, text="720p", variable=res, value=720, command=radio, font="Times 12 italic bold", bg="#98F5FF")
    rad_but3.place(x=400, y=120)

    rad_but4 = Radiobutton(root, text="1080p", variable=res, value=1080, command=radio, font="Times 12 italic bold", bg="#98F5FF")
    rad_but4.place(x=400, y=150)


def radio():
    selection2 = "YOUR SELECTED OPTION " + str(res.get()) + "p"
    print(selection2)
    pass

#defining the checkbutton
Label(root, text = 'Select the required format of video: ', font = 'Times 12 italic bold', bg="#98F5FF").place(x= 80 , y = 90)
var = IntVar()
res = IntVar()
rad_but1 = Radiobutton(root, text="MP-4", variable=var, value=1, command=selection, font="Times 12 italic bold", bg="#98F5FF")
rad_but1.place(x = 80, y = 120)

rad_but2 = Radiobutton(root, text="MP-3", variable=var, value=2, command=selection, font="Times 12 italic bold", bg="#98F5FF")
rad_but2.place(x = 80, y = 150)



createWidgets()

root.mainloop()