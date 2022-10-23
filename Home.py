import os
import re
import time
from tkinter import *
from tkinter import messagebox

from home_logic import *


def on_mousewheel(event):
    if show_personal_data.allowScroll and not show_academics.isAcademics:
        profile_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


def home_hovered(event):
    home_bright_lbl.grid_remove()
    home_hovered_lbl.grid(row=0, column=0)


def home_normal(event):
    home_hovered_lbl.grid_remove()
    home_bright_lbl.grid(row=0, column=0)


def show_home(event):
    hide_account_options()
    new_and_events_frame.grid_remove()
    reporting_frame.grid_remove()
    deferment_frame.grid_remove()
    fees_frame.grid_remove()
    side_units_frame.grid_remove()
    examination_frame.grid_remove()
    evaluation_frame.grid_remove()
    clearance_frame.grid_remove()
    my_message_frame.grid_remove()
    profile_canvas.grid_remove()
    change_password_frame.grid_remove()
    display_home()


def display_scrollable_profile():
    get_profile_personal_data(the_user, personal_information_registration_number_lbl, personal_information_name_lbl,
                              personal_programme_lbl, personal_national_id_lbl, personal_date_of_birth_lbl,
                              personal_gender_lbl, personal_marital_status_lbl, personal_nationality_lbl,
                              personal_religion_lbl, personal_source_lbl, personal_disability_lbl,
                              personal_contact_telephone_number_lbl, personal_contact_email_lbl,
                              personal_contact_address_lbl, personal_contact_county_lbl, personal_contact_domicile_lbl,
                              personal_contact_subcounty_lbl, personal_contact_constituency_lbl,
                              personal_emergency_name_lbl, personal_emergency_relationship_lbl,
                              personal_emergency_telephone_lbl, personal_emergency_email_lbl,
                              personal_emergency_address_lbl, personal_emergency_remarks_lbl,
                              personal_other_details_language_lbl, personal_other_details_medical_lbl,
                              personal_other_details_cirriculum_lbl)
    profile_canvas.yview_moveto(float(0 + 1) / height - nav_bar_height)
    cancel_personal_contact()
    cancel_emergency_contact()
    profile_canvas.grid(row=0, column=0)


def display_home():
    home_frame.grid(row=0, column=0)
    get_home_data(the_user, fee_balance_data_lbl)


def news_hovered(event):
    news_bright_lbl.grid_remove()
    news_hovered_lbl.grid(row=1, column=0)


def news_normal(event):
    news_hovered_lbl.grid_remove()
    news_bright_lbl.grid(row=1, column=0)


def show_news(event):
    hide_account_options()
    home_frame.grid_remove()
    reporting_frame.grid_remove()
    deferment_frame.grid_remove()
    fees_frame.grid_remove()
    side_units_frame.grid_remove()
    examination_frame.grid_remove()
    evaluation_frame.grid_remove()
    clearance_frame.grid_remove()
    my_message_frame.grid_remove()
    profile_canvas.grid_remove()
    change_password_frame.grid_remove()
    new_and_events_frame.grid(row=0, column=0)


def reporting_hovered(event):
    reporting_bright_lbl.grid_remove()
    reporting_hovered_lbl.grid(row=2, column=0)


def reporting_normal(event):
    reporting_hovered_lbl.grid_remove()
    reporting_bright_lbl.grid(row=2, column=0)


def show_reporting(event):
    hide_account_options()
    new_and_events_frame.grid_remove()
    deferment_frame.grid_remove()
    fees_frame.grid_remove()
    side_units_frame.grid_remove()
    examination_frame.grid_remove()
    evaluation_frame.grid_remove()
    clearance_frame.grid_remove()
    my_message_frame.grid_remove()
    profile_canvas.grid_remove()
    change_password_frame.grid_remove()
    home_frame.grid_remove()
    reporting_frame.grid(row=0, column=0)


def deferment_hovered(event):
    deferment_bright_lbl.grid_remove()
    deferment_hovered_lbl.grid(row=3, column=0)


def deferment_normal(event):
    deferment_hovered_lbl.grid_remove()
    deferment_bright_lbl.grid(row=3, column=0)


def show_deferment(event):
    hide_account_options()
    new_and_events_frame.grid_remove()
    reporting_frame.grid_remove()
    fees_frame.grid_remove()
    side_units_frame.grid_remove()
    examination_frame.grid_remove()
    evaluation_frame.grid_remove()
    clearance_frame.grid_remove()
    my_message_frame.grid_remove()
    profile_canvas.grid_remove()
    change_password_frame.grid_remove()
    home_frame.grid_remove()
    deferment_frame.grid(row=0, column=0)


def fees_hovered(event):
    fees_bright_lbl.grid_remove()
    fees_hovered_lbl.grid(row=4, column=0)


def fees_normal(event):
    fees_hovered_lbl.grid_remove()
    fees_bright_lbl.grid(row=4, column=0)


def show_fees(event):
    hide_account_options()
    home_frame.grid_remove()
    new_and_events_frame.grid_remove()
    reporting_frame.grid_remove()
    deferment_frame.grid_remove()
    side_units_frame.grid_remove()
    examination_frame.grid_remove()
    evaluation_frame.grid_remove()
    clearance_frame.grid_remove()
    my_message_frame.grid_remove()
    profile_canvas.grid_remove()
    change_password_frame.grid_remove()
    fees_frame.grid(row=0, column=0)


def units_hovered(event):
    units_bright_lbl.grid_remove()
    units_hovered_lbl.grid(row=5, column=0)


def units_normal(event):
    units_hovered_lbl.grid_remove()
    units_bright_lbl.grid(row=5, column=0)


def show_units(event):
    hide_account_options()
    home_frame.grid_remove()
    new_and_events_frame.grid_remove()
    reporting_frame.grid_remove()
    deferment_frame.grid_remove()
    fees_frame.grid_remove()
    examination_frame.grid_remove()
    evaluation_frame.grid_remove()
    clearance_frame.grid_remove()
    my_message_frame.grid_remove()
    profile_canvas.grid_remove()
    change_password_frame.grid_remove()
    side_units_frame.grid(row=0, column=0)


def examination_hovered(event):
    examination_bright_lbl.grid_remove()
    examination_hovered_lbl.grid(row=6, column=0)


def examination_normal(event):
    examination_hovered_lbl.grid_remove()
    examination_bright_lbl.grid(row=6, column=0)


def show_examination(event):
    hide_account_options()
    home_frame.grid_remove()
    new_and_events_frame.grid_remove()
    reporting_frame.grid_remove()
    deferment_frame.grid_remove()
    fees_frame.grid_remove()
    side_units_frame.grid_remove()
    evaluation_frame.grid_remove()
    clearance_frame.grid_remove()
    my_message_frame.grid_remove()
    profile_canvas.grid_remove()
    change_password_frame.grid_remove()
    examination_frame.grid(row=0, column=0)


def evaluation_hovered(event):
    evaluation_bright_lbl.grid_remove()
    evaluation_hovered_lbl.grid(row=7, column=0)


def evaluation_normal(event):
    evaluation_hovered_lbl.grid_remove()
    evaluation_bright_lbl.grid(row=7, column=0)


def show_evaluation(event):
    hide_account_options()
    home_frame.grid_remove()
    new_and_events_frame.grid_remove()
    reporting_frame.grid_remove()
    deferment_frame.grid_remove()
    fees_frame.grid_remove()
    side_units_frame.grid_remove()
    examination_frame.grid_remove()
    evaluation_frame.grid_remove()
    clearance_frame.grid_remove()
    clearance_frame.grid_remove()
    my_message_frame.grid_remove()
    profile_canvas.grid_remove()
    change_password_frame.grid_remove()
    evaluation_frame.grid(row=0, column=0)


def clearance_hovered(event):
    clearance_bright_lbl.grid_remove()
    clearance_hovered_lbl.grid(row=8, column=0)


def clearance_normal(event):
    clearance_hovered_lbl.grid_remove()
    clearance_bright_lbl.grid(row=8, column=0)


def show_clearance(event):
    hide_account_options()
    home_frame.grid_remove()
    new_and_events_frame.grid_remove()
    reporting_frame.grid_remove()
    deferment_frame.grid_remove()
    fees_frame.grid_remove()
    side_units_frame.grid_remove()
    examination_frame.grid_remove()
    evaluation_frame.grid_remove()
    clearance_frame.grid_remove()
    my_message_frame.grid_remove()
    profile_canvas.grid_remove()
    change_password_frame.grid_remove()
    clearance_frame.grid(row=0, column=0)


def more_units():
    if more_units.clicked:
        units_minus_lbl.grid_remove()
        units_delete_lbl.grid_remove()
        more_units.clicked = False
    else:
        units_minus_lbl.grid(row=0, column=0)
        units_delete_lbl.grid(row=0, column=1, padx=20)
        more_units.clicked = True


def my_profile(event):
    if my_profile.clicked:
        account_canvas_container.place(x=2000, y=nav_bar_height)
        my_profile.clicked = False
    else:
        account_canvas_container.place(x=1165, y=nav_bar_height)
        my_profile.clicked = True


def my_messages_hovered(event):
    my_messages_lbl.grid_remove()
    my_messages_hovered_lbl.grid(row=0, column=0)


def profile_hovered(event):
    profile_hovered_lbl.grid_remove()
    profile_hovered_lbl.grid(row=1, column=0)


def change_password_hovered(event):
    change_password_lbl.grid_remove()
    change_password_hovered_lbl.grid(row=2, column=0)


def logout_hovered(event):
    logout_lbl.grid_remove()
    logout_hovered_lbl.grid(row=3, column=0)


def my_messages_normal(event):
    my_messages_hovered_lbl.grid_remove()
    my_messages_lbl.grid(row=0, column=0)


def profile_normal(event):
    profile_hovered_lbl.grid_remove()
    profile_lbl.grid(row=1, column=0)


def change_password_normal(event):
    change_password_hovered_lbl.grid_remove()
    change_password_lbl.grid(row=2, column=0)


def logout_normal(event):
    logout_hovered_lbl.grid_remove()
    logout_lbl.grid(row=3, column=0)


def hide_account_options():
    if my_profile.clicked:
        account_canvas_container.place(x=2000, y=nav_bar_height)
        my_profile.clicked = False


def show_my_messages(event):
    hide_account_options()
    home_frame.grid_remove()
    new_and_events_frame.grid_remove()
    reporting_frame.grid_remove()
    deferment_frame.grid_remove()
    fees_frame.grid_remove()
    side_units_frame.grid_remove()
    examination_frame.grid_remove()
    evaluation_frame.grid_remove()
    clearance_frame.grid_remove()
    profile_canvas.grid_remove()
    change_password_frame.grid_remove()
    my_message_frame.grid(row=0, column=0)


def show_profile(event):
    hide_account_options()
    home_frame.grid_remove()
    new_and_events_frame.grid_remove()
    reporting_frame.grid_remove()
    deferment_frame.grid_remove()
    fees_frame.grid_remove()
    side_units_frame.grid_remove()
    examination_frame.grid_remove()
    evaluation_frame.grid_remove()
    clearance_frame.grid_remove()
    my_message_frame.grid_remove()
    change_password_frame.grid_remove()
    display_scrollable_profile()


def show_change_password(event):
    hide_account_options()
    home_frame.grid_remove()
    new_and_events_frame.grid_remove()
    reporting_frame.grid_remove()
    deferment_frame.grid_remove()
    fees_frame.grid_remove()
    side_units_frame.grid_remove()
    examination_frame.grid_remove()
    evaluation_frame.grid_remove()
    clearance_frame.grid_remove()
    my_message_frame.grid_remove()
    profile_canvas.grid_remove()
    display_change_password()


def display_change_password():
    display_change_password.current_password = get_change_password_data(the_user)
    change_password_frame.grid(row=0, column=0)


def show_logout(event):
    actually_logout()


def switch_window():
    os.system('python login.py')


def actually_logout():
    try:
        if error_animation.t1.is_alive():
            return
    except:
        pass
    threading.Thread(target=switch_window).start()
    time.sleep(1.6)
    kill_threads()


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


def show_inbox(event):
    deselect_compose()
    deselect_sent()
    deselect_trash()
    select_inbox()
    hide_compose_content()
    hide_sent_content()
    hide_trash_content()
    display_inbox_content()


def select_inbox():
    inbox_lbl.grid_remove()
    inbox_selected_lbl.grid(row=0, column=0)


def deselect_inbox():
    inbox_selected_lbl.grid_remove()
    inbox_lbl.grid(row=0, column=0)


def show_compose(event):
    deselect_inbox()
    deselect_sent()
    deselect_trash()
    select_compose()
    hide_inbox_content()
    hide_sent_content()
    hide_trash_content()
    display_compose_content()


def select_compose():
    compose_lbl.grid_remove()
    compose_selected_lbl.grid(row=0, column=0)
    hide_inbox_content()


def deselect_compose():
    compose_selected_lbl.grid_remove()
    compose_lbl.grid(row=0, column=0)


def show_sent(event):
    deselect_inbox()
    deselect_compose()
    deselect_trash()
    select_sent()
    hide_inbox_content()
    hide_compose_content()
    hide_trash_content()
    display_sent_content()


def select_sent():
    sent_lbl.grid_remove()
    sent_selected_lbl.grid(row=0, column=0)


def deselect_sent():
    sent_selected_lbl.grid_remove()
    sent_lbl.grid(row=0, column=0)


def show_trash(event):
    deselect_inbox()
    deselect_compose()
    deselect_sent()
    select_trash()
    hide_inbox_content()
    hide_compose_content()
    hide_sent_content()
    display_trash_content()


def select_trash():
    trash_lbl.grid_remove()
    trash_selected_lbl.grid(row=0, column=0)


def deselect_trash():
    trash_selected_lbl.grid_remove()
    trash_lbl.grid(row=0, column=0)


def display_inbox_content():
    inbox_details_frame.grid(row=0, column=0)


def hide_inbox_content():
    inbox_details_frame.grid_remove()


def display_compose_content():
    compose_details_frame.grid(row=0, column=0)


def hide_compose_content():
    compose_details_frame.grid_remove()


def send_the_message():
    print(editor_entry.get("1.0", "end-1c"))


def go_back_to_inbox():
    deselect_compose()
    deselect_sent()
    deselect_trash()
    select_inbox()
    hide_compose_content()
    display_inbox_content()


def display_sent_content():
    sent_details_frame.grid(row=0, column=0)


def hide_sent_content():
    sent_details_frame.grid_remove()


def display_trash_content():
    trash_details_frame.grid(row=0, column=0)


def hide_trash_content():
    trash_details_frame.grid_remove()


def show_personal_data(event):
    deselect_academics()
    select_personal_data()
    display_personal_data()
    enable_scroll()
    show_academics.isAcademics = False


def select_personal_data():
    personal_data_lbl.grid_remove()
    personal_data_selected_lbl.grid(row=0, column=0)


def deselect_personal_data():
    personal_data_selected_lbl.grid_remove()
    personal_data_lbl.grid(row=0, column=0)


def display_personal_data():
    show_personal_data_content()
    display_scrollable_profile()


def hide_personal_data_content():
    personal_information_details_container_frame.grid_remove()
    personal_contact_details_container_frame.grid_remove()
    personal_emergency_contact_details_container_frame.grid_remove()
    personal_other_details_details_container_frame.grid_remove()


