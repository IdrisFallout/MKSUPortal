import os
import threading
import time
from tkinter import *
from dotenv import dotenv_values

from login_logic import initialize_selenium

config = dotenv_values(".env")

driver = initialize_selenium()


def switch_window():
    os.system('python registration.py')


def switch_window2():
    os.system('python account_recovery.py')


def switch_window3():
    os.system('python Home.py')


def create_account():
    try:
        if error_animation.t1.is_alive():
            return
    except:
        pass
    threading.Thread(target=switch_window).start()
    time.sleep(1.6)
    kill_threads()


def try_login(event):
    login_submit()


def login_submit():
    if username_entry.get() == "Enter Student No. / Employee No." or username_entry.get() == "" or password_entry.get() == "Enter Password" or password_entry.get() == "":
        display_feedback(error_lbl)
        return
    try:
        # 13 is length of student's admission and 5 for the staff
        if len(username_entry.get()) == 13:
            url = f"{config['URL']}operation=login-student&admission={username_entry.get().lower()}"
            # print(f"USERNAME: {username_entry.get()}\nPASSWORD: {password_entry.get()}")
            driver.get(url)
            html = driver.execute_script("return document.body.innerHTML;")
            if html == password_entry.get():
                with open('portal.txt', 'w') as f:
                    f.write(username_entry.get().lower())
                actually_login()
            elif html == "0 results":
                display_feedback(account_error_lbl)
            else:
                display_feedback(password_error_lbl)
        elif len(username_entry.get()) == 5:
            url = f"{config['URL']}operation=login-employee&admission={username_entry.get().lower()}"
            driver.get(url)
            html = driver.execute_script("return document.body.innerHTML;")
            if html == password_entry.get():
                # display_feedback(success_login_lbl)
                with open('portal.txt', 'w') as f:
                    f.write(username_entry.get().lower())
                actually_login()
            elif html == "0 results":
                display_feedback(account_error_lbl)
            else:
                display_feedback(password_error_lbl)
        else:
            display_feedback(error_lbl)


    except:
        display_feedback(network_error_lbl)


def display_feedback(widget):
    try:
        if error_animation.counter > 0:
            error_animation.counter = 1
            return
        error_animation.t = 0.5
        error_animation.t1 = threading.Thread(target=error_animation, args={widget})
        error_animation.t1.start()
        error_animation.counter = 1
    except:
        pass


def forgot_password():
    try:
        if error_animation.t1.is_alive():
            return
    except:
        pass
    threading.Thread(target=switch_window2).start()
    time.sleep(1.6)
    kill_threads()


def actually_login():
    try:
        if error_animation.t1.is_alive():
            return
    except:
        pass
    threading.Thread(target=switch_window3).start()
    time.sleep(1.6)
    kill_threads()


def student_placeholder():
    username_entry.configure(fg="#A8A8A9")
    password_entry.configure(fg="#A8A8A9")
    username_entry.insert(0, f"Enter Student No. / Employee No.")
    password_entry.insert(0, "Enter Password")


def clear_username_placeholder(event):
    if username_entry.get() == "Enter Student No. / Employee No.":
        username_entry.delete(0, END)
        username_entry.configure(fg="#3C3F41")


def add_username_placeholder(event):
    if username_entry.get() == "":
        username_entry.configure(fg="#A8A8A9")
        username_entry.insert(0, "Enter Student No. / Employee No.")


def clear_password_placeholder(event):
    if password_entry.get() == "Enter Password":
        password_entry.delete(0, END)
        password_entry.configure(fg="#3C3F41", show="*")


def add_password_placeholder(event):
    if password_entry.get() == "":
        password_entry.configure(fg="#A8A8A9", show="", )
        password_entry.insert(0, "Enter Password")


def error_animation(error_widget):
    try:
        t = 0
        while t < 0.5:
            error_widget.place_configure(y=int(error_widget.place_info()["y"]) + 20)
            time.sleep(0.1)
            t += 0.1
        else:
            while t < error_animation.sleep:
                if error_animation.sleep < t:
                    return
                time.sleep(0.1)
                t += 0.1
                pass

            while error_animation.t > 0:
                if error_animation.t < 0:
                    return
                error_widget.place_configure(y=int(error_widget.place_info()["y"]) - 20)
                time.sleep(0.1)
                error_animation.t -= 0.1
            error_widget.place_configure(y=-50)
            error_animation.counter = 0
    except:
        pass


