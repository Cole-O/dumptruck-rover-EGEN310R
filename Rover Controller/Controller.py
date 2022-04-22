import msvcrt
import serial
import time
from xlwt import Workbook

# Function to test latency and write information to excel
def testLatency(connection):
    startTime = time.time()
    lastTime = startTime
    lap = 1

    wb = Workbook()
    TestSheet = wb.add_sheet("Test Sheet")

    while True:
        if msvcrt.kbhit():
            cmd = msvcrt.getwch()

            if (cmd == 'q'):
                connection.write(' '.encode())
                bluetooth.close()
                # Save workbook
                wb.save("LatencyTest.xls")
                break

            else:
                #Start timer
                connection.write(cmd.encode())
                connection.read()
            
                # Take lap time after the connection reads and write that to an excel file.
                lapTime = (time.time() - lastTime)
                lapTime *= 1000
                print(lapTime)
                # Write command in column 0 and lap time in column 1
                TestSheet.write(lap, 0, cmd)
                TestSheet.write(lap, 1, lapTime)
                

                # Increase lap aka row
                lastTime = time.time()
                lap += 1

def userInput(connection):
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
    # testLatency(bluetooth)

