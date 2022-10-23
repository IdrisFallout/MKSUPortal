import os
import smtplib
import threading
import time
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import *
from dotenv import dotenv_values
from load_envs import add_env_file
from shared_functions import initialize_selenium
from encryptor import my_encrypt

add_env_file()
config = dotenv_values(".env")
os.remove(".env")

driver = initialize_selenium()


def return_to_login():
    try:
        if error_animation.t1.is_alive():
            return
    except:
        pass
    threading.Thread(target=switch_window).start()
    time.sleep(1.6)
    kill_threads()


def email_sent_feedback():
    try:
        if error_animation.t1.is_alive():
            return
    except:
        pass
    threading.Thread(target=switch_window2).start()
    time.sleep(1.6)
    kill_threads()


def username_placeholder():
    username_entry.configure(fg="#A8A8A9")
    username_entry.insert(0, "Enter Employee No | Registration No")


def clear_username_placeholder(event):
    if username_entry.get() == "Enter Employee No | Registration No":
        username_entry.delete(0, END)
        username_entry.configure(fg="#3C3F41")


def add_username_placeholder(event):
    if username_entry.get() == "":
        username_entry.configure(fg="#A8A8A9")
        username_entry.insert(0, "Enter Employee No | Registration No")


def try_to_reset_password(event):
    reset_password()


def reset_password():
    if username_entry.get() == "Enter Employee No | Registration No" or username_entry.get() == "":
        try:
            if error_animation.counter > 0:
                error_animation.counter = 1
                return
            error_animation.t = 0.5
            error_animation.feedback_height = -50
            error_animation.t1 = threading.Thread(target=error_animation, args={error_lbl})
            error_animation.t1.start()
            error_animation.counter = 1
        except:
            pass
        return
    else:
        try:
            if error_animation.counter > 0:
                error_animation.counter = 1
                return
            if len(username_entry.get()) == 13:
                url = f"{config['URL']}operation=check-student-account&admission={username_entry.get().lower().lower()}"
                driver.get(url)
                html = driver.execute_script("return document.body.innerHTML;")
                if html.split(":")[0] == "Success":
                    the_email = get_email(username_entry.get())
                    the_username = get_username(username_entry.get())
                    result = send_email(receiver=the_email,
                                        ulr_link=f"{config['RESET_PASSWORD_URL']}id={my_encrypt(the_email, config['SECRET_KEY']).decode('utf-8')}",
                                        username=the_username)
                    verification_email.configure(text=f"({the_email}).")
                    email_address = f"({the_email})."
                else:
                    error_animation.feedback_height = -50
                    display_feedback(account_error_lbl)
                    return
            elif len(username_entry.get()) == 5:
                url = f"{config['URL']}operation=check-employee-account&admission={username_entry.get().lower().lower()}"
                driver.get(url)
                html = driver.execute_script("return document.body.innerHTML;")
                if html.split(":")[0] == "Success":
                    result = send_email(receiver=f"{username_entry.get()}@staff.mksu.ac.ke",
                                        ulr_link=f"{config['RESET_PASSWORD_URL']}id={my_encrypt(f'{username_entry.get()}@staff.mksu.ac.ke', config['SECRET_KEY']).decode('utf-8')}",
                                        username=username_entry.get())
                    verification_email.configure(text=f"({username_entry.get()}@staff.mksu.ac.ke).")
                    email_address = f"({username_entry.get()}@staff.mksu.ac.ke)."
                else:
                    error_animation.feedback_height = -50
                    display_feedback(account_error_lbl)
                    return
            else:
                error_animation.feedback_height = -50
                display_feedback(account_error_lbl)
                return
            if result == "Success":
                with open('portal.txt', 'w') as f:
                    f.write(email_address)
                email_sent_feedback()
            else:
                error_animation.feedback_height = -50
                display_feedback(send_email_error_lbl)
        except:
            error_animation.feedback_height = -50
            display_feedback(network_error_lbl)


def error_animation(error_widget):
    try:
        t = 0
        while t < 0.5 and not kill_threads.isClosing:
            error_widget.place_configure(
                y=int(error_widget.place_info()["y"]) + ((abs(error_animation.feedback_height) * 2) * 0.2))
            time.sleep(0.1)
            t += 0.1
        else:
            while t < error_animation.sleep and not kill_threads.isClosing:
                if error_animation.sleep < t:
                    return
                time.sleep(0.1)
                t += 0.1
                pass

            while error_animation.t > 0 and not kill_threads.isClosing:
                if error_animation.t < 0:
                    return
                error_widget.place_configure(
                    y=int(error_widget.place_info()["y"]) - ((abs(error_animation.feedback_height) * 2) * 0.2))
                time.sleep(0.1)
                error_animation.t -= 0.1
            error_widget.place_configure(y=error_animation.feedback_height)
            error_animation.counter = 0
    except:
        pass


def switch_window():
    os.system('python login.py')


def switch_window2():
    os.system('python sent_email_successfully.py')


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


