# variables de entorno
# SENDGRID_API_KEY = "CONTRASEÑA1234"

import os

apikey = os.environ.get("SENDGRID_API_KEY")
print(apikey)