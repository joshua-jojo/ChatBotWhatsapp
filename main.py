from logging import exception
import colours_and_positions as position
import pyautogui as pt
from time import sleep
import pyperclip

sleep(3)


def get_messeage():
    global x,y
    position2 = pt.locateOnScreen("Smile.png", confidence=.9)
    x = position2[0]
    y = position2[1]
    pt.moveTo(x, y, duration=.05)
    pt.moveTo(x + 70, y - 50, duration=.05)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(15,15)
    pt.click
    whatsapp_messeage = pyperclip.paste()
    pt.click()
    return whatsapp_messeage

def response_messeage(messeage):
    global x, y
    position2 = pt.locateOnScreen("Smile.png", confidence=.9)
    x = position2[0]
    y = position2[1]
    pt.moveTo(x + 120, y + 10, duration=.05)
    pt.click()
    pt.typewrite(messeage,interval=.01)
    pt.typewrite("\n", interval=.01)

def process_messeage(messeage): 
    if messeage == "halo" or messeage == "Halo" :
        return "Halo Juga!"

def check_new_messeage():
    global x, y
    while True:
        sleep(1)
        try : 
            position1 = pt.locateOnScreen("NewMessage.png", confidence=.7)

            if position is not None:
                x = position1[0]
                y = position1[1]
                pt.moveTo(x,y,duration=0.1)
                pt.click()
                sleep(.5)
                final_messeage = process_messeage(get_messeage())
                response_messeage(final_messeage)

        except:
            print('Belum ada pesan masuk!')


check_new_messeage()