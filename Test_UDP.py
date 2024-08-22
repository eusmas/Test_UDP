import socket

# Definir la dirección IP y el puerto al que se va a enviar el mensaje
UDP_IP = "192.168.1.16"  # Reemplázalo con la dirección IP del receptor
UDP_PORT = 5000     # Reemplázalo con el puerto adecuado

# Mensaje que se enviará
MESSAGE = b"Hola desde Python2!"

# Crear el socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enviar el mensaje
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

print(f"Mensaje enviado a {UDP_IP}:{UDP_PORT}")

# Cerrar el socket
sock.close()