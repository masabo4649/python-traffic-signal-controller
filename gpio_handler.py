from gpiozero import LED, Button
import json

green = LED(17)
yellow = LED(18)
red = LED(27)

button_green = Button(6)
button_yellow = Button(12)
button_red = Button(13)

def getStatus():

    dict_data = {
        "green": green.value,
        "yellow": yellow.value,
        "red": red.value
    }
    return dict_data


def setStatus(dict_data):



    green_value = dict_data.get("green")
    yellow_value = dict_data.get("yellow")
    red_value = dict_data.get("red")

    if green_value is not None:
        green.value = green_value

    if yellow_value is not None:
        yellow.value = yellow_value

    if red_value is not None:
        red.value = red_value


def toggle_green():
    green.toggle()
button_green.when_pressed = toggle_green

def toggle_yellow():
    yellow.toggle()

button_yellow.when_pressed = toggle_yellow

def toggle_red():
    red.toggle()

button_red.when_pressed = toggle_red

if __name__ == '__main__':
    pass
