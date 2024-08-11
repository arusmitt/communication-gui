Arushi Mittal 
ENGR 1050
Final Project 


Talk to the Hand


Project Title: Talk to the Hand




Author: Arushi Mittal 




Instructions:
1. Open PyCharm and open the folder in PyCharm. 
2. Download all libraries necessary. They will be highlighted in red at the top if they are not installed properly. Some instructions for this are in the dependencies section of this readme. Make sure start.py, create new board, and reopen new board python files are open. 
3. Make sure you’re in the working folder, it contains the audio files and the path is set up in the code as such that it will only be able to access the audio files if they are in the same folder as the running .py file 
4. Run the start.py file 
5. type in NEW or OLD to the textbox depending on if you want to create a new menu or run the last one that was created (stored in the menu.json file). The menu.json file is overwritten every time a new board is created. Note that if entering OLD, you specifically on your computer must have already made a menu, because those are the paths stored in the json file. Paths stored on another computer will not match with a new computer. So, the first time you run this, you will need to create a new menu board.
6. If you type in OLD, the stored menu will launch. When the images are clicked, the corresponding sound will play.
7. If you type in NEW, a window will popup asking you how many image buttons you want to create. Based on this, the program will allow you to input images (already in the working folder, just pick one of the .png images) and audio files correlating with the images (the audio files are also already in the working folder, and they have the same names as the image files, just .mp3 instead of .png). The image files can be browsed for and you must simply enter the name of the audio files. 
8. Once you are done entering all of the images and audio files, the new menu you created will show up, and is usable!
9. If you hit the red button in the corner to close the window, the data will be saved to the menu.json file. Next time you run start.py, if you enter OLD, this is the menu that will be pulled up. 




Summary:
This project was created to serve as a communication device, specifically for people who cannot currently communicate via speaking, but are able to recognize images. The final goal of this project is to turn it into a wearable device that allows for portability of the user interface (current idea: using a Raspberry Pi). In this demonstration, a proof of concept is shown. 
Before this project, I had very little experience coding in Python, using libraries, and creating GUIs. For this reason, I started by learning about user interfaces and different libraries that can be used to create them in Python. My initial idea was to use the GTK library for Python, but I had a hard time figuring out how to download it. Once I downloaded it, it did not import properly, so I switched to the PySimpleGUI library instead. I learned how to use it with the example video referenced in the next section of this README, and from this began to create popup windows. I wanted to create buttons from images that could be inputted by the user, but PySimpleGUI requires these images to be converted to a base64 byte string, so I referenced some more code in order to do this. I had to combine methods and certain lines here and there to make this work for my project specifically, which was confusing at first but taught me a lot about how data is stored in Python. 
Once I could convert the images into buttons, I explored how I could get specific audio files to play when the buttons were clicked. I discovered the playsound library and used the playsound function specifically. However, I had a lot of trouble figuring out how to input the correct path for the audio files, and in this process learned how paths can be identified, either through right-clicking the file itself or through “./” if in the same working folder. In this process, I realized that I had to store the image files and audio files in lists in order to correlate which image went with which audio file. 
Once the sound was figured out, I worked on fixing the layout, because at a max of 12 buttons able to be created, the buttons were created in a vertical window that went off the screen. I learned about the column element in PySimpleGUI and was able to create a layout with 3 rows and 4 columns. 
Lastly, I worked with json to save user inputs so they did not have to re-inputted every time the same menu board was desired. At first, I could not save my lists as is, and learned more about the types that json took in. I realized that my image list was actually a list of type base64 byte, so I had to input my original image file list instead of this and then was able to use the json file. The json file only stores the bare minimum, and when the same menu board is requested by the user, it recreates it. This was not what I expected as I thought I could just save the entire window. I made it so that a user can run the start.py file and all other scripts also run from there. 
Looking forwards, I want to create a touch screen version of my program using raspberry pi, and later making it wearable, such as on an arm. 




Attributions/Citations:
* Used to learn the basics of PySimpleGUI library, especially how to make popup windows and input boxes using it 
   * https://www.youtube.com/watch?v=LzCfNanQ_9c 
* Reference code used to convert a .png image into a base64 byte string 
   * https://www.pysimplegui.org/en/latest/cookbook/#step-1-find-your-graphic
   * https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_Base64_Single_Image_Encoder.py 
* Used to learn how to use json
   * https://stackoverflow.com/questions/4450144/easy-save-load-of-data-in-python 




Dependencies:
* PySimpleGUI was imported and installed to create the GUI 
   * install PySimpleGUI by typing pip install PySimpleGUI in the terminal 
* base64 was imported to turn images into base64 byte strings
* the method playsound was imported from the library playsound to play the audio files (.mp3)
* PyObjCTools was imported to help playsound run
* json was imported to save user input