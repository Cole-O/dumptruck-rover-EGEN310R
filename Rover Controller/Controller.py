import serial
import keyboard


def keyboardController(connection):
    while True:
        # Forwards Slow: Move both tracks forward slow
        if keyboard.is_pressed('w'):
            connection.write('w')

        # Forwards Fast: move both tracks forward faster
        elif keyboard.is_pressed('W'):
            connection.write('W')

        # Slow Right Turn: right track forward slowly
        elif keyboard.is_pressed('a'):
            connection.write('a')

        # Hard Right Turn: right track forward, left track backward
        elif keyboard.is_pressed('A'):
            connection.write('A')

        # Backwards Slow: move both tracks backwards slow
        elif keyboard.is_pressed('s'):
            connection.write('s')

        # Backwards Fast: move both tracks backwards fast
        elif keyboard.is_pressed('S'):
            connection.write('S')

        # Slow Left Turn: move left track forward slow
        elif keyboard.is_pressed('d'):
            connection.write('d')

        # Hard Left Turn: move left track forward and right track backward
        elif keyboard.is_pressed('D'):
            connection.write('D')

        # Stop all motors
        elif keyboard.is_pressed('g'):
            connection.write('g')

        elif keyboard.is_pressed('G'):
            connection.write('G')

        # Panic break loop
        elif keyboard.is_pressed('space'):
            break

        # Slow rover down?
        else:
            pass


if __name__ == "__main__":
    bluetooth = serial.Serial(port='COM3', baudrate=9600)
    keyboardController(bluetooth)
