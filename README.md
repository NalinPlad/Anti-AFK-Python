# Anti-AFK-Python
A gui based app that has a few settings that can help stop your computer from going to sleep. Very useful for rendering long sequences or animations in 3d software, when you want your computer to stay awake. If you find any bugs or issues, feel free to work on the code. If you need help getting it up and running, you can reach me at piffle#8822 on discord. Keep in mind that ive only tested this software on MacOS machines, but it will hopefully run fine on other operating systems.

<img width="450" alt="License and About page" src="https://user-images.githubusercontent.com/43052612/119201709-4ac68a00-ba44-11eb-9882-2323af44672d.png">

### Dependancies
This program relies on DearPyGUI `pip install dearpygui` or `pip3 install dearpygui`
And PyAutoGUI `pip install pyautogui`

### Running
Once you have all of the dependancies set up, open a command line enter the directory where the file is stored, then run `python AntiAFKPython.py`. A window should pop up giving you access to the control panel where you can change settings and start the movement.

### Settings
<img width="449" alt="Control Panel" src="https://user-images.githubusercontent.com/43052612/119201714-4dc17a80-ba44-11eb-8380-33307ae3bfd5.png">
Once in the control panel, you will have access to Movement Modes [Local,Global] and Speed [Slow,Medium,Fast].
The Movement mode Local means the mouse will more relative to its current position. that means that instead of moving to (0,0) it will move to (MouseX + 10,MouseY + 10), meaning it is posibble to move the mouse(to some extent) and hase the movement continue wherever you go. Global coordinates simply go to a preditermined spot on the screen.

The speed setting just set the speed of the movement. Nothing special here.

