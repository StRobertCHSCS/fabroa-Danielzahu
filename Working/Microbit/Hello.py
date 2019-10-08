from microbit import*

while True:
    reading = accelerometer.get_x()
    reading_2 = accelerometer.get_y()
    if reading < 50 and reading_2 < 50:
        center = Image("00000:09990:09990:09990:00000")
        display.show(center)
    if reading >= 50:
        right = Image("00000:00999:00999:00999:00000")
        display.show(right)
    if reading <= -50:
        left = Image("00000:99900:99900:99900:00000")
        display.show(left)
    if reading_2 >= 50:
        up = Image("09990:09990:09990:00000:00000")
        display.show(up)
    if reading_2 <= -50:
        down = Image("00000:00000:09990:09990:09990")