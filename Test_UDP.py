import socket
import time

# Mensaje que se enviará
Trama1 = b"09LPDID3915+MD0+SN5065  3 1+WBC-C720+FLC+SI2+SMFZ+OL2+BI32083/1+BUSK COR MED+CD050031 MEDELLIN+BW16000+BL25500+ST16000+BO1+BC63+SH62+SP1+BP0+ET1+TS0+PST+LP0+CMESPE+MNESPE+DD20240823+PC8406301+PW0+PL0+NW0+NL0+DO0+TB0+BD0+EP0+P1+P2+P3+P4+BAT+RT0+CS0+06"
Trama2 = b"10LPDID3915+MD0+SN5065  3 1+WBC-C720+FLC+SI2+SMFZ+OL2+BI32083/1+BUSK COR MED+CD050031 MEDELLIN+BW16000+BL25500+ST16000+BO1+BC63+SH62+SP1+BP0+ET1+TS0+PST+LP0+CMESPE+MNESPE+DD20240823+PC8406301+PW0+PL0+NW0+NL0+DO0+TB0+BD0+EP0+P1+P2+P3+P4+BAT+RT0+CS0+06"
T_Espera= 1 #Tiempo en segundos

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