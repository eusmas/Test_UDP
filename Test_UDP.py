import socket
import time
import Fosber

# Definir la dirección IP y el puerto al que se va a enviar el mensaje
UDP_IP = "192.168.0.10"  # Dirección IP del receptor
UDP_PORT = 2000     # Puerto del receptor
T_Espera= 3 #Tiempo en segundos

Trama= Fosber.Fosber_temp
#Trama="LPDID4011MD0SN5073 19 1WBC-C450FLCSI1SMWILOL1BI723115A-01/1BUPRODUCTOS FAMILIACD050031 MEDELLINBW5100BL8680ST850 3400 850BO1BC393SH400SP2BP0ET0TS0PSTLP0CMFF21MNFF21DD20240822PC16047943PW0PL0NW0NL0DO0TB0BD0EP0P1 P2 P3 P4 BATRT0CS03D"

# Crear el socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Consecutivo
for x in range(100):
    Fosber= "" + f"{x:02}" + Trama
    print(Fosber) 
    sock.sendto(Fosber.encode(encoding="utf-8"), (UDP_IP, UDP_PORT))
    time.sleep(T_Espera)


print(f"Mensaje enviado a {UDP_IP}:{UDP_PORT}")
# Cerrar el socket
sock.close()