from microbit import*
import music
green_led = pin1
blue_led = pin14
red_led = pin2
PIRsensor_pin = pin15
jingle = [
 'e:2','e:2','e:4',
 'e:2','e:2','e:4',
 'e:2','g:2','c','d',
 'e:8',
 'f:2','f:2','f:3',
 'f:1','f:2','e:2',
 'e:2','e:1','e:1',
 'e:2','d:2','d:2',
 'e:2','d:4','g:4',
 'e:2','e:2','e:4',
 'e:2','e:2','e:4',
 'e:2','g:2','c','d',
 'e:8','f:2','f:2','f:2',
 'f:2','f:2','e:2',
 'e:2','e:1','e:1',
 'g:2','g:2','f:2',
 'd:2', 'c:4'
]


alarm = ['g#4:4', 'c#4:4', 'g#4:4', 'c#4:4', 'g#4:4', 'c#4:4', 'g#4:4', 'c#4:4', 
'g#4:4', 'c#4:4', 'g#4:4', 'c#4:4', 'g#4:4', 'c#4:4', 'g#4:4', 'c#4:4', 'g#4:4', 
'c#4:4', 'g#4:4', 'c#4:4']

while True:
    if button_a.is_pressed():
        music.play(jingle,wait=False,loop=True)
        display.scroll(
            "Merry Christmas!", delay=90, wait=False, loop=False, monospace=False)
        while True:
            red_led.write_digital(1)
            sleep(100)
            red_led.write_digital(0)
            sleep(100)
            green_led.write_digital(1)
            sleep(150)
            green_led.write_digital(0)
            sleep(150)
    elif button_b.is_pressed():
        music.play(music.ODE,wait=False,loop=True)
        display.scroll(
            "Happy New Year!", delay=90, wait=False, loop=False, monospace=False)
        while True:
            red_led.write_digital(1)
            sleep(100)
            red_led.write_digital(0)
            sleep(100)
            green_led.write_digital(1)
            sleep(150)
            green_led.write_digital(0)
            sleep(150)
    elif PIRsensor_pin.read_digital() == 1:
        music.play(alarm, wait=False, loop=False)
        display.scroll("Intruder!", delay=90, wait=False, loop=True)
        while True:
            red_led.write_digital(1)
            sleep(100)
            red_led.write_digital(0)
            sleep(100)
            blue_led.write_digital(1)
            sleep(150)
            blue_led.write_digital(0)
            sleep(150)
        break