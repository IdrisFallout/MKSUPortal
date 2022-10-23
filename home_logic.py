import os

from dotenv import dotenv_values

from load_envs import add_env_file
from shared_functions import initialize_selenium
import threading
import ast
from encryptor import my_encrypt

add_env_file()
config = dotenv_values(".env")
os.remove(".env")
driver = initialize_selenium()


def get_username():
    try:
        with open('portal.txt', 'r') as f:
            adm = f.read()
        url = f"{config['URL']}operation=get-student-username&admission={adm.lower()}"
        driver.get(url)
        if driver.execute_script('return document.readyState') == 'complete':
            get_username.hasFinished = True
        html = driver.execute_script("return document.body.innerHTML;")
        try:
            if html.split(" ")[-1] != "" and html.split(" ")[-1] != "results":
                the_user = html.split(" ")[-1]
            else:
                the_user = adm.lower()
        except:
            the_user = "Anknown"
        return adm, the_user
    except:
        get_username.hasFinished = True
        pass


get_username.hasFinished = False


def actually_update_username(root, username_label, fee_balance_data_label):
    try:
        adm, the_user = get_username()
        root.title(the_user)
        username_label.configure(text=the_user)
        get_home_data(adm, fee_balance_data_label)
    except:
        pass


def update_the_username(root, username_label, fee_balance_data_label):
    try:
        threading.Thread(target=actually_update_username, args=[root, username_label, fee_balance_data_label]).start()
    except:
        pass


def get_home_data(admission, fee_balance_data_label):
    try:
        url = f"{config['URL']}operation=get-student-home-data&admission={admission.lower()}"
        driver.get(url)
        html = driver.execute_script("return document.body.innerHTML;")
        fee_balance_data_label.configure(text='KES {:,.2f}'.format(float(html)))
    except:
        pass


def get_change_password_data(admission):
    if not get_username.hasFinished:
        return
    try:
        url = f"{config['URL']}operation=get-student-change-password-data&admission={admission.lower()}"
        driver.get(url)
        html = driver.execute_script("return document.body.innerHTML;")
        # the value in 'html' variable is the account password
        return html
    except:
        pass


def set_the_new_password(admission, the_new_password):
    try:
        url = f"{config['URL']}operation=update-student-password-using-admission&password={the_new_password}&admission={admission.lower()}"
        driver.get(url)
        html = driver.execute_script("return document.body.innerHTML;")
        return True, html
    except:
        return False


def get_profile_personal_data(admission, registration_number_lbl, name_lbl, programme_lbl, national_id_lbl,
                              date_of_birth_lbl, gender_lbl, marital_status_lbl, nationality_lbl, religion_lbl,
                              source_lbl, disability_lbl, telephone_lbl, email_lbl, address_lbl, county_lbl,
                              domicile_lbl, subcounty_lbl, constituency_lbl, emergency_name_lbl,
                              emergency_relationship_lbl, emergency_telephone_lbl, emergency_email_lbl,
                              emergency_address_lbl, emergency_remarks_lbl, language_lbl, medical_lbl, cirricular_lbl):
    if not get_username.hasFinished:
        return
    try:
        url = f"{config['URL']}operation=get-student-profile-personal-data&admission={admission.lower()}"
        driver.get(url)
        html = driver.execute_script("return document.body.innerHTML;")
        actual_list = ast.literal_eval(html)
        registration_number_lbl.configure(text=f"{admission}")
        name_lbl.configure(text=f"{actual_list[0]}")
        programme_lbl.configure(text=f"{actual_list[1]}")
        national_id_lbl.configure(text=f"{actual_list[2]}")
        date_of_birth_lbl.configure(text=f"{convert_date(actual_list[3])}")
        gender_lbl.configure(text=f"{actual_list[4]}")
        marital_status_lbl.configure(text=f"{actual_list[5]}")
        nationality_lbl.configure(text=f"{actual_list[6]}")
        religion_lbl.configure(text=f"{actual_list[7]}")
        source_lbl.configure(text=f"{actual_list[8]}")
        disability_lbl.configure(text=f"{actual_list[9]}")

        telephone_lbl.configure(text=f"{actual_list[10]}")
        email_lbl.configure(text=f"{actual_list[11]}")
        address_lbl.configure(text=f"{actual_list[12]}")
        county_lbl.configure(text=f"{actual_list[13]}")
        domicile_lbl.configure(text=f"{actual_list[14]}")
        subcounty_lbl.configure(text=f"{actual_list[15]}")
        constituency_lbl.configure(text=f"{actual_list[16]}")

        emergency_name_lbl.configure(text=f"{actual_list[17]}")
        emergency_relationship_lbl.configure(text=f"{actual_list[18]}")
        emergency_telephone_lbl.configure(text=f"{actual_list[19]}")
        emergency_email_lbl.configure(text=f"{actual_list[20]}")
        emergency_address_lbl.configure(text=f"{actual_list[21]}")
        emergency_remarks_lbl.configure(text=f"{actual_list[22]}")

        language_lbl.configure(text=f"{actual_list[23]}")
        medical_lbl.configure(text=f"{actual_list[24]}")
        cirricular_lbl.configure(text=f"{actual_list[25]}")
    except:
        pass


def convert_date(short_date):
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]
    year = short_date.split("-")[0]
    month = int(short_date.split("-")[1])
    day = short_date.split("-")[2]
    return f"{day} {months[month - 1]} {year}"


def update_contacts(admission, telephone, email, address, county, domicile, subcounty, constituency):
    try:
        url = f"{config['URL']}operation=update-student-contacts-with-email&admission={admission.lower()}&telephone=" \
              f"{telephone}&email={email}&address={address}&county={county}&domicile=" \
              f"{domicile}&subcounty={subcounty}&constituency={constituency}"
        driver.get(url)
        html = driver.execute_script("return document.body.innerHTML;")
        return html.split(":")[0]
    except:
        pass


def get_email(admission):
    try:
        url = f"{config['URL']}operation=get-email&admission={admission.lower()}"
        driver.get(url)
        html = driver.execute_script("return document.body.innerHTML;")
        return html
    except:
        pass


def update_emergency_contacts(admission, name, relationship, telephone, email, address, remarks):
    try:
        url = f"{config['URL']}operation=update-student-emergency-contacts-with-admission&admission={admission.lower()}&name=" \
              f"{name}&relationship={relationship}&telephone={telephone}&email={email}&address=" \
              f"{address}&remarks={remarks}"
        driver.get(url)
        html = driver.execute_script("return document.body.innerHTML;")
        return html.split(":")[0]
    except:
        pass


def update_other_details(admission, language, medical, cirricular):
    try:
        url = f"{config['URL']}operation=update-student-other-details-with-admission&id={my_encrypt(f'{admission.lower()},{language},{medical},{cirricular}', config['SECRET_KEY']).decode('utf-8')}"
        driver.get(url)
        html = driver.execute_script("return document.body.innerHTML;")
        return html.split(":")[0]
    except:
        pass
