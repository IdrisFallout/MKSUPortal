import os
import time
from tkinter import *
import threading
from dotenv import dotenv_values
from shared_functions import initialize_selenium
import re

driver = initialize_selenium()

config = dotenv_values(".env")


def switch_window():
    os.system('python login.py')


def switch_window2():
    os.system('python personal_form.py')


def return_to_login():
    try:
        if error_animation.t1.is_alive():
            return
    except:
        pass
    threading.Thread(target=switch_window).start()
    time.sleep(1.6)
    kill_threads()


def register_employee():
    register_employee.isStudent = False
    register_student.section = "Employee No."
    student_checked_btn.grid_remove()
    student_unchecked_btn.grid(row=0, column=0)
    if admission_entry.get() == "Enter your student Admission No.":
        admission_entry.delete(0, END)
        admission_entry.insert(0, f"Enter your {register_student.section}")
    employee_unchecked_btn.grid_remove()
    employee_checked_btn.grid(row=0, column=0)


def register_student():
    register_employee.isStudent = True
    register_student.section = "student Admission No."
    student_unchecked_btn.grid_remove()
    student_checked_btn.grid(row=0, column=0)
    if admission_entry.get() == "Enter your Employee No.":
        admission_entry.delete(0, END)
        admission_entry.insert(0, f"Enter your {register_student.section}")
    employee_checked_btn.grid_remove()
    employee_unchecked_btn.grid(row=0, column=0)


def student_placeholder():
    admission_entry.configure(fg="#A8A8A9")
    password_entry.configure(fg="#A8A8A9")
    password_confirm_entry.configure(fg="#A8A8A9")
    admission_entry.insert(0, f"Enter your {register_student.section}")
    password_entry.insert(0, "Enter Your Password")
    password_confirm_entry.insert(0, "Confirm Your Password")


def clear_admission_placeholder(event):
    if admission_entry.get() == f"Enter your {register_student.section}":
        admission_entry.delete(0, END)
        admission_entry.configure(fg="#3C3F41")


def add_admission_placeholder(event):
    if admission_entry.get() == "":
        admission_entry.configure(fg="#A8A8A9")
        admission_entry.insert(0, f"Enter your {register_student.section}")


def clear_password_placeholder(event):
    if password_entry.get() == "Enter Your Password":
        password_entry.delete(0, END)
        password_entry.configure(fg="#3C3F41", show="*")


def add_password_placeholder(event):
    if password_entry.get() == "":
        password_entry.configure(fg="#A8A8A9", show="", )
        password_entry.insert(0, "Enter Your Password")


def clear_password_confirm_placeholder(event):
    if password_confirm_entry.get() == "Confirm Your Password":
        password_confirm_entry.delete(0, END)
        password_confirm_entry.configure(fg="#000000", show="*")


def add_password_confirm_placeholder(event):
    if password_confirm_entry.get() == "":
        password_confirm_entry.configure(fg="#A8A8A9", show="")
        password_confirm_entry.insert(0, "Confirm Your Password")


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


def try_to_submit_logins(event):
    submit_logins()


