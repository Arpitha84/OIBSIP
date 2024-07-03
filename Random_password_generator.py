from tkinter import*
from random import randint
from tkinter import messagebox
import pyperclip
import tkinter
root =Tk()
root.title('Strong password generator')
root.geometry("500x300")
root.config(bg="#008080")  #89023E
root.resizable(0,0)
fg_color="#140152"
bg_color="#ffd9da"

def new_rand():
    pw_entry.delete(0,END)
    #get pw length and convert to integer
    pw_length=int(my_entry.get())
    #create a variable to hold our password
    mypass=''
    #loop through password length
    for x in range(pw_length):
        my_password = chr(randint(33,126))

    #Output password to the screen
        pw_entry.insert(0,my_password)
    
 #copy to the clipboard
def copy_to_clipboard():
    password=pw_entry.get()
    if password:
        pyperclip.copy(password)
        tkinter.messagebox.showinfo("Copied","Password copied to clipboard")
    else:
        tkinter.messagebox.showwarning("No password","Create password first")
    root.clipboard_clear()
    root.clipboard_append
    
 #creating Lable Frame
lf=LabelFrame(root,text="How Many Characters")
lf.pack(pady=20)
#Create Entry Box to designate number of characters

my_entry=Entry(lf,font=("Rockswell",26))
my_entry.pack(pady=20,padx=20)
#creating entry box for our Returned Password
pw_entry=Entry(lf,font=("Rockswell",26))
pw_entry.pack(pady=20)

my_frame=Frame(root)
my_frame.pack(pady=20) 
#creating frames for button
my_button=Button(my_frame,text="Generate Strong Password",activebackground=bg_color,activeforeground=fg_color,command=new_rand)
my_button.grid(row=0,column=0,padx=10)
#creating our buttons
clip_button=Button(my_frame,text="copy to clipboard",activebackground=bg_color,activeforeground=fg_color,command=copy_to_clipboard)
clip_button.grid(row=0,column=1,padx=1)


root.mainloop()
