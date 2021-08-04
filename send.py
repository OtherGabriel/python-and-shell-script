# -*- coding: utf-8 -*-

# Resource import.

import constants
import postman

from helpers.messageHelper import buildMessage
from helpers.htmlHelper import htmlTransform

# Html transform.

email_title = htmlTransform(tag = "h2", content = constants.EMAIL_TITLE)
email_body = htmlTransform(tag = "h4", content = constants.EMAIL_BODY)

# Format message.
all_texts = [ email_title, email_body ]

# Email configuration.

send_from = { "email": constants.EMAIL, "password": constants.PASSWORD }
send_to = [ "other-mail@your-domain" ]
subject = "Your email subject"

builded_message = buildMessage(texts = all_texts, format = "html")

# Send mail.
postman.sendEmail(send_from = send_from,
                  send_to = send_to,
                  send_subject = subject,
                  send_message = builded_message,
                  format = "html")
