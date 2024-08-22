import socket
import time

# Mensaje que se enviará
Trama1 = b"Hola desde Python21!"
Trama2 = b"Hola desde Python22!"
T_Espera= 0.5 #Tiempo en segundos

# Definir la dirección IP y el puerto al que se va a enviar el mensaje
UDP_IP = "192.168.1.11"  # Dirección IP del receptor
UDP_PORT = 4000     # Puerto del receptor

# Crear el socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enviar el mensaje
sock.sendto(Trama1, (UDP_IP, UDP_PORT))
time.sleep(T_Espera)
sock.sendto(Trama2 , (UDP_IP, UDP_PORT))

print(f"Mensaje enviado a {UDP_IP}:{UDP_PORT}")

# Cerrar el socket
sock.close()

#asd

Trama3 = b"Hola desde Python21!"