#PASTE DUMP
# print("Checking License...")
# simple.set_window_pos("License and About", 0, 0)
# core.add_text("Anti AFK Program developed by Piffle",color=[158, 238, 247])
# core.add_separator()
# core.add_text("This program is meant to help people render out long\nsequences in 3D software, but it can be used for many\nmore uses than just that.")
# core.add_separator()
# core.add_text("This work is licensed under a Creative Commons\nAttribution 4.0 International License.\nhttps://creativecommons.org/licenses/by/4.0/")
# print("License... OK")













#Imports
from dearpygui.core import *
from dearpygui.simple import *
import pyautogui
#Appearence
set_main_window_size(420,230)
set_global_font_scale(1)
set_theme("Dark")

#Values, Variables, and Lists
movement_types = ["Local","Global"]
speed_sets = ["Slow","Medium","Fast"]



#Define functions
def Start(sender,data):
    mt = get_value("Movement Mode")
    speed_radio = get_value("Speed Mode")
    speed = 0.75
    if speed_radio == 0:
        speed = 0.75
    elif speed_radio == 1:
        speed = 0.45
    elif speed_radio == 2:
        speed = 0.25

    screen_size = pyautogui.size()
    size = 50
    if mt == 1:
        while True:
            pyautogui.moveTo(screen_size.width/2 - size,screen_size.height/2 + size,duration=speed)
            pyautogui.moveTo(screen_size.width/2 + size,screen_size.height/2 + size,duration=speed)
            pyautogui.moveTo(screen_size.width/2 + size,screen_size.height/2 - size,duration=speed)
            pyautogui.moveTo(screen_size.width/2 - size,screen_size.height/2 - size,duration=speed)
    else:
        while True:
            pyautogui.moveRel(-size,size,duration=speed)
            pyautogui.moveRel(+size,+size,duration=speed)
            pyautogui.moveRel(+size,-size,duration=speed)
            pyautogui.moveRel(-size,-size,duration=speed)







#License and About
with window("Anti AFK", width=400, height=150, no_close=True):
    with tab_bar("tb1"):
        with tab("License and About"):
            print("Checking License...")
            add_text("Anti AFK Program developed by Piffle",color=[158, 238, 247])
            add_separator()
            add_text("This program is meant to help people render out long\nsequences in 3D software, but it can be used for many\nmore uses than just that.")
            add_separator()
            add_text("This work is licensed under a Creative Commons\nAttribution 4.0 International License.\nhttps://creativecommons.org/licenses/by/4.0/")
            add_separator()
            add_text("To stop the program at any time drag the cursor\nto any corner of the screen in a quick motion",color=[158, 238, 247])
            add_separator()
            add_text("V1.6",color=[104,31,109])

            print("License... OK")

        with tab("Control Panel"):
            print("Control Panel Starting...")

            #Movement Type
            add_text("Movement mode",color=[158, 238, 247])
            add_radio_button(name="Movement Mode", items=movement_types)
            add_separator()

            #Movement Type
            add_text("Speed",color=[158, 238, 247])
            add_radio_button(name="Speed Mode", items=speed_sets)
            add_separator()


            add_button("Start", callback=Start)





print("Starting Window...")
start_dearpygui(primary_window="Anti AFK")
print("Window Closed. Goodbye!")
