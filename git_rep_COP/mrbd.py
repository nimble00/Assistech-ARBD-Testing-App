import Tkinter
import Tkinter as tk
from Tkinter import *
import ttk

class mainclass():
    def __init__(self,master):
        #self.text = tk.StringVar()
        #tk.Tk.__init__(self,master,*args,**kwargs)
        self.master = master
        master.frame = tk.Frame(master)
        #master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(),master.winfo_screenheight()))
        master.title("Automated RBD testing")
        master["bg"]= "turquoise"
        label1 = Label(master,text="Welcome to Automated RBD Testing",bg="turquoise",fg="hot pink",font=  ("Times","40","bold italic"))
        label1.place(relx=0.5,rely=0.4,anchor="center")
        self.button1 = ttk.Button(master, text="connect", command=lambda:self.connect())
        #self.text.set("connect")
        self.button1.place(relx=0.5,rely=0.5,anchor="center")
        #button2 = ttk.Button(master, text="Excecute Testcases", command=lambda:self.execute())
        #button2.place(relx=0.6,rely=0.5,anchor="center")
        #master.rowconfigure(0,weight=1)
        #master.columnconfigure(0,weight=1)
        self.button2 = ttk.Button(master, text="Record Testcase", command=lambda:self.Record(),state=DISABLED)
        self.button2.place(relx=0.4,rely=0.5,anchor="center")
        #button2.lower(master.frame)
        self.button3 = ttk.Button(master, text="Excecute Testcases", command=lambda:self.execute(),state = DISABLED)
        self.button3.place(relx=0.6,rely=0.5,anchor="center")
        #button3.lower(master.frame)
    def execute(self):
        #print "s"
        root2=Toplevel(self.master,bg="turquoise")
        app = execute_testcase(root2)
    def Record(self):
        #print "s"
        root2=Toplevel(self.master,bg="turquoise")
        app = Record_Testcases(root2)
    def connect(self):
        execfile("alclient.py")
        root3=Toplevel(self.master)
        root3.geometry("300x200")
        label0 = Label(root3,text="Please enter credidentials").grid(row=0,column=0,columnspan=2)
        label1 = Label(root3,text="User ID").grid(row=1,column=0,sticky=E)
        label2 = Label(root3,text="Password").grid(row=2,column=0,sticky=E)
        label3 = Label(root3,text="IP Address").grid(row=3,column=0,sticky=E)
        label4 = Label(root3,text="Port number").grid(row=4,column=0,sticky=E)
        Entry1=Entry(root3).grid(row=1,column=1)
        Entry2=Entry(root3).grid(row=2,column=1)
        Entry3=Entry(root3).grid(row=3,column=1)
        Entry4=Entry(root3).grid(row=4,column=1)
        root3.grid_rowconfigure(5, minsize=20)
        button4 = Button(root3, text="OK", command=lambda:self.disconnect(),height=1,width=8).grid(row=6,column=0,columnspan=2)
    def disconnect(self):
        #self.text.set("Disconnect")
        self.button1["text"]="Disconnect"
        self.button2["state"]= "snormal"
        self.button3["state"]="normal"
        Labelx = Label(self.master,text="Successfully connected to arbd",bg="turquoise")
        Labelx.place(relx=0.8,rely=0.1)





class Record_Testcases():
    def __init__(self,master):
        self .master = master
        Labelx = Label(self.master,text="Enter the name of testcase").grid(row=0,column=0)
        Entry1=Entry(master).grid(row=0,column=1)
        master.grid_rowconfigure(1, minsize=20)
        button4 = Button(master, text="OK", command=lambda:self.disconnect(),height=1,width=8).grid(row=2,column=0,columnspan=2)
        
