from tkinter import*
from random import randint,random
from tkinter import ttk
root = Tk()
root.title("my new window")
#root.iconbitmap('c:/gui/hackthon21may')
label=Label(root,font=("Bold",30),text="Rock,Paper,Scissor-game",
bg="light green",fg="blue",)
label.pack()
root.geometry("700x900+500+100")
root.resizable(0,0)
#root.mainloop()
rock=PhotoImage(file="/home/pooja/Desktop/photo/rocks.png")
paper=PhotoImage(file="/home/pooja/Desktop/photo/paper.png")
scissors=PhotoImage(file="/home/pooja/Desktop/photo/scissor.png")

# rock=PhotoImage(file='/home/aaratiee/Desktop/stone.png')
# paper=PhotoImage(file='/home/aaratiee/Desktop/paper.png')
# scissor=PhotoImage(file='/home/aaratiee/Desktop/scissior.png')
image_list=[rock,paper,scissors]
pick_number=randint(0,2)
image_label=Label(root,image=image_list[pick_number])
image_label.pack(pady=20)
#creat spin function
def spin():
    pick_number=randint(0,2)
    image_label.config(image=image_list[pick_number])
    if user_choice.get()=="rock":
        user_choice_value=0
    elif user_choice.get()=="paper":
        user_choice_value=1
    elif user_choice.get()=="scissor":
         user_choice_value=2
    if user_choice_value==0:#rock
        if pick_number==0:
            win_lose_label.config(text="It's a Tie!,spin again...")
        elif pick_number==1:
              win_lose_label.config(text="paper cover rock!you lose...")
        elif pick_number==2:
              win_lose_label.config(text="rock smashes scissor!you win!!!")
        if user_choice_value==1:#paper
            if pick_number==1:
                win_lose_label.config(text="It's a Tie!,spin again...")
        elif pick_number==0:
              win_lose_label.config(text="paper cover rock!you win!!!")
        elif pick_number==2:
              win_lose_label.config(text="scissor cut paper!you lose...")
        if user_choice_value==2:#scissor
            if pick_number==2:
                win_lose_label.config(text="It's a Tie!,spin again...")
        elif pick_number==0:
              win_lose_label.config(text="rock smashes scissor!you lose...")
        elif pick_number==1:
              win_lose_label.config(text="rock smashes scissor!you win")

user_choice = ttk.Combobox(root,value=("rock","paper","scissor"))
user_choice.current(0)
user_choice.pack(pady=20)
spin_button=Button(root,text="spin!",command=spin)
spin_button.pack(pady=10)
# exit_button=Button(root,text="exit!",command=exit)
# exit_button.pack(pady=20)
win_lose_label=Label(root,text="",font=("Arial",18),bg="white")
win_lose_label.pack(pady=50)
def ex():
    pick_number=randint(0,2)
    image_label.config(image=image_list[pick_number])
    exit()
exit_button=Button(root,text="exit",command=ex)
exit_button.pack(pady=20)

root.mainloop()