def submit_logins():
    if admission_entry.get() == f"Enter your {register_student.section}" or password_entry.get() == "Enter Your " \
                                                                                                    "Password" or \
            password_confirm_entry.get() == "Confirm Your Password" or admission_entry.get() == "" or password_entry.get() == "" or password_confirm_entry.get() == "":
        error_animation.feedback_height = -50
        display_feedback(error_lbl)
        return
    elif password_entry.get() != password_confirm_entry.get():
        error_animation.feedback_height = -50
        display_feedback(password_error_lbl)
    else:
        try:
            if register_employee.isStudent:
                if not re.match(r'[a-zA-Z]{1}[0-9]{2}-[0-9]{4}-[0-9]{4}$', admission_entry.get()):
                    error_animation.feedback_height = -50
                    display_feedback(admission_format_error_lbl)
                    return
                url = f"{config['URL']}operation=register-student&admission={admission_entry.get().lower()}&password={password_entry.get()}"
                driver.get(url)
                html = driver.execute_script("return document.body.innerHTML;")
                if html.split(":")[0] == "Success":
                    success_lbl.place(x=width / 2, y=50, anchor=CENTER)
                    with open('portal.txt', 'w') as f:
                        f.write(admission_entry.get().lower())
                    threading.Thread(target=switch_window2).start()
                    time.sleep(1.6)
                    kill_threads()
                    return
                elif html.split(":")[0] == "Error":
                    error_animation.feedback_height = -78
                    error_message.configure(text=f"{html}")
                    display_feedback(error_frame)
            else:
                if not re.match(r'[a-zA-Z]{2}-[0-9]{2}$', admission_entry.get()):
                    error_animation.feedback_height = -50
                    display_feedback(employee_format_error_lbl)
                    return
                url = f"{config['URL']}operation=register-employee&admission={admission_entry.get().lower()}&password={password_entry.get()}"
                driver.get(url)
                html = driver.execute_script("return document.body.innerHTML;")
                if html.split(":")[0] == "Success":
                    # error_animation.feedback_height = -50
                    # display_feedback(success_lbl)
                    # time.sleep(1)
                    success_lbl.place(x=width / 2, y=50, anchor=CENTER)
                    # kill_threads()
                    # os.system('python login.py')
                    threading.Thread(target=switch_window).start()
                    time.sleep(1.6)
                    kill_threads()
                elif html.split(":")[0] == "Error":
                    error_animation.feedback_height = -78
                    error_message.configure(text=f"{html}")
                    display_feedback(error_frame)
        except:
            error_animation.feedback_height = -50
            display_feedback(network_error_lbl)


def error_animation(error_widget):
    try:
        t = 0
        while t < 0.5:
            error_widget.place_configure(
                y=int(error_widget.place_info()["y"]) + ((abs(error_animation.feedback_height) * 2) * 0.2))
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
                error_widget.place_configure(
                    y=int(error_widget.place_info()["y"]) - ((abs(error_animation.feedback_height) * 2) * 0.2))
                time.sleep(0.1)
                error_animation.t -= 0.1
            error_widget.place_configure(y=error_animation.feedback_height)
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

# -------------------------------------------------------------------------------------
register_student.section = "student Admission No."
error_animation.t = 0.5
error_animation.counter = 0
error_animation.sleep = 2
register_employee.isStudent = True
error_animation.feedback_height = -75

# root.geometry("1440x735")
root.title("ACCOUNT REGISTRATION")
# -------------------change application icon---------------------
photo = PhotoImage(file='images/machakos-logo.png')
root.wm_iconphoto(True, photo)

root.configure(bg="#ecf0f5")
canvas = Canvas(
    root,
    bg="#ecf0f5",
    height=735,
    width=1440,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"images/registration/background.png")
background = canvas.create_image(
    720.0, 367.5,
    image=background_img)

entry0_img = PhotoImage(file=f"images/registration/img_textBox0.png")
entry0_bg = canvas.create_image(
    720.0, 386.0,
    image=entry0_img)

admission_entry = Entry(
    bd=0,
    bg="#ffffff",
    fg="#A8A8A9",
    font=("", 11),
    highlightthickness=0)

admission_entry.place(
    x=516.0 + 8, y=370,
    width=408.0 - 16,
    height=30)

entry1_img = PhotoImage(file=f"images/registration/img_textBox1.png")
entry1_bg = canvas.create_image(
    720.0, 440.0,
    image=entry1_img)

password_entry = Entry(
    bd=0,
    bg="#ffffff",
    fg="#A8A8A9",
    font=("", 11),
    highlightthickness=0)

password_entry.place(
    x=516.0 + 8, y=424,
    width=408.0 - 16,
    height=30)

entry2_img = PhotoImage(file=f"images/registration/img_textBox2.png")
entry2_bg = canvas.create_image(
    720.0, 495.0,
    image=entry2_img)

password_confirm_entry = Entry(
    bd=0,
    bg="#ffffff",
    fg="#A8A8A9",
    font=("", 11),
    highlightthickness=0)

password_confirm_entry.place(
    x=516.0 + 8, y=479,
    width=408.0 - 16,
    height=30)

password_confirm_entry.bind("<Return>", try_to_submit_logins)

submit_img = PhotoImage(file=f"images/registration/img0.png")
submit_btn = Button(
    image=submit_img,
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    borderwidth=0,
    highlightthickness=0,
    command=submit_logins,
    relief="flat")

submit_btn.place(
    x=652, y=551,
    width=137,
    height=44)

