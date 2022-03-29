import msvcrt
import serial

def userInput(connection):
    while True:
        # Check if there is a char to get
        if msvcrt.kbhit():
            # Set cmd to the user's char input 
            cmd = msvcrt.getwch()
            #Panic break while loop on 'q'
            if (cmd == 'q'):
                break
            # Send cmd to Arduino
            else:
                connection.write(cmd.encode())
    
if __name__ == "__main__":
    # Connect to bluetooth via serial COM3 port
    bluetooth = serial.Serial(port='COM3', baudrate=9600)

    # Visual check to see if connection is opened
    print(bluetooth.isOpen())

    # Get user input
    userInput(bluetooth)