class execute_testcase():
    def __init__(self,master):
        #print "y"
        self.master=master
        tree = ttk.Treeview(master)
        #tree.pack(side=LEFT,fill=Y)
        tree.grid(row=0,column=0,sticky="nsew")
        #tree.grid(row=0,column=0,rowspan=2,columnspan=8,sticky=NSEW)
        #.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(),self.winfo_screenheight()))
        helps = tree.insert("",0,"help",text = "Help")
        #tree.bind("<Double-1>", self.OnDoubleClick)
        #tree.bind("<Double-1>",self.running)
        master.grid_columnconfigure(0,weight=1)
        #master.grid_columnconfigure(1,weight=1)
        #master.columnconfigure(0,weight=1)
        master.rowconfigure(1,weight=1)
        master.rowconfigure(0,weight=1)
        tree.insert(helps,"end",text="testcase1")
        tree.insert(helps,"end",text="testcase2")
        tree.insert(helps,"end",text="testcase3")
        tree.insert(helps,"end",text="testcase4")
        tree.insert(helps,"end",text="testcase5") 
        system = tree.insert("",0,"Systeminformation",text = "System Information")
        tree.insert(system,"end",text="testcase1")
        tree.insert(system,"end",text="testcase2")
        tree.insert(system,"end",text="testcase3")
        tree.insert(system,"end",text="testcase4")
        tree.insert(system,"end",text="testcase5")
        setting = tree.insert("",0,"settings",text = "Settings")
        tree.insert(setting,"end",text="testcase1")
        tree.insert(setting,"end",text="testcase2")
        tree.insert(setting,"end",text="testcase3")
        tree.insert(setting,"end",text="testcase4")
        tree.insert(setting,"end",text="testcase5")
        filebrowser = tree.insert("",0,"filebrowser",text = "File Browser")
        tree.insert(filebrowser,"end",text="Open File browser")
        tree.insert(filebrowser,"end",text="First Letter Navigation")
        tree.insert(filebrowser,"end",text="File/folder creation")
        tree.insert(filebrowser,"end",text="cut/copy operations")
        tree.insert(filebrowser,"end",text="Paste operation")
        tree.insert(filebrowser,"end",text="Delete operation")
        tree.insert(filebrowser,"end",text="rename operation")
        tree.insert(filebrowser,"end",text="Mark multiple files/folders")
        browser = tree.insert("",0,"browser",text = "Web Browser")
        tree.insert(browser,"end",text="Starting Web Browser")
        tree.insert(browser,"end",text="Reading a web browser")
        tree.insert(browser,"end",text="Opening a link")
        tree.insert(browser,"end",text="Back and forward")
        tree.insert(browser,"end",text="changing URL/Opening new URL")
        email = tree.insert("",0,"email",text = "Email")
        tree.insert(email,"end",text="testcase1")
        tree.insert(email,"end",text="testcase2")
        tree.insert(email,"end",text="testcase3")
        tree.insert(email,"end",text="testcase4")
        tree.insert(email,"end",text="testcase5")
        word = tree.insert("",0,"Word processor",text = "Word Processor")
        tree.insert(word,"end",text="testcase1")
        tree.insert(word,"end",text="testcase2")
        tree.insert(word,"end",text="testcase3")
        tree.insert(word,"end",text="testcase4")
        tree.insert(word,"end",text="testcase5")
        notepad = tree.insert("",0,"notepad",text = "Notepad")
        tree.insert(notepad,"end",text="testcase1")
        tree.insert(notepad,"end",text="testcase2")
        tree.insert(notepad,"end",text="testcase3")
        tree.insert(notepad,"end",text="testcase4")
        tree.insert(notepad,"end",text="testcase5")
        Applicationmenu = tree.insert("",0,"Applicationmenu",text = "Applicationmenu")
        tree.insert(Applicationmenu,"end",text="Opening Menu")
        nttm = tree.insert(Applicationmenu,"end",text="Navigate through the menu")
        tree.insert(nttm,"end",text="First letter navigation")
        tree.insert(nttm,"end",text="Exit the menu")
        menu = tree.insert(Applicationmenu,"end",text="Menu items")
        tree.insert(menu,"end",text="notepad")
        tree.insert(menu,"end",text="Word processor")
        tree.insert(menu,"end",text="Email")
        tree.insert(menu,"end",text="Web Browser")
        tree.insert(menu,"end",text="File Browser")
        tree.insert(menu,"end",text="Settings")
        tree.insert(menu,"end",text="Help")
        tree.insert(menu,"end",text="System Information")
        self.table()
    def table(self):
        style = ttk.Style()
        #style.configure(".", font=('Helvetica', 8), foreground="white")
        style.configure("Treeview", foreground='red')
        style.configure("Treeview.Heading", foreground='Black',background="SkyBlue")
        self.tree = ttk.Treeview( self.master, columns=('Main heading', 'heading','sub heading','Testcase','KeyStrokes','Output','Passed'))
        self.tree.heading('#0', text='Main heading')
        self.tree.heading('#1', text='heading')
        self.tree.heading('#2', text='sub heading')
        self.tree.heading('#3', text='Testcase')
        self.tree.heading('#4', text='KeyStrokes')
        self.tree.heading('#5', text='Output')
        self.tree.heading('#6', text='Passed')
        self.tree.column('#2',width=150, stretch=False)
        self.tree.column('#1',width=160, stretch=False)
        self.tree.column('#0',width=150, stretch=False)
        self.tree.column('#3',width=150, stretch=False)
        self.tree.column('#4',width=150, stretch=False)
        self.tree.column('#5',width=150, stretch=False)
        self.tree.column('#6',width=150, stretch=False)
        self.tree.grid(row=0,column=1, columnspan=7,rowspan=3, sticky='nsew')
        #self.tree.pack()
        self.treeview = self.tree
        scrollbar1=Scrollbar(self.master,command=self.tree.yview)
        scrollbar1.grid(row=0,column=8,rowspan=3,sticky=N+S)
        self.treeview.configure(yscrollcommand=scrollbar1.set)
        self.master.rowconfigure(0,weight=1)
        #self.master.columnconfigure(0,weight=0)
        #scrollbar1.pack(side=RIGHT)
        self.loadtable1()
        botton1 = Button(self.master, text="RUN", command="",height=2,width=15,bg="Skyblue")
        botton1.grid(row=1,column=0)
        botton2 = Button(self.master, text="STOP", command="",height=2,width=15,bg= "Skyblue")
        botton2.grid(row=2,column=0)
    def loadtable1(self):
        f = open("inputkey.txt","r")
        for line in f:
              self.treeview.insert('',"end",text ="Application Menu",values=("Opening Menu","","",line))
        g = open("inputkey.txt","r")
        for line in g:
              self.treeview.insert('',"end",text ="Application Menu",values=("Navigate through the menu","First letter navigation","",line))
        h = open("inputkey.txt","r")
        for line in h:
              self.treeview.insert('',"end",text ="Application Menu",values=("Navigate through the menu","Exit the Menu","",line))
        i = open("inputkey.txt","r")
        for line in i:
              self.treeview.insert('',"end",text ="Application Menu",values=("Menu items","notepad","",line))
        j = open("inputkey.txt","r")
        for line in j:
              self.treeview.insert('',"end",text ="Application Menu",values=("Menu items","Word processor","",line))
        k = open("inputkey.txt","r")
        for line in k:
              self.treeview.insert('',"end",text ="Application Menu",values=("Menu items","Email","",line))
        l = open("inputkey.txt","r")
        for line in l:
              self.treeview.insert('',"end",text ="Application Menu",values=("Menu items","File Browser","",line))
        m = open("inputkey.txt","r")
        for line in m:
              self.treeview.insert('',"end",text ="Application Menu",values=("Menu items","Settings","",line))
        n = open("inputkey.txt","r")
        for line in n:
              self.treeview.insert('',"end",text ="Application Menu",values=("Menu items","Help","",line))
        o = open("inputkey.txt","r")
        for line in o:
              self.treeview.insert('',"end",text ="Application Menu",values=("Menu items","System Information","",line))
        g = open("inputkey.txt","r")
        for line in g:
              self.treeview.insert('',"end",text ="Notepad",values=("","","Testcase1",line))
        h = open("inputkey.txt","r")
        for line in h:
              self.treeview.insert('',"end",text ="Notepad",values=("","","Testcase2",line))
        i = open("inputkey.txt","r")
        for line in g:
              self.treeview.insert('',"end",text ="Notepad",values=("","","Testcase3",line))
        j = open("inputkey.txt","r")
        for line in g:
              self.treeview.insert('',"end",text ="Notepad",values=("","","Testcase4",line))
        k = open("inputkey.txt","r")
        for line in g:
              self.treeview.insert('',"end",text ="Notepad",values=("","","Testcase5",line))
def main():
    root =Tk()
    app = mainclass(root)
    root.mainloop()

if __name__=='__main__':
    main()
