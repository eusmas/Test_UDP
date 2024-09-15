import socket
import time
from GeneradorFosber import SimulacionTramaFosber

# Definir la dirección IP y el puerto al que se va a enviar el mensaje
UDP_IP = "192.168.0.10"  # Dirección IP del receptor
UDP_PORT = 2000     # Puerto del receptor
T_Espera= 1 #Tiempo en segundos

# Crear el socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Consecutivo
for x in range(100):
    Fosber= "" + f"{x:02}" + SimulacionTramaFosber()
    print(Fosber) 
    sock.sendto(Fosber.encode(encoding="utf-8"), (UDP_IP, UDP_PORT))
    time.sleep(T_Espera)

print(f"Mensaje enviado a {UDP_IP}:{UDP_PORT}")
# Cerrar el socket
sock.close()