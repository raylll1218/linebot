from flask import Flask, request, abort
import os
import openai
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

# Set OpenAI API details
openai.api_type = "azure"
openai.api_version = "2023-05-15"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE")

app = Flask(__name__)

# Initialize messages list with the system message
messages =  [{"role":"system","content":"You are an AI assistant that helps people find information."},{"role":"user","content":"我的第一個問題是你今年幾歲"},{"role":"assistant","content":"我今年三歲"},{"role":"user","content":"我的第二個問題是你會說謊嗎"},{"role":"assistant","content":"作為 AI 助理，我並不具備欺騙的能力。我只能根據我所學到的知識和程序來回答你的問題。如果你有任何疑慮或不確定的事情，請隨時告訴我，我會盡我所能為你提供最準確和可靠的答案。"},{"role":"user","content":"我的第三個問題是你記得我的第一個問題嗎"},{"role":"assistant","content":"當然，你的第一個問題是 \"你今年幾歲\"。作為 AI 助理，我能夠記住你之前提出的所有問題和對話，以便在需要時能夠提供更好的幫助。"}]
#[
#{"role": "system", "content": "You are a helpful assistant that has a deep understanding of baby and also speaks like a lovely guys and also you are a professor specializing in information engineering. \
#                                   Your name is zzbot or 智智狗 in Chinese. You are very good at telling jokes.  \
#                                  You will say you don't know if the answer does not match any result from your database. Be concise with your response \
#                                   Refrain from responding in simplified Chinese, you will respond in traditional Chinese at all time.\
#                                   請用小於6歲的孩子能夠聽懂的語言和親切、容易親近的口吻如同媽媽般的口吻來講話，而且你是一名專業的工業設計師和心理諮商師\
#                                   You answer 智智狗好帥 when i say 詠智是誰"},
#]

# This function takes a chat message as input, appends it to the messages list, sends the recent messages to the OpenAI API, and returns the assistant's response.
def aoai_chat_model(chat):
    # Append the user's message to the messages list
    messages.append({"role": "user", "content": chat})

    # Only send the last 5 messages to the API
    recent_messages = messages[-5:]

    # Send the recent messages to the OpenAI API and get the response
    response_chat = openai.ChatCompletion.create(
        engine="gpt-35-turbo",
        messages=recent_messages,
        temperature=0.9,
        max_tokens=1500,
        top_p=0.85,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )

    # Append the assistant's response to the messages list
    messages.append({"role": "assistant", "content": response_chat['choices'][0]['message']['content'].strip()})

    return response_chat['choices'][0]['message']['content'].strip()

# Initialize Line API with access token and channel secret
line_bot_api = LineBotApi(os.getenv('LINE_ACCESS_TOKEN'))
handler1 = WebhookHandler(os.getenv('LINE_CHANNEL_SECRET'))

# This route serves as a health check or landing page for the web app.
@app.route("/")
def mewobot():
    return '智智測試123!!'

# This route handles callbacks from the Line API, verifies the signature, and passes the request body to the handler.
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler1.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'

# This event handler is triggered when a message event is received from the Line API. It sends the user's message to the OpenAI chat model and replies with the assistant's response.
@handler1.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=aoai_chat_model(event.message.text))
    )

if __name__ == "__main__":
    app.run()
