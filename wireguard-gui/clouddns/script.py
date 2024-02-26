#!/usr/bin/python
import sys
import time
import os
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Arranco el contenedor")

# Se obtiene la variable de entorno DYNAMIC_DNS_URL
DYNAMIC_DNS_URL = os.getenv("DYNAMIC_DNS_URL")
HOSTNAME = os.getenv("HOSTNAME")

logging.info(f"HSOTNAME: {HOSTNAME}");

if not DYNAMIC_DNS_URL:
    logging.info("Error: La variable de entorno DYNAMIC_DNS_URL no está definida.")
    exit(1)

while True:
    if sys.version_info[0] < 3:
        import urllib
        page = urllib.urlopen(DYNAMIC_DNS_URL, None, 30)
        ip_publica = urllib.urlopen("https://api.ipify.org").read().decode("utf-8")
    else:
        import urllib.request
        page = urllib.request.urlopen(DYNAMIC_DNS_URL, None, 30)
        ip_publica = urllib.request.urlopen("https://api.ipify.org").read().decode("utf-8")
    
    # Se imprime la IP pública en el log
    logging.info(f"IP pública: {ip_publica}")
    # Se decodifica la respuesta a string
    resultado = page.read().decode("utf-8")
    page.close()

    logging.info(f"Resultado: {resultado}")

    if resultado == "OK":
        logging.info("Esperando 10 minutos...")
        time.sleep(600)
    else:
        # Se imprime el valor de resultado y se sale del programa
        logging.info(f"El resultado ha cambiado a: {resultado}")
        break

logging.info("Termino el contenedor")