def kill_threads():
    try:
        if error_animation.t1.is_alive():
            return
    except:
        pass
    error_animation.sleep = 0.1
    error_animation.t = -5
    root.destroy()
    try:
        driver.quit()
    except:
        pass


root = Tk()

width = 1440
height = 735

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = ((screen_width / 2) - (width / 2))
y = ((screen_height / 2) - (height / 2))

root.geometry(f'{width}x{height}+{int(x)}+{int(y) - 30}')

root.title("LOGIN")
# -------------------change application icon---------------------
photo = PhotoImage(file='images/machakos-logo.png')
root.wm_iconphoto(True, photo)

root.configure(bg="#ecf0f5")

# ---------------------------------------------------------------------------
error_animation.sleep = 2
error_animation.t = 0.5
error_animation.counter = 0

canvas = Canvas(
    root,
    bg="#ecf0f5",
    height=735,
    width=1440,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"images/login/background.png")
background = canvas.create_image(
    720.0, 367.5,
    image=background_img)

username_entry_img = PhotoImage(file=f"images/login/img_textBox0.png")
username_entry_bg = canvas.create_image(
    723.0, 368.0,
    image=username_entry_img)

username_entry = Entry(
    bd=0,
    bg="#ffffff",
    font=("", 11),
    highlightthickness=0)

username_entry.place(
    x=527.0, y=352,
    width=392.0,
    height=30)

password_entry_img = PhotoImage(file=f"images/login/img_textBox1.png")
password_entry_bg = canvas.create_image(
    723.0, 448.0,
    image=password_entry_img)

password_entry = Entry(
    bd=0,
    bg="#ffffff",
    font=("", 11),
    highlightthickness=0)

password_entry.place(
    x=527.0, y=432,
    width=392.0,
    height=30)

password_entry.bind("<Return>", try_login)

login_img = PhotoImage(file=f"images/login/img0.png")
login_btn = Button(
    image=login_img,
    borderwidth=0,
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    highlightthickness=0,
    command=login_submit,
    relief="flat")

login_btn.place(
    x=686, y=483,
    width=76,
    height=44)

forgot_password_img = PhotoImage(file=f"images/login/img1.png")
forgot_password_btn = Button(
    image=forgot_password_img,
    borderwidth=0,
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    highlightthickness=0,
    command=forgot_password,
    relief="flat")

forgot_password_btn.place(
    x=582, y=554,
    width=119,
    height=20)

create_account_img = PhotoImage(file=f"images/login/img2.png")
create_account_btn = Button(
    image=create_account_img,
    borderwidth=0,
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    highlightthickness=0,
    command=create_account,
    relief="flat")

create_account_btn.place(
    x=742, y=554,
    width=123,
    height=20)

student_placeholder()

username_entry.bind('<FocusIn>', clear_username_placeholder)
username_entry.bind('<FocusOut>', add_username_placeholder)

password_entry.bind('<FocusIn>', clear_password_placeholder)
password_entry.bind('<FocusOut>', add_password_placeholder)

error_img = PhotoImage(file="images/login/error-login.png")
error_lbl = Label(canvas, image=error_img)
error_lbl.place(x=width / 2, y=-50, anchor=CENTER)

success_login_img = PhotoImage(file="images/login/success-login.png")
success_login_lbl = Label(canvas, image=success_login_img)
success_login_lbl.place(x=width / 2, y=-50, anchor=CENTER)

account_error_img = PhotoImage(file="images/login/account-not-exist.png")
account_error_lbl = Label(canvas, image=account_error_img)
account_error_lbl.place(x=width / 2, y=-50, anchor=CENTER)

password_error_img = PhotoImage(file="images/login/invalid-password.png")
password_error_lbl = Label(canvas, image=password_error_img)
password_error_lbl.place(x=width / 2, y=-50, anchor=CENTER)

network_error_img = PhotoImage(file="images/registration/network-error.png")
network_error_lbl = Label(canvas, image=network_error_img)
network_error_lbl.place(x=width / 2, y=-50, anchor=CENTER)

root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", kill_threads)
root.mainloop()
