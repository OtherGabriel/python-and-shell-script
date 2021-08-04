# -*- coding: utf-8 -*-

# Importação dos recursos usados.

import smtplib
import os

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Functions.

def sendEmail (send_from, send_to, send_subject, send_message, image_embebed_path="", document_path="", image_path="", format="text"):
  # Autentication.  
  try:
    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp.login(send_from["email"], send_from["password"])
  except:
    print("\nAutentication error.")

    return

  # Message configuration.

  message = MIMEMultipart()

  message["From"] = send_from["email"]
  message["To"] = ", ".join(send_to)
  message["Subject"] = send_subject

  # Image embebed verification - Add image embebed? -> Image embebed exist?
  if image_embebed_path != "":
    try:
      html_from_image = "<img src=" + image_embebed_path + ">"

      embebed_image = MIMEText(html_from_image, "html")

      message.attach(embebed_image)
    except:
      print("Path not found (embebed image).")

  # Document verification - Add document? -> Document exist?
  if document_path != "":
    if os.path.isfile(document_path):
      binary_document = open(document_path, 'rb')

      document = MIMEBase('application', 'octate-stream', Name=document_path)
      document.set_payload((binary_document).read())

      encoders.encode_base64(document)

      document.add_header('Content-Decomposition', 'attachment', filename=document_path)
      message.attach(document)
    else:
      print("Path not found (document).")

  # Image verification - Add image? -> Image exist?
  if image_path != "":
    if os.path.isfile(image_path):
      with open(image_path, 'rb') as f: image_data = f.read()

      image = MIMEImage(image_data, name=os.path.basename(image_path))
      message.attach(image)
    else:
      print("Path not found (image).")

  # Add text.
  message.attach(send_message)

  # Send mail.
  try:
    smtp.sendmail(send_from["email"], send_to, message.as_string())
    smtp.quit()
  except:
    print("Message not sent.")

  # Confirmation message.
  print("Success in sent mail.")
