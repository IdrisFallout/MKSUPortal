import os
import threading
import time
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import date
from dotenv import dotenv_values
from shared_functions import initialize_selenium
from tkinter import messagebox
import re

config = dotenv_values(".env")

driver = initialize_selenium()


def on_mousewheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


def select_date(event):
    def close_select_date():
        if len(the_date.get()) != 0:
            date_of_birth_lbl.configure(text=the_date.get())
        top.destroy()

    top = Toplevel(root)

    widthC = 500
    heightC = 150

    screen_widthC = top.winfo_screenwidth()
    screen_heightC = top.winfo_screenheight()

    x = ((screen_widthC / 2) - (widthC / 2))
    y = ((screen_heightC / 2) - (heightC / 2))

    top.geometry(f'{widthC}x{heightC}+{int(x)}+{int(y)}')
    top.title("SELECT DATE OF BIRTH")
    top.resizable(False, False)
    dt = date.today()  # today
    current_year = int(str(dt).split("-")[0])
    current_month = int(str(dt).split("-")[1])
    current_date = int(str(dt).split("-")[2])

    dt1 = date(current_year - 100, current_month, current_date)  # specific date Year, month , day
    dt2 = date(current_year - 15, current_month, current_date)  # Maximum date in Year, month , day

    the_date = StringVar()

    date_of_birth_entry = DateEntry(top, font=font1, state='readonly', style="test1.TCombobox", mindate=dt1,
                                    maxdate=dt2, textvariable=the_date, date_pattern='mm/dd/y')
    date_of_birth_entry.place(relx=0.5, rely=0.5, width=(398.70379972457886 + 4) / 2, height=47 / 2, anchor=CENTER)

    top.protocol("WM_DELETE_WINDOW", close_select_date)


def save_personal_information():
    if registration_number_entry.get() == "" or name_entry.get() == "":
        messagebox.showwarning("Warning", "Name or Registration number required")
        return
    try:
        year = date_of_birth_lbl.cget('text').split("/")[2]
        month = date_of_birth_lbl.cget('text').split("/")[0]
        day = date_of_birth_lbl.cget('text').split("/")[1]
    except:
        pass

    try:
        url = f"{config['URL']}operation=update-student-personal-information&admission={registration_number_entry.get().lower()}&name={name_entry.get()}&programme={programme_entry.get()}&national-id={national_id_entry.get()}&date-of-birth={f'{year}-{month}-{day}' if date_of_birth_lbl.cget('text') != '---Select a date---' else ''}&gender={gender_entry.get()}&marital-status={marital_status_entry.get()}&nationality={nationality_entry.get()}&religion={religion_entry.get()}&source={source_entry.get()}&disability={disability_entry.get()} "
        driver.get(url)
        html = driver.execute_script("return document.body.innerHTML;")
        if html.split(":")[0] == "Success":
            save_personal_information_btn.grid_remove()
            saved_personal_information_btn.grid(row=0, column=0)
            save_personal_information.is_saved = True
        else:
            messagebox.showerror("Error", "An error occurred. Please Retry.")
    except:
        messagebox.showerror("Error", "There were network issues. Check your internet connection and retry.")


def save_contacts():
    if telephone_number_entry.get() == "":
        messagebox.showwarning("Warning", "Telephone number must not be empty")
        return
    if not save_personal_information.is_saved:
        messagebox.showwarning("Warning", "You need to save the Personal details above first before proceeding")
        return
    try:
        url = f"{config['URL']}operation=update-student-contacts&admission={registration_number_entry.get().lower()}&telephone={telephone_number_entry.get()}&address={home_address_entry.get()}&county={county_entry.get()}&domicile={domicile_entry.get()}&subcounty={subcounty_entry.get()}&constituency={constituency_entry.get()}"
        driver.get(url)
        html = driver.execute_script("return document.body.innerHTML;")
        if html.split(":")[0] == "Success":
            save_contacts_btn.grid_remove()
            saved_contacts_btn.grid(row=0, column=0)
            save_contacts.is_saved = True
        else:
            messagebox.showerror("Error", "An error occurred. Please Retry.")
    except:
        messagebox.showerror("Error", "There were network issues. Check your internet connection and retry.")