def show_personal_data_content():
    personal_information_details_container_frame.grid(row=0, column=0)
    personal_contact_details_container_frame.grid(row=0, column=0)
    personal_emergency_contact_details_container_frame.grid(row=0, column=0)
    personal_other_details_details_container_frame.grid(row=0, column=0)


def show_academics(event):
    deselect_personal_data()
    hide_account_options()
    hide_personal_data_content()
    select_academics()
    profile_canvas.yview_moveto(float(0 + 1) / height - nav_bar_height)
    disable_scroll()
    show_academics.isAcademics = True


def select_academics():
    academics_lbl.grid_remove()
    academics_selected_lbl.grid(row=0, column=0)


def deselect_academics():
    academics_selected_lbl.grid_remove()
    academics_lbl.grid(row=0, column=0)


def enable_scroll():
    show_personal_data.allowScroll = True


def disable_scroll():
    show_personal_data.allowScroll = False


def show_new_section(event):
    deselect_events_section()
    select_news()
    display_news_section_content()


def select_news():
    new_and_events_lbl.grid_remove()
    new_and_events_selected_lbl.grid(row=0, column=0)


def deselect_news():
    new_and_events_selected_lbl.grid_remove()
    new_and_events_lbl.grid(row=0, column=0)


def show_events_section(event):
    deselect_news()
    select_events_section()
    display_event_section_content()


def display_event_section_content():
    news_section_details_frame.grid_remove()
    events_section_details_frame.grid(row=0, column=0)


def display_news_section_content():
    events_section_details_frame.grid_remove()
    news_section_details_frame.grid(row=0, column=0)


def select_events_section():
    events_section_unselected_lbl.grid_remove()
    events_section_selected_lbl.grid(row=0, column=0)


def deselect_events_section():
    events_section_selected_lbl.grid_remove()
    events_section_unselected_lbl.grid(row=0, column=0)


def show_defer_section(event):
    deselect_session_section()
    select_defer_section()
    display_defer_content()


def deselect_defer_section():
    defer_selected_lbl.grid_remove()
    defer_lbl.grid(row=0, column=0)


def select_defer_section():
    defer_lbl.grid_remove()
    defer_selected_lbl.grid(row=0, column=0)


def show_session_section(event):
    deselect_defer_section()
    select_session_section()
    display_session_content()


def select_session_section():
    session_lbl.grid_remove()
    session_selected_lbl.grid(row=0, column=0)


def deselect_session_section():
    session_selected_lbl.grid_remove()
    session_lbl.grid(row=0, column=0)


def display_defer_content():
    session_section_details_frame.grid_remove()
    defer_section_details_container_frame.grid(row=0, column=0)


def display_session_content():
    defer_section_details_container_frame.grid_remove()
    session_section_details_frame.grid(row=0, column=0)


# --------------------------
def show_fee_statement_section(event):
    deselect_fee_structure_section()
    select_fee_statement_section()
    display_fee_statement_content()


def deselect_fee_statement_section():
    fee_statement_selected_lbl.grid_remove()
    fee_statement_lbl.grid(row=0, column=0)


def select_fee_statement_section():
    fee_statement_lbl.grid_remove()
    fee_statement_selected_lbl.grid(row=0, column=0)


def show_fee_structure_section(event):
    deselect_fee_statement_section()
    select_fee_structure_section()
    display_fee_structure_content()


def select_fee_structure_section():
    fee_structure_lbl.grid_remove()
    fee_structure_selected_lbl.grid(row=0, column=0)


def deselect_fee_structure_section():
    fee_structure_selected_lbl.grid_remove()
    fee_structure_lbl.grid(row=0, column=0)


def display_fee_statement_content():
    fee_structure_section_details_frame.grid_remove()
    fee_statement_section_details_container_frame.grid(row=0, column=0)


def display_fee_structure_content():
    fee_statement_section_details_container_frame.grid_remove()
    fee_structure_section_details_frame.grid(row=0, column=0)


def show_register_units_section(event):
    deselect_units_history_section()
    deselect_curriculum_section()
    select_register_units_section()
    display_register_units_content()


def deselect_register_units_section():
    register_units_selected_lbl.grid_remove()
    register_units_lbl.grid(row=0, column=0)


def select_register_units_section():
    register_units_lbl.grid_remove()
    register_units_selected_lbl.grid(row=0, column=0)


def show_units_history_section(event):
    deselect_register_units_section()
    deselect_curriculum_section()
    select_units_history_section()
    display_units_history_content()


def select_units_history_section():
    units_history_lbl.grid_remove()
    units_history_selected_lbl.grid(row=0, column=0)


def deselect_units_history_section():
    units_history_selected_lbl.grid_remove()
    units_history_lbl.grid(row=0, column=0)


def display_register_units_content():
    units_history_section_details_frame.grid_remove()
    register_units_section_details_container_frame.grid(row=0, column=0)


def display_units_history_content():
    register_units_section_details_container_frame.grid_remove()
    units_history_section_details_frame.grid(row=0, column=0)


def show_curriculum_section(event):
    deselect_register_units_section()
    deselect_units_history_section()
    select_curriculum_section()


def select_curriculum_section():
    curriculum_lbl.grid_remove()
    curriculum_selected_lbl.grid(row=0, column=0)


def deselect_curriculum_section():
    curriculum_selected_lbl.grid_remove()
    curriculum_lbl.grid(row=0, column=0)


def show_exam_card_section(event):
    deselect_previous_exam_card_section()
    deselect_admin_exam_card_section()
    deselect_progress_report_section()
    deselect_retake_section()
    select_exam_card_section()
    display_exam_card_content()


def deselect_exam_card_section():
    exam_card_selected_lbl.grid_remove()
    exam_card_lbl.grid(row=0, column=0)


def select_exam_card_section():
    exam_card_lbl.grid_remove()
    exam_card_selected_lbl.grid(row=0, column=0)


def show_previous_exam_card_section(event):
    deselect_exam_card_section()
    deselect_admin_exam_card_section()
    deselect_progress_report_section()
    deselect_retake_section()
    select_previous_exam_card_section()
    display_previous_exam_card_content()


def select_previous_exam_card_section():
    previous_exam_card_lbl.grid_remove()
    previous_exam_card_selected_lbl.grid(row=0, column=0)


def deselect_previous_exam_card_section():
    previous_exam_card_selected_lbl.grid_remove()
    previous_exam_card_lbl.grid(row=0, column=0)


def display_exam_card_content():
    previous_exam_card_section_details_frame.grid_remove()
    admin_exam_card_section_details_frame.grid_remove()
    progress_report_section_details_frame.grid_remove()
    retake_section_details_frame.grid_remove()
    exam_card_section_details_container_frame.grid(row=0, column=0)


def display_previous_exam_card_content():
    exam_card_section_details_container_frame.grid_remove()
    admin_exam_card_section_details_frame.grid_remove()
    progress_report_section_details_frame.grid_remove()
    retake_section_details_frame.grid_remove()
    previous_exam_card_section_details_frame.grid(row=0, column=0)


def show_admin_exam_card_section(event):
    deselect_exam_card_section()
    deselect_previous_exam_card_section()
    deselect_progress_report_section()
    deselect_retake_section()
    select_admin_exam_card_section()
    display_admin_exam_card_content()


def select_admin_exam_card_section():
    admin_exam_card_lbl.grid_remove()
    admin_exam_card_selected_lbl.grid(row=0, column=0)


def deselect_admin_exam_card_section():
    admin_exam_card_selected_lbl.grid_remove()
    admin_exam_card_lbl.grid(row=0, column=0)


def display_admin_exam_card_content():
    exam_card_section_details_container_frame.grid_remove()
    previous_exam_card_section_details_frame.grid_remove()
    progress_report_section_details_frame.grid_remove()
    retake_section_details_frame.grid_remove()
    admin_exam_card_section_details_frame.grid(row=0, column=0)


def show_progress_report_section(event):
    deselect_exam_card_section()
    deselect_previous_exam_card_section()
    deselect_admin_exam_card_section()
    deselect_retake_section()
    select_progress_report_section()
    display_progress_report_content()


def select_progress_report_section():
    progress_report_lbl.grid_remove()
    progress_report_selected_lbl.grid(row=0, column=0)


def deselect_progress_report_section():
    progress_report_selected_lbl.grid_remove()
    progress_report_lbl.grid(row=0, column=0)


def display_progress_report_content():
    exam_card_section_details_container_frame.grid_remove()
    previous_exam_card_section_details_frame.grid_remove()
    admin_exam_card_section_details_frame.grid_remove()
    retake_section_details_frame.grid_remove()
    progress_report_section_details_frame.grid(row=0, column=0)


def show_retake_section(event):
    deselect_exam_card_section()
    deselect_previous_exam_card_section()
    deselect_admin_exam_card_section()
    deselect_progress_report_section()
    select_retake_section()
    display_retake_content()


def select_retake_section():
    retake_lbl.grid_remove()
    retake_selected_lbl.grid(row=0, column=0)


def deselect_retake_section():
    retake_selected_lbl.grid_remove()
    retake_lbl.grid(row=0, column=0)


def display_retake_content():
    exam_card_section_details_container_frame.grid_remove()
    previous_exam_card_section_details_frame.grid_remove()
    admin_exam_card_section_details_frame.grid_remove()
    progress_report_section_details_frame.grid_remove()
    retake_section_details_frame.grid(row=0, column=0)


# -------------------------------------------

def show_current_evaluation_section(event):
    deselect_evaluation_history_section()
    select_current_evaluation_section()
    display_current_evaluation_content()


def deselect_current_evaluation_section():
    current_evaluation_selected_lbl.grid_remove()
    current_evaluation_lbl.grid(row=0, column=0)


def select_current_evaluation_section():
    current_evaluation_lbl.grid_remove()
    current_evaluation_selected_lbl.grid(row=0, column=0)


def show_evaluation_history_section(event):
    deselect_current_evaluation_section()
    select_evaluation_history_section()
    display_evaluation_history_content()


def select_evaluation_history_section():
    evaluation_history_lbl.grid_remove()
    evaluation_history_selected_lbl.grid(row=0, column=0)


def deselect_evaluation_history_section():
    evaluation_history_selected_lbl.grid_remove()
    evaluation_history_lbl.grid(row=0, column=0)


def display_current_evaluation_content():
    evaluation_history_section_details_frame.grid_remove()
    current_evaluation_section_details_container_frame.grid(row=0, column=0)


def display_evaluation_history_content():
    current_evaluation_section_details_container_frame.grid_remove()
    evaluation_history_section_details_frame.grid(row=0, column=0)


# ------------------------------------------

def show_apply_for_clearance_section(event):
    deselect_clearance_certificate_section()
    deselect_clearance_history_section()
    select_apply_for_clearance_section()
    display_apply_for_clearance_content()


def deselect_apply_for_clearance_section():
    apply_for_clearance_selected_lbl.grid_remove()
    apply_for_clearance_lbl.grid(row=0, column=0)


def select_apply_for_clearance_section():
    apply_for_clearance_lbl.grid_remove()
    apply_for_clearance_selected_lbl.grid(row=0, column=0)


def show_clearance_certificate_section(event):
    deselect_apply_for_clearance_section()
    deselect_clearance_history_section()
    select_clearance_certificate_section()
    display_clearance_certificate_content()


def select_clearance_certificate_section():
    clearance_certificate_lbl.grid_remove()
    clearance_certificate_selected_lbl.grid(row=0, column=0)


def deselect_clearance_certificate_section():
    clearance_certificate_selected_lbl.grid_remove()
    clearance_certificate_lbl.grid(row=0, column=0)


def display_apply_for_clearance_content():
    clearance_certificate_section_details_frame.grid_remove()
    clearance_history_section_details_frame.grid_remove()
    apply_for_clearance_section_details_container_frame.grid(row=0, column=0)


def display_clearance_certificate_content():
    apply_for_clearance_section_details_container_frame.grid_remove()
    clearance_history_section_details_frame.grid_remove()
    clearance_certificate_section_details_frame.grid(row=0, column=0)


# ---------------------------------------

def show_clearance_history_section(event):
    deselect_apply_for_clearance_section()
    deselect_clearance_certificate_section()
    select_clearance_history_section()
    display_clearance_history_content()


def select_clearance_history_section():
    clearance_history_lbl.grid_remove()
    clearance_history_selected_lbl.grid(row=0, column=0)


def deselect_clearance_history_section():
    clearance_history_selected_lbl.grid_remove()
    clearance_history_lbl.grid(row=0, column=0)


def display_clearance_history_content():
    apply_for_clearance_section_details_container_frame.grid_remove()
    clearance_certificate_section_details_frame.grid_remove()
    clearance_history_section_details_frame.grid(row=0, column=0)


def hide_old_password_placeholder(event):
    if old_password_entry.get() == "Enter Old Password":
        old_password_entry.delete(0, END)
        old_password_entry.configure(fg="#3C3F41")
        old_password_entry.configure(fg="#3C3F41", show="*")


def show_old_password_placeholder(event):
    if old_password_entry.get() == "":
        old_password_entry.configure(fg="#A8A8A9")
        old_password_entry.insert(0, "Enter Old Password")
        old_password_entry.configure(fg="#A8A8A9", show="")


def hide_new_password_placeholder(event):
    if new_password_entry.get() == "Enter new password":
        new_password_entry.delete(0, END)
        new_password_entry.configure(fg="#3C3F41")
        new_password_entry.configure(fg="#3C3F41", show="*")


def show_new_password_placeholder(event):
    if new_password_entry.get() == "":
        new_password_entry.configure(fg="#A8A8A9")
        new_password_entry.insert(0, "Enter new password")
        new_password_entry.configure(fg="#A8A8A9", show="")


def hide_new_confirm_password_placeholder(event):
    if new_confirm_password_entry.get() == "Confirm new password":
        new_confirm_password_entry.delete(0, END)
        new_confirm_password_entry.configure(fg="#3C3F41")
        new_confirm_password_entry.configure(fg="#3C3F41", show="*")


def show_new_confirm_password_placeholder(event):
    if new_confirm_password_entry.get() == "":
        new_confirm_password_entry.configure(fg="#A8A8A9")
        new_confirm_password_entry.insert(0, "Confirm new password")
        new_confirm_password_entry.configure(fg="#A8A8A9", show="")


def actually_change_password():
    if old_password_entry.get() == "" or old_password_entry.get() == "Enter Old Password" or new_password_entry.get() \
            == "" or new_password_entry.get() == "Enter new password" or new_confirm_password_entry.get() == "" \
            or new_confirm_password_entry.get() == "Confirm new password":
        messagebox.showwarning("Warning", "All fields are required")
        return
    if old_password_entry.get() != display_change_password.current_password:
        messagebox.showwarning("Warning", "Your old password is wrong. You cannot change the password")
        return
    if new_password_entry.get() != new_confirm_password_entry.get():
        messagebox.showwarning("Warning", "The new password and the confirm password have to be the same")
        return
    try:
        wasNoError, the_feedback = set_the_new_password(the_user, new_password_entry.get())
        if wasNoError:
            messagebox.showinfo(f"{the_feedback.split(':')[0]}", f"{the_feedback.split(':')[1]}")
            display_change_password.current_password = new_password_entry.get()
        else:
            messagebox.showerror("Error", "An error occurred. Please retry")
    except:
        messagebox.showerror("Error", "An error occurred. Please retry")


