import serial

# Define the UART port and baud rate for communication
uart_port = '/dev/ttyS0'  # Replace with the appropriate UART port on your Raspberry Pi
baud_rate = 9600  # Adjust the baud rate to match the configuration

# Initialize the UART connection
ser = serial.Serial(uart_port, baud_rate)

# Log message to be sent
log_message = "This is a log message from Raspberry Pi."

# Send the log message via UART
ser.write(log_message.encode())

# Close the UART connection
ser.close()