def save_emergency_contacts():
    if emergency_tel_number_entry.get() == "":
        messagebox.showwarning("Warning", "Telephone number must not be empty")
        return
    if emergency_email_entry.get() != "":
        if not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', emergency_email_entry.get()):
            messagebox.showwarning("Warning", "Your email address is invalid. Correct it then retry")
            return
    if not save_personal_information.is_saved or not save_contacts.is_saved:
        messagebox.showwarning("Warning", "You need to save the data above first before proceeding")
        return
    try:
        url = f"{config['URL']}operation=update-student-emergency-contacts&admission={registration_number_entry.get().lower()}&name={emergency_name_entry.get()}&relationship={relationship_entry.get()}&telephone={emergency_tel_number_entry.get()}&email={emergency_email_entry.get()}&address={emergency_address_entry.get()}&remarks={remarks_entry.get()}"
        driver.get(url)
        html = driver.execute_script("return document.body.innerHTML;")
        if html.split(":")[0] == "Success":
            save_emergency_contacts_btn.grid_remove()
            saved_emergency_contacts_btn.grid(row=0, column=0)
            save_emergency_contacts.is_saved = True
        else:
            messagebox.showerror("Error", "An error occurred. Please Retry.")
    except:
        messagebox.showerror("Error", "There were network issues. Check your internet connection and retry.")


def save_other_details():
    if not save_personal_information.is_saved or not save_contacts.is_saved or not save_emergency_contacts.is_saved:
        messagebox.showwarning("Warning", "You need to save the data above first before proceeding")
        return
    try:
        url = f"{config['URL']}operation=update-student-other-details&admission={registration_number_entry.get().lower()}&language={language_entry.get()}&medical={medical_entry.get()}&co-cirricular={co_cirricular_entry.get()}"
        driver.get(url)
        html = driver.execute_script("return document.body.innerHTML;")
        if html.split(":")[0] == "Success":
            save_other_details_btn.grid_remove()
            saved_other_details_btn.grid(row=0, column=0)
            save_other_details.is_saved = True
            go_to_login()
        else:
            messagebox.showerror("Error", "An error occurred. Please Retry.")
    except:
        messagebox.showerror("Error", "There were network issues. Check your internet connection and retry.")


def switch_window():
    os.system('python login.py')


def go_to_login():
    threading.Thread(target=switch_window).start()
    time.sleep(1.6)
    kill_threads()


def kill_threads():
    MsgBox = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application without saving the changes', icon='warning')
    if MsgBox == 'yes':
        root.destroy()
        driver.quit()
    else:
        return


root = Tk()

width = 1440
height = 735

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = ((screen_width / 2) - (width / 2))
y = ((screen_height / 2) - (height / 2))

root.geometry(f'{width}x{height}+{int(x)}+{int(y) - 30}')
root.title("PERSONAL FORM")
photo = PhotoImage(file='images/machakos-logo.png')
# ----------------------------------------------------------------------------
font1 = ("OpenSans-Regular", 11)
save_personal_information.is_saved = False
save_contacts.is_saved = False
save_emergency_contacts.is_saved = False
save_other_details.is_saved = False

root.wm_iconphoto(True, photo)
root.configure(bg="#ffffff")
canvas = Canvas(
    root,
    bg="#ffffff",
    height=735,
    width=1440,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"images/personal_form/background.png")
my_frame = Frame(canvas, bg="#FFFFFF", width=1440, height=background_img.height() + 100)

canvas.create_window((0, 0), window=my_frame, anchor='nw')

background_canvas = Canvas(
    my_frame,
    bg="#ffffff",
    height=background_img.height() + 100,
    width=1440,
    bd=0,
    highlightthickness=0,
    relief="ridge")
background_canvas.place(x=0, y=0)
background = background_canvas.create_image(
    720.0, background_img.height() / 2 + 10,
    image=background_img)

entry0_img = PhotoImage(file=f"images/personal_form/TextBoxImage.png")
entry0_bg = background_canvas.create_image(
    946.0, 313.5,
    image=entry0_img)

with open('portal.txt', 'r') as f:
    admission_no = f.read()