def insert_default_contacts():
    personal_contact_telephone_number_entry.delete(0, END)
    personal_contact_telephone_number_entry.insert(0, personal_contact_telephone_number_lbl.cget('text'))

    personal_contact_email_entry.delete(0, END)
    personal_contact_email_entry.insert(0, personal_contact_email_lbl.cget('text'))

    personal_contact_address_entry.delete(0, END)
    personal_contact_address_entry.insert(0, personal_contact_address_lbl.cget('text'))


def insert_default_emergency_contacts():
    personal_emergency_contact_name_entry.delete(0, END)
    personal_emergency_contact_name_entry.insert(0, personal_emergency_name_lbl.cget('text'))

    personal_emergency_contact_relationship_entry.delete(0, END)
    personal_emergency_contact_relationship_entry.insert(0, personal_emergency_relationship_lbl.cget('text'))

    personal_emergency_contact_telephone_number_entry.delete(0, END)
    personal_emergency_contact_telephone_number_entry.insert(0, personal_emergency_telephone_lbl.cget('text'))

    personal_emergency_contact_email_entry.delete(0, END)
    personal_emergency_contact_email_entry.insert(0, personal_emergency_email_lbl.cget('text'))

    personal_emergency_contact_address_entry.delete(0, END)
    personal_emergency_contact_address_entry.insert(0, personal_emergency_address_lbl.cget('text'))

    personal_emergency_contact_remarks_entry.delete(0, END)
    personal_emergency_contact_remarks_entry.insert(0, personal_emergency_remarks_lbl.cget('text'))


def insert_default_other_details():
    personal_other_details_language_entry.delete(0, END)
    personal_other_details_language_entry.insert(0, personal_other_details_language_lbl.cget('text'))

    personal_other_details_medical_entry.delete(0, END)
    personal_other_details_medical_entry.insert(0, personal_other_details_medical_lbl.cget('text'))

    personal_other_details_cirriculum_entry.delete(0, END)
    personal_other_details_cirriculum_entry.insert(0, personal_other_details_cirriculum_lbl.cget('text'))


def edit_personal_contact():
    cancel_emergency_contact()
    cancel_personal_other_details()
    insert_default_contacts()
    personal_contact_frame.grid_remove()
    personal_contact_edit_frame.grid(row=0, column=0)


def edit_personal_emergency_contact():
    cancel_personal_contact()
    cancel_personal_other_details()
    insert_default_emergency_contacts()
    personal_other_details_details_frame.place_configure(x=262 - side_bar_width - 10, y=1028 + 52)
    personal_emergency_contact_frame.grid_remove()
    personal_emergency_contact_edit_frame.grid(row=0, column=0)
    profile_canvas.configure(height=profile_canvas.winfo_height() + 250)
    profile_frame_container.configure(height=profile_frame_container.winfo_height() + 300)
    profile_frame.configure(height=profile_frame.winfo_height() + 300)


def edit_personal_other_details():
    cancel_personal_contact()
    cancel_emergency_contact()
    insert_default_other_details()
    personal_other_details_frame.grid_remove()
    personal_other_details_edit_frame.grid(row=0, column=0)
    profile_canvas.configure(height=profile_canvas.winfo_height() + 215)
    profile_frame_container.configure(height=profile_frame_container.winfo_height() + 300)
    profile_frame.configure(height=profile_frame.winfo_height() + 300)


def cancel_personal_contact():
    personal_contact_edit_frame.grid_remove()
    personal_contact_frame.grid(row=0, column=0)


def cancel_emergency_contact():
    profile_canvas.configure(height=735)
    profile_frame.configure(height=1286)
    profile_frame_container.configure(height=1286)
    personal_other_details_details_frame.place_configure(x=262 - side_bar_width - 10, y=1028)
    personal_emergency_contact_edit_frame.grid_remove()
    personal_emergency_contact_frame.grid(row=0, column=0)


def cancel_personal_other_details():
    profile_canvas.configure(height=735)
    profile_frame.configure(height=1286)
    personal_other_details_edit_frame.grid_remove()
    personal_other_details_frame.grid(row=0, column=0)


def update_the_contacts():
    if personal_information_registration_number_lbl.cget('text') == '':
        return
    if not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', personal_contact_email_entry.get()):
        messagebox.showwarning("Warning", "Your email address is invalid. Correct it then retry")
        return
    feedback = update_contacts(personal_information_registration_number_lbl.cget('text'),
                               personal_contact_telephone_number_entry.get(),
                               personal_contact_email_entry.get(),
                               personal_contact_address_entry.get(),
                               personal_contact_county_lbl.cget('text'),
                               personal_contact_domicile_lbl.cget('text'),
                               personal_contact_subcounty_lbl.cget('text'),
                               personal_contact_constituency_lbl.cget('text'))

    if feedback == 'Success':
        personal_contact_telephone_number_lbl.configure(text=personal_contact_telephone_number_entry.get())
        personal_contact_email_lbl.configure(text=personal_contact_email_entry.get())
        personal_contact_address_lbl.configure(text=personal_contact_address_entry.get())
        cancel_personal_contact()


def update_the_emergency_contacts():
    if personal_information_registration_number_lbl.cget('text') == '':
        return
    if not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
                    personal_emergency_contact_email_entry.get()):
        messagebox.showwarning("Warning", "Your email address is invalid. Correct it then retry")
        return
    feedback = update_emergency_contacts(personal_information_registration_number_lbl.cget('text'),
                                         personal_emergency_contact_name_entry.get(),
                                         personal_emergency_contact_relationship_entry.get(),
                                         personal_emergency_contact_telephone_number_entry.get(),
                                         personal_emergency_contact_email_entry.get(),
                                         personal_emergency_contact_address_entry.get(),
                                         personal_emergency_contact_remarks_entry.get())

    if feedback == 'Success':
        personal_emergency_name_lbl.configure(text=personal_emergency_contact_name_entry.get())
        personal_emergency_relationship_lbl.configure(text=personal_emergency_contact_relationship_entry.get())
        personal_emergency_telephone_lbl.configure(text=personal_emergency_contact_telephone_number_entry.get())
        personal_emergency_email_lbl.configure(text=personal_emergency_contact_email_entry.get())
        personal_emergency_address_lbl.configure(text=personal_emergency_contact_address_entry.get())
        personal_emergency_remarks_lbl.configure(text=personal_emergency_contact_remarks_entry.get())
        cancel_emergency_contact()


def update_the_other_details():
    if personal_information_registration_number_lbl.cget('text') == '':
        return
    feedback = update_other_details(personal_information_registration_number_lbl.cget('text'),
                                    personal_other_details_language_entry.get(),
                                    personal_other_details_medical_entry.get(),
                                    personal_other_details_cirriculum_entry.get())

    if feedback == 'Success':
        personal_other_details_language_lbl.configure(text=personal_other_details_language_entry.get())
        personal_other_details_medical_lbl.configure(text=personal_other_details_medical_entry.get())
        personal_other_details_cirriculum_lbl.configure(text=personal_other_details_cirriculum_entry.get())
        cancel_personal_other_details()


# ------------------------------------------------------------------------------------
more_units.clicked = False
my_profile.clicked = False
error_animation.sleep = 2
error_animation.t = 0.5
error_animation.counter = 0
show_personal_data.allowScroll = True
show_academics.isAcademics = False
display_change_password.current_password = ""

with open('portal.txt', 'r') as f:
    the_user = f.read()

root = Tk()

width = 1440
height = 735

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = ((screen_width / 2) - (width / 2))
y = ((screen_height / 2) - (height / 2))

root.geometry(f'{width}x{height}+{int(x)}+{int(y) - 30}')
photo = PhotoImage(file='images/machakos-logo.png')
root.wm_iconphoto(True, photo)

font1 = ("OpenSans-Regular", 11, "bold")
font2 = ("OpenSans-Regular", 11)
font3 = ("OpenSans", 11)

root.title(the_user)
root.configure(bg="#ECF0F5")
canvas = Canvas(
    root,
    bg="#ECF0F5",
    height=735,
    width=1440,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"images/home/home-background.png")
background = canvas.create_image(
    717.0, 367.5,
    image=background_img)

nav_bar_height = 48
side_bar_width = 244

nav_bar = Frame(canvas, height=nav_bar_height, bg="#2E3091", width=width)
nav_bar.place(x=0, y=0)
nav_bar.bind("<Button-1>", lambda e: hide_account_options())

user_name_frame = Frame(nav_bar, width=50, height=nav_bar_height / 2, bg="#2E3091")
user_name_frame.place(relx=0.982, rely=0.3, anchor='ne')

user_name_lbl = Label(user_name_frame, text=the_user, foreground="white", bg="#2E3091", font=font1)
user_name_lbl.grid(row=0, column=0)
user_name_lbl.bind("<Button-1>", my_profile)

point_down_img = PhotoImage(file="images/home/point-down.png")
point_down_lbl = Label(user_name_frame, image=point_down_img, bg="#2E3091")
point_down_lbl.grid(row=0, column=1)
point_down_lbl.bind("<Button-1>", my_profile)

left_side_bar = Canvas(root, bg="#ffffff", height=height - nav_bar.winfo_height(), width=side_bar_width, bd=0,
                       highlightthickness=0, relief="ridge")
left_side_bar.place(x=0, y=nav_bar_height)
left_side_bar.bind("<Button-1>", lambda e: hide_account_options())

side_background_img = PhotoImage(file="images/home/side_background.png")
side_background = left_side_bar.create_image(
    (side_background_img.width() / 2) - 7, (side_background_img.height() / 2) - 5,
    image=side_background_img)

content_area = Canvas(root, bg="#ECF0F5", height=height - nav_bar.winfo_height(),
                      width=width - left_side_bar.winfo_width(), bd=0, highlightthickness=0, relief="ridge")
content_area.place(x=side_bar_width, y=nav_bar_height)
# content_area.bind_all("<MouseWheel>", on_mousewheel)

home_frame = Frame(content_area, bg="#ECF0F5", width=width - left_side_bar.winfo_width(),
                   height=height - nav_bar.winfo_height())
home_frame.grid(row=0, column=0)
home_frame.bind("<Button-1>", lambda e: hide_account_options())

news_frame = Frame(home_frame)
news_frame.place(x=262 - side_bar_width - 10, y=63 - nav_bar_height)

news_img = PhotoImage(file="images/home/news.png")
news_lbl = Label(news_frame, image=news_img, bg="#ECF0F5")
news_lbl.grid(row=0, column=0)

units_frame = Frame(home_frame)
units_frame.place(x=262 - side_bar_width - 10, y=191 - nav_bar_height)

units_img = PhotoImage(file="images/home/units.png")
units_lbl = Label(units_frame, image=units_img, bg="#ECF0F5")
units_lbl.grid(row=0, column=0)

units_more_img = PhotoImage(file="images/home/more.png")
units_more_lbl = Button(units_frame, image=units_more_img, bg="#ffffff", relief="flat", bd=0,
                        activebackground="#ffffff", command=more_units)
units_more_lbl.place(relx=0.93, rely=0.47, anchor=CENTER)

units_more_extras_frame = Frame(units_frame, bg="#ffffff")
units_more_extras_frame.place(relx=0.86, rely=0.47, anchor=CENTER)

units_minus_img = PhotoImage(file="images/home/minus.png")
units_minus_lbl = Button(units_more_extras_frame, image=units_minus_img, bg="#ffffff", relief="flat", bd=0,
                         activebackground="#ffffff")
# units_minus_lbl.grid(row=0, column=0)

units_delete_img = PhotoImage(file="images/home/delete.png")
units_delete_lbl = Button(units_more_extras_frame, image=units_delete_img, bg="#ffffff", relief="flat", bd=0,
                          activebackground="#ffffff")
# units_delete_lbl.grid(row=0, column=1, padx=20)

events_frame = Frame(home_frame)
events_frame.place(x=262 - side_bar_width - 10, y=279 - nav_bar_height)

events_img = PhotoImage(file="images/home/events.png")
events_lbl = Label(events_frame, image=events_img, bg="#ECF0F5")
events_lbl.grid(row=0, column=0)

fee_frame = Frame(home_frame)
fee_frame.place(x=956 - side_bar_width - 10, y=65 - nav_bar_height)

fee_img = PhotoImage(file="images/home/fee-balance.png")
fee_lbl = Label(fee_frame, image=fee_img, bg="#ECF0F5")
fee_lbl.grid(row=0, column=0)

fee_balance_data_lbl = Label(fee_frame, text="KES 0.00", foreground="#ffffff", font=("OpenSans-Regular", 20, "bold"),
                             bg="#FFBA57")
fee_balance_data_lbl.place(relx=0.5, rely=0.55, anchor=CENTER)

hostel_frame = Frame(home_frame)
hostel_frame.place(x=956 - side_bar_width - 10, y=206 - nav_bar_height)

hostel_img = PhotoImage(file="images/home/hostel.png")
hostel_lbl = Label(hostel_frame, image=hostel_img, bg="#ECF0F5")
hostel_lbl.grid(row=0, column=0)

hostel_data_lbl = Label(hostel_frame, text="No hostel History", foreground="#ffffff",
                        font=("OpenSans-Regular", 20, "bold"),
                        bg="#448AFF")
hostel_data_lbl.place(relx=0.5, rely=0.572, anchor=CENTER)
# ----------------------------------------------------------------------------------------------

new_and_events_frame = Frame(content_area, bg="#ECF0F5", width=width - left_side_bar.winfo_width(),
                             height=height - nav_bar.winfo_height())

new_and_events_options_frame = Frame(new_and_events_frame)
new_and_events_options_frame.place(x=262 - side_bar_width - 10, y=19)

new_and_events_options_img = PhotoImage(file="images/news&events/news/news-options-container.png")
new_and_events_options_lbl = Label(new_and_events_options_frame, image=new_and_events_options_img, bg="#ECF0F5")
new_and_events_options_lbl.grid(row=0, column=0)

new_section_frame = Frame(new_and_events_frame)
new_section_frame.place(x=20, y=25)

new_and_events_selected_img = PhotoImage(file="images/news&events/news/news-selected.png")
new_and_events_selected_lbl = Label(new_section_frame, image=new_and_events_selected_img, bg="#ffffff",
                                    relief='flat', bd=0)
new_and_events_selected_lbl.grid(row=0, column=0)
new_and_events_selected_lbl.bind("<Button-1>", show_new_section)

new_and_events_img = PhotoImage(file="images/news&events/news/news.png")
new_and_events_lbl = Label(new_section_frame, image=new_and_events_img, bg="#ffffff",
                           relief='flat', bd=0)
new_and_events_lbl.bind("<Button-1>", show_new_section)

news_details_frame = Frame(new_and_events_frame, bg="#ECF0F5")
news_details_frame.place(x=262 - side_bar_width - 10, y=173 - nav_bar_height)

news_section_details_frame = Frame(news_details_frame, bg="#ECF0F5")
news_section_details_frame.grid(row=0, column=0)

news_section_details_container_frame = Frame(news_section_details_frame)
news_section_details_container_frame.grid(row=0, column=0)

news_section_details_container_img = PhotoImage(file="images/news&events/news/news-container.png")
news_section_details_container_lbl = Label(news_section_details_container_frame,
                                           image=news_section_details_container_img, bg="#ECF0F5")
news_section_details_container_lbl.grid(row=0, column=0)

