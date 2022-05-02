import msvcrt
import serial
import time

def userInput(connection):
    
    prev = None
    i = 0
    while True:
        # Check if there is a char to get
        if msvcrt.kbhit():
            
            # Set cmd to the user's char input 
            cmd = msvcrt.getwch()
            
            #Panic break while loop on 'q'
            if (cmd == 'q'):
                connection.write(' '.encode())
                bluetooth.close()
                break

            elif(cmd == 'l' or cmd == 'L'):
                
                # Only allow one direction movement 
                if (prev != cmd):

                    # Make sure dump bed moves up on the first cmd input
                    if (i == 0):
                        connection.write('L'.encode())
                        time.sleep(.60)
                        connection.write(' '.encode())
                        prev = 'L'
                        
                    else:
                        connection.write(cmd.encode())
                        time.sleep(.60)
                        connection.write(' '.encode())
                        prev = cmd

                i += 1

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

