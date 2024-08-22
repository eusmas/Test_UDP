import socket

# Configurar la dirección IP y el puerto del destinatario
dest_ip = "192.168.1.16"
dest_port = 5001

# Crear un socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Mensaje que se desea enviar
message = "Hola desde Python!"

# Enviar el mensaje
sock.sendto(message.encode(), (dest_ip, dest_port))

# Cerrar el socket
sock.close()