# -------------------------------------------------------------------
event_section_frame = Frame(new_and_events_frame)
event_section_frame.place(x=599, y=25)

events_section_unselected_img = PhotoImage(file="images/news&events/news/events.png")
events_section_unselected_lbl = Label(event_section_frame, image=events_section_unselected_img, bg="#ffffff",
                                      relief='flat', bd=0)
events_section_unselected_lbl.grid(row=0, column=0)
events_section_unselected_lbl.bind("<Button-1>", show_events_section)

events_section_selected_img = PhotoImage(file="images/news&events/news/events-selected.png")
events_section_selected_lbl = Label(event_section_frame, image=events_section_selected_img, bg="#ffffff",
                                    relief='flat', bd=0)
events_section_selected_lbl.bind("<Button-1>", show_events_section)

# events_details_frame = Frame(new_and_events_frame, bg="#ECF0F5")
# events_details_frame.place(x=262 - side_bar_width - 10, y=173 - nav_bar_height)

events_section_details_frame = Frame(news_details_frame, bg="#ECF0F5")
# events_section_details_frame.grid(row=0, column=0)

events_section_details_container_frame = Frame(events_section_details_frame)
events_section_details_container_frame.grid(row=0, column=0)

events_section_details_container_img = PhotoImage(file="images/news&events/events/events-container.png")
events_section_details_container_lbl = Label(events_section_details_container_frame,
                                             image=events_section_details_container_img, bg="#ECF0F5")
events_section_details_container_lbl.grid(row=0, column=0)

# ----------------------------------------------------------------------------------------------
reporting_frame = Frame(content_area, bg="#ECF0F5", width=width - left_side_bar.winfo_width(),
                        height=height - nav_bar.winfo_height())

reporting_options_frame = Frame(reporting_frame)
reporting_options_frame.place(x=262 - side_bar_width - 10, y=88 - nav_bar_height)

reporting_options_container_frame = Frame(reporting_options_frame)
reporting_options_container_frame.grid(row=0, column=0)

reporting_options_img = PhotoImage(file="images/reporting/reporting-container.png")
reporting_options_lbl = Label(reporting_options_container_frame, image=reporting_options_img, bg="#ECF0F5")
reporting_options_lbl.grid(row=0, column=0)

reporting_options_btn_img = PhotoImage(file="images/reporting/report-now.png")
reporting_options_btn = Button(reporting_options_container_frame, image=reporting_options_btn_img, bg="#ffffff",
                               activebackground="#ffffff", bd=0, relief='flat')
reporting_options_btn.place(x=989, y=121)

# -------------------------------------------------------------------------------------------
deferment_frame = Frame(content_area, bg="#ECF0F5", width=width - left_side_bar.winfo_width(),
                        height=height - nav_bar.winfo_height())

deferment_options_frame = Frame(deferment_frame)
deferment_options_frame.place(x=262 - side_bar_width - 10, y=19)

deferment_options_img = PhotoImage(file="images/deferment/defer/deferment-options-container.png")
deferment_options_lbl = Label(deferment_options_frame, image=deferment_options_img, bg="#ECF0F5")
deferment_options_lbl.grid(row=0, column=0)

defer_section_frame = Frame(deferment_frame)
defer_section_frame.place(x=20, y=25)

defer_selected_img = PhotoImage(file="images/deferment/defer/defer-selected.png")
defer_selected_lbl = Label(defer_section_frame, image=defer_selected_img, bg="#ffffff",
                           relief='flat', bd=0)
defer_selected_lbl.grid(row=0, column=0)
defer_selected_lbl.bind("<Button-1>", show_defer_section)

defer_img = PhotoImage(file="images/deferment/defer/defer.png")
defer_lbl = Label(defer_section_frame, image=defer_img, bg="#ffffff",
                  relief='flat', bd=0)
defer_lbl.bind("<Button-1>", show_defer_section)

defer_details_frame = Frame(deferment_frame, bg="#ECF0F5")
defer_details_frame.place(x=262 - side_bar_width - 10, y=173 - nav_bar_height)

defer_section_details_frame = Frame(defer_details_frame, bg="#ECF0F5")
defer_section_details_frame.grid(row=0, column=0)

defer_section_details_container_frame = Frame(defer_section_details_frame)
defer_section_details_container_frame.grid(row=0, column=0)

defer_section_details_container_img = PhotoImage(file="images/deferment/defer/defer-container.png")
defer_section_details_container_lbl = Label(defer_section_details_container_frame,
                                            image=defer_section_details_container_img, bg="#ECF0F5")
defer_section_details_container_lbl.grid(row=0, column=0)

defer_section_add_img = PhotoImage(file="images/deferment/defer/add.png")
defer_section_details_add_btn = Button(defer_section_details_container_frame, image=defer_section_add_img, bg="#ffffff",
                                       activebackground="#ffffff", bd=0, relief='flat')
defer_section_details_add_btn.place(x=25, y=78)

# ----------------------------------------------------------------------------------------------------------
session_section_frame = Frame(deferment_frame)
session_section_frame.place(x=599, y=25)

session_selected_img = PhotoImage(file="images/deferment/sessions/session-selected.png")
session_selected_lbl = Label(session_section_frame, image=session_selected_img, bg="#ffffff",
                             relief='flat', bd=0)
session_selected_lbl.bind("<Button-1>", show_session_section)

session_img = PhotoImage(file="images/deferment/sessions/session.png")
session_lbl = Label(session_section_frame, image=session_img, bg="#ffffff",
                    relief='flat', bd=0)
session_lbl.grid(row=0, column=0)
session_lbl.bind("<Button-1>", show_session_section)

# session_details_frame = Frame(deferment_frame, bg="#ECF0F5")
# session_details_frame.place(x=262 - side_bar_width - 10, y=173 - nav_bar_height)
#
session_section_details_frame = Frame(defer_section_details_frame, bg="#ECF0F5")
# session_section_details_frame.grid(row=0, column=0)

session_section_details_container_frame = Frame(session_section_details_frame)
session_section_details_container_frame.grid(row=0, column=0)

session_section_details_container_img = PhotoImage(file="images/deferment/sessions/session-container.png")
session_section_details_container_lbl = Label(session_section_details_container_frame,
                                              image=session_section_details_container_img, bg="#ECF0F5")
session_section_details_container_lbl.grid(row=0, column=0)

# -------------------------------------------------------------------------------------------------
fees_frame = Frame(content_area, bg="#ECF0F5", width=width - left_side_bar.winfo_width(),
                   height=height - nav_bar.winfo_height())

fees_options_frame = Frame(fees_frame)
fees_options_frame.place(x=262 - side_bar_width - 10, y=19)

fees_options_img = PhotoImage(file="images/fees/fees-statement/option-container.png")
fees_options_lbl = Label(fees_options_frame, image=fees_options_img, bg="#ECF0F5")
fees_options_lbl.grid(row=0, column=0)

fee_statement_section_frame = Frame(fees_frame)
fee_statement_section_frame.place(x=20, y=25)

fee_statement_selected_img = PhotoImage(file="images/fees/fees-statement/fee-statement-selected.png")
fee_statement_selected_lbl = Label(fee_statement_section_frame, image=fee_statement_selected_img, bg="#ffffff",
                                   relief='flat', bd=0)
fee_statement_selected_lbl.grid(row=0, column=0)
fee_statement_selected_lbl.bind("<Button-1>", show_fee_statement_section)

fee_statement_img = PhotoImage(file="images/fees/fees-statement/fee-statement.png")
fee_statement_lbl = Label(fee_statement_section_frame, image=fee_statement_img, bg="#ffffff",
                          relief='flat', bd=0)
fee_statement_lbl.bind("<Button-1>", show_fee_statement_section)

fee_statement_details_frame = Frame(fees_frame, bg="#ECF0F5")
fee_statement_details_frame.place(x=262 - side_bar_width - 10, y=173 - nav_bar_height)

fee_statement_section_details_frame = Frame(fee_statement_details_frame, bg="#ECF0F5")
fee_statement_section_details_frame.grid(row=0, column=0)

fee_statement_section_details_container_frame = Frame(fee_statement_section_details_frame)
fee_statement_section_details_container_frame.grid(row=0, column=0)

fee_statement_section_details_container_img = PhotoImage(file="images/fees/fees-statement/fee-statement-container.png")
fee_statement_section_details_container_lbl = Label(fee_statement_section_details_container_frame,
                                                    image=fee_statement_section_details_container_img, bg="#ECF0F5")
fee_statement_section_details_container_lbl.grid(row=0, column=0)

fee_statement_section_add_img = PhotoImage(file="images/fees/fees-statement/download.png")
fee_statement_section_details_add_btn = Button(fee_statement_section_details_container_frame,
                                               image=fee_statement_section_add_img, bg="#ffffff",
                                               activebackground="#ffffff", bd=0, relief='flat')
fee_statement_section_details_add_btn.place(x=960, y=17)

# ----------------------------------------------------------------------------------------------------------
fee_structure_section_frame = Frame(fees_frame)
fee_structure_section_frame.place(x=599, y=25)

fee_structure_selected_img = PhotoImage(file="images/fees/fees-structure/fee-structure-selected.png")
fee_structure_selected_lbl = Label(fee_structure_section_frame, image=fee_structure_selected_img, bg="#ffffff",
                                   relief='flat', bd=0)
fee_structure_selected_lbl.bind("<Button-1>", show_fee_structure_section)

fee_structure_img = PhotoImage(file="images/fees/fees-structure/fee-structure.png")
fee_structure_lbl = Label(fee_structure_section_frame, image=fee_structure_img, bg="#ffffff",
                          relief='flat', bd=0)
fee_structure_lbl.grid(row=0, column=0)
fee_structure_lbl.bind("<Button-1>", show_fee_structure_section)

# session_details_frame = Frame(fees_frame, bg="#ECF0F5")
# session_details_frame.place(x=262 - side_bar_width - 10, y=173 - nav_bar_height)
#
fee_structure_section_details_frame = Frame(fee_statement_section_details_frame, bg="#ECF0F5")
# fee_structure_section_details_frame.grid(row=0, column=0)

fee_structure_section_details_container_frame = Frame(fee_structure_section_details_frame)
fee_structure_section_details_container_frame.grid(row=0, column=0)

fee_structure_section_details_container_img = PhotoImage(file="images/fees/fees-structure/fee-structure-container.png")
fee_structure_section_details_container_lbl = Label(fee_structure_section_details_container_frame,
                                                    image=fee_structure_section_details_container_img, bg="#ECF0F5")
fee_structure_section_details_container_lbl.grid(row=0, column=0)

# -----------------------------------------------------------------------------------------------------

side_units_frame = Frame(content_area, bg="#ECF0F5", width=width - left_side_bar.winfo_width(),
                         height=height - nav_bar.winfo_height())

side_units_options_frame = Frame(side_units_frame)
side_units_options_frame.place(x=262 - side_bar_width - 10, y=19)

side_units_options_img = PhotoImage(file="images/units/register-units/units-options-container.png")
side_units_options_lbl = Label(side_units_options_frame, image=side_units_options_img, bg="#ECF0F5")
side_units_options_lbl.grid(row=0, column=0)

register_units_section_frame = Frame(side_units_frame)
register_units_section_frame.place(x=20, y=25)

register_units_selected_img = PhotoImage(file="images/units/register-units/registered-units-selected.png")
register_units_selected_lbl = Label(register_units_section_frame, image=register_units_selected_img, bg="#ffffff",
                                    relief='flat', bd=0)
register_units_selected_lbl.grid(row=0, column=0)
register_units_selected_lbl.bind("<Button-1>", show_register_units_section)

register_units_img = PhotoImage(file="images/units/register-units/registered-units.png")
register_units_lbl = Label(register_units_section_frame, image=register_units_img, bg="#ffffff",
                           relief='flat', bd=0)
register_units_lbl.bind("<Button-1>", show_register_units_section)

register_units_details_frame = Frame(side_units_frame, bg="#ECF0F5")
register_units_details_frame.place(x=262 - side_bar_width - 10, y=173 - nav_bar_height)

register_units_section_details_frame = Frame(register_units_details_frame, bg="#ECF0F5")
register_units_section_details_frame.grid(row=0, column=0)

register_units_section_details_container_frame = Frame(register_units_section_details_frame)
register_units_section_details_container_frame.grid(row=0, column=0)

register_units_section_details_container_img = PhotoImage(
    file="images/units/register-units/units-details-container.png")
register_units_section_details_container_lbl = Label(register_units_section_details_container_frame,
                                                     image=register_units_section_details_container_img, bg="#ECF0F5")
register_units_section_details_container_lbl.grid(row=0, column=0)

register_units_section_add_img = PhotoImage(file="images/units/register-units/units-status-container.png")
register_units_section_details_add_btn = Label(side_units_frame, image=register_units_section_add_img, bg="#ECF0F5",
                                               bd=0, relief='flat')
register_units_section_details_add_btn.place(x=10, y=270)

# ----------------------------------------------------------------------------------------------------------
units_history_section_frame = Frame(side_units_frame)
units_history_section_frame.place(x=406, y=25)

units_history_selected_img = PhotoImage(file="images/units/units-history/units-history-selected.png")
units_history_selected_lbl = Label(units_history_section_frame, image=units_history_selected_img, bg="#ffffff",
                                   relief='flat', bd=0)
units_history_selected_lbl.bind("<Button-1>", show_units_history_section)

units_history_img = PhotoImage(file="images/units/units-history/units-history.png")
units_history_lbl = Label(units_history_section_frame, image=units_history_img, bg="#ffffff",
                          relief='flat', bd=0)
units_history_lbl.grid(row=0, column=0)
units_history_lbl.bind("<Button-1>", show_units_history_section)

units_history_section_details_frame = Frame(register_units_section_details_frame, bg="#ECF0F5")

units_history_section_details_container_frame = Frame(units_history_section_details_frame)
units_history_section_details_container_frame.grid(row=0, column=0)

units_history_section_details_container_img = PhotoImage(file="images/units/register-units/units-details-container.png")
units_history_section_details_container_lbl = Label(units_history_section_details_container_frame,
                                                    image=units_history_section_details_container_img, bg="#ECF0F5")
units_history_section_details_container_lbl.grid(row=0, column=0)

curriculum_section_frame = Frame(side_units_frame)
curriculum_section_frame.place(x=791, y=25)

curriculum_selected_img = PhotoImage(file="images/units/curriculum/curriculum-selected.png")
curriculum_selected_lbl = Label(curriculum_section_frame, image=curriculum_selected_img, bg="#ffffff",
                                relief='flat', bd=0)
curriculum_selected_lbl.bind("<Button-1>", show_curriculum_section)

curriculum_img = PhotoImage(file="images/units/curriculum/curriculum.png")
curriculum_lbl = Label(curriculum_section_frame, image=curriculum_img, bg="#ffffff",
                       relief='flat', bd=0)
curriculum_lbl.grid(row=0, column=0)
curriculum_lbl.bind("<Button-1>", show_curriculum_section)

# -----------------------------------------------------------------------------------------------------

examination_frame = Frame(content_area, bg="#ECF0F5", width=width - left_side_bar.winfo_width(),
                          height=height - nav_bar.winfo_height())

examination_options_frame = Frame(examination_frame)
examination_options_frame.place(x=262 - side_bar_width - 10, y=19)

