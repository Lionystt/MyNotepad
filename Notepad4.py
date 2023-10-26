# OM NAMAH SHIVAAY
# import tempfile
# import shutil
# import os
from tkinter import Tk
from functools import partial
import subprocess
import smtplib
from threading import Thread
from tkinter import Toplevel, Listbox, IntVar, BooleanVar, Menu, Text, Label, Scrollbar, END, StringVar, VERTICAL, Entry, Button, Frame
from tkinter import font, PhotoImage, messagebox, INSERT, X, CHAR, colorchooser, SEL
from tkinter.ttk import Combobox
import re
from functools import reduce
import pyttsx3
import os
from datetime import datetime
# from tkinter import font
import webbrowser
from tkinter.filedialog import askopenfilename, asksaveasfilename
class NotePad(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("900x600")
        self.title("Untitled - Notepad")
        # self.p1 = PhotoImage(file=b"C:\Users\hp\Documents\Harman (Python Practice)\Tkinter\\boat3.png")
        # self.p2 = PhotoImage(file=b"C:\Users\hp\Documents\Harman (Python Practice)\Tkinter\\boat3.png")
# 
        # self.iconphoto(False, self.p1, self.p2)
        # self.iconbitmap("abcd.ico")
        # self.wm_iconbitmap("C:Users\hp\Documents\Harman (Python Practice)\\Tkinter\\abcd.ico")
    # def icon(self):
        self.en = pyttsx3.init("sapi5")
        self.en.setProperty("volume", 1)
        self.en.setProperty("rate", 150)
        self.deffontlist = []
    def createspeak(self):
        try:
            t1 = Thread(target=self.Speak, args=(str(MyText.get(1.0, END)),))
            t1.start()
            # t1.join()
        except Exception as e:
            MyText.insert(END, f" {e}")
        
    def Speak(self, txt):
        try:
        # print("start")
        # global en, t1
        # en = pyttsx3.init("sapi5")
        # en.setProperty("volume", 1)
        # en.setProperty("rate", 150)
            self.en.say(txt)
            self.en.runAndWait()
        except Exception as e:
            MyText.insert(END, f" {e}")
    # def Stop(self):
        # self.en.stop()
        # self.en.runAndWait()
    def SaveAudioFileNameDialog(self):
        global audioo,filename
        try:
            audioo = Toplevel(self)
            filename = Entry(audioo, textvariable=StringVar())
            filename.grid(row=0,column=0, padx=10,pady=5)
            savebutton = Button(audioo, text="Save Audio File", command=lambda: self.SaveAudioFile(filename.get()))
            savebutton.grid(row=1, column=1,padx=10, pady=5)
        except Exception as e:
            MyText.insert(1.0, f" {e}")
    def SaveAudioFile(self, audiofile):
        try:
        # global en
            audiono = 0
            self.en.save_to_file(MyText.get(1.0, END), audiofile)
            audiono += 1
            messagebox.showinfo("Audio File Saved",f"Audio file saved as '{filename.get()}'")
            audioo.destroy()
        except Exception as e:
            MyText.insert(END, f" {e}")
    def RunAsTerminal(self, event="<Control-r>"):
        try:
            output = subprocess.run(MyText.get(1.0, END).removesuffix("\n").split(" "), shell=True, capture_output=True, text=True)
            # print(output)
            MyText.insert(END, "\n"+str(output).replace('\\n', '\n')+" ")
            # print(MyText.get(1.0, END))
            # print("hi\n j")
        except subprocess.CalledProcessError as e:
            MyText.insert(END, f"  Error: {e}")
            # print(MyText.get(1.0,END).removesuffix("\n").split(" "))
    def SendMail(self):
        try:
            smt = smtplib.SMTP("smtp.gmail.com", 587)
            smt.starttls()
            smt.login(user= MyText.get(1.0, END).split("_")[1], password=MyText.get(1.0, END).split("_")[2])
            smt.sendmail(MyText.get(1.0, END).split("_")[1], MyText.get(1.0, END).split("_")[0], MyText.get(1.0, END).split("_")[3])
            smt.quit()
        except Exception as e:
            MyText.insert(END, f" {e}")
    def NewFile(self, event="<Control-n>"):
        global File
        try:
            self.title("Untitled - Notepad")
            MyText.delete(1.0, END)
            File = None
        except Exception as e:
            # MyText.insert(END, f" {e}")
            pass
    def OpenFile(self, event="<Control-o>"):
        global File, MyText
        try:
            MyText.delete(1.0, END)
            File = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
            f = open(File, "r")
            MyText.insert(1.0, f.read())
            f.close()
            self.title(f"{File}   -   Notepad")
        except Exception as e:
            # MyText.insert(END, f" {e}")
            pass
    def SaveFile(self, event="<Control-s"):
        global File, MyText
        try:
            if File == None:
                File = asksaveasfilename(initialfile="*.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
                with open(File, "a") as f:
                    f.write(MyText.get(1.0, END))
                self.title(f"{File}   -   Notepad")
                # save_file = True   
            else:
                with open(File, "w") as f:
                    f.write(MyText.get(1.0, END))
        except Exception as e:
            # MyText.insert(END, f" {e}")
            pass
    def Index(self, e = "<KeyPress>"):
        # print(MyText.index(END))  
        pass  
    def ExitNotepad(self):
        try:
            self.destroy()
        except Exception as e:
            MyText.insert(END, f" {e}")
    def Copy(self):
        try:
            MyText.event_generate("<<Copy>>")
        except Exception as e:
            MyText.insert(END, f" {e}")
    def Paste(self):
        try:
            MyText.event_generate("<<Paste>>")
        except Exception as e:
            MyText.insert(END, f" {e}")
    def Cut(self):
        try:
            MyText.event_generate("<<Cut>>")
        except Exception as e:
            MyText.insert(END, f" {e}")
    def Undo(self):
        try:
            # MyText.insert(1.0, a)
            MyText.event_generate("<<Undo>>")
        except Exception as e:
            MyText.insert(END, f" {e}")
    def Redo(self):
        try:
            MyText.event_generate("<<Redo>>")
            # MyText.event_generate("<<SelectPrevWord>>")
        except Exception as e:
            MyText.insert(END, f" {e}")
    def Replace(self):
        global rep, repfra, label3, label2, value1, value2
        try:
            rep = Toplevel(self)
            rep.title("Replace...")
            repfra = Frame(rep, width=200, height=200)
            repfra.grid(row=0, column=0)
            label3 = Label(repfra, text="Find What")
            label3.grid(row=0, column=0, padx=30, pady=3)
            value1 = Entry(repfra, textvariable=StringVar())
            value1.grid(row=0,column=1)
            # button1 = Button(repfra, text="Replace", command=self.Replaces)
            # button1.grid(row=0,column=2,padx=30, pady=30)
            label2 = Label(repfra, text="Replace With")
            label2.grid(row=1, column=0, padx=30, pady=3)
            value2 = Entry(repfra, textvariable=StringVar())
            value2.grid(row=1,column=1)
            button2 = Button(repfra, text="Replace All", command=lambda: self.ReplaceAll())
            button2.grid(row=2,column=2,padx=30, pady=3)
        except Exception as e:
            MyText.insert(END, f" {e}")
    def ReplaceAll(self):
        global text
        try:
            text = MyText.get(1.0, END)
            replaced_text = text.replace(value1.get(), value2.get())
            MyText.delete(1.0, END)
            MyText.insert(1.0, replaced_text)
            rep.destroy()
            # print(replaced_text)
        except Exception as e:
            MyText.insert(END, f" {e}")
    def Delete(self):
        try:
            # global a
            # b = ""
            # a = MyText.get(1.0, END)
            MyText.event_generate("<<Clear>>")
            # print("hi")
            # MyText.delete(1.0, END) 
        except Exception as e:
            MyText.insert(END, f" {e}")
    def SelectAll(self):
        try:
            MyText.event_generate("<<SelectAll>>")
        except Exception as e:
            MyText.insert(END, f" {e}")
    def DateTime(self, event="<F5>"):
        try:
            # print("hlo")
            # MainMenu.post(event.x, event.y)
            MyText.insert(1.0, f"Current Time is {datetime.now()}.  ")
        except Exception as e:
            MyText.insert(END, f" {e}")
    def Find(self):
        global input, findwin, frame1, label1, button1
        try:
            findwin = Toplevel(self)
            findwin.title("Find")
            frame1 = Frame(findwin, width=180, height=50)
            frame1.grid(row=0,column=0)
            label1 = Label(frame1, text="Find What")
            label1.grid(row=0, column=0, padx=50, pady=50)
            input = Entry(frame1, textvariable=StringVar())
            input.grid(row=0,column=1)
            button1 = Button(frame1, text="Find", command=self.Finds)
            button1.grid(row=0, column=2, padx=50, pady=50)
        except Exception as e:
            MyText.insert(END, f" {e}")
    def Search(self):
        try:
            url = f"https://www.google.com/search?q={MyText.get(1.0, END).replace(' ', '+')}&rlz=1C1RXQR_enIN1050IN1050&oq={MyText.get(1.0, END).replace(' ', '+')}&aqs=chrome.0.0i433i512l2j0i131i433i512j0i512l5j0i131i433i512j0i512.442426391j0j15&sourceid=chrome&ie=UTF-8"
            # MyText.get(1.0, END).replace(" ", "+")
            webbrowser.open_new_tab(url=url)
        except Exception as e:
            MyText.insert(END, f" {e}")
    def NewWindow(self):
        try:
            top = NotePad()
            top.grid()
            File = None
            self.createMenuBar(top)
            # self.Date2(sel=sel)
            # self.Bindings(sel=top)
            self.OpenFile(top)
            # men = Menu(sel)
            # fmenu = Menu(men, tearoff=0)
            # fmenu.add_command(label="File")
            # men.add_cascade(menu=fmenu, label="File")
            # sel.config(menu=men)
            self.createTextwidget(top)
        except Exception as e:
            MyText.insert(END, f" {e}")
    # def Date2(self, sel):/
        # sel.event_generate("<F5>")
    def Bindings(self, sel):
        try:
            sel.bind("<F5>", self.DateTime)
            sel.bind("<Control-o>",self.OpenFile)
            sel.bind("<Control-n>",self.NewFile)
            sel.bind("<Control-s>",self.SaveFile)
            sel.bind("<Control-p>", self.ZoomOut)
            sel.bind("<Control-m>", self.ZoomIn)
            sel.bind("<KeyPress>", self.StatusBare)
            sel.bind("<Button-3>", self.ContextualMenu)
            sel.bind("<Control-r>", self.RunAsTerminal)
        except Exception as e:
            MyText.insert(END, f" {e}")
    def Check(self):
        try:
            if MyText["wrap"]== "none":
                MyText["wrap"] = "word"
            else :
                MyText["wrap"] = "none"
        except Exception as e:
            MyText.insert(END, f" {e}")
    def Finds(self):
        try:
            search_term = input.get()
            start_position = "1.0"
            found_position = MyText.search(search_term, start_position, stopindex=END)
            
            while found_position:
                end_position = f"{found_position}+{len(search_term)}c"
                MyText.tag_add(SEL, found_position, end_position)
                start_position = end_position
                found_position = MyText.search(search_term, start_position, stopindex=END)
            findwin.destroy()
        except Exception as e:
            MyText.insert(END, f" {e}")
            # print(e)
    def FontBox(self):
        global fontfamily, fb, fontstyle, fontsize, fontframe1, fontframe2, fontframe3
        try:
            fb = Toplevel(self)
            fb.title("Fonts...")
            fontframe1 = Frame(fb, width=100, height=100)
            fontframe1.grid(row=0, column=0)
            label1 = Label(fontframe1, text="Font-Family:  ")
            label1.grid(row=0, column=0)
            fontframe2 = Frame(fb, width=100, height=100)
            fontframe2.grid(row=0, column=1)
            label2 = Label(fontframe2, text="Font-Weight:  ")
            label2.grid(row=0, column=0)
            fontframe3 = Frame(fb, width=100, height=100)
            fontframe3.grid(row=0, column=2)
            label3 = Label(fontframe3, text="Font-Size:  ")
            label3.grid(row=0, column=0)
            fontlist = list(font.families())
            fontstylelist = list(("bold", "italic", "underline", "bold italic", "italic underline", "bold underline italic"))
            fontsizelist = [18, 20, 24, 30, 36, 40, 48, 54, 60, 66, 72, 80, 90]
            # print(fontlist)
            fonts = StringVar(value=fontlist)
            fontfamily = Combobox(fontframe1, values=fontlist, exportselection=False)
            fontfamily.grid(row=1, column=1, padx=50, pady=50)
            fontfamily.set("script")
            fontstyle = Combobox(fontframe2, values=fontstylelist, exportselection=False)
            fontstyle.grid(row=1, column=1,padx=50,pady=50)
            fontstyle.set("italic")
            fontsize = Combobox(fontframe3, values=fontsizelist, exportselection=True)
            fontsize.grid(row=1,column=1, padx=50, pady=50)
            fontsize.set(18)
            fontfamily.bind("<<ComboBoxSelected>>", self.FontUpdate)
            SaveButton = Button(fb, text="Update", command=self.FontUpdate)
            SaveButton.grid(row=5, column=3)
        except Exception as e:
            MyText.insert(END, f" {e}")
    def FontUpdate(self):
        global value3, value2, value1
        try:
            value1, value2, value3 = fontfamily.get(), fontstyle.get(), fontsize.get()
                # print(MyText["font"])
            # print(value3+value1)
            if value1 =="" or value2 == "" or value3=="":
                messagebox.showinfo("Font Selection", "Please select all the 3 properties values and then click 'Update' Button.")
            else:
                MyText["font"] = (value1, value3, value2)
                fb.destroy()
            # if MyText["font"]=="TkFixedFont":
            #     MyText["font"] = (value1, value3,value2)
            # self.deffontlist.append(MyText["font"])
            # fontfamily.set(value1)
            # # fontsize.set(value3)
            # # fontstyle.set(value2)

            # elif value1=="":
            #     MyText["font"] = ("Lucida", value3, value2)
            # elif value2=="":
            #     MyText["font"] = (value1, value3, "Italic")
            # elif value3 =="":
            #     MyText["font"] = (value1, "18", value2)
            # elif value1 == "" and value2 =="":
            #     MyText["font"] = ("Lucida", value3, "Italic")
            # elif value2 == "" and value3 =="":
            #     MyText["font"] = (value1, "18", "Italic")
            # elif value1 == "" and value3 =="":
            #     MyText["font"] = ("Lucida", "18", value2)
        except Exception as e:
            MyText.insert(END, f" {e}")
    def GoTo(self):
        global entr, got, gofra, golab, but
        try:
            got = Toplevel(self)
            got.title("Go To...")
            gofra = Frame(got, width=100, height=100)
            gofra.grid(row=0, column=0)
            golab = Label(gofra, text="Go to line no. : ", bg="black", fg="cyan")
            golab.grid(row=0, column=0, padx=20,pady=20)
            entr = Entry(gofra, textvariable=StringVar())
            entr.grid(row=1,column=0, padx=20,pady=20)
            but = Button(gofra, text="Go", command=self.GoToFeature, bg="black", fg="cyan")
            but.grid(row=2, column=0, padx=20, pady=20)
        except Exception as e:
            # MyText.insert(END, f" {e}")
            print(e)
    def GoToFeature(self):
        try:
            ent = entr.get()
            if ent:
                ent_str = f"{entr.get()}.0"
                MyText.tag_add("sel", ent_str, ent_str + "+1l")
                MyText.mark_set(INSERT, ent_str)
                MyText.see(INSERT)
                got.destroy()
        except Exception as e:
            MyText.insert(END, f" {e}")
            # print(e)
    # def Zoom(self):
        # MyText.bind("Control-u>", self.ZoomOut)
    def ZoomOut(self, event="<Control-p>"):
        try:
            current_size = MyText.cget("font")
            current_size = int(current_size.split(" ")[1])
            new_size = max(1, current_size + 1)
            MyText.configure(font=("TkDefaultFont", new_size))
        except Exception as e:
            MyText.insert(END, f" {e}")
    def ZoomIn(self, event="<Control-m>"):
        try:
            current_size = MyText.cget("font")
            current_size = int(current_size.split(" ")[1])
            new_size = max(1, current_size - 1)
            MyText.configure(font=("TkDefaultFont", new_size))
            # pass
        except Exception as e:
            MyText.insert(END, f" {e}")
    def createMenuBar(self, sel):
        try:
            global MainMenu, FileMenu, EditMenu, FormatMenu, ViewMenu, SpeakMenu, HelpMenu
            MainMenu = Menu(sel, bg="black", fg="cyan", font="cursive 18 italic bold")
            FileMenu = Menu(MainMenu, tearoff= "0", bg="black", fg="cyan", font="cursive 18 italic bold")
            FileMenu.add_command(label="New", command = lambda: self.NewFile(sel))
            # FileMenu.add_command(label="New  Window", command = lambda:self.NewWindow(sel))
            FileMenu.add_command(label="Open", command = lambda: self.OpenFile(sel))
            FileMenu.add_command(label="Save", command = lambda:self.SaveFile(sel))
            FileMenu.add_command(label="Save As", command = lambda:self.SaveFile(sel))
            # FileMenu.add_separator()
            # FileMenu.add_command(label="Page Setup", command = self.SaveFile)
            # FileMenu.add_command(label="Print", command = self.SaveFile)
            FileMenu.add_separator()
            FileMenu.add_command(label="Exit", command = self.ExitNotepad)
            EditMenu = Menu(MainMenu, tearoff="0", bg="black", fg="cyan", font="cursive 18 italic bold")
            EditMenu.add_command(label="Undo", command=self.Undo)
            EditMenu.add_command(label="Redo", command=self.Redo)
            EditMenu.add_separator()
            EditMenu.add_command(label="Copy", command=self.Copy)
            EditMenu.entryconfigure("Copy", accelerator="Ctrl+C",state="active")
            EditMenu.add_command(label="Paste", command=self.Paste)
            EditMenu.entryconfigure("Paste", accelerator="Ctrl+V",state="active")
            EditMenu.add_command(label="Cut", command=self.Cut)
            EditMenu.entryconfigure("Cut", accelerator="Ctrl+X",state="active")
            EditMenu.add_command(label="Delete", command=self.Delete)
            EditMenu.entryconfigure("Delete", accelerator="Del",state="active")
            EditMenu.add_separator()
            EditMenu.add_command(label="Search On Internet", command= self.Search)
            EditMenu.add_command(label="Find", command=self.Find)
            # EditMenu.add_command(label="Find Next", command=self.Copy)
            # EditMenu.add_command(label="Find Previous", command=self.Copy)
            EditMenu.add_command(label="Replace", command=self.Replace)
            EditMenu.add_command(label="Go To", command=self.GoTo)
            # EditMenu.add_command(label="Copy", command=self.Copy)
            EditMenu.add_separator()
            EditMenu.add_command(label="Select All", command=self.SelectAll)
            EditMenu.entryconfigure("Select All", accelerator="Ctrl+A",state="active")
            EditMenu.add_command(label="Time", command=self.DateTime)
            EditMenu.entryconfigure("Time", accelerator="F5",state="active")
            EditMenu.add_command(label="Change Background Color", command=self.Colorchoose)
            EditMenu.add_command(label="Change Foreground Color", command=self.Colorchoose2)

            FormatMenu = Menu(MainMenu, tearoff=0, bg="black", fg="cyan", font="cursive 18 italic bold")
            FormatMenu.add_checkbutton(label="Word Wrap    ", variable=BooleanVar(), command=self.Check)

            FormatMenu.add_command(label="Fonts...", command=self.FontBox)
            FormatMenu.add_command(label="Run As Terminal", command=self.RunAsTerminal)
            FormatMenu.add_command(label="Send Email", command=self.SendMail)
            # ZoomMenu =Menu(ViewMenu, tearoff=0, background="black",foreground="cyan",font="cursive 18 italic bold")
            SpeakMenu = Menu(MainMenu,tearoff=0, bg="black", fg="cyan", font="cursive 18 italic bold")       
            SpeakMenu.add_command(label="Speak", command=self.createspeak)
            # SpeakMenu.add_command(label="Stop Speaking", command=self.Stop)
            # SpeakMenu.add_command(label="Save As Audio File", command=self.SaveAudioFileNameDialog)
            ViewMenu = Menu(MainMenu, tearoff=0, bg="black", fg="cyan", font="cursive 18 italic bold")
            ViewMenu.add_command(label="Zoom In",command=self.ZoomIn)
            ViewMenu.entryconfigure("Zoom In", accelerator="Ctrl+P")
            ViewMenu.add_command(label="Zoom Out",command=self.ZoomOut)
            ViewMenu.entryconfigure("Zoom Out", accelerator="Ctrl+M")
            # ViewMenu.add_cascade(label="Zoom", menu=ZoomMenu, background="black",foreground="cyan")
            # ViewMenu.add_checkbutton(label="Status Bar", onvalue=1, offvalue=0, variable=bo)
            HelpMenu = Menu(MainMenu, tearoff=0, bg="black", fg="cyan", font="cursive 18 italic bold")
            HelpMenu.add_command(label="Help",command=self.Help, background="black", foreground="cyan", font="cursive 18 bold italic")
            MainMenu.add_cascade(label="File", menu=FileMenu, background="black", foreground="cyan", font="cursive 18 bold italic")
            MainMenu.add_cascade(label="Edit", menu=EditMenu, background="black", foreground="cyan", font="cursive 18 bold italic")
            MainMenu.add_cascade(label="Format", menu=FormatMenu, background="black", foreground="cyan", font="cursive 18 bold italic")
            MainMenu.add_cascade(label="Speak", menu=SpeakMenu, background="black", foreground="cyan", font="cursive 18 bold italic")
            MainMenu.add_cascade(label = "View", menu=ViewMenu, background="black", foreground="cyan", font="cursive 18 bold italic")
            MainMenu.add_cascade(label="Help", menu=HelpMenu, background="black", foreground="cyan", font="cursive 18 bold italic")
            sel.config(menu=MainMenu)
        except Exception as e:
            MyText.insert(END, f" {e}")
    def Help(self):
        messagebox.showinfo("Help", 'Notepad is created by Harman Singh.\n "New" starts a blank textarea.\n "Open" opens an existing file.\n "Save" saves the file.\n "Save As" works same as "Save".\n "Exit" closes the notepad.\n "Undo" cancels the last action done.\n "Redo" completes the last canceled action.\n "Cut" cuts the selected text.\n "Copy" copies the selected text.\n "Paste" pastes the copied text.\n "Delete" delete the selected text.\n "Search on Internet" searches the text written in the textarea on internet.\n "Find" finds a word from the text.\n "Replace" replaces a word by the give word.\n "Go To" displays the text on the line no. entered by the user.\n "Select All" selects all the text in the textarea.\n "Time" displays the date with time.\n "Word Wrap" sets the word wrap.\n "Fonts" changes the font and style and size of the font.\n "Run As Terminal" runs the command entered in the textarea.\n\n Note: Only one command should be run at once\n\n "Send Email" sends the email.\n\n Email should be written as described below:\n\n recievergmailaccount_sendergmailaccount_apppassword_Your Message goes here.\n\n "Zoom In and Zoom Out" are used for zooming in and out.')
    def StatusBar(self):
        global statfra
        try:
            statfra = Frame(self, height=50, bg="black")
            statfra.grid(row=2, column=0, sticky="ew")
        except Exception as e:
            MyText.insert(END, f" {e}")
    def StatusBare(self, e="<KeyPress>"):
        global lab
        try:
            # list1 = []

            lab = Label(statfra, text=f"Line {str(MyText.index('end -2 chars')).split('.')[0]}", bg="black", fg="cyan")
            lab.grid(row=0, column=0)
            # print(MyText.index("end+3c"))
        except Exception as e:
            MyText.insert(END, f" {e}")
    def createTextwidget(self, sel):
        global MyText, scroll, Scroll
        try:
            # img = PhotoImage(file=r"C:\\Users\\hp\documents\\Harman (Python Practice)\\Tkinter\boat3.png")
            MyText = Text(sel, wrap="word", undo=True,background="black", foreground="cyan", font="cursive 18 bold italic", insertbackground="cyan", insertwidth=9)
            # MyText.image_create(1.0, image=img)
            MyText.grid(row=0,column=0, sticky="nsew")
            Scroll = Scrollbar(sel, orient=VERTICAL, command=MyText.yview)
            Scroll.grid(row=0, column=1, sticky="ns")
            self.grid_columnconfigure(0, weight=1)
            MyText.config(yscrollcommand=Scroll.set)
            scroll = Scrollbar(sel, orient="horizontal", command=MyText.xview)
            scroll.grid(row=1, column=0, sticky="we")
            self.grid_rowconfigure(0, weight=1)
            MyText.config(xscrollcommand=scroll.set)
            # print(MyText["font"])
        except Exception as e:
            MyText.insert(END, f" {e}")
    def Colorchoose(self):
        global c
        try:
            c = colorchooser.askcolor(initialcolor="white")
            list3 = [MyText, scroll, Scroll, statfra, FileMenu, EditMenu,  FormatMenu, SpeakMenu, ViewMenu, HelpMenu]
            for a in list3:
                a["background"] = c[1]
        except Exception as e:
            MyText.insert(END, f" {e}")

        #  print(c[1])
        #  MyText["bg"]= c[1]
    def Colorchoose2(self):
        global d
        try:
            d = colorchooser.askcolor(initialcolor="black")
            list3 = [MainMenu, FileMenu, EditMenu, FormatMenu, SpeakMenu, ViewMenu, HelpMenu]
            for b in list3:
                 b["foreground"] = d[1]
            MyText["insertbackground"] = d[1]
            ViewMenu["fg"] = d[1]
            HelpMenu["fg"] = d[1]
            list4 = [MyText, scroll, Scroll, statfra]
            for e in list4:
                e["fg"] = d[1]
        except Exception as e:
            MyText.insert(END, f" {e}")


        #  print(c)
        #  self.config(colorchooser=Color)
    def ContextualMenu(self, e = "<Button-3>"):
        try:
            EditMenu.post(e.x+100, e.y+100)
        except Exception as e:
            MyText.insert(END, f" {e}")
def func1():
    global Note, File
    Note = NotePad()
    File = None
    Note.createMenuBar(Note)
    Note.createTextwidget(Note)
    Note.Bindings(sel=Note)
    Note.StatusBar()
    Note.mainloop()
    # print(Note.deffontlist)
    # MyText["font"] = Note.deffontlist[len(Note.deffontlist)-1]
    # print(Note.deffontlist)




if __name__ == "__main__":
    func1()
    