import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x_data = []
y_data = []

fig, ax = plt.subplots()

def ler_porta_serial(porta, baudrate):
    # Configurar a porta serial

    try:
        while True:
            try:
                if ser.in_waiting > 0:
                    # Lê uma linha da porta serial
                    data = ser.readline().decode('utf-8').strip()
                    
                    # Imprime os dados lidos
                    #print(data)
                    values = data.split(';')
                    print(values)
            
            except serial.SerialException as e:
                print(f"Erro na porta serial: {e}")
    
    except KeyboardInterrupt:
        # Encerra o programa quando você pressiona Ctrl+C
        ser.close()
        print("Programa encerrado.")

def update(i):
    # Your code to get the new data goes here
    # For example, you might read a line from the serial port
    line = ser.readline().decode('utf-8').strip()

    # Split the line into values
    values = line.split(';')
    print(values)
    
    # Check if the line contains 4 values
    if len(values) == 6:
        # Convert the values to floats
        try:
            x = float(values[4])/5000
            y = float(values[5])/5000
        except:
            print("Erro na conversão dos dados.")
            return
        # Append the values to the data lists
        x_data.append(x)
        y_data.append(y)
        
    # Clear the current plot
    #ax.clear()

    # Plot the data
    ax.plot(y, 'ro')
    ax.plot(x, 'bo')
    

if __name__ == "__main__":
    
    porta = 'COM4'  # Substitua pela porta serial correta
    baudrate = 115200  # Substitua pela taxa de baud correta
    ser = serial.Serial(porta, baudrate)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Serial Data Plot')

    ani = FuncAnimation(fig, update, interval=5)

    plt.show()

    #ler_porta_serial(porta, baudrate)