examination_options_img = PhotoImage(file="images/examination/exam-card/options-container.png")
examination_options_lbl = Label(examination_options_frame, image=examination_options_img, bg="#ECF0F5")
examination_options_lbl.grid(row=0, column=0)

exam_card_section_frame = Frame(examination_frame)
exam_card_section_frame.place(x=20, y=25)

exam_card_selected_img = PhotoImage(file="images/examination/exam-card/exam-card-selected.png")
exam_card_selected_lbl = Label(exam_card_section_frame, image=exam_card_selected_img, bg="#ffffff",
                               relief='flat', bd=0)
exam_card_selected_lbl.grid(row=0, column=0)
exam_card_selected_lbl.bind("<Button-1>", show_exam_card_section)

exam_card_img = PhotoImage(file="images/examination/exam-card/exam-card.png")
exam_card_lbl = Label(exam_card_section_frame, image=exam_card_img, bg="#ffffff",
                      relief='flat', bd=0)
exam_card_lbl.bind("<Button-1>", show_exam_card_section)

exam_card_details_frame = Frame(examination_frame, bg="#ECF0F5")
exam_card_details_frame.place(x=262 - side_bar_width - 10, y=173 - nav_bar_height)

exam_card_section_details_frame = Frame(exam_card_details_frame, bg="#ECF0F5")
exam_card_section_details_frame.grid(row=0, column=0)

exam_card_section_details_container_frame = Frame(exam_card_section_details_frame)
exam_card_section_details_container_frame.grid(row=0, column=0)

exam_card_section_details_container_img = PhotoImage(file="images/examination/exam-card/exam-card-container.png")
exam_card_section_details_container_lbl = Label(exam_card_section_details_container_frame,
                                                image=exam_card_section_details_container_img, bg="#ECF0F5")
exam_card_section_details_container_lbl.grid(row=0, column=0)

exam_card_section_add_img = PhotoImage(file="images/examination/exam-card/download-history.png")
exam_card_section_details_add_btn = Button(exam_card_section_details_container_frame, image=exam_card_section_add_img,
                                           bg="#ffffff",
                                           activebackground="#ffffff", bd=0, relief='flat')
exam_card_section_details_add_btn.place(x=829, y=39)

# ----------------------------------------------------------------------------------------------------------
previous_exam_card_section_frame = Frame(examination_frame)
previous_exam_card_section_frame.place(x=252, y=25)

previous_exam_card_selected_img = PhotoImage(file="images/examination/previous-exam-card/exam-card-selected.png")
previous_exam_card_selected_lbl = Label(previous_exam_card_section_frame, image=previous_exam_card_selected_img,
                                        bg="#ffffff",
                                        relief='flat', bd=0)
previous_exam_card_selected_lbl.bind("<Button-1>", show_previous_exam_card_section)

previous_exam_card_img = PhotoImage(file="images/examination/previous-exam-card/exam-card.png")
previous_exam_card_lbl = Label(previous_exam_card_section_frame, image=previous_exam_card_img, bg="#ffffff",
                               relief='flat', bd=0)
previous_exam_card_lbl.grid(row=0, column=0)
previous_exam_card_lbl.bind("<Button-1>", show_previous_exam_card_section)

# previous_exam_card_details_frame = Frame(examination_frame, bg="#ECF0F5")
# previous_exam_card_details_frame.place(x=262 - side_bar_width - 10, y=173 - nav_bar_height)
#
previous_exam_card_section_details_frame = Frame(exam_card_section_details_frame, bg="#ECF0F5")
# previous_exam_card_section_details_frame.grid(row=0, column=0)

previous_exam_card_section_details_container_frame = Frame(previous_exam_card_section_details_frame)
previous_exam_card_section_details_container_frame.grid(row=0, column=0)

previous_exam_card_section_details_container_img = PhotoImage(
    file="images/examination/previous-exam-card/exam-card-container.png")
previous_exam_card_section_details_container_lbl = Label(previous_exam_card_section_details_container_frame,
                                                         image=previous_exam_card_section_details_container_img,
                                                         bg="#ECF0F5")
previous_exam_card_section_details_container_lbl.grid(row=0, column=0)

previous_exam_card_section_add_img = PhotoImage(file="images/examination/previous-exam-card/download-history.png")
previous_exam_card_section_details_add_btn = Button(previous_exam_card_section_details_container_frame,
                                                    image=previous_exam_card_section_add_img, bg="#ffffff",
                                                    activebackground="#ffffff", bd=0, relief='flat')
previous_exam_card_section_details_add_btn.place(x=829, y=39)

# ---------------------------------------------

admin_exam_card_section_frame = Frame(examination_frame)
admin_exam_card_section_frame.place(x=482, y=25)

admin_exam_card_selected_img = PhotoImage(file="images/examination/exam-card-set-by-admin/exam-card-selected.png")
admin_exam_card_selected_lbl = Label(admin_exam_card_section_frame, image=admin_exam_card_selected_img, bg="#ffffff",
                                     relief='flat', bd=0)
admin_exam_card_selected_lbl.bind("<Button-1>", show_admin_exam_card_section)

admin_exam_card_img = PhotoImage(file="images/examination/exam-card-set-by-admin/exam-card.png")
admin_exam_card_lbl = Label(admin_exam_card_section_frame, image=admin_exam_card_img, bg="#ffffff",
                            relief='flat', bd=0)
admin_exam_card_lbl.grid(row=0, column=0)
admin_exam_card_lbl.bind("<Button-1>", show_admin_exam_card_section)

# admin_exam_card_details_frame = Frame(examination_frame, bg="#ECF0F5")
# admin_exam_card_details_frame.place(x=262 - side_bar_width - 10, y=173 - nav_bar_height)
#
admin_exam_card_section_details_frame = Frame(exam_card_section_details_frame, bg="#ECF0F5")
# admin_exam_card_section_details_frame.grid(row=0, column=0)

admin_exam_card_section_details_container_frame = Frame(admin_exam_card_section_details_frame)
admin_exam_card_section_details_container_frame.grid(row=0, column=0)

admin_exam_card_section_details_container_img = PhotoImage(
    file="images/examination/exam-card-set-by-admin/exam-card-container.png")
admin_exam_card_section_details_container_lbl = Label(admin_exam_card_section_details_container_frame,
                                                      image=admin_exam_card_section_details_container_img, bg="#ECF0F5")
admin_exam_card_section_details_container_lbl.grid(row=0, column=0)

admin_exam_card_section_add_img = PhotoImage(file="images/examination/exam-card-set-by-admin/download-history.png")
admin_exam_card_section_details_add_btn = Button(admin_exam_card_section_details_container_frame,
                                                 image=admin_exam_card_section_add_img, bg="#ffffff",
                                                 activebackground="#ffffff", bd=0, relief='flat')
admin_exam_card_section_details_add_btn.place(x=829, y=39)

# -----------------------------------

progress_report_section_frame = Frame(examination_frame)
progress_report_section_frame.place(x=714, y=25)

progress_report_selected_img = PhotoImage(file="images/examination/progress-report/progress-report-selected.png")
progress_report_selected_lbl = Label(progress_report_section_frame, image=progress_report_selected_img, bg="#ffffff",
                                     relief='flat', bd=0)
progress_report_selected_lbl.bind("<Button-1>", show_progress_report_section)

progress_report_img = PhotoImage(file="images/examination/progress-report/progress-report.png")
progress_report_lbl = Label(progress_report_section_frame, image=progress_report_img, bg="#ffffff",
                            relief='flat', bd=0)
progress_report_lbl.grid(row=0, column=0)
progress_report_lbl.bind("<Button-1>", show_progress_report_section)

progress_report_section_details_frame = Frame(exam_card_section_details_frame, bg="#ECF0F5")

progress_report_section_details_container_frame = Frame(progress_report_section_details_frame)
progress_report_section_details_container_frame.grid(row=0, column=0)

progress_report_section_details_container_img = PhotoImage(
    file="images/examination/progress-report/progress-report-container.png")
progress_report_section_details_container_lbl = Label(progress_report_section_details_container_frame,
                                                      image=progress_report_section_details_container_img, bg="#ECF0F5")
progress_report_section_details_container_lbl.grid(row=0, column=0)

progress_report_section_print_img = PhotoImage(file="images/examination/progress-report/print.png")
progress_report_section_details_print_btn = Button(progress_report_section_details_container_frame,
                                                   image=progress_report_section_print_img, bg="#ffffff",
                                                   activebackground="#ffffff", bd=0, relief='flat')
progress_report_section_details_print_btn.place(x=973, y=39)

progress_report_section_generate_img = PhotoImage(file="images/examination/progress-report/generate.png")
progress_report_section_details_generate_btn = Button(progress_report_section_details_container_frame,
                                                      image=progress_report_section_generate_img, bg="#ffffff",
                                                      activebackground="#ffffff", bd=0, relief='flat')
progress_report_section_details_generate_btn.place(x=973, y=128)

# -------------------------------------------

retake_section_frame = Frame(examination_frame)
retake_section_frame.place(x=946, y=25)

retake_selected_img = PhotoImage(file="images/examination/retake/retake-selected.png")
retake_selected_lbl = Label(retake_section_frame, image=retake_selected_img, bg="#ffffff",
                            relief='flat', bd=0)
retake_selected_lbl.bind("<Button-1>", show_retake_section)

retake_img = PhotoImage(file="images/examination/retake/retake.png")
retake_lbl = Label(retake_section_frame, image=retake_img, bg="#ffffff",
                   relief='flat', bd=0)
retake_lbl.grid(row=0, column=0)
retake_lbl.bind("<Button-1>", show_retake_section)

retake_section_details_frame = Frame(exam_card_section_details_frame, bg="#ECF0F5")

retake_section_details_container_frame = Frame(retake_section_details_frame)
retake_section_details_container_frame.grid(row=0, column=0)

# retake_section_details_container_img = PhotoImage(file="images/examination/progress-report/progress-report-container.png")
# retake_section_details_container_lbl = Label(retake_section_details_container_frame,
#                                               image=retake_section_details_container_img, bg="#ECF0F5")
# retake_section_details_container_lbl.grid(row=0, column=0)

# ------------------------------------------------------------------------------------------------------------

evaluation_frame = Frame(content_area, bg="#ECF0F5", width=width - left_side_bar.winfo_width(),
                         height=height - nav_bar.winfo_height())

evaluation_options_frame = Frame(evaluation_frame)
evaluation_options_frame.place(x=262 - side_bar_width - 10, y=19)

evaluation_options_img = PhotoImage(file="images/evaluation/current-evaluations/options-container.png")
evaluation_options_lbl = Label(evaluation_options_frame, image=evaluation_options_img, bg="#ECF0F5")
evaluation_options_lbl.grid(row=0, column=0)

current_evaluation_section_frame = Frame(evaluation_frame)
current_evaluation_section_frame.place(x=20, y=25)

current_evaluation_selected_img = PhotoImage(file="images/evaluation/current-evaluations/evaluations-selected.png")
current_evaluation_selected_lbl = Label(current_evaluation_section_frame, image=current_evaluation_selected_img,
                                        bg="#ffffff",
                                        relief='flat', bd=0)
current_evaluation_selected_lbl.grid(row=0, column=0)
current_evaluation_selected_lbl.bind("<Button-1>", show_current_evaluation_section)

current_evaluation_img = PhotoImage(file="images/evaluation/current-evaluations/evaluations.png")
current_evaluation_lbl = Label(current_evaluation_section_frame, image=current_evaluation_img, bg="#ffffff",
                               relief='flat', bd=0)
current_evaluation_lbl.bind("<Button-1>", show_current_evaluation_section)

current_evaluation_details_frame = Frame(evaluation_frame, bg="#ECF0F5")
current_evaluation_details_frame.place(x=262 - side_bar_width - 10, y=173 - nav_bar_height)

current_evaluation_section_details_frame = Frame(current_evaluation_details_frame, bg="#ECF0F5")
current_evaluation_section_details_frame.grid(row=0, column=0)

current_evaluation_section_details_container_frame = Frame(current_evaluation_section_details_frame)
current_evaluation_section_details_container_frame.grid(row=0, column=0)

current_evaluation_section_details_container_img = PhotoImage(
    file="images/evaluation/current-evaluations/evaluations-container.png")
current_evaluation_section_details_container_lbl = Label(current_evaluation_section_details_container_frame,
                                                         image=current_evaluation_section_details_container_img,
                                                         bg="#ECF0F5")
current_evaluation_section_details_container_lbl.grid(row=0, column=0)

# ----------------------------------------------------------------------------------------------------------
evaluation_history_section_frame = Frame(evaluation_frame)
evaluation_history_section_frame.place(x=599, y=25)

evaluation_history_selected_img = PhotoImage(
    file="images/evaluation/evaluations-history/evaluations-history-selected.png")
evaluation_history_selected_lbl = Label(evaluation_history_section_frame, image=evaluation_history_selected_img,
                                        bg="#ffffff",
                                        relief='flat', bd=0)
evaluation_history_selected_lbl.bind("<Button-1>", show_evaluation_history_section)

evaluation_history_img = PhotoImage(file="images/evaluation/evaluations-history/evaluations-history.png")
evaluation_history_lbl = Label(evaluation_history_section_frame, image=evaluation_history_img, bg="#ffffff",
                               relief='flat', bd=0)
evaluation_history_lbl.grid(row=0, column=0)
evaluation_history_lbl.bind("<Button-1>", show_evaluation_history_section)

# evaluation_history_details_frame = Frame(evaluation_frame, bg="#ECF0F5")
# evaluation_history_details_frame.place(x=262 - side_bar_width - 10, y=173 - nav_bar_height)
#
evaluation_history_section_details_frame = Frame(current_evaluation_section_details_frame, bg="#ECF0F5")
# evaluation_history_section_details_frame.grid(row=0, column=0)

evaluation_history_section_details_container_frame = Frame(evaluation_history_section_details_frame)
evaluation_history_section_details_container_frame.grid(row=0, column=0)

evaluation_history_section_details_container_img = PhotoImage(
    file="images/evaluation/evaluations-history/evaluations-history-container.png")
evaluation_history_section_details_container_lbl = Label(evaluation_history_section_details_container_frame,
                                                         image=evaluation_history_section_details_container_img,
                                                         bg="#ECF0F5")
evaluation_history_section_details_container_lbl.grid(row=0, column=0)

# --------------------------------------------------------------------------------------------------------

clearance_frame = Frame(content_area, bg="#ECF0F5", width=width - left_side_bar.winfo_width(),
                        height=height - nav_bar.winfo_height())

clearance_options_frame = Frame(clearance_frame)
clearance_options_frame.place(x=262 - side_bar_width - 10, y=19)

clearance_options_img = PhotoImage(file="images/clearance/apply-for-clearance/options-container.png")
clearance_options_lbl = Label(clearance_options_frame, image=clearance_options_img, bg="#ECF0F5")
clearance_options_lbl.grid(row=0, column=0)

apply_for_clearance_section_frame = Frame(clearance_frame)
apply_for_clearance_section_frame.place(x=20, y=25)

apply_for_clearance_selected_img = PhotoImage(
    file="images/clearance/apply-for-clearance/apply-for-clearance-selected.png")
apply_for_clearance_selected_lbl = Label(apply_for_clearance_section_frame, image=apply_for_clearance_selected_img,
                                         bg="#ffffff",
                                         relief='flat', bd=0)