return_to_login_img = PhotoImage(file=f"images/registration/img1.png")
return_to_login_btn = Button(
    image=return_to_login_img,
    borderwidth=0,
    activebackground="#FFFFFF",
    highlightthickness=0,
    command=return_to_login,
    relief="flat")

return_to_login_btn.place(
    x=666, y=622,
    width=108,
    height=17)

radio_student_grid = Frame(canvas)
radio_student_grid.place(
    x=683, y=342,
    width=69,
    height=17)

student_unchecked_img = PhotoImage(file=f"images/registration/img3s.png")
student_unchecked_btn = Button(
    radio_student_grid,
    image=student_unchecked_img,
    borderwidth=0,
    activebackground="#FFFFFF",
    highlightthickness=0,
    command=register_student,
    relief="flat")

student_checked_img = PhotoImage(file=f"images/registration/img3.png")
student_checked_btn = Button(
    radio_student_grid,
    image=student_checked_img,
    borderwidth=0,
    activebackground="#FFFFFF",
    highlightthickness=0,
    command=register_student,
    relief="flat")

student_checked_btn.grid(row=0, column=0)

radio_employee_grid = Frame(canvas)
radio_employee_grid.place(
    x=769, y=342,
    width=83,
    height=17)

employee_unchecked_img = PhotoImage(file=f"images/registration/img2.png")
employee_unchecked_btn = Button(
    radio_employee_grid,
    image=employee_unchecked_img,
    borderwidth=0,
    activebackground="#FFFFFF",
    highlightthickness=0,
    command=register_employee,
    relief="flat")

employee_unchecked_btn.grid(row=0, column=0)

employee_checked_img = PhotoImage(file=f"images/registration/img2e.png")
employee_checked_btn = Button(
    radio_employee_grid,
    image=employee_checked_img,
    borderwidth=0,
    activebackground="#FFFFFF",
    highlightthickness=0,
    command=register_employee,
    relief="flat")

student_placeholder()
admission_entry.bind('<FocusIn>', clear_admission_placeholder)
admission_entry.bind('<FocusOut>', add_admission_placeholder)

password_entry.bind('<FocusIn>', clear_password_placeholder)
password_entry.bind('<FocusOut>', add_password_placeholder)

password_confirm_entry.bind('<FocusIn>', clear_password_confirm_placeholder)
password_confirm_entry.bind('<FocusOut>', add_password_confirm_placeholder)

error_img = PhotoImage(file="images/registration/error-login.png")
error_lbl = Label(canvas, image=error_img)
error_lbl.place(x=width / 2, y=-50, anchor=CENTER)

password_error_img = PhotoImage(file="images/registration/password-match-error.png")
password_error_lbl = Label(canvas, image=password_error_img)
password_error_lbl.place(x=width / 2, y=-50, anchor=CENTER)

success_img = PhotoImage(file="images/registration/registration-success.png")
success_lbl = Label(canvas, image=success_img)
success_lbl.place(x=width / 2, y=-50, anchor=CENTER)

error_frame = Frame(canvas, bg="#C65B57")
error_frame.place(x=width / 2, y=error_animation.feedback_height, anchor=CENTER)

feedback_img = PhotoImage(file="images/registration/error-dialog.png")
feedback_lbl = Label(error_frame, image=feedback_img)
feedback_lbl.grid(row=0, column=0)

error_message = Label(error_frame, text="Display Error Here", wraplength=290, bg="#C65B57", fg="#FBFCFD",
                      font=("", 9, "bold"))
error_message.place(relx=0.15, rely=0.25)

network_error_img = PhotoImage(file="images/registration/network-error.png")
network_error_lbl = Label(canvas, image=network_error_img)
network_error_lbl.place(x=width / 2, y=-50, anchor=CENTER)

admission_format_error_img = PhotoImage(file="images/registration/wrong-admission-format.png")
admission_format_error_lbl = Label(canvas, image=admission_format_error_img)
admission_format_error_lbl.place(x=width / 2, y=-50, anchor=CENTER)

employee_format_error_img = PhotoImage(file="images/registration/employee-format-error.png")
employee_format_error_lbl = Label(canvas, image=employee_format_error_img)
employee_format_error_lbl.place(x=width / 2, y=-50, anchor=CENTER)

root.resizable(False, False)

root.protocol("WM_DELETE_WINDOW", kill_threads)
root.mainloop()
