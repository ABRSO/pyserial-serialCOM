import serial
import time

# Serial port configuration
ser = serial.Serial('COM3', 115200, timeout=1)  # COM3 is my system's serial port, please change it as required

def send_and_receive_message(message):
    ser.write((message + '\n').encode())  # Sends the message and encodes the string into bits
    time.sleep(2)  # Wait for the response
    response = ser.readline().decode().strip()  # Reads the response and decodes the bits back into string
    return response

if __name__ == "__main__":
    message = input("Enter the message to send: ")
    response = send_and_receive_message(message) # Calls the function with input message
    print(f"Sent: {message}")
    print(f"Received: {response} \nSerial port closed")
    ser.close() # Closes the serial port