apply_for_clearance_selected_lbl.grid(row=0, column=0)
apply_for_clearance_selected_lbl.bind("<Button-1>", show_apply_for_clearance_section)

apply_for_clearance_img = PhotoImage(file="images/clearance/apply-for-clearance/apply-for-clearance.png")
apply_for_clearance_lbl = Label(apply_for_clearance_section_frame, image=apply_for_clearance_img, bg="#ffffff",
                                relief='flat', bd=0)
apply_for_clearance_lbl.bind("<Button-1>", show_apply_for_clearance_section)

apply_for_clearance_details_frame = Frame(clearance_frame, bg="#ECF0F5")
apply_for_clearance_details_frame.place(x=262 - side_bar_width - 10, y=173 - nav_bar_height)

apply_for_clearance_section_details_frame = Frame(apply_for_clearance_details_frame, bg="#ECF0F5")
apply_for_clearance_section_details_frame.grid(row=0, column=0)

apply_for_clearance_section_details_container_frame = Frame(apply_for_clearance_section_details_frame)
apply_for_clearance_section_details_container_frame.grid(row=0, column=0)

apply_for_clearance_section_details_container_img = PhotoImage(
    file="images/clearance/apply-for-clearance/apply-for-clearance-container.png")
apply_for_clearance_section_details_container_lbl = Label(apply_for_clearance_section_details_container_frame,
                                                          image=apply_for_clearance_section_details_container_img,
                                                          bg="#ECF0F5")
apply_for_clearance_section_details_container_lbl.grid(row=0, column=0)

apply_for_clearance_section_add_img = PhotoImage(file="images/clearance/apply-for-clearance/submit.png")
apply_for_clearance_section_details_add_btn = Button(apply_for_clearance_section_details_container_frame,
                                                     image=apply_for_clearance_section_add_img, bg="#ffffff",
                                                     activebackground="#ffffff", bd=0, relief='flat')
apply_for_clearance_section_details_add_btn.place(x=1051, y=213)

# ----------------------------------------------------------------------------------------------------------
clearance_certificate_section_frame = Frame(clearance_frame)
clearance_certificate_section_frame.place(x=405, y=25)

clearance_certificate_selected_img = PhotoImage(
    file="images/clearance/clearance-certificate/clearance-certificate-selected.png")
clearance_certificate_selected_lbl = Label(clearance_certificate_section_frame,
                                           image=clearance_certificate_selected_img, bg="#ffffff",
                                           relief='flat', bd=0)
clearance_certificate_selected_lbl.bind("<Button-1>", show_clearance_certificate_section)

clearance_certificate_img = PhotoImage(file="images/clearance/clearance-certificate/clearance-certificate.png")
clearance_certificate_lbl = Label(clearance_certificate_section_frame, image=clearance_certificate_img, bg="#ffffff",
                                  relief='flat', bd=0)
clearance_certificate_lbl.grid(row=0, column=0)
clearance_certificate_lbl.bind("<Button-1>", show_clearance_certificate_section)

# clearance_certificate_details_frame = Frame(clearance_frame, bg="#ECF0F5")
# clearance_certificate_details_frame.place(x=262 - side_bar_width - 10, y=173 - nav_bar_height)
#
clearance_certificate_section_details_frame = Frame(apply_for_clearance_section_details_frame, bg="#ECF0F5")
# clearance_certificate_section_details_frame.grid(row=0, column=0)

clearance_certificate_section_details_container_frame = Frame(clearance_certificate_section_details_frame)
clearance_certificate_section_details_container_frame.grid(row=0, column=0)

clearance_certificate_section_details_container_img = PhotoImage(
    file="images/clearance/clearance-certificate/clearance-certificate-content.png")
clearance_certificate_section_details_container_lbl = Label(clearance_certificate_section_details_container_frame,
                                                            image=clearance_certificate_section_details_container_img,
                                                            bg="#ECF0F5")
clearance_certificate_section_details_container_lbl.grid(row=0, column=0)

# ---------------------------------------------------

clearance_history_section_frame = Frame(clearance_frame)
clearance_history_section_frame.place(x=791, y=25)

clearance_history_selected_img = PhotoImage(file="images/clearance/clearance-history/clearance-history-selected.png")
clearance_history_selected_lbl = Label(clearance_history_section_frame, image=clearance_history_selected_img,
                                       bg="#ffffff",
                                       relief='flat', bd=0)
clearance_history_selected_lbl.bind("<Button-1>", show_clearance_history_section)

clearance_history_img = PhotoImage(file="images/clearance/clearance-history/clearance-history.png")
clearance_history_lbl = Label(clearance_history_section_frame, image=clearance_history_img, bg="#ffffff",
                              relief='flat', bd=0)
clearance_history_lbl.grid(row=0, column=0)
clearance_history_lbl.bind("<Button-1>", show_clearance_history_section)

# clearance_history_details_frame = Frame(clearance_frame, bg="#ECF0F5")
# clearance_history_details_frame.place(x=262 - side_bar_width - 10, y=173 - nav_bar_height)
#
clearance_history_section_details_frame = Frame(apply_for_clearance_section_details_frame, bg="#ECF0F5")
# clearance_history_section_details_frame.grid(row=0, column=0)

clearance_history_section_details_container_frame = Frame(clearance_history_section_details_frame)
clearance_history_section_details_container_frame.grid(row=0, column=0)

clearance_history_section_details_container_img = PhotoImage(
    file="images/clearance/clearance-history/clearance-history-container.png")
clearance_history_section_details_container_lbl = Label(clearance_history_section_details_container_frame,
                                                        image=clearance_history_section_details_container_img,
                                                        bg="#ECF0F5")
clearance_history_section_details_container_lbl.grid(row=0, column=0)

clearance_history_section_add_img = PhotoImage(file="images/clearance/clearance-history/apply-clearance.png")
clearance_history_section_details_add_btn = Button(clearance_history_section_details_container_frame,
                                                   image=clearance_history_section_add_img, bg="#ffffff",
                                                   activebackground="#ffffff", bd=0, relief='flat')
clearance_history_section_details_add_btn.place(x=38, y=99)

# --------------------------------------------------------------------------------------------------------

account_canvas_container = Frame(root)
# account_canvas_container.place(x=1165, y=nav_bar_height)

account_info_img = PhotoImage(file="images/home/account-info.png")
account_info_canvas = Canvas(account_canvas_container, bg="#ECF0F5", width=account_info_img.width() - 14.6,
                             height=account_info_img.height() - 11.6)
account_info_canvas.grid(row=0, column=0)

account_canvas_container.bind("<Leave>", lambda e: hide_account_options())

account_info_background = account_info_canvas.create_image(
    account_info_img.width() / 2 - 10, account_info_img.height() / 2,
    image=account_info_img)

# , width=account_info_img.width() - 14.6, height=account_info_img.height() - 30
account_info_frame = Frame(account_info_canvas, bg="#ffffff")
account_info_frame.place(x=account_info_img.width() / 2 - 6, y=account_info_img.height() / 2 + 4, anchor=CENTER)
# ----------------------------------------------------------------------------------------------
my_messages_img = PhotoImage(file="images/home/my-messages.png")
my_messages_lbl = Label(account_info_frame, image=my_messages_img, bg="#ffffff", bd=0, relief='flat')
my_messages_lbl.grid(row=0, column=0)
my_messages_lbl.bind('<Enter>', my_messages_hovered)

profile_img = PhotoImage(file="images/home/profile.png")
profile_lbl = Label(account_info_frame, image=profile_img, bg="#ffffff", bd=0, relief='flat')
profile_lbl.grid(row=1, column=0)
profile_lbl.bind('<Enter>', profile_hovered)

change_password_img = PhotoImage(file="images/home/change-password.png")
change_password_lbl = Label(account_info_frame, image=change_password_img, bg="#ffffff", bd=0, relief='flat')
change_password_lbl.grid(row=2, column=0)
change_password_lbl.bind('<Enter>', change_password_hovered)

logout_img = PhotoImage(file="images/home/logout.png")
logout_lbl = Label(account_info_frame, image=logout_img, bg="#ffffff", bd=0, relief='flat')
logout_lbl.grid(row=3, column=0)
logout_lbl.bind('<Enter>', logout_hovered)
# --------------------------------------------------------------
my_messages_hovered_img = PhotoImage(file="images/home/my-messages-hovered.png")
my_messages_hovered_lbl = Label(account_info_frame, image=my_messages_hovered_img, bg="#ffffff", bd=0, relief='flat')
my_messages_hovered_lbl.bind('<Leave>', my_messages_normal)
my_messages_hovered_lbl.bind('<Button-1>', show_my_messages)

profile_hovered_img = PhotoImage(file="images/home/profile-hovered.png")
profile_hovered_lbl = Label(account_info_frame, image=profile_hovered_img, bg="#ffffff", bd=0, relief='flat')
profile_hovered_lbl.bind('<Leave>', profile_normal)
profile_hovered_lbl.bind('<Button-1>', show_profile)

change_password_hovered_img = PhotoImage(file="images/home/change-password-hovered.png")
change_password_hovered_lbl = Label(account_info_frame, image=change_password_hovered_img, bg="#ffffff", bd=0,
                                    relief='flat')
change_password_hovered_lbl.bind('<Leave>', change_password_normal)
change_password_hovered_lbl.bind('<Button-1>', show_change_password)

logout_hovered_img = PhotoImage(file="images/home/logout-hovered.png")
logout_hovered_lbl = Label(account_info_frame, image=logout_hovered_img, bg="#ffffff", bd=0, relief='flat')
logout_hovered_lbl.bind('<Leave>', logout_normal)
logout_hovered_lbl.bind('<Button-1>', show_logout)

# -----------------------------------------------------------------------------------------------------------

logo_img = PhotoImage(file="images/home/logo.png")
logo_lbl = Label(left_side_bar, image=logo_img, bg="#ffffff")
logo_lbl.place(x=34, y=63 - nav_bar_height)
logo_lbl.bind("<Button-1>", lambda e: hide_account_options())

# ----------------------------------------------------------------------------
side_options_frame = Frame(left_side_bar)
side_options_frame.place(x=8.78, y=285.05 - nav_bar_height)

home_bright_img = PhotoImage(file="images/home/home.png")
home_bright_lbl = Label(side_options_frame, image=home_bright_img, bg="#ffffff")
home_bright_lbl.grid(row=0, column=0)
home_bright_lbl.bind("<Enter>", home_hovered)

home_hovered_img = PhotoImage(file="images/home/home-hoved.png")
home_hovered_lbl = Label(side_options_frame, image=home_hovered_img, bg="#ffffff")
home_hovered_lbl.bind("<Leave>", home_normal)
home_hovered_lbl.bind("<Button-1>", show_home)
# ------------------------------------------------------------------------------------

news_bright_img = PhotoImage(file="images/home/news-button.png")
news_bright_lbl = Label(side_options_frame, image=news_bright_img, bg="#ffffff")
news_bright_lbl.grid(row=1, column=0)
news_bright_lbl.bind("<Enter>", news_hovered)

news_hovered_img = PhotoImage(file="images/home/news-hoved.png")
news_hovered_lbl = Label(side_options_frame, image=news_hovered_img, bg="#ffffff")
news_hovered_lbl.bind("<Leave>", news_normal)
news_hovered_lbl.bind("<Button-1>", show_news)
# ------------------------------------------------------------------------------------

reporting_bright_img = PhotoImage(file="images/home/reporting.png")
reporting_bright_lbl = Label(side_options_frame, image=reporting_bright_img, bg="#ffffff")
reporting_bright_lbl.grid(row=2, column=0)
reporting_bright_lbl.bind("<Enter>", reporting_hovered)

reporting_hovered_img = PhotoImage(file="images/home/reporting-hoved.png")
reporting_hovered_lbl = Label(side_options_frame, image=reporting_hovered_img, bg="#ffffff")
reporting_hovered_lbl.bind("<Leave>", reporting_normal)
reporting_hovered_lbl.bind("<Button-1>", show_reporting)
# ------------------------------------------------------------------------------------

deferment_bright_img = PhotoImage(file="images/home/deferment.png")
deferment_bright_lbl = Label(side_options_frame, image=deferment_bright_img, bg="#ffffff")
deferment_bright_lbl.grid(row=3, column=0)
deferment_bright_lbl.bind("<Enter>", deferment_hovered)

deferment_hovered_img = PhotoImage(file="images/home/deferment-hoved.png")
deferment_hovered_lbl = Label(side_options_frame, image=deferment_hovered_img, bg="#ffffff")
deferment_hovered_lbl.bind("<Leave>", deferment_normal)
deferment_hovered_lbl.bind("<Button-1>", show_deferment)
# ------------------------------------------------------------------------------------

fees_bright_img = PhotoImage(file="images/home/fees.png")
fees_bright_lbl = Label(side_options_frame, image=fees_bright_img, bg="#ffffff")
fees_bright_lbl.grid(row=4, column=0)
fees_bright_lbl.bind("<Enter>", fees_hovered)

fees_hovered_img = PhotoImage(file="images/home/fees-hoved.png")
fees_hovered_lbl = Label(side_options_frame, image=fees_hovered_img, bg="#ffffff")
fees_hovered_lbl.bind("<Leave>", fees_normal)
fees_hovered_lbl.bind("<Button-1>", show_fees)
# ------------------------------------------------------------------------------------

units_bright_img = PhotoImage(file="images/home/units-button.png")
units_bright_lbl = Label(side_options_frame, image=units_bright_img, bg="#ffffff")
units_bright_lbl.grid(row=5, column=0)
units_bright_lbl.bind("<Enter>", units_hovered)

units_hovered_img = PhotoImage(file="images/home/units-hoved.png")
units_hovered_lbl = Label(side_options_frame, image=units_hovered_img, bg="#ffffff")
units_hovered_lbl.bind("<Leave>", units_normal)
units_hovered_lbl.bind("<Button-1>", show_units)
# ------------------------------------------------------------------------------------

examination_bright_img = PhotoImage(file="images/home/examination.png")
examination_bright_lbl = Label(side_options_frame, image=examination_bright_img, bg="#ffffff")
examination_bright_lbl.grid(row=6, column=0)
examination_bright_lbl.bind("<Enter>", examination_hovered)

examination_hovered_img = PhotoImage(file="images/home/examination-hoved.png")
examination_hovered_lbl = Label(side_options_frame, image=examination_hovered_img, bg="#ffffff")
examination_hovered_lbl.bind("<Leave>", examination_normal)
examination_hovered_lbl.bind("<Button-1>", show_examination)
# ------------------------------------------------------------------------------------

evaluation_bright_img = PhotoImage(file="images/home/evaluation.png")
evaluation_bright_lbl = Label(side_options_frame, image=evaluation_bright_img, bg="#ffffff")
evaluation_bright_lbl.grid(row=7, column=0)
evaluation_bright_lbl.bind("<Enter>", evaluation_hovered)

evaluation_hovered_img = PhotoImage(file="images/home/Evaluation-hoved.png")
evaluation_hovered_lbl = Label(side_options_frame, image=evaluation_hovered_img, bg="#ffffff")
evaluation_hovered_lbl.bind("<Leave>", evaluation_normal)
evaluation_hovered_lbl.bind("<Button-1>", show_evaluation)
# ------------------------------------------------------------------------------------

