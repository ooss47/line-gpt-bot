import os
from dotenv import load_dotenv
import google.generativeai as genai
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

# 載入 .env 文件
load_dotenv()

# 創建 Flask 應用程式
app = Flask(__name__)

# 從環境變數讀取憑證
LINE_CHANNEL_ACCESS_TOKEN = os.environ.get('LINE_CHANNEL_ACCESS_TOKEN')
LINE_CHANNEL_SECRET = os.environ.get('LINE_CHANNEL_SECRET')
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')

# 初始化 Line Bot API 和 Webhook Handler
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

# 配置 Gemini API
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

# Webhook 路由
@app.route("/callback", methods=['POST'])
def callback():
    # 獲取 X-Line-Signature 請求頭
    signature = request.headers['X-Line-Signature']

    # 獲取請求主體
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # 處理 webhook 事件
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# 處理文字訊息事件
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text

    # 調用 Gemini API 生成回覆
    try:
        response = model.generate_content(user_message)
        ai_response = response.text
    except Exception as e:
        app.logger.error(f"Gemini API error: {e}")
        ai_response = "抱歉，我現在無法處理您的請求。"

    # 回覆用戶消息
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=ai_response)
    )

# 主程式入口
if __name__ == "__main__":
    app.run(debug=True)
