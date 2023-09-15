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
messages = [
    {"role": "system", "content": "你是詠智的好朋友"},
]

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
        temperature=0.7,
        max_tokens=500,
        top_p=0.95,
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
    <!DOCTYPE html>

<html lang="en">
<head>
    <!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-149360615-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-149360615-1');
</script>

<meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><meta charset="utf-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" /><title>
	逢甲土木數位學習平台：首頁
</title><script src="/fcutv/bundles/modernizr?v=inCVuEFe6J4Q07A0AcRsbJic_UE5MwpRMNGcOtk94TE1"></script>
<link href="/fcutv/Content/css?v=NAdJiCAdEHGkvAyhISGtrHuwWK503bJYevfBVESxgSY1" rel="stylesheet"/>
<link href="favicon.ico" rel="shortcut icon" type="image/x-icon" /></head>
<body><!-- style="background-image:url('/fcutv/fcu-back.png');background-repeat:no-repeat"-->
    <form method="post" action="./" id="ctl01">
<div class="aspNetHidden">
<input type="hidden" name="__EVENTTARGET" id="__EVENTTARGET" value="" />
<input type="hidden" name="__EVENTARGUMENT" id="__EVENTARGUMENT" value="" />
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="b9IJEDxgLxefa0dHJmF0RiXpERevXE9HJ1f++x4N75l4twk2lUPEC59PXrLmbxUOAfWez3E4o0HQS0n/4TmLionQ4L9L8txw9rAO5rVpk9kkxm2oCBNyU3sH/isBJCYOJS2e7zOZCb6O1DIybNegyLfFFZCc4XZHEPFdvN20lvIFwvvo2sAdoYg9npfRR0sd76Z8KVE+puLugtMb8MpgpQ==" />
</div>

<script type="text/javascript">
//<![CDATA[
var theForm = document.forms['ctl01'];
if (!theForm) {
    theForm = document.ctl01;
}
function __doPostBack(eventTarget, eventArgument) {
    if (!theForm.onsubmit || (theForm.onsubmit() != false)) {
        theForm.__EVENTTARGET.value = eventTarget;
        theForm.__EVENTARGUMENT.value = eventArgument;
        theForm.submit();
    }
}
//]]>
</script>



<script src="/fcutv/bundles/MsAjaxJs?v=D6VN0fHlwFSIWjbVzi6mZyE9Ls-4LNrSSYVGRU46XF81" type="text/javascript"></script>
<script src="Scripts/jquery-3.3.1.min.js" type="text/javascript"></script>
<script src="Scripts/bootstrap.min.js" type="text/javascript"></script>
<script src="/fcutv/bundles/WebFormsJs?v=N8tymL9KraMLGAMFuPycfH3pXe6uUlRXdhtYv8A_jUU1" type="text/javascript"></script>
<div class="aspNetHidden">

	<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="BDC86CFF" />
</div>
        <script type="text/javascript">
//<![CDATA[
Sys.WebForms.PageRequestManager._initialize('ctl00$ctl09', 'ctl01', [], [], [], 90, 'ctl00');
//]]>
</script>

       
        <div class="navbar navbar-inverse navbar-fixed-top">
            <div class="container">
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
                    <a href="./" class="navbar-brand">逢甲土木數位學習平台</a>
                </div>
                <div class="navbar-collapse collapse">
                    <ul class="nav navbar-nav">
                        <li><a href="./">首頁</a></li>
                        <li><a href="About">關於我們</a></li>
                        <li><a href="Department/CEVideoList.aspx">系務影音專區</a></li>
                        
                    </ul>
                    
                            <ul class="nav navbar-nav navbar-right">
                                <!--<li><a href="Account/Register">註冊</a></li>-->
                                <li><a href="Account/Login">登入</a></li>
                            </ul>
                        
                </div>
            </div>
        </div>
        <div class="container body-content">



            
    <style>