clearance_bright_img = PhotoImage(file="images/home/clearance.png")
clearance_bright_lbl = Label(side_options_frame, image=clearance_bright_img, bg="#ffffff")
clearance_bright_lbl.grid(row=8, column=0)
clearance_bright_lbl.bind("<Enter>", clearance_hovered)

clearance_hovered_img = PhotoImage(file="images/home/clearance-hoved.png")
clearance_hovered_lbl = Label(side_options_frame, image=clearance_hovered_img, bg="#ffffff")
clearance_hovered_lbl.bind("<Leave>", clearance_normal)
clearance_hovered_lbl.bind("<Button-1>", show_clearance)
# ------------------------------------------------------------------------------------

my_message_frame = Frame(content_area, bg="#ECF0F5", width=width - left_side_bar.winfo_width(),
                         height=height - nav_bar.winfo_height())

my_message_options_frame = Frame(my_message_frame)
my_message_options_frame.place(x=262 - side_bar_width - 10, y=88 - nav_bar_height)

my_message_options_img = PhotoImage(file="images/my_messages/inbox/options-container.png")
my_message_options_lbl = Label(my_message_options_frame, image=my_message_options_img, bg="#ECF0F5")
my_message_options_lbl.grid(row=0, column=0)

inbox_frame = Frame(my_message_frame)
inbox_frame.place(x=262 - side_bar_width, y=94 - nav_bar_height)

inbox_selected_img = PhotoImage(file="images/my_messages/inbox/inbox-selected.png")
inbox_selected_lbl = Label(inbox_frame, image=inbox_selected_img, bg="#ffffff", relief='flat', bd=0)
inbox_selected_lbl.grid(row=0, column=0)
inbox_selected_lbl.bind("<Button-1>", show_inbox)

inbox_img = PhotoImage(file="images/my_messages/inbox/inbox.png")
inbox_lbl = Label(inbox_frame, image=inbox_img, bg="#ffffff", relief='flat', bd=0)
inbox_lbl.bind("<Button-1>", show_inbox)

details_frame = Frame(my_message_frame, bg="#ECF0F5")
details_frame.place(x=262 - side_bar_width - 10, y=173 - nav_bar_height)

inbox_details_frame = Frame(details_frame, bg="#ECF0F5")
inbox_details_frame.grid(row=0, column=0)

inbox_details_container_frame = Frame(inbox_details_frame)
inbox_details_container_frame.grid(row=0, column=0)

inbox_details_container_img = PhotoImage(file="images/my_messages/inbox/inbox-message-container.png")
inbox_details_container_lbl = Label(inbox_details_container_frame, image=inbox_details_container_img, bg="#ECF0F5")
inbox_details_container_lbl.grid(row=0, column=0)

inbox_details_message_img = PhotoImage(file="images/my_messages/inbox/inbox-messages.png")
inbox_details_message_lbl = Label(inbox_details_container_frame, image=inbox_details_message_img, bg="#ffffff",
                                  relief='flat',
                                  bd=0)
inbox_details_message_lbl.place(x=33, y=79)
# ---------------------------------------------------------------------------------------------

compose_frame = Frame(my_message_frame)
compose_frame.place(x=552 - side_bar_width, y=94 - nav_bar_height)

compose_img = PhotoImage(file="images/my_messages/inbox/compose.png")
compose_lbl = Label(compose_frame, image=compose_img, bg="#ffffff", relief='flat', bd=0)
compose_lbl.grid(row=0, column=0)
compose_lbl.bind("<Button-1>", show_compose)

compose_selected_img = PhotoImage(file="images/my_messages/inbox/compose-selected.png")
compose_selected_lbl = Label(compose_frame, image=compose_selected_img, bg="#ffffff", relief='flat', bd=0)
compose_selected_lbl.bind("<Button-1>", show_compose)

compose_details_frame = Frame(details_frame, bg="#ECF0F5")

compose_details_container_frame = Frame(compose_details_frame)
compose_details_container_frame.grid(row=0, column=0)

compose_details_container_img = PhotoImage(file="images/my_messages/compose/container.png")
compose_details_container_lbl = Label(compose_details_container_frame, image=compose_details_container_img,
                                      bg="#ECF0F5")
compose_details_container_lbl.grid(row=0, column=0)

recipient_img = PhotoImage(file="images/my_messages/compose/recipient.png")
recipient_lbl = Label(compose_details_frame, image=recipient_img, bd=0, relief='flat', bg="#ffffff")
recipient_lbl.place(x=119, y=78)

recipient_entry = Entry(compose_details_frame, bd=0, relief='flat', bg="#ffffff")
recipient_entry.place(x=209 + 7, y=78 + 2, width=355 - 14, height=31 - 4)

subject_img = PhotoImage(file="images/my_messages/compose/subject.png")
subject_lbl = Label(compose_details_frame, image=subject_img, bd=0, relief='flat', bg="#ffffff")
subject_lbl.place(x=131, y=130)

subject_entry = Entry(compose_details_frame, bd=0, relief='flat', bg="#ffffff")
subject_entry.place(x=209 + 7, y=130 + 2, width=355 - 14, height=33 - 4)

editor_img = PhotoImage(file="images/my_messages/compose/message-editor.png")
editor_lbl = Label(compose_details_frame, image=editor_img, bd=0, relief='flat', bg="#ffffff")
editor_lbl.place(x=65, y=180)

editor_entry = Text(compose_details_frame, bd=0, relief='flat', bg="#ffffff")
editor_entry.place(x=211 + 7, y=258 + 2, width=737 - 14, height=188 - 7)

send_message_img = PhotoImage(file="images/my_messages/compose/send.png")
send_message_btn = Button(compose_details_frame, image=send_message_img, bd=0, relief='flat', bg="#ffffff",
                          activebackground="#ffffff", command=send_the_message)
send_message_btn.place(x=926, y=475)

back_to_inbox_img = PhotoImage(file="images/my_messages/compose/back-to-inbox.png")
back_to_inbox_btn = Button(compose_details_frame, image=back_to_inbox_img, bd=0, relief='flat', bg="#ffffff",
                           activebackground="#ffffff", command=go_back_to_inbox)
back_to_inbox_btn.place(x=1007, y=476)
# ---------------------------------------------------------------------------------------------

sent_frame = Frame(my_message_frame)
sent_frame.place(x=842 - side_bar_width, y=94 - nav_bar_height)

sent_img = PhotoImage(file="images/my_messages/inbox/sent.png")
sent_lbl = Label(sent_frame, image=sent_img, bg="#ffffff", relief='flat', bd=0)
sent_lbl.grid(row=0, column=0)
sent_lbl.bind("<Button-1>", show_sent)

sent_selected_img = PhotoImage(file="images/my_messages/inbox/sent-selected.png")
sent_selected_lbl = Label(sent_frame, image=sent_selected_img, bg="#ffffff", relief='flat', bd=0)
sent_selected_lbl.bind("<Button-1>", show_sent)

sent_details_frame = Frame(details_frame, bg="#ECF0F5")

sent_details_container_frame = Frame(sent_details_frame)
sent_details_container_frame.grid(row=0, column=0)

sent_container_img = PhotoImage(file="images/my_messages/sent/container.png")
sent_container_lbl = Label(sent_details_container_frame, image=sent_container_img, bg="#ECF0F5")
sent_container_lbl.grid(row=0, column=0)

sent_details_message_img = PhotoImage(file="images/my_messages/sent/the-message.png")
sent_details_message_lbl = Label(sent_details_container_frame, image=sent_details_message_img, bg="#ffffff",
                                 relief='flat',
                                 bd=0)
sent_details_message_lbl.place(x=33, y=79)

# -----------------------------------------------------------------------------------

trash_frame = Frame(my_message_frame)
trash_frame.place(x=1132 - side_bar_width, y=94 - nav_bar_height)

trash_img = PhotoImage(file="images/my_messages/inbox/trash.png")
trash_lbl = Label(trash_frame, image=trash_img, bg="#ffffff", relief='flat', bd=0)
trash_lbl.grid(row=0, column=0)
trash_lbl.bind("<Button-1>", show_trash)

trash_selected_img = PhotoImage(file="images/my_messages/inbox/trash-selected.png")
trash_selected_lbl = Label(trash_frame, image=trash_selected_img, bg="#ffffff", relief='flat', bd=0)
trash_selected_lbl.bind("<Button-1>", show_trash)

trash_details_frame = Frame(details_frame, bg="#ECF0F5")

trash_details_container_frame = Frame(trash_details_frame)
trash_details_container_frame.grid(row=0, column=0)

trash_container_img = PhotoImage(file="images/my_messages/trash/container.png")
trash_container_lbl = Label(trash_details_container_frame, image=trash_container_img, bg="#ECF0F5")
trash_container_lbl.grid(row=0, column=0)

trash_details_message_img = PhotoImage(file="images/my_messages/trash/message.png")
trash_details_message_lbl = Label(trash_details_container_frame, image=trash_details_message_img, bg="#ffffff",
                                  relief='flat',
                                  bd=0)
trash_details_message_lbl.place(x=33, y=79)
# ---------------------------------------------------------------------------------------------
profile_canvas = Canvas(content_area, bg="#ECF0F5", width=width - left_side_bar.winfo_width(),
                        height=height - nav_bar.winfo_height(), bd=0, relief='flat', highlightthickness=0)
profile_canvas.bind('<Configure>', lambda e: profile_canvas.configure(scrollregion=profile_canvas.bbox("all")))
profile_canvas.bind_all("<MouseWheel>", on_mousewheel)
profile_canvas.bind("<Enter>", lambda e: enable_scroll())
profile_canvas.bind("<Leave>", lambda e: disable_scroll())

profile_frame_container = Frame(profile_canvas, bg="#ECF0F5", width=width - left_side_bar.winfo_width(),
                                height=1258 + 28, bd=0, relief='flat')

profile_frame = Frame(profile_frame_container, bg="#ECF0F5", width=width - left_side_bar.winfo_width(),
                      height=1258 + 28)
# height - nav_bar.winfo_height()
profile_frame.grid(row=0, column=0)

profile_canvas.create_window((0, 0), window=profile_frame_container, anchor='nw')

profile_options_frame = Frame(profile_frame)
profile_options_frame.place(x=262 - side_bar_width - 10, y=66 - nav_bar_height)

profile_options_img = PhotoImage(file="images/profile/personal-data/options-container.png")
profile_options_lbl = Label(profile_options_frame, image=profile_options_img, bg="#ECF0F5")
profile_options_lbl.grid(row=0, column=0)

personal_information_frame = Frame(profile_frame)
personal_information_frame.place(x=263 - side_bar_width, y=66 - nav_bar_height + 6)

personal_data_selected_img = PhotoImage(file="images/profile/personal-data/personal-data-selected.png")
personal_data_selected_lbl = Label(personal_information_frame, image=personal_data_selected_img, bg="#ffffff",
                                   relief='flat', bd=0)
personal_data_selected_lbl.grid(row=0, column=0)
personal_data_selected_lbl.bind("<Button-1>", show_personal_data)

personal_data_img = PhotoImage(file="images/profile/personal-data/personal-data.png")
personal_data_lbl = Label(personal_information_frame, image=personal_data_img, bg="#ffffff", relief='flat', bd=0)
personal_data_lbl.bind("<Button-1>", show_personal_data)
# -------------------------------------------------------------------

personal_information_details_frame = Frame(profile_frame, bg="#ECF0F5")
personal_information_details_frame.place(x=262 - side_bar_width - 10, y=104)

personal_information_details_container_frame = Frame(personal_information_details_frame, bg="#ECF0F5")
personal_information_details_container_frame.grid(row=0, column=0)

personal_information_container_frame = Frame(personal_information_details_container_frame)
personal_information_container_frame.grid(row=0, column=0)

personal_information_container_img = PhotoImage(file="images/profile/personal-data/personal-information-display.png")
personal_information_container_lbl = Label(personal_information_container_frame,
                                           image=personal_information_container_img, bg="#ECF0F5")
personal_information_container_lbl.grid(row=0, column=0)

personal_information_registration_number_lbl = Label(personal_information_container_frame, bg="#ffffff", font=font3)
personal_information_registration_number_lbl.place(x=330, y=73)

personal_information_name_lbl = Label(personal_information_container_frame, bg="#ffffff", font=font3)
personal_information_name_lbl.place(x=330, y=96)

personal_programme_lbl = Label(personal_information_container_frame, bg="#ffffff", font=font3)
personal_programme_lbl.place(x=330, y=119)

personal_national_id_lbl = Label(personal_information_container_frame, bg="#ffffff", font=font3)
personal_national_id_lbl.place(x=330, y=142)

personal_date_of_birth_lbl = Label(personal_information_container_frame, bg="#ffffff", font=font3)
personal_date_of_birth_lbl.place(x=330, y=165)

personal_gender_lbl = Label(personal_information_container_frame, bg="#ffffff", font=font3)
personal_gender_lbl.place(x=330, y=188)

personal_marital_status_lbl = Label(personal_information_container_frame, bg="#ffffff", font=font3)
personal_marital_status_lbl.place(x=330, y=211)

personal_nationality_lbl = Label(personal_information_container_frame, bg="#ffffff", font=font3)
personal_nationality_lbl.place(x=330, y=234)

personal_religion_lbl = Label(personal_information_container_frame, bg="#ffffff", font=font3)
personal_religion_lbl.place(x=330, y=257)

personal_source_lbl = Label(personal_information_container_frame, bg="#ffffff", font=font3)
personal_source_lbl.place(x=330, y=280)

personal_disability_lbl = Label(personal_information_container_frame, bg="#ffffff", font=font3)
personal_disability_lbl.place(x=330, y=303)

# --------------------------------------------------------

personal_contact_details_frame = Frame(profile_frame, bg="#ECF0F5")
personal_contact_details_frame.place(x=262 - side_bar_width - 10, y=463)

personal_contact_details_container_frame = Frame(personal_contact_details_frame, bg="#ECF0F5")
personal_contact_details_container_frame.grid(row=0, column=0)

personal_contact_frame = Frame(personal_contact_details_container_frame, bg="#ECF0F5")
personal_contact_frame.grid(row=0, column=0)

personal_contact_container_img = PhotoImage(file="images/profile/personal-data/personal-contact-display.png")
personal_contact_container_lbl = Label(personal_contact_frame,
                                       image=personal_contact_container_img, bg="#ECF0F5")
personal_contact_container_lbl.grid(row=0, column=0)

personal_contact_telephone_number_lbl = Label(personal_contact_frame, bg="#ffffff", font=font3)
personal_contact_telephone_number_lbl.place(x=330, y=98)

personal_contact_email_lbl = Label(personal_contact_frame, bg="#ffffff", font=font3)
personal_contact_email_lbl.place(x=330, y=121)

personal_contact_address_lbl = Label(personal_contact_frame, bg="#ffffff", font=font3)
personal_contact_address_lbl.place(x=330, y=144)

personal_contact_county_lbl = Label(personal_contact_frame, bg="#ffffff", font=font3)
personal_contact_county_lbl.place(x=330, y=167)

personal_contact_domicile_lbl = Label(personal_contact_frame, bg="#ffffff", font=font3)
personal_contact_domicile_lbl.place(x=330, y=190)

personal_contact_subcounty_lbl = Label(personal_contact_frame, bg="#ffffff", font=font3)
personal_contact_subcounty_lbl.place(x=330, y=213)

personal_contact_constituency_lbl = Label(personal_contact_frame, bg="#ffffff", font=font3)
personal_contact_constituency_lbl.place(x=330, y=236)

