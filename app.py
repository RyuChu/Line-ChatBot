from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('trgzoh9s4be5EIFyZqGREHKtkLulFANEb1B6yKvmiAHBKphLZ+69snktF1C6EH4drd0TQzw7rVzi57s5B3W9O4ZKmgobzWZH+UX3wUn/jI02iAxZyaZuKaHZ3rK45rfBnJ5TQ2HpNbFa34+hJnGtPQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('d54e9bb9b9ff4fe2b9c734bceeabaaf8')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # message = TextSendMessage(text=event.message.text)
    # line_bot_api.reply_message(event.reply_token, message)

    infoMsg = "Welcome to the Ryu's channel.\nWe have some instruction for this robot.\n\n1. menu : Show the list.\n2. introduce : Tell you who I am.\n3. education : Chek it out!\n4. experience : My Intern Life"
    # introMsg = "我是一個學習意願高、肯吃苦耐勞會積極完成每件事的人，同與老師眼中我是一個沉著冷靜、會利用時間學習力強的人。我想要透過在學期間的實習機會獲得更多經驗、知識且提升自我能力!"
    introMsg = "I am a person who has a high willingness to learn, work and do everything positively. Being a calm man who will use time to learn. To gain more experience, knowledge and self-ability through internships during my studies."
    # eduMsg = "1. 元智大學 資訊工程學系\n2. 國立政治大學 資訊科學所".encode('utf8')
    eduMsg = "1. Yuan-Ze Univesity - Bachelor of Computer Science\n2. National Cheng-Chi Univesity - Master of Computer Science"
    # exMsg = "1. 於日月光半導體 - CIM部門協助工程師開發軟體、系統(C#, VB.NET, VBA等\n2. 於訊連科技股份有限公司 - QA部門協助軟體測試、系統錯誤偵錯等\n3. 於英特爾股份有限公司 - CCG部門開發測試軟體(C#. PowerShell))".encode('utf8')
    exMsg = "1. Advanced Semiconductor Engineering - Deparment of CIM (Software development using C#, VB .NET...)\n2. CyberLink Corp. - Department of QA (Software testing and debuging)\n3. Intel Corp. - Deparment of CCG (Testing software development using C#, PowerShell...)"
    aboutMsg = "Hi, I'm Chu Yi-Ning.\nMajor in department of Computer science and information engineering. Learning blockchain in the institute now. Looking to leverage strong programming skills as developer."
    skillMsg = "C C++ C#\nNode.js\nVisual Basic .NET\nSolidity\nPowerShell Script\nSQL\nJavaScript HTML CSS PHP\nPython\nR"
    button_template_message = ButtonsTemplate(
        thumbnail_image_url="https://imgur.com/vQgskOu",
        title='Leo Chu', 
        text='Click any button to know me!',
        ratio="1.51:1",
        image_size="cover",
        actions=[
            MessageTemplateAction(
                label='About me', 
                text='About me'
            ),
            MessageTemplateAction(
                label='My Email', 
                text='My Email'
            ),
            MessageTemplateAction(
                label='Skills', 
                text='Skills'
            )
        ]
    )
    if event.message.text.replace(" ", "").lower() == "menu":
        line_bot_api.reply_message(event.reply_token, TemplateSendMessage(alt_text="Profile", template=button_template_message))
    elif event.message.text.replace(" ", "").lower() == "introduce":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=introMsg))
    elif event.message.text.replace(" ", "").lower() == "education":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=eduMsg))
    elif event.message.text.replace(" ", "").lower() == "experience":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=exMsg))
    elif event.message.text == "About me":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=aboutMsg))
    elif event.message.text == "My Email":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="shspsleo@gmail.com"))
    elif event.message.text == "Skills":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=skillMsg))
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=infoMsg))


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
