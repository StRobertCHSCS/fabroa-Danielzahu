from microbit import*
import music
red_led = pin1
green_led = pin2
blue_led = pin3
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

while True:
    if button_a.is_pressed():
        while True:
            music.play(jingle,wait=False,loop=True)
            display.scroll("merry christmas")
            while True:
                red_led.write_digital(1)
                sleep(100)
                red_led.write_digital(0)
                sleep(100)
                green_led.write_digital(1)
                sleep(150)
                green_led.write_digital(0)
                sleep(150)
        
        


