from time import sleep
import json
from threading import Thread, Timer
import configparser

# config.propertiesからMockを使うか設定を読み込む
config = configparser.ConfigParser()
config.read('config.properties')
mock = config.get("mode", "mock")

if mock == False:

    # initialize the circuit inside the GUI
    from tkgpio import TkCircuit

    configuration = {
        "width": 400,
        "height": 200,
        "leds": [
            {"x": 50, "y": 40, "name": "Green", "pin": 17},
            {"x": 150, "y": 40, "name": "Yellow", "pin": 18},
            {"x": 250, "y": 40, "name": "Red", "pin": 27}
        ],
        "buttons": [
            {"x": 50, "y": 130, "name": "Toggle Green", "pin": 6},
            {"x": 150, "y": 130, "name": "Toggle Yellow", "pin": 12},
            {"x": 250, "y": 130, "name": "Toggle Red", "pin": 13}
        ]
    }

    circuit = TkCircuit(configuration)

import gpio_handler as handler

def aux():

    # now just write the code you would use on a real Raspberry Pi
    while True:
        # ここに時間制御ルールを記述できる

        # 10秒待つ
        sleep(10)

        # greenをON/OFFして10秒待つ
        handler.toggle_green()
        sleep(10)

        # yellowをON/OFFして10秒待つ
        handler.toggle_yellow()
        sleep(10)

        # redをON/OFFして10秒待つ
        handler.toggle_red()
        sleep(10)

if mock == False:

    # 直接起動した場合
    if __name__ == '__main__':

        @circuit.run
        def mock_main():
            print("starting mock controller directly")
            aux()
    else:
        print("starting mock controller as server")
        thread = Thread(target=aux, daemon=True)
        thread.start()

        # Tinkerをマルチスレッドで実行できない、つまりUIとサーバーの併用はできない

else:

    # 直接起動した場合
    if __name__ == '__main__':
        print("starting controller dicrectly")
        aux()

    # サーバーとして起動した場合
    else:
        print("starting controller as server")
        thread = Thread(target=aux, daemon=True)
        thread.start()

def getStatus():
    return handler.getStatus()

def setStatus(dict_data):
    handler.setStatus(dict_data)
