import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import PhotoImage
import string
import random
import pyperclip
import csv

difficulty="medium"
def show_password():
    for i in frame2.winfo_children():
        i.destroy()
    if chkbtn.get():
        index=1
        bg_frame.place_forget()
      
        frame2.place(x=0,y=0)
        with open("data.csv","r") as f:
            reader=csv.reader(f)
            for lines in (reader):
                txtbox2=ctk.CTkEntry(frame2,font=("",20),width=330,height=50)
                txtbox2.insert(index,f"{index}. {lines[0]} ----> {lines[1]}")
                index+=1
                txtbox2.pack(pady=5)

    else:
        frame2.place_forget()
        bg_frame.place(x=0,y=0)
        
        bg=ctk.CTkLabel(bg_frame,image=bg_img,text=None)
        bg.place(x=0,y=0)
    
def copy():
    pyperclip.copy(txtbox.get())
def set_difficulty(value):
    global difficulty
    if (value<=0.3):
        difficulty_logo.configure(image=easy)
        difficulty="easy"
    elif (value>0.3 and value <=0.7):
        difficulty_logo.configure(image=medium)
        difficulty="medium"
    elif (value>0.7):
        difficulty_logo.configure(image=hard)
        difficulty="hard"
def generate():
    
    try:
        length= int(length_entry.get()) if length_entry.get() else None
        if length is not None and (length < 0 or length > 50):
            print("Invalid length, using default length for selected difficulty.")
            length = None
    except ValueError:
        print("Invalid input for length, using default length for selected difficulty.")
        length = None
    
    if length is None or length < 0 or length > 50:
        if difficulty== 'easy':
            length = 6
        elif difficulty== 'medium':
            length = 10
        elif difficulty == 'hard':
            length = 15

    if difficulty== 'easy':
        characters = string.ascii_letters + string.digits
    elif difficulty== 'medium' or difficulty == 'hard':
        characters = string.ascii_letters + string.digits + string.punctuation

    txtbox.delete(0,ctk.END)
    password=''.join(random.choice(characters) for _ in range(length))
    if (label.get()):
        with open("data.csv","a") as f:
            writer=csv.writer(f)
            writer.writerow([label.get(),password])  

    txtbox.insert(0,password)




    


root=ctk.CTk()
ctk.set_default_color_theme("green")

icon=PhotoImage("icon.png")
root.iconphoto(False,icon)
root.geometry("800x600")
root.resizable(0,0)
root.title("PASSWORD GENERATOR")

bg_frame=ctk.CTkFrame(root,width=350,height=600,corner_radius=0)
bg_frame.place(x=0,y=0,anchor="nw")
frame=ctk.CTkFrame(root,width=450,height=600,fg_color="white",corner_radius=0)
frame.place(x=350,y=0)

frame2=ctk.CTkScrollableFrame(root,width=350,height=600,corner_radius=0,scrollbar_button_color="#2cc985")

bg_img = Image.open('leaves-5610361_1280.png')
bg_img = ctk.CTkImage(bg_img,size=(350,600))

logo= Image.open('logo.png')
logo= ctk.CTkImage(logo,size=(380,60))

tag= Image.open('tag.png')
tag= ctk.CTkImage(tag,size=(50,50))

bg=ctk.CTkLabel(bg_frame,image=bg_img,text=None)
bg.place(x=0,y=0)

easy= Image.open('easy.png')
easy= ctk.CTkImage(easy,size=(50,50))

medium= Image.open('medium.png')
medium= ctk.CTkImage(medium,size=(50,50))

hard= Image.open('hard.png')
hard= ctk.CTkImage(hard,size=(50,50))


size= Image.open('size.png')
size= ctk.CTkImage(size,size=(50,50))

copyicon= Image.open('copy.png')
copyicon= ctk.CTkImage(copyicon,size=(40,40))

heading=ctk.CTkLabel(frame,
                       text=None,
                       image=logo,
                     
                       fg_color="white",
                       bg_color="white")
heading.place(relx=0.5,y=20,anchor="n")

difficulty_logo=ctk.CTkLabel(frame,text=None,image=medium)
difficulty_logo.place(x=35,y=160)
difficulty_slider=ctk.CTkSlider(frame,
                                number_of_steps=30,
                                width=300,
                                height=20,command=set_difficulty)
difficulty_slider.place(x=95,y=175)

length_label=ctk.CTkLabel(frame,
                          text=None,
                          image=size)
length_label.place(x=35,y=240)
length_entry=ctk.CTkEntry(frame,
                    width=285,
                    height=40,
                    font=("",14),
                    placeholder_text="Length  maximum 50")
length_entry.place(x=105,y=240)

label_logo=ctk.CTkLabel(frame,text=None,image=tag)
label_logo.place(x=35,y=320)
label=ctk.CTkEntry(frame,width=285,height=40,font=("",14),
                    placeholder_text="Add Label to save password to library ")
label.place(x=105,y=320)

btn=ctk.CTkButton(frame,
                  width=290,
                  height=40,
                  font=("",20),
                  text="Generate",
                  command=generate)
btn.place(x=105,y=400)
cpbtn=ctk.CTkButton(frame,
                  width=40,
                  height=0,
                  text=None,
                  image=copyicon,
                  fg_color="white",
                  hover_color="#efeee8",
                  command=copy)
cpbtn.place(x=40,y=480)
txtbox=ctk.CTkEntry(frame,
                      width=290,
                      height=45,
                      font=("",20),
                      fg_color="white"
                      )
txtbox.place(x=105,y=480)

chkbtn=ctk.CTkCheckBox(frame,text="show saved password",width=10,height=10,font=("",14),command=show_password)
chkbtn.place(x=250,y=570)
root.mainloop()