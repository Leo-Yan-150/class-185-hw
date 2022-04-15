from tkinter import *
from tkinter import filedialog as fd
import hashlib

root=Tk()
root.geometry("250x190")

def apply_md5():
    print("MD5 function")
    text_file = fd.askopenfilename(title="Open Text File", filetypes=(("Text Files","*.txt"),))
    print(text_file)
    read_file = open(text_file, 'r')
    paragraph = read_file.read()
    Data = paragraph
    file_result = hashlib.md5( Data.encode() )
    file_hexd = file_result.hexdigest()
    print(file_hexd)
    md5_file = open("md5.txt", 'w')
    md5_file.write(file_hexd)
    
def apply_sha256():
    print("SHA function")   
    
    
btn=Button(root, text="Apply MD5",command=apply_md5)
btn.place(relx=0.3,rely=0.5, anchor=CENTER)
btn1=Button(root, text="Apply SHA256",command=apply_sha256)
btn1.place(relx=0.7,rely=0.5, anchor=CENTER)
root.mainloop()