def send_email(receiver=None, ulr_link=None, username=None):
    try:
        # print('Sending Email...')
        server = smtplib.SMTP('smtp.gmail.com', 587, timeout=30)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login(config['GMAIL_ACCOUNT'], config['GMAIL_TOKEN'])

        strFrom = config['GMAIL_ACCOUNT']
        strTo = receiver

        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = 'Reset Account Password'
        msgRoot['From'] = strFrom
        msgRoot['To'] = strTo
        msgRoot.preamble = 'Multi-part message in MIME format.'

        msgAlternative = MIMEMultipart('alternative')
        msgRoot.attach(msgAlternative)

        msgText = MIMEText('Alternative plain text message.')
        msgAlternative.attach(msgText)

        with open('email.html', 'r') as file:
            the_html = file.read().replace("{name}", username).replace("{url}", ulr_link)

        # '<b>Some <i>HTML</i> text</b> and an image.<br><img src="cid:image1"><br>KPI-DATA!'
        msgText = MIMEText(the_html, 'html')
        msgAlternative.attach(msgText)

        # Attach Image
        fp = open('images/machakos-logo.png', 'rb')  # Read image
        msgImage = MIMEImage(fp.read())
        fp.close()

        # Define the image's ID as referenced above
        msgImage.add_header('Content-ID', '<image1>')
        msgRoot.attach(msgImage)

        msg = msgRoot.as_string()
        # msg = f"Subject: {subject}\n\n{body}"
        server.sendmail(
            config['GMAIL_ACCOUNT'],
            receiver,
            msg
        )
        # print("EMAIL HAS BEEN SENT")
        server.quit()
        return "Success"
    except:
        return "Error"


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


def get_username(admission):
    url = f"{config['URL']}operation=get-student-username&admission={admission.lower()}"
    driver.get(url)
    if driver.execute_script('return document.readyState') == 'complete':
        get_username.hasFinished = True
    html = driver.execute_script("return document.body.innerHTML;")
    return html


def get_email(admission):
    try:
        url = f"{config['URL']}operation=get-email&admission={admission.lower()}"
        driver.get(url)
        html = driver.execute_script("return document.body.innerHTML;")
        return html
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
root.configure(bg="#ffffff")
root.title("ACCOUNT RECOVERY")
# -------------------change application icon---------------------
photo = PhotoImage(file='images/machakos-logo.png')
root.wm_iconphoto(True, photo)

# -------------------------------------------------------------------------------
error_animation.sleep = 2
error_animation.t = 0.5
error_animation.counter = 0
error_animation.feedback_height = -75
kill_threads.isClosing = False

canvas = Canvas(
    root,
    bg="#ecf0f5",
    height=735,
    width=1440,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"images/account_recovery/background.png")
background = canvas.create_image(
    720.0, 367.5,
    image=background_img)

username_entry_img = PhotoImage(file=f"images/account_recovery/img_textBox0.png")
username_entry_bg = canvas.create_image(
    728.5, 354.5,
    image=username_entry_img)

username_entry = Entry(
    bd=0,
    bg="#ffffff",
    font=("", 11),
    highlightthickness=0)

username_entry.place(
    x=574.0, y=336,
    width=309.0,
    height=39)

username_entry.bind("<Return>", try_to_reset_password)

reset_password_img = PhotoImage(file=f"images/account_recovery/img0.png")
reset_password_btn = Button(
    image=reset_password_img,
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    borderwidth=0,
    highlightthickness=0,
    command=reset_password,
    relief="flat")

reset_password_btn.place(
    x=634, y=428,
    width=190,
    height=58)

return_to_login_img = PhotoImage(file=f"images/account_recovery/img1.png")
return_to_login_btn = Button(
    image=return_to_login_img,
    borderwidth=0,
    bg="#FFFFFF",
    activebackground="#FFFFFF",
    highlightthickness=0,
    command=return_to_login,
    relief="flat")

return_to_login_btn.place(
    x=658, y=522,
    width=137,
    height=20)

username_placeholder()

username_entry.bind('<FocusIn>', clear_username_placeholder)
username_entry.bind('<FocusOut>', add_username_placeholder)

error_img = PhotoImage(file="images/account_recovery/provide-registration.png")
error_lbl = Label(canvas, image=error_img)
error_lbl.place(x=width / 2, y=-50, anchor=CENTER)

feedback_frame = Frame(canvas)
feedback_frame.place(x=width / 2, y=error_animation.feedback_height, anchor=CENTER)

success_img = PhotoImage(file="images/account_recovery/email-verification.png")
success_lbl = Label(feedback_frame, image=success_img)
success_lbl.pack()
# success_lbl.place(x=width / 2, y=error_animation.feedback_height, anchor=CENTER)

verification_email = Label(feedback_frame, text=f"(********@mksu.ac.ke).", font=("", 13, "bold"), bg="#2C6B46",
                           fg="#87BD9D")
verification_email.place(relx=0.15, rely=0.7)

account_error_img = PhotoImage(file="images/account_recovery/account-not-exist.png")
account_error_lbl = Label(canvas, image=account_error_img)
account_error_lbl.place(x=width / 2, y=-50, anchor=CENTER)

network_error_img = PhotoImage(file="images/account_recovery/network-error.png")
network_error_lbl = Label(canvas, image=network_error_img)
network_error_lbl.place(x=width / 2, y=-50, anchor=CENTER)

send_email_error_img = PhotoImage(file="images/account_recovery/error-occured.png")
send_email_error_lbl = Label(canvas, image=send_email_error_img)
send_email_error_lbl.place(x=width / 2, y=-50, anchor=CENTER)

root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", kill_threads)
root.mainloop()