.jumbotronx {
    background-color: #eeeeee;
    padding: 20px;
    
}

    </style>
    <div class="jumbotronx">
        <h1 style="font-family: 微軟正黑體;font-size:60px;font-weight:500">逢甲土木數位學習平台</h1>
    </div>

    <div class="row">
        <div class="col-md-4">
            <h2 style="font-family: 微軟正黑體">課程清單</h2>
            <ul class="list-group">

                    <li class="list-group-item"><a href="Courses/111-2_AEC/Default.aspx">112(上)土木工程學系/營建產業數位原型實作</a></li>
                    <li class="list-group-item"><a href="Courses/111-2_CAD/Default.aspx">112(上)土木工程學系/工程圖學(一)</a></li>
                    <li class="list-group-item"><a href="Courses/111-2_APP_Night/Default.aspx">111(下)土木工程學系(進修部)/電腦程式應用</a></li>
                    <li class="list-group-item"><a href="Courses/111-2_Python/Default.aspx">111(下)土木工程學系/計算機程式語言</a></li>
                    <li class="list-group-item"><a href="Courses/111-2_CAD/Default.aspx">111(下)土木工程學系/工程圖學(二)</a></li>
                <!--
                    <li class="list-group-item"><a href="Courses/111-1_CS_Night/Default.aspx">111(上)土木工程學系(進修部)/計算機概論</a></li>
                    <li class="list-group-item"><a href="Courses/111-1_CS/Default.aspx">111(上)土木工程學系/計算機概論</a></li>
                    <li class="list-group-item"><a href="Courses/111-1_CAD/Default.aspx">111(上)土木工程學系/工程圖學(一)</a></li>
                    
                
                    <li class="list-group-item"><a href="Courses/110-2_APP_Night/Default.aspx">110(下)土木工程學系(進修部)/電腦程式應用</a></li>
                    <li class="list-group-item"><a href="Courses/110-2_Python/Default.aspx">110(下)土木工程學系/計算機程式語言</a></li>
                    <li class="list-group-item"><a href="Courses/110-2_CAD/Default.aspx">110(下)土木工程學系/工程圖學(二)</a></li>
                    <li class="list-group-item"><a href="Courses/110-2_IEIM/Default.aspx">110(下)土木工程學系/工程資訊管理導論</a></li>


                    <li class="list-group-item"><a href="Courses/110-1_CAD/Default.aspx">110(上)土木工程學系/工程圖學(一)</a></li>
                    <li class="list-group-item"><a href="Courses/109-2_CAD/Default.aspx">109(下)土木工程學系/工程圖學(二)</a></li>
                    
                    <li class="list-group-item"><a href="Courses/110-1_SketchUp/Default.aspx">110(上)土木工程學系(進修部)/智慧生活空間</a></li>      
                    <li class="list-group-item"><a href="Courses/110-1_CS_Night/Default.aspx">110(上)土木工程學系(進修部)/計算機概論</a></li>    
                    <li class="list-group-item"><a href="Courses/110-1_APP/Default.aspx">110(上)土木工程學系/計算機概論</a></li>
                    <li class="list-group-item"><a href="Courses/110-1_CAD/Default.aspx">110(上)土木工程學系/工程圖學(一)</a></li>
                    <li class="list-group-item"><a href="Courses/109-1_CAD/Default.aspx">109(上)土木工程學系/工程圖學(一)</a></li>
                    <li class="list-group-item"><a href="Courses/109-1_CS/Default.aspx">109(上)土木工程學系/計算機概論</a></li>
                    
                    <li class="list-group-item"><a href="Courses/109-2_APP_Night/Default.aspx">109(下)土木工程學系(進修部)/電腦程式應用</a></li>
                    <li class="list-group-item"><a href="Courses/109-1_CS_Night/Default.aspx">109(上)土木工程學系(進修部)/計算機概論</a></li>
                    <li class="list-group-item"><a href="Courses/109-2_Python/Default.aspx">109(下)土木工程學系/計算機程式語言</a></li>
                    <li class="list-group-item"><a href="Courses/109-2_CAD/Default.aspx">109(下)土木工程學系/工程圖學(二)</a></li>
                    -->
                </ul>
            <p>
                <a class="btn btn-default" href="Courses/CourseList.aspx">Learn more &raquo;</a>
            </p>
        </div>
        <div class="col-md-4">
            <h2 style="font-family: 微軟正黑體">使用規則</h2>
            <p>
                若有瀏覽需求，請來信(<a href="mailto:weiylin@mail.fcu.edu.tw">weiylin@mail.fcu.edu.tw</a>)索取帳號密碼。
            </p>
            <p>
                <a class="btn btn-default" href="https://go.microsoft.com/fwlink/?LinkId=301949">Learn more &raquo;</a>
            </p>
        </div>
        <div class="col-md-4">
            <h2 style="font-family: 微軟正黑體">關於我們</h2>
            <p>
                本平台為逢甲大學土木工程學系林威延副教授上課錄影檔，版權所有，盜用必究。
            </p>
            <p>
                <a class="btn btn-default" href="https://go.microsoft.com/fwlink/?LinkId=301950">Learn more &raquo;</a>
            </p>
        </div>
    </div>


            <hr />
            <footer>
                <table class="nav-justified">
                    <tr>
                        <td width="200px"><img id="Image1" src="fcu-logo.png" style="width:200px;" /></td>
                        <td><p style="font-size:small">
                            Copyright © 2023 [逢甲大學土木工程學系]林威延副教授 Feng Chia University All rights reserved</p></td>
                    </tr>
                </table>
            </footer>
        </div>
    </form>
</body>
</html>
    return 'Cat Time!!!'

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
