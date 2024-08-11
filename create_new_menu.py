import PySimpleGUI as sg  # import PySimpleGUI
import base64  # import base64 to convert the images to strings for the buttons
from playsound import playsound  # import playsound to play audio recorded files
import PyObjCTools  # I think this is needed to make playsound method more effective but I'm not sure
import json  # used for saving files


def convert_file_to_base64(filename):  # this method converts a .png image to a base64byte string
    try:
        contents = open(filename, 'rb').read()
        encoded = base64.b64encode(contents)
    except Exception as error:
        sg.popup_error('Cancelled - An error occurred', error)
    return encoded


if __name__ == '__main__':  # if run button is clicked,

    # ask the user how many image buttons they want to create in the first menu
    numButtons = int(sg.popup_get_text('Enter how many buttons (of images) that you want to create (up to 12): '))

    # allow the user to input as many buttons as they input in the previous popup window
    imageFiles = []  # initializes a list to store the image files
    audioNames = []  # initializes a list to store the name of the audio files
    for i in range(numButtons):
        imageFiles.append(sg.popup_get_file('choose an image to insert for this menu:'))  # creates popup that lets you
        # browse for a .png image file and stores it in the list images
        audioName = sg.popup_get_text('enter the name of this audio file (with extension .mp3)')  # creates
        # popup that lets you input the name of the audio file that is in the current folder
        audioName = './' + str(audioName)
        audioNames.append(audioName)

    layout = []  # initializes the layout of the window
    key = []  # initializes a list that will store the button names
    buttons = []  # initializes a list that will store the buttons
    imageBytes = []
    for i in range(numButtons):
        if imageFiles[i]:
            imageBytes.append(convert_file_to_base64(imageFiles[i]))  # updates images to have base64 byte strings instead of
            # files
            key.append(i)  # adds the name of the button to the list key
            buttons.append([sg.Button('', image_data=imageBytes[i],
                                      button_color=(sg.theme_background_color(), sg.theme_background_color()),
                                      border_width=0, key=str(key[i]), )])
        else:
            sg.popup_cancel('Cancelled - No valid file entered')  # cancels the window if no picture is entered

    # creates columns of buttons (3 columns per button)
    counter = 0
    column1 = []
    column2 = []
    column3 = []
    column4 = []
    for i in range(len(buttons)):
        if counter < 3:
            column1.append(buttons[i])
            counter += 1
        elif 3 <= counter < 6:
            column2.append(buttons[i])
            counter += 1
        elif 6 <= counter < 9:
            column3.append(buttons[i])
            counter += 1
        elif 9 <= counter < 12:
            column4.append(buttons[i])
            counter += 1

    # creates the layout based on how many buttons you put in
    if 1 <= len(buttons) <= 3:
        layout = [
            [sg.Column(column1), ]
        ]
    elif 4 <= len(buttons) <= 6:
        layout = [
            [sg.Column(column1),
             sg.VSeperator(),
             sg.Column(column2), ]
        ]
    elif 7 <= len(buttons) <= 9:
        layout = [
            [sg.Column(column1),
             sg.VSeperator(),
             sg.Column(column2),
             sg.VSeperator(),
             sg.Column(column3), ]
        ]
    elif 10 <= len(buttons) <= 12:
        layout = [
            [sg.Column(column1),
             sg.VSeperator(),
             sg.Column(column2),
             sg.VSeperator(),
             sg.Column(column3),
             sg.VSeperator(),
             sg.Column(column4), ]
        ]

    window = sg.Window("Talk to the Hand", layout)  # opens window with set layout

    # executes certain code if specific buttons are pressed
    while True:
        event, values = window.read()  # reads in and stores user interaction with the window
        if event == sg.WINDOW_CLOSED:  # if the window close button is pressed, closes the window
            break
        else:
            for i in range(len(buttons)):  # runs the selected audio for the specific button (audio must be in
                # working folder
                if event == str(key[i]):
                    sound = str(audioNames[i])
                    playsound(sound)

    # saving user inputs
    data = [imageFiles, audioNames]
    with open('./menu.json', 'w') as file:
        json.dump(data, file)
