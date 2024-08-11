import PySimpleGUI as sg  # import PySimpleGUI

if __name__ == "__main__":
    boardType = sg.popup_get_text('Do you want to create a new menu or use the last one you created? Note a menu '
                                  'must already be created if you want to use the last one you created. Type NEW or '
                                  'OLD.')       # takes user inputs whether they want to create a new board or
    # use the last one they made

    if boardType == 'NEW':
        exec(open("create_new_menu.py").read())
    elif boardType == "OLD":
        exec(open("reopen_last_menu.py").read())
    else:
        sg.popup("Please rerun this file and make sure to type either NEW or OLD in the text box.")

