from imapclient import IMAPClient
import pyzmail

HOST = "imap.gmail.com"
USERNAME = "kshirsagarkanishka@gmail.com"
PASSWORD = "fnul mfmh ygrq gdhq"

def read_latest_mail():
  server = IMAPClient(HOST)
  server.login(USERNAME,PASSWORD)
  server.select_folder("INBOX")

  messages = server.search()
  if len(messages) == 0:
      server.logout()
      return None,None
  else:
     last_id = messages[-1]
     raw_text_content = server.fetch([last_id],["BODY[]"])

     text_content = pyzmail.PyzMessage.factory(raw_text_content[last_id][b"BODY[]"])
     subject = text_content.get_subject()
     body = text_content.text_part.get_payload().decode(text_content.text_part.charset)

     return subject, body

subject, body = read_latest_mail()
print(subject)
print(body)