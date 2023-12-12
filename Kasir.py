from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title("Nants Restaurant")
window.minsize(width=500, height=700)
window.configure(bg= "tomato")

def button_clicked():
    ayambakar_total = int(ayambakar_sb.get()) * 2
    bebekbakar_total = int(bebekbakar_sb.get()) * 1
    sateayam_total = int(sateayam_sb.get()) * 1
    teh_total = int(teh_sb.get()) * 2
    jus_total = int(jus_sb.get()) * 1
    lemon_total = int(lemon_sb.get()) * 1

    total_bills = ayambakar_total, bebekbakar_total, sateayam_total, teh_total, jus_total, lemon_total
    bills = Label(text="Your Total Bills ${total_bills}", font=("Times New Roman", 18, "bold"), bg="tomato")
    bills.place(x=150, y=600)

#Restauran Name label 1
resto_name = Label(text= 'Welcome To Nants Restaurant', font=("Times New Roman", 20, "bold"), bg="tomato")
resto_name.grid(column = 1, row=0)

#Restaurant Quote Label 2
quote = Label(text= 'We Serve What You Deserve', font=("Times New Roman", 18, "italic"), bg="tomato")

#Food Label
food_label = Label(text= 'Choose Your Food', font=("Times New Roman", 13, "normal"), bg="tomato")
food_label.grid(column=0, row=3)

#Ayam Bakar (food) image + foto + Spinbox
ayambakar = PhotoImage(file="D:\\KULIAH SMT 5\\PRAK Fungsional\\TUBES\\Ayambakar.jpg")
ayambakar_label = Label(image=ayambakar, borderwidth=0)
ayambakar_label.place(x=50, y=130)
ayambakar_info = Label("Ayam Bakar Kecap\n$10", font=("Times New Roman", 10, "normal"), bg="tomato")
ayambakar_info.place(x=40, y=230)
ayambakar_sb = Spinbox(from_=0, to=10, width=5)
ayambakar_sb.place(x=80, y=270)

#Bebek Bakar (food) image + foto + Spinbox
bebekbakar = PhotoImage(file="D:\\KULIAH SMT 5\\PRAK Fungsional\\TUBES\\Bebekbakar.jpg")
bebekbakar_label = Label(image=bebekbakar, borderwidth=0)
bebekbakar_label.place(x=200, y=130)
bebekbakar_info = Label("Bebek Bakar Kecap\n$15", font=("Times New Roman", 10, "normal"), bg="tomato")
bebekbakar_info.place(x=210, y=230)
bebekbakar_sb = Spinbox(from_=0, to=10, width=5)
bebekbakar_sb.place(x=225, y=270)

#Sate Ayam (food) image + foto + Spinbox
sateayam = PhotoImage(file="D:\\KULIAH SMT 5\\PRAK Fungsional\\TUBES\\Sateayam.jpg")
sateayam_label = Label(image=sateayam, borderwidth=0)
sateayam_label.place(x=350, y=130)
sateayam_info = Label("Sate Ayam\n$10", font=("Times New Roman", 10, "normal"), bg="tomato")
sateayam_info.place(x=350, y=230)
sateayam_sb = Spinbox(from_=0, to=10, width=5)
sateayam_sb.place(x=300, y=270)

#Food Label
drink_label = Label(text= 'Choose Your Drink', font=("Times New Roman", 13, "normal"), bg="tomato")
drink_label.place(x=0, y=350)

#Es Teh (food) image + foto + Spinbox
teh = PhotoImage(file="D:\\KULIAH SMT 5\\PRAK Fungsional\\TUBES\\Esteh.jpg")
teh_label = Label(image=teh, borderwidth=0)
teh_label.place(x=50, y=380)
teh_info = Label("Ice Tea\n$2", font=("Times New Roman", 10, "normal"), bg="tomato")
teh_info.place(x=40, y=480)
teh_sb = Spinbox(from_=0, to=10, width=5)
teh_sb.place(x=80, y=520)

#Orange Juice (food) image + foto + Spinbox
jus = PhotoImage(file="D:\\KULIAH SMT 5\\PRAK Fungsional\\TUBES\\Jusjeruk.jpg")
jus_label = Label(image=jus, borderwidth=0)
jus_label.place(x=200, y=380)
jus_info = Label("Orange Juice\n$4", font=("Times New Roman", 10, "normal"), bg="tomato")
jus_info.place(x=225, y=480)
jus_sb = Spinbox(from_=0, to=10, width=5)
jus_sb.place(x=230, y=520)

#Lemon Tea (food) image + foto + Spinbox
lemon = PhotoImage(file="D:\\KULIAH SMT 5\\PRAK Fungsional\\TUBES\\Lemontea.jpg")
lemon_label = Label(image=lemon, borderwidth=0)
lemon_label.place(x=350, y=380)
lemon_info = Label("Lemon Tea\n$3", font=("Times New Roman", 10, "normal"), bg="tomato")
lemon_info.place(x=360, y=480)
lemon_sb = Spinbox(from_=0, to=10, width=5)
lemon_sb.place(x=375, y=520)

#Finish Button
finish = Button(text="Order", command=button_clicked)
finish.place(x=210, y=560)

window.mainloop()