edit_img = PhotoImage(file="images/profile/personal-data/edit.png")
edit_contacts_btn = Button(personal_contact_details_container_frame, image=edit_img, relief='flat', bd=0, bg="#ffffff",
                           activebackground="#ffffff", command=edit_personal_contact)
edit_contacts_btn.place(x=1004, y=31)
# ----------------------------------------------------------------
personal_contact_edit_frame = Frame(personal_contact_details_container_frame, bg="#ECF0F5")
# personal_contact_edit_frame.grid(row=0, column=0)

personal_contact_edit_container_img = PhotoImage(
    file="images/profile/personal-data/edit-contacts/contact-container.png")
personal_contact_edit_container_lbl = Label(personal_contact_edit_frame,
                                            image=personal_contact_edit_container_img, bg="#ECF0F5")
personal_contact_edit_container_lbl.grid(row=0, column=0)

personal_contact_telephone_number_entry = Entry(personal_contact_edit_frame, bg="#ffffff", font=font3, bd=0,
                                                relief='flat')
personal_contact_telephone_number_entry.place(x=46, y=135, width=327, height=32)
personal_contact_telephone_number_entry.bind("<Return>", lambda e: update_the_contacts())

personal_contact_email_entry = Entry(personal_contact_edit_frame, bg="#ffffff", font=font3, bd=0, relief='flat')
personal_contact_email_entry.place(x=426, y=135, width=327, height=32)
personal_contact_email_entry.bind("<Return>", lambda e: update_the_contacts())

personal_contact_address_entry = Entry(personal_contact_edit_frame, bg="#ffffff", font=font3, bd=0, relief='flat')
personal_contact_address_entry.place(x=806, y=135, width=327, height=32)
personal_contact_address_entry.bind("<Return>", lambda e: update_the_contacts())

update_img = PhotoImage(file="images/profile/personal-data/edit-contacts/update.png")
update_contacts_btn = Button(personal_contact_edit_frame, image=update_img, relief='flat', bd=0, bg="#ffffff",
                             activebackground="#ffffff",
                             command=update_the_contacts)
update_contacts_btn.place(x=938, y=194)

cancel_img = PhotoImage(file="images/profile/personal-data/edit-contacts/cancel.png")
cancel_contacts_btn = Button(personal_contact_edit_frame, image=cancel_img, relief='flat', bd=0, bg="#ffffff",
                             activebackground="#ffffff", command=cancel_personal_contact)
cancel_contacts_btn.place(x=1036, y=194)

# -------------------------------------------------------------------------------------------------------------

personal_emergency_contact_details_frame = Frame(profile_frame, bg="#ECF0F5")
personal_emergency_contact_details_frame.place(x=262 - side_bar_width - 10, y=755)

personal_emergency_contact_details_container_frame = Frame(personal_emergency_contact_details_frame, bg="#ECF0F5")
personal_emergency_contact_details_container_frame.grid(row=0, column=0)

personal_emergency_contact_frame = Frame(personal_emergency_contact_details_container_frame, bg="#ECF0F5")
personal_emergency_contact_frame.grid(row=0, column=0)

personal_emergency_contact_container_img = PhotoImage(
    file="images/profile/personal-data/personal-emergency-contact-display.png")
personal_emergency_contact_container_lbl = Label(personal_emergency_contact_frame,
                                                 image=personal_emergency_contact_container_img, bg="#ECF0F5")
personal_emergency_contact_container_lbl.grid(row=0, column=0)

personal_emergency_name_lbl = Label(personal_emergency_contact_frame, bg="#ffffff", font=font3)
personal_emergency_name_lbl.place(x=330, y=96)

personal_emergency_relationship_lbl = Label(personal_emergency_contact_frame, bg="#ffffff", font=font3)
personal_emergency_relationship_lbl.place(x=330, y=119)

personal_emergency_telephone_lbl = Label(personal_emergency_contact_frame, bg="#ffffff", font=font3)
personal_emergency_telephone_lbl.place(x=330, y=142)

personal_emergency_email_lbl = Label(personal_emergency_contact_frame, bg="#ffffff", font=font3)
personal_emergency_email_lbl.place(x=330, y=165)

personal_emergency_address_lbl = Label(personal_emergency_contact_frame, bg="#ffffff", font=font3)
personal_emergency_address_lbl.place(x=330, y=188)

personal_emergency_remarks_lbl = Label(personal_emergency_contact_frame, bg="#ffffff", font=font3)
personal_emergency_remarks_lbl.place(x=330, y=211)

edit_emergency_contacts_btn = Button(personal_emergency_contact_details_container_frame, image=edit_img, relief='flat',
                                     bd=0,
                                     bg="#ffffff",
                                     activebackground="#ffffff",
                                     command=edit_personal_emergency_contact)
edit_emergency_contacts_btn.place(x=1004, y=32)

# ----------------------------------
personal_emergency_contact_edit_frame = Frame(personal_emergency_contact_details_container_frame, bg="#ECF0F5")
# personal_emergency_contact_edit_frame.grid(row=0, column=0)

personal_emergency_contact_edit_container_img = PhotoImage(
    file="images/profile/personal-data/edit-emergency-contacts/container.png")
personal_emergency_contact_edit_container_lbl = Label(personal_emergency_contact_edit_frame,
                                                      image=personal_emergency_contact_edit_container_img, bg="#ECF0F5")
personal_emergency_contact_edit_container_lbl.grid(row=0, column=0)

personal_emergency_contact_name_entry = Entry(personal_emergency_contact_edit_frame, bg="#ffffff", font=font3, bd=0,
                                              relief='flat')
personal_emergency_contact_name_entry.place(x=46, y=116, width=327, height=32)
personal_emergency_contact_name_entry.bind("<Return>", lambda e: update_the_emergency_contacts())

personal_emergency_contact_relationship_entry = Entry(personal_emergency_contact_edit_frame, bg="#ffffff", font=font3,
                                                      bd=0,
                                                      relief='flat')
personal_emergency_contact_relationship_entry.place(x=426, y=116, width=327, height=32)
personal_emergency_contact_relationship_entry.bind("<Return>", lambda e: update_the_emergency_contacts())

personal_emergency_contact_telephone_number_entry = Entry(personal_emergency_contact_edit_frame, bg="#ffffff",
                                                          font=font3, bd=0,
                                                          relief='flat')
personal_emergency_contact_telephone_number_entry.place(x=806, y=116, width=327, height=32)
personal_emergency_contact_telephone_number_entry.bind("<Return>", lambda e: update_the_emergency_contacts())

personal_emergency_contact_email_entry = Entry(personal_emergency_contact_edit_frame, bg="#ffffff", font=font3, bd=0,
                                               relief='flat')
personal_emergency_contact_email_entry.place(x=46, y=190, width=327, height=32)
personal_emergency_contact_email_entry.bind("<Return>", lambda e: update_the_emergency_contacts())

personal_emergency_contact_address_entry = Entry(personal_emergency_contact_edit_frame, bg="#ffffff", font=font3, bd=0,
                                                 relief='flat')
personal_emergency_contact_address_entry.place(x=426, y=190, width=327, height=32)
personal_emergency_contact_address_entry.bind("<Return>", lambda e: update_the_emergency_contacts())

personal_emergency_contact_remarks_entry = Entry(personal_emergency_contact_edit_frame, bg="#ffffff",
                                                 font=font3, bd=0,
                                                 relief='flat')
personal_emergency_contact_remarks_entry.place(x=806, y=190, width=327, height=32)
personal_emergency_contact_remarks_entry.bind("<Return>", lambda e: update_the_emergency_contacts())

# update_img = PhotoImage(file="images/profile/personal-data/edit-contacts/update.png")
update_emergency_contacts_btn = Button(personal_emergency_contact_edit_frame, image=update_img, relief='flat', bd=0,
                                       bg="#ffffff",
                                       activebackground="#ffffff",
                                       command=update_the_emergency_contacts)
update_emergency_contacts_btn.place(x=938, y=233)

# cancel_img = PhotoImage(file="images/profile/personal-data/edit-contacts/cancel.png")
cancel_emergency_contacts_btn = Button(personal_emergency_contact_edit_frame, image=cancel_img, relief='flat', bd=0,
                                       bg="#ffffff",
                                       activebackground="#ffffff", command=cancel_emergency_contact)
cancel_emergency_contacts_btn.place(x=1036, y=233)

# -----------------------------------------------------------

personal_other_details_details_frame = Frame(profile_frame, bg="#ECF0F5")
personal_other_details_details_frame.place(x=262 - side_bar_width - 10, y=1028)

personal_other_details_details_container_frame = Frame(personal_other_details_details_frame, bg="#ECF0F5")
personal_other_details_details_container_frame.grid(row=0, column=0)

personal_other_details_frame = Frame(personal_other_details_details_container_frame, bg="#ECF0F5")
personal_other_details_frame.grid(row=0, column=0)

personal_other_details_container_img = PhotoImage(
    file="images/profile/personal-data/personal-other-details-display.png")
personal_other_details_container_lbl = Label(personal_other_details_frame,
                                             image=personal_other_details_container_img, bg="#ECF0F5")
personal_other_details_container_lbl.grid(row=0, column=0)

personal_other_details_language_lbl = Label(personal_other_details_frame, bg="#ffffff", font=font3)
personal_other_details_language_lbl.place(x=330, y=96)

personal_other_details_medical_lbl = Label(personal_other_details_frame, bg="#ffffff", font=font3)
personal_other_details_medical_lbl.place(x=330, y=119)

personal_other_details_cirriculum_lbl = Label(personal_other_details_frame, bg="#ffffff", font=font3)
personal_other_details_cirriculum_lbl.place(x=330, y=142)

edit_other_details_btn = Button(personal_other_details_details_container_frame, image=edit_img, relief='flat', bd=0,
                                bg="#ffffff",
                                activebackground="#ffffff",
                                command=edit_personal_other_details)
edit_other_details_btn.place(x=1004, y=32)

# ----------------------------------------

personal_other_details_edit_frame = Frame(personal_other_details_details_container_frame, bg="#ECF0F5")
# personal_other_details_edit_frame.grid(row=0, column=0)

personal_other_details_edit_container_img = PhotoImage(
    file="images/profile/personal-data/edit-other-details/container.png")
personal_other_details_edit_container_lbl = Label(personal_other_details_edit_frame,
                                                  image=personal_other_details_edit_container_img, bg="#ECF0F5")
personal_other_details_edit_container_lbl.grid(row=0, column=0)

personal_other_details_language_entry = Entry(personal_other_details_edit_frame, bg="#ffffff", font=font3, bd=0,
                                              relief='flat')
personal_other_details_language_entry.place(x=46, y=135, width=327, height=32)
personal_other_details_language_entry.bind("<Return>", lambda e: update_the_other_details())

personal_other_details_medical_entry = Entry(personal_other_details_edit_frame, bg="#ffffff", font=font3, bd=0,
                                             relief='flat')
personal_other_details_medical_entry.place(x=426, y=135, width=327, height=32)
personal_other_details_medical_entry.bind("<Return>", lambda e: update_the_other_details())

personal_other_details_cirriculum_entry = Entry(personal_other_details_edit_frame, bg="#ffffff", font=font3, bd=0,
                                                relief='flat')
personal_other_details_cirriculum_entry.place(x=806, y=135, width=327, height=32)
personal_other_details_cirriculum_entry.bind("<Return>", lambda e: update_the_other_details())

update_other_details_btn = Button(personal_other_details_edit_frame, image=update_img, relief='flat', bd=0,
                                  bg="#ffffff",
                                  activebackground="#ffffff",
                                  command=update_the_other_details)
update_other_details_btn.place(x=938, y=194)

cancel_other_details_btn = Button(personal_other_details_edit_frame, image=cancel_img, relief='flat', bd=0,
                                  bg="#ffffff",
                                  activebackground="#ffffff", command=cancel_personal_other_details)
cancel_other_details_btn.place(x=1036, y=194)

# ---------------------------------------------------------
academics_frame = Frame(profile_frame)
academics_frame.place(x=842 - side_bar_width, y=66 - nav_bar_height + 6)

academics_selected_img = PhotoImage(file="images/profile/academics/academics-selected.png")
academics_selected_lbl = Label(academics_frame, image=academics_selected_img, bg="#ffffff", relief='flat', bd=0)
academics_selected_lbl.bind("<Button-1>", show_academics)

academics_img = PhotoImage(file="images/profile/academics/academics.png")
academics_lbl = Label(academics_frame, image=academics_img, bg="#ffffff", relief='flat', bd=0)
academics_lbl.grid(row=0, column=0)
academics_lbl.bind("<Button-1>", show_academics)

# ---------------------------------------------------------------------------------------------
change_password_frame = Frame(content_area, bg="#ECF0F5", width=width - left_side_bar.winfo_width(),
                              height=height - nav_bar.winfo_height())

change_password_options_frame = Frame(change_password_frame)
change_password_options_frame.place(x=356 + 30, y=146 - nav_bar_height)

change_password_options_container_frame = Frame(change_password_options_frame)
change_password_options_container_frame.grid(row=0, column=0)

my_message_options_img = PhotoImage(file="images/password-change/password-container.png")
my_message_options_lbl = Label(change_password_options_container_frame, image=my_message_options_img, bg="#ECF0F5")
my_message_options_lbl.grid(row=0, column=0)

old_password_entry = Entry(change_password_options_container_frame, bd=0, relief='flat', bg="#ffffff", font=font2,
                           foreground="#A8A8A9")
old_password_entry.place(x=28 + 7, y=80 + 8, width=371 - 14, height=33 - 4)
old_password_entry.insert(0, "Enter Old Password")
old_password_entry.bind("<FocusIn>", hide_old_password_placeholder)
old_password_entry.bind("<FocusOut>", show_old_password_placeholder)

new_password_entry = Entry(change_password_options_container_frame, bd=0, relief='flat', bg="#ffffff", font=font2,
                           foreground="#A8A8A9")
new_password_entry.place(x=28 + 7, y=134 + 8, width=371 - 14, height=33 - 4)
new_password_entry.insert(0, "Enter new password")
new_password_entry.bind("<FocusIn>", hide_new_password_placeholder)
new_password_entry.bind("<FocusOut>", show_new_password_placeholder)

new_confirm_password_entry = Entry(change_password_options_container_frame, bd=0, relief='flat', bg="#ffffff",
                                   font=font2, foreground="#A8A8A9")
new_confirm_password_entry.place(x=28 + 7, y=188 + 8, width=371 - 14, height=33 - 4)
new_confirm_password_entry.insert(0, "Confirm new password")
new_confirm_password_entry.bind("<FocusIn>", hide_new_confirm_password_placeholder)
new_confirm_password_entry.bind("<FocusOut>", show_new_confirm_password_placeholder)
new_confirm_password_entry.bind("<Return>", lambda e: actually_change_password())

change_password_submit_img = PhotoImage(file="images/password-change/change-pass.png")
change_password_submit_btn = Button(change_password_options_container_frame, image=change_password_submit_img, bd=0,
                                    relief='flat',
                                    bg="#ffffff", activebackground="#ffffff", command=actually_change_password)
change_password_submit_btn.place(x=130, y=241)

update_the_username(root, user_name_lbl, fee_balance_data_lbl)

root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", kill_threads)
root.mainloop()