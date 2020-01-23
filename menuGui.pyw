import tkinter as tk
from tkinter import messagebox as mb
import os
import sys
import webbrowser

programs = {
    "Discord": r'C:\Users\Karun\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Discord Inc\Discord', #Discord
    "Keepass": r'C:\Program Files (x86)\KeePass Password Safe 2\KeePass.exe', #Keepass
    "Spotify": r'C:\Users\Karun\AppData\Roaming\Spotify\Spotify.exe', #Spotify
    "Firefox": r'C:\Program Files\Mozilla Firefox\firefox.exe', #Firefox
    "Netflix": "https://www.netflix.com/browse", #Netflix
    "Youtube": "https://www.youtube.com/", #Youtube
    "Steam": r'C:\Program Files (x86)\Steam\Steam.exe', #Steam
    "AOE3": r'E:\SteamLibrary\steamapps\common\Age Of Empires 3\bin\ESOCPatchLauncher.exe', #Age of Empires 3
    "Shadow of Mordor": r'C:\Program Files (x86)\Steam\steamapps\common\ShadowOfMordor\x64\ShadowOfMordor.exe' #ShadowOfMordor
    }

def main():
    win = tk.Tk()
    new_window = application(win)
    win.mainloop()

class application:
    def __init__(self, master):
        bg_colour = "#dbdbdb"
        btn_colour = "#b5b5b5"
        self.master = master
        self.master.title("Menu")
        self.master.resizable(False,False)
        self.master.config(bg=bg_colour)

        self.btn_frame = tk.Frame(self.master, bd=10, bg=bg_colour)
        self.btn_frame.pack()

        row_count = 0
        column_count = 0

        for key in programs:
            self.btn = tk.Button(self.btn_frame, text=key, width=15, font=('Open Sans', 20), command=lambda i=key: self.openApps(i))
            self.btn.grid(row=row_count, column=column_count, padx=8, pady=20)
            if column_count == 2:
                column_count = 0
                row_count += 1
            else:
                column_count += 1
        

    def openApps(self, AppChoice):
        userApp = programs.get(AppChoice)
        if AppChoice == "Netflix" or AppChoice == "Youtube" :
            webbrowser.open_new_tab(userApp)
        else:
            path = os.path.realpath(userApp)
            os.startfile(path)
        
                
if __name__ == '__main__':
    main()