registration_number_entry = Entry(
    my_frame,
    font=font1,
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

registration_number_entry.place(
    x=746.6481001377106 - 2, y=289 + 1,
    width=398.70379972457886 + 4,
    height=47)

registration_number_entry.insert(0, admission_no)
registration_number_entry.configure(state=DISABLED)

entry1_img = PhotoImage(file=f"images/personal_form/TextBoxImage.png")
entry1_bg = background_canvas.create_image(
    946.0, 380.5,
    image=entry1_img)

name_entry = Entry(
    my_frame,
    font=font1,
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

name_entry.place(
    x=746.6481001377106 + 7, y=356 + 1,
    width=398.70379972457886 - 14,
    height=47)

entry2_img = PhotoImage(file=f"images/personal_form/TextBoxImage.png")
entry2_bg = background_canvas.create_image(
    946.0, 447.5,
    image=entry2_img)

style = ttk.Style()
style.theme_use('clam')
style.configure("test1.TCombobox", fieldbackground="#ffffff")

with open('coarses.txt', 'r') as f:
    programmes_offered = f.read().split("\n")

programme_entry = ttk.Combobox(my_frame, values=programmes_offered, font=font1, state='readonly',
                               style="test1.TCombobox")
programme_entry.current(0)

programme_entry.place(
    x=746.6481001377106 - 2, y=423 + 1,
    width=398.70379972457886 + 4,
    height=48)

entry3_img = PhotoImage(file=f"images/personal_form/TextBoxImage.png")
entry3_bg = background_canvas.create_image(
    946.0, 514.5,
    image=entry3_img)

national_id_entry = Entry(
    my_frame,
    font=font1,
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

national_id_entry.place(
    x=746.6481001377106 + 7, y=490 + 1,
    width=398.70379972457886 - 14,
    height=47)

entry4_img = PhotoImage(file=f"images/personal_form/TextBoxImage.png")
entry4_bg = background_canvas.create_image(
    946.0, 581.5,
    image=entry4_img)

date_frame = Frame(my_frame, bg="#DCDAD5")
date_frame.place(
    x=746.6481001377106 - 2, y=557 + 1,
    width=398.70379972457886 + 4,
    height=47)

select_date_frame = Frame(my_frame, bg="#DCDAD5")
select_date_frame.place(
    x=746.6481001377106 - 2, y=557 + 1,
    width=398.70379972457886,
    height=47)

date_of_birth_lbl = Label(
    select_date_frame,
    text="---Select a date---",
    font=font1,
    bd=0,
    bg="#DCDAD5",
    highlightthickness=0)

date_of_birth_lbl.pack(pady=15)

date_of_birth_lbl.bind('<Button-1>', select_date)
select_date_frame.bind('<Button-1>', select_date)

entry5_img = PhotoImage(file=f"images/personal_form/TextBoxImage.png")
entry5_bg = background_canvas.create_image(
    946.0, 648.5,
    image=entry5_img)

gender = [
    "Male",
    "Female"
]
gender_entry = ttk.Combobox(my_frame, values=gender, font=font1, state='readonly', style="test1.TCombobox")
gender_entry.current(0)

gender_entry.place(
    x=746.6481001377106 - 2, y=624 + 1,
    width=398.70379972457886 + 4,
    height=47)

entry6_img = PhotoImage(file=f"images/personal_form/TextBoxImage.png")
entry6_bg = background_canvas.create_image(
    946.0, 715.5,
    image=entry6_img)

marital_status = [
    "Single",
    "Married",
    "Widowed",
    "Divorced",
    "Seperated"
]

marital_status_entry = ttk.Combobox(my_frame, values=marital_status, font=font1, state='readonly',
                                    style="test1.TCombobox")
marital_status_entry.current(0)

marital_status_entry.place(
    x=746.6481001377106 - 2, y=691 + 1,
    width=398.70379972457886 + 4,
    height=47)

entry7_img = PhotoImage(file=f"images/personal_form/TextBoxImage.png")
entry7_bg = background_canvas.create_image(
    946.0, 782.5,
    image=entry7_img)

nationality_entry = Entry(
    my_frame,
    font=font1,
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

nationality_entry.place(
    x=746.6481001377106 + 7, y=758 + 1,
    width=398.70379972457886 - 14,
    height=47)

entry8_img = PhotoImage(file=f"images/personal_form/TextBoxImage.png")
entry8_bg = background_canvas.create_image(
    946.0, 849.5,
    image=entry8_img)

religion_entry = Entry(
    my_frame,
    font=font1,
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

religion_entry.place(
    x=746.6481001377106 + 7, y=825 + 1,
    width=398.70379972457886 - 14,
    height=47)

entry9_img = PhotoImage(file=f"images/personal_form/TextBoxImage.png")
entry9_bg = background_canvas.create_image(
    946.0, 916.5,
    image=entry9_img)

source_entry = Entry(
    my_frame,
    font=font1,
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

source_entry.place(
    x=746.6481001377106 + 7, y=892 + 1,
    width=398.70379972457886 - 14,
    height=47)

entry10_img = PhotoImage(file=f"images/personal_form/TextBoxImage.png")
entry10_bg = background_canvas.create_image(
    945.0, 988.5,
    image=entry10_img)

disability_entry = Entry(
    my_frame,
    font=font1,
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

disability_entry.place(
    x=745.6481001377106 + 7, y=964 + 1,
    width=398.70379972457886 - 14,
    height=47)

entry11_img = PhotoImage(file=f"images/personal_form/TextBoxImage.png")
entry11_bg = background_canvas.create_image(
    946.0, 1160.5,
    image=entry11_img)

telephone_number_entry = Entry(
    my_frame,
    font=font1,
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

telephone_number_entry.place(
    x=746.6481001377106 + 7, y=1136 + 1,
    width=398.70379972457886 - 14,
    height=47)

entry12_img = PhotoImage(file=f"images/personal_form/TextBoxImage.png")
entry12_bg = background_canvas.create_image(
    946.0, 1227.5,
    image=entry12_img)

email_entry = Entry(
    my_frame,
    font=font1,
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

email_entry.place(
    x=746.6481001377106 - 2, y=1203 + 1,
    width=398.70379972457886 + 4,
    height=47)

email_entry.insert(0, f'{admission_no}@student.mksu.ac.ke')
email_entry.configure(state=DISABLED)

entry13_img = PhotoImage(file=f"images/personal_form/TextBoxImage.png")
entry13_bg = background_canvas.create_image(
    946.0, 1294.5,
    image=entry13_img)

home_address_entry = Entry(
    my_frame,
    font=font1,
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

home_address_entry.place(
    x=746.6481001377106 + 7, y=1270 + 1,
    width=398.70379972457886 - 14,
    height=47)

entry14_img = PhotoImage(file=f"images/personal_form/TextBoxImage.png")
entry14_bg = background_canvas.create_image(
    946.0, 1361.5,
    image=entry14_img)

county_entry = Entry(
    my_frame,
    font=font1,
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

county_entry.place(
    x=746.6481001377106 + 7, y=1337 + 1,
    width=398.70379972457886 - 14,
    height=47)

entry15_img = PhotoImage(file=f"images/personal_form/TextBoxImage.png")
entry15_bg = background_canvas.create_image(
    946.0, 1428.5,
    image=entry15_img)

domicile_entry = Entry(
    my_frame,
    font=font1,
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

domicile_entry.place(
    x=746.6481001377106 + 7, y=1404 + 1,
    width=398.70379972457886 - 14,
    height=47)

entry16_img = PhotoImage(file=f"images/personal_form/TextBoxImage.png")
entry16_bg = background_canvas.create_image(
    946.0, 1495.5,
    image=entry16_img)

subcounty_entry = Entry(
    my_frame,
    font=font1,
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

subcounty_entry.place(
    x=746.6481001377106 + 7, y=1471 + 1,
    width=398.70379972457886 - 14,
    height=47)

entry17_img = PhotoImage(file=f"images/personal_form/TextBoxImage.png")
entry17_bg = background_canvas.create_image(
    946.0, 1562.5,
    image=entry17_img)

constituency_entry = Entry(
    my_frame,
    font=font1,
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

constituency_entry.place(
    x=746.6481001377106 + 7, y=1538 + 1,
    width=398.70379972457886 - 14,
    height=47)

entry18_img = PhotoImage(file=f"images/personal_form/TextBoxImage.png")
entry18_bg = background_canvas.create_image(
    946.0, 1724.5,
    image=entry18_img)

emergency_name_entry = Entry(
    my_frame,
    font=font1,
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

emergency_name_entry.place(
    x=746.6481001377106 + 7, y=1700 + 1,
    width=398.70379972457886 - 14,
    height=47)

entry19_img = PhotoImage(file=f"images/personal_form/TextBoxImage.png")
entry19_bg = background_canvas.create_image(
    946.0, 1791.5,
    image=entry19_img)

marital_status = [
    "Father",
    "Mother",
    "Guardian",
    "Wife",
    "Husband",
    "Other"
]

relationship_entry = ttk.Combobox(my_frame, values=marital_status, font=font1, state='readonly',
                                  style="test1.TCombobox")
relationship_entry.current(0)

relationship_entry.place(
    x=746.6481001377106 - 2, y=1767 + 1,
    width=398.70379972457886 + 4,
    height=47)

entry20_img = PhotoImage(file=f"images/personal_form/TextBoxImage.png")
entry20_bg = background_canvas.create_image(
    946.0, 1858.5,
    image=entry20_img)

emergency_tel_number_entry = Entry(
    my_frame,
    font=font1,
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

emergency_tel_number_entry.place(
    x=746.6481001377106 + 7, y=1834 + 1,
    width=398.70379972457886 - 14,
    height=47)

entry21_img = PhotoImage(file=f"images/personal_form/TextBoxImage.png")
entry21_bg = background_canvas.create_image(
    946.0, 1925.5,
    image=entry21_img)

emergency_email_entry = Entry(
    my_frame,
    font=font1,
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

emergency_email_entry.place(
    x=746.6481001377106 + 7, y=1901 + 1,
    width=398.70379972457886 - 14,
    height=47)

entry22_img = PhotoImage(file=f"images/personal_form/TextBoxImage.png")
entry22_bg = background_canvas.create_image(
    946.0, 1992.5,
    image=entry22_img)

emergency_address_entry = Entry(
    my_frame,
    font=font1,
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

emergency_address_entry.place(
    x=746.6481001377106 + 7, y=1968 + 1,
    width=398.70379972457886 - 14,
    height=47)

entry23_img = PhotoImage(file=f"images/personal_form/TextBoxImage.png")
entry23_bg = background_canvas.create_image(
    946.0, 2059.5,
    image=entry23_img)

remarks_entry = Entry(
    my_frame,
    font=font1,
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

remarks_entry.place(
    x=746.6481001377106 + 7, y=2035 + 1,
    width=398.70379972457886 - 14,
    height=47)

entry24_img = PhotoImage(file=f"images/personal_form/TextBoxImage.png")
entry24_bg = background_canvas.create_image(
    946.0, 2225.5,
    image=entry24_img)

language_entry = Entry(
    my_frame,
    font=font1,
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

language_entry.place(
    x=746.6481001377106 + 7, y=2201 + 1,
    width=398.70379972457886 - 14,
    height=47)

entry25_img = PhotoImage(file=f"images/personal_form/TextBoxImage.png")
entry25_bg = background_canvas.create_image(
    946.0, 2292.5,
    image=entry25_img)

medical_entry = Entry(
    my_frame,
    font=font1,
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

medical_entry.place(
    x=746.6481001377106 + 7, y=2268 + 1,
    width=398.70379972457886 - 14,
    height=47)

entry26_img = PhotoImage(file=f"images/personal_form/TextBoxImage.png")
entry26_bg = background_canvas.create_image(
    946.0, 2359.5,
    image=entry26_img)

co_cirricular_entry = Entry(
    my_frame,
    font=font1,
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

co_cirricular_entry.place(
    x=746.6481001377106 + 7, y=2335 + 1,
    width=398.70379972457886 - 14,
    height=47)

save_personal_info_frame = Frame(my_frame)
save_personal_info_frame.place(x=1227, y=1020)

save_button_img = PhotoImage(file="images/personal_form/save-button.png")
save_personal_information_btn = Button(save_personal_info_frame, image=save_button_img, bg="#ffffff", relief='flat',
                                       bd=0,
                                       activebackground='#ffffff', command=save_personal_information)
save_personal_information_btn.grid(row=0, column=0)

saved_button_img = PhotoImage(file="images/personal_form/saved-button.png")
saved_personal_information_btn = Button(save_personal_info_frame, image=saved_button_img, bg="#ffffff", relief='flat',
                                        bd=0,
                                        activebackground='#ffffff', command=save_personal_information)

save_contacts_frame = Frame(my_frame)
save_contacts_frame.place(x=1227, y=1587)

save_contacts_btn = Button(save_contacts_frame, image=save_button_img, bg="#ffffff", relief='flat', bd=0,
                           activebackground='#ffffff', command=save_contacts)
save_contacts_btn.grid(row=0, column=0)

saved_contacts_btn = Button(save_contacts_frame, image=saved_button_img, bg="#ffffff", relief='flat', bd=0,
                            activebackground='#ffffff', command=save_contacts)

save_emergency_contacts_frame = Frame(my_frame)
save_emergency_contacts_frame.place(x=1227, y=2084)

save_emergency_contacts_btn = Button(save_emergency_contacts_frame, image=save_button_img, bg="#ffffff", relief='flat',
                                     bd=0,
                                     activebackground='#ffffff', command=save_emergency_contacts)
save_emergency_contacts_btn.grid(row=0, column=0)

saved_emergency_contacts_btn = Button(save_emergency_contacts_frame, image=saved_button_img, bg="#ffffff",
                                      relief='flat', bd=0,
                                      activebackground='#ffffff', command=save_emergency_contacts)

save_other_details_frame = Frame(my_frame)
save_other_details_frame.place(x=1227, y=2384)

save_other_details_btn = Button(save_other_details_frame, image=save_button_img, bg="#ffffff", relief='flat', bd=0,
                                activebackground='#ffffff', command=save_other_details)
save_other_details_btn.grid(row=0, column=0)

saved_other_details_btn = Button(save_other_details_frame, image=saved_button_img, bg="#ffffff", relief='flat', bd=0,
                                 activebackground='#ffffff', command=save_other_details)

canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.bind_all("<MouseWheel>", on_mousewheel)

root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", kill_threads)
root.mainloop()
