import os
from tkinter import *
from tkinter import filedialog

# Get PDF directory 
def GetPDFDirectory():
    filepath= filedialog.askdirectory(
        title="Click to select PDF folder"
        )
    replaced=filepath.replace("/","\\\\")
    CheckPDF(replaced,filepath)

# Get Foxit Reader EXE FILE  
def GetFoxDirectory():
        global foxitpath
        foxitpath = filedialog.askopenfilename(
        title="Click to select Foxit Reader EXE",
        filetypes = (
            ('EXE', '*.exe'),
            ('All files', '*.*')
        )
        )
        button = Button(text="Select Printer", command=GetPrinterName)
        button.pack()
        window.mainloop()
        
# Get Printer Name
def GetPrinterName():
 
        root = Tk()
        root.geometry("400x100")
        root.title("Write printer name")

        def getTextInput():
            global printername
            printername=textExample.get("1.0","end")
            print(printername)
            root.destroy()
            button = Button(text="Select PDF folder", command=GetPDFDirectory)
            button.pack()
            window.mainloop()

        textExample= Text(root, height=1)
        textExample.pack()
        btnRead= Button(root, height=1, width=20, text="Confirm name", 
                            command=getTextInput)
        btnRead.pack()
        root.mainloop()      


        
# Execute print from using foxit reader on target printer name
def CheckPDF(replaced,filepath):
    for filename in os.listdir(replaced):
        f = os.path.join(replaced,filename)
        # checking if it is a file
        if os.path.isfile(f):
 
            mainpath=foxitpath+" /t "+f+" "+printername
            print(mainpath)
            os.system(mainpath)
            
window = Tk()
button = Button(text="Select Foxit Reader EXE", command=GetFoxDirectory)
button.pack()
window.mainloop()


 
