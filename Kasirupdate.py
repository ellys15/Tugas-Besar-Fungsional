from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title("Nants Restaurant")
window.minsize(width=500, height=700)
window.configure(bg="tomato")

# Label to display total bills
bills = Label(
    text="Your Total Bills: Rp 0", font=("Times New Roman", 12, "normal"), bg="tomato"
)
bills.grid(row=11, column=1, pady=10)

# Dictionary untuk menyimpan harga setiap item
harga_menu = {
    "Ayam Bakar": 18000,
    "Bebek Bakar": 25000,
    "Sate Ayam": 15000,
    "Es Teh": 4000,
    "Orange Juice": 6000,
    "Lemon Tea": 8000,
}


def button_clicked():
    ayambakar_total = int(ayambakar_sb.get()) * harga_menu["Ayam Bakar"]
    bebekbakar_total = int(bebekbakar_sb.get()) * harga_menu["Bebek Bakar"]
    sateayam_total = int(sateayam_sb.get()) * harga_menu["Sate Ayam"]
    teh_total = int(teh_sb.get()) * harga_menu["Es Teh"]
    jus_total = int(jus_sb.get()) * harga_menu["Orange Juice"]
    lemon_total = int(lemon_sb.get()) * harga_menu["Lemon Tea"]

    # Menghitung total tagihan dari seluruh pesanan
    total_bills = (
        ayambakar_total
        + bebekbakar_total
        + sateayam_total
        + teh_total
        + jus_total
        + lemon_total
    )

    # Memperbarui teks pada label total tagihan
    bills.config(text=f"Your Total Bills: Rp {total_bills}")


# Restaurant Name label 1
resto_name = Label(
    text="Welcome To Nant's Restaurant",
    font=("Times New Roman", 20, "bold"),
    bg="tomato",
)
resto_name.grid(column=1, row=0)

# Food Label
food_label = Label(
    text="Choose Your Food", font=("Times New Roman", 13, "normal"), bg="tomato"
)
food_label.grid(column=0, row=3)

# Ayam Bakar (food) image + foto + Spinbox
ayambakar_img = Image.open(
    "D:/KULIAH SMT 5/PRAK Fungsional/TUBES/Ayambakar.jpg"
).resize((200, 200))
ayambakar = ImageTk.PhotoImage(ayambakar_img)
ayambakar_label = Label(image=ayambakar, borderwidth=0)
ayambakar_label.grid(row=4, column=0, padx=20)  # Tambahkan padx untuk jarak horizontal
ayambakar_info = Label(
    text="Ayam Bakar Kecap\nRp.18.000",
    font=("Times New Roman", 10, "normal"),
    bg="tomato",
)
ayambakar_info.grid(row=5, column=0)
ayambakar_sb = Spinbox(from_=0, to=10, width=5)
ayambakar_sb.grid(row=6, column=0)

# Bebek Bakar (food) image + foto + Spinbox
bebekbakar_img = Image.open(
    "D:/KULIAH SMT 5/PRAK Fungsional/TUBES/Bebekbakar.jpg"
).resize((200, 200))
bebekbakar = ImageTk.PhotoImage(bebekbakar_img)
bebekbakar_label = Label(image=bebekbakar, borderwidth=0)
bebekbakar_label.grid(row=4, column=1, padx=20)  # Tambahkan padx untuk jarak horizontal
bebekbakar_info = Label(
    text="Bebek Bakar Kecap\nRp.25.000",
    font=("Times New Roman", 10, "normal"),
    bg="tomato",
)
bebekbakar_info.grid(row=5, column=1)
bebekbakar_sb = Spinbox(from_=0, to=10, width=5)
bebekbakar_sb.grid(row=6, column=1)

# Sate Ayam (food) image + foto + Spinbox
sateayam_img = Image.open("D:/KULIAH SMT 5/PRAK Fungsional/TUBES/Sateayam.jpg").resize(
    (200, 200)
)
sateayam = ImageTk.PhotoImage(sateayam_img)
sateayam_label = Label(image=sateayam, borderwidth=0)
sateayam_label.grid(row=4, column=2, padx=20)  # Tambahkan padx untuk jarak horizontal
sateayam_info = Label(
    text="Sate Ayam\nRp.15.000", font=("Times New Roman", 10, "normal"), bg="tomato"
)
sateayam_info.grid(row=5, column=2)
sateayam_sb = Spinbox(from_=0, to=10, width=5)
sateayam_sb.grid(row=6, column=2)

# Food Label
drink_label = Label(
    text="Choose Your Drink", font=("Times New Roman", 13, "normal"), bg="tomato"
)
drink_label.grid(column=0, row=7)

# Es Teh (food) image + foto + Spinbox
teh_img = Image.open("D:/KULIAH SMT 5/PRAK Fungsional/TUBES/Esteh.jpg").resize(
    (200, 200)
)
teh = ImageTk.PhotoImage(teh_img)
teh_label = Label(image=teh, borderwidth=0)
teh_label.grid(row=8, column=0, padx=20)  # Tambahkan padx untuk jarak horizontal
teh_info = Label(
    text="Ice Tea\nRp.4.000", font=("Times New Roman", 10, "normal"), bg="tomato"
)
teh_info.grid(row=9, column=0)
teh_sb = Spinbox(from_=0, to=10, width=5)
teh_sb.grid(row=10, column=0)

# Orange Juice (food) image + foto + Spinbox
jus_img = Image.open("D:/KULIAH SMT 5/PRAK Fungsional/TUBES/Jusjeruk.jpg").resize(
    (200, 200)
)
jus = ImageTk.PhotoImage(jus_img)
jus_label = Label(image=jus, borderwidth=0)
jus_label.grid(row=8, column=1, padx=20)  # Tambahkan padx untuk jarak horizontal
jus_info = Label(
    text="Orange Juice\nRp.6.000", font=("Times New Roman", 10, "normal"), bg="tomato"
)
jus_info.grid(row=9, column=1)
jus_sb = Spinbox(from_=0, to=10, width=5)
jus_sb.grid(row=10, column=1)

# Lemon Tea (food) image + foto + Spinbox
lemon_img = Image.open("D:/KULIAH SMT 5/PRAK Fungsional/TUBES/Lemontea.jpg").resize(
    (200, 200)
)
lemon = ImageTk.PhotoImage(lemon_img)
lemon_label = Label(image=lemon, borderwidth=0)
lemon_label.grid(row=8, column=2, padx=20)  # Tambahkan padx untuk jarak horizontal
lemon_info = Label(
    text="Lemon Tea\nRp.8.000", font=("Times New Roman", 10, "normal"), bg="tomato"
)
lemon_info.grid(row=9, column=2)
lemon_sb = Spinbox(from_=0, to=10, width=5)
lemon_sb.grid(row=10, column=2)

# Finish Button
finish = Button(
    text="Order", font=("Times New Roman", 15, "normal"), command=button_clicked
)
finish.place(relx=0.5, rely=1.0, anchor="s")

window.mainloop()