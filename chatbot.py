#!/usr/bin/python
import sleekxmpp
import logging
import sys

logging.basicConfig(level=logging.DEBUG)

def session_start(event):
    chatbot.send_presence()
    print('Session started')
    chatbot.get_roster()

def message(msg):
    if msg['type'] in ('chat','normal'):
        print('msg received')
        print(msg['body'])

        msg.reply('Thanks').send()

print sys.argv

jid = sys.argv[1] if len(sys.argv) > 1 else 'myusername@chat.facebook.com'
password = sys.argv[2] if len(sys.argv) > 1 else 'mypassword'
server = ('chat.facebook.com', 5222)

chatbot = sleekxmpp.ClientXMPP(jid,password)
chatbot.add_event_handler('session_start', session_start)
chatbot.add_event_handler('message', message)
chatbot.auto_reconnect = True
chatbot.connect(server)
chatbot.process(block=True)
