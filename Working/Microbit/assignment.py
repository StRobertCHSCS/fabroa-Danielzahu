from microbit import*
import music
red_led = pin1
green_led = pin2
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

otherjingle = [
    'c4:1', 'e', 'g', 'c5', 'e5', 'g4', 'c5', 'e5', 'c4', 'e', 'g', 'c5', 'e5', 'g4', 'c5', 'e5',
    'c4', 'd', 'g', 'd5', 'f5', 'g4', 'd5', 'f5', 'c4', 'd', 'g', 'd5', 'f5', 'g4', 'd5', 'f5',
    'b3', 'd4', 'g', 'd5', 'f5', 'g4', 'd5', 'f5', 'b3', 'd4', 'g', 'd5', 'f5', 'g4', 'd5', 'f5',
    'c4', 'e', 'g', 'c5', 'e5', 'g4', 'c5', 'e5', 'c4', 'e', 'g', 'c5', 'e5', 'g4', 'c5', 'e5',
    'c4', 'e', 'a', 'e5', 'a5', 'a4', 'e5', 'a5', 'c4', 'e', 'a', 'e5', 'a5', 'a4', 'e5', 'a5',
    'c4', 'd', 'f#', 'a', 'd5', 'f#4', 'a', 'd5', 'c4', 'd', 'f#', 'a', 'd5', 'f#4', 'a', 'd5',
    'b3', 'd4', 'g', 'd5', 'g5', 'g4', 'd5', 'g5', 'b3', 'd4', 'g', 'd5', 'g5', 'g4', 'd5', 'g5',
    'b3', 'c4', 'e', 'g', 'c5', 'e4', 'g', 'c5', 'b3', 'c4', 'e', 'g', 'c5', 'e4', 'g', 'c5',
    'b3', 'c4', 'e', 'g', 'c5', 'e4', 'g', 'c5', 'b3', 'c4', 'e', 'g', 'c5', 'e4', 'g', 'c5',
    'a3', 'c4', 'e', 'g', 'c5', 'e4', 'g', 'c5', 'a3', 'c4', 'e', 'g', 'c5', 'e4', 'g', 'c5',
    'd3', 'a', 'd4', 'f#', 'c5', 'd4', 'f#', 'c5', 'd3', 'a', 'd4', 'f#', 'c5', 'd4', 'f#', 'c5',
    'g3', 'b', 'd4', 'g', 'b', 'd', 'g', 'b', 'g3', 'b3', 'd4', 'g', 'b', 'd', 'g', 'b'
]

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



