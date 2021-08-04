# Message helper.

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders

# Métodos para formação de mensagens ou campos.

def buildMessage (texts, format="text"):
  if format == "text":
    message = ""
    for line in texts: message = message + "\n" + str(line)

    return message
  elif format == "html":
    message = MIMEMultipart()
    for line in texts: message.attach(MIMEText(line, "html"))

    return message
  else: 
    return
