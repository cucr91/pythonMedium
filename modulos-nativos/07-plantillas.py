# S SIMPLE
# M MAIL
# T TRANSFER
# P PROTOCOL


# https://myaccount.google.com/u/1/lesssecureapps

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

# M  MULTIPORPOSE
# I  INTERNET
# M  MAIL
# E  EXTENSION


plantilla = Path("modulos-nativos/plantila.html").read_text()
template = Template(plantilla)
# cuerpo = template.substitute({"usuario": "chanchito feliz"})
cuerpo = template.substitute(usuario="chanchito feliz")

path = Path("modulos-nativos/holamundo.png")
mime_image = MIMEImage(path.read_bytes())
mensaje = MIMEMultipart()
mensaje["from"] = "Camilo"
mensaje["to"] = "camilocalderonrojas@gmail.com"
mensaje["subject"] = "Esta es una prueba"
cuerpo = MIMEText(cuerpo, "html")
mensaje.attach(cuerpo)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()

    smtp.login("camilocalderonrojas@gmail.com", "contraseña")
    smtp.send_message(mensaje)
    print("mensaje enviado")
