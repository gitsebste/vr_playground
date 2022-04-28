import pyautogui
import pydirectinput
import time
from pynput.mouse import Button, Controller
mouse = Controller()

screen_w, screen_h = (tuple(pydirectinput.size()))

def move_mouse_to_point(p_x, p_h):
    pydirectinput.moveTo(p_x, p_h)

# move_mouse_to_point(point_w=1900, point_h=1000)

def move_mouse_by(x_diff, y_diff):
    pydirectinput.moveRel(x_diff, y_diff)

# move_mouse_by(x_diff=1000, y_diff=1000)

def get_mouse_position():
    return pydirectinput.position()

# print(get_mouse_position())

def mouse_click_left_at(p_x, p_y):
    pydirectinput.click(p_x, p_y)

# mouse_click_left_at(200,400)

def button_name_abbreviation_to_button_name(abbr):
    first_letter_lowered = abbr.lower()[0]
    button_names = ['right', 'left', 'middle']
    for button_name in button_names:
        if button_name.startswith(first_letter_lowered):
            return button_name
    raise ValueError(f'Abbr {abbr} cannot be matched to a button!')

def mouse_button_down(button_name_abbreviation):
    x, y = tuple(get_mouse_position())
    button_name = button_name_abbreviation_to_button_name(button_name_abbreviation)
    pydirectinput.mouseDown(x=x, y=y, button=button_name)

def mouse_button_up(button_name_abbreviation):
    x, y = tuple(get_mouse_position())
    button_name = button_name_abbreviation_to_button_name(button_name_abbreviation)
    pydirectinput.mouseUp(x=x, y=y, button=button_name)
    
pyautogui.hotkey('alt', 'tab')
time.sleep(1)

def translate_head_by(x_diff=0, y_diff=0):
    x, y = tuple(get_mouse_position())
    mouse_button_down('r')
    move_mouse_by(x_diff=x_diff,y_diff=y_diff)
    mouse_button_up('r')
    move_mouse_to_point(x, y)

translate_head_by(y_diff=200)

def rotate_head_by(x_diff=0, y_diff=0):
    x, y = tuple(get_mouse_position())
    mouse_button_down('r')
    mouse_button_down('m')
    move_mouse_by(x_diff=x_diff,y_diff=-y_diff)
    mouse_button_up('m')
    mouse_button_up('r')
    move_mouse_to_point(x, y)

rotate_head_by(200, 200)
rotate_head_by(-200, -200)

def key_down(key_name):
    pydirectinput.keyDown(key_name)

def key_up(key_name):
    pydirectinput.keyUp(key_name)

def translate_left_controller(x_diff=0, y_diff=0):
    x, y = tuple(get_mouse_position())
    key_down('shiftleft')
    move_mouse_by(x_diff=x_diff,y_diff=-y_diff)
    mouse.scroll(0, 200)
    key_up('shiftleft')
    move_mouse_to_point(x, y)

translate_left_controller(x_diff=200, y_diff=200)

def rotate_left_controller(x_diff=0, y_diff=0):
    x, y = tuple(get_mouse_position())
    key_down('shiftleft')
    mouse_button_down('m')
    move_mouse_by(x_diff=x_diff,y_diff=-y_diff)
    mouse.scroll(0, 200)
    mouse_button_up('m')
    key_up('shiftleft')
    move_mouse_to_point(x, y)

rotate_left_controller(x_diff=200, y_diff=200)

def translate_right_controller(x_diff=0, y_diff=0):
    x, y = tuple(get_mouse_position())
    key_down('space')
    move_mouse_by(x_diff=x_diff,y_diff=-y_diff)
    key_up('space')
    move_mouse_to_point(x, y)

translate_right_controller(x_diff=-200, y_diff=200)

def rotate_right_controller(x_diff=0, y_diff=0):
    x, y = tuple(get_mouse_position())
    key_down('space')
    mouse_button_down('m')
    move_mouse_by(x_diff=x_diff,y_diff=-y_diff)
    mouse_button_up('m')
    key_up('space')
    move_mouse_to_point(x, y)

rotate_right_controller(x_diff=200, y_diff=200)