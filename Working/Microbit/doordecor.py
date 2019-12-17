from microbit import *
import radio

def set_servo_angle(pin, angle):
    duty = 26 + (angle * 102) / 180
    pin.write_analog(duty)


angle = 90
set_servo_angle(pin2, angle)
set_servo_angle(pin1, angle)
set_servo_angle(pin0, angle)

radio.on()

while True:
    new_message = radio.receive()
    if new_message == "a message":
        angle += 180
        set_servo_angle(pin2, angle)
        set_servo_angle(pin1, angle)
        set_servo_angle(pin0, angle)
        sleep(300)
        angle -= 180
        set_servo_angle(pin2, angle)
        set_servo_angle(pin1, angle)
        set_servo_angle(pin0, angle)
        sleep(300)
