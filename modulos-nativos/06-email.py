# S SIMPLE
# M MAIL
# T TRANSFER
# P PROTOCOL


# https://myaccount.google.com/u/1/lesssecureapps

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# M  MULTIPORPOSE
# I  INTERNET
# M  MAIL
# E  EXTENSION

mensaje = MIMEMultipart()
mensaje["from"] = "Camilo"
mensaje["to"] = "camilocalderonrojas@gmail.com"
mensaje["subject"] = "Esta es una prueba"
cuerpo = MIMEText("Cuerpo del mensaje", )
mensaje.attach(cuerpo)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()

    smtp.login("camilocalderonrojas@gmail.com", "contraseña")
    smtp.send_message(mensaje)
    print("mensaje enviado")
