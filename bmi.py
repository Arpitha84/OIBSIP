import tkinter as tk

def calculate():
    weight=float(entry_weight.get())
    height=float(entry_height.get())
    height=height/100 #convert into meter
    bmi=weight/(height*height)
    bmi_result.config(text="Your BMI : {:.2f}".format(bmi))

    if bmi<=18.4:
        status.config(text="Status : Underweight",fg="#002147")
    elif bmi > 18.5 and bmi < 24.9:
        status.config(text="Status : Normal",fg="#002147")
    elif bmi > 25.5 and bmi < 39.9:
        status.config(text="Status : Overweight",fg="#002147")
    else:
        status.config(text="Status: Obesity",fg="#002147",)

def clear():
        entry_weight.delete(0,'end')
        entry_height.delete(0,'end')
        bmi_result.config(text="")
        status.config(text="")


        pass
 
bg_color=  "#754043"#"#D3D3D3"#"#87CEEB"#D3D3D3"#"#87cefa"#87CEEB"#D3D3D3" #"#D3D3D3" #"#8B7D6B" #GOLD  "#D3D3D3"  #87cefa  #87CEEB
fg_color= "#87cefa" #D3D3D3" #"#f2EAED"

window=tk.Tk()
window.title("BMI CALCULATOR")
window.geometry("400x450")
window.config(bg=bg_color)
window.resizable(0,0)

label_weight=tk.Label(window,text="Weight(kg) :", font=("Californian FB",16,"bold"))
label_weight.pack(pady=10)

entry_weight=tk.Entry(window,font=("Californian FB",16))
entry_weight.pack()

label_height=tk.Label(window,text="Height(cm):",font=("Californian FB",16,"bold"))
label_height.pack(pady=15)

entry_height=tk.Entry(window,font=("Californian FB",15))
entry_height.pack()
#create frames for buttons

frame=tk.Frame(window)
frame.pack(pady=30)

cal_but= tk.Button(frame,text="Calculate",font=("Californian FB",15),activebackground=bg_color,activeforeground=fg_color,command=calculate)#activebackground=bg_color,activeforeground=fg_color,command=calculate
cal_but.grid(row=0, column=0, padx=10)

clear_but=tk.Button(frame,text="Clear",font=("Californian FB",15),activebackground=bg_color,activeforeground=fg_color,command=clear)
clear_but.grid(row=0,column=1,padx=10)



#create label for the result
bmi_result=tk.Label(window,text="",font=("Californian FB",15),bg=bg_color,fg=fg_color)
bmi_result.pack()

status=tk.Label(window,text="",font=("Californian FB",15),bg=bg_color,fg=fg_color)
status.pack(pady=10)

window.mainloop()