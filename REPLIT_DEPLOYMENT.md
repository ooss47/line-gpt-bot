# Line GPT 聊天機器人 - Replit 部署指南

## 🎯 為什麼選擇 Replit？

- ✅ **完全免費**：無需信用卡
- ✅ **無需安裝**：在瀏覽器中編寫和運行代碼
- ✅ **自動部署**：代碼保存後自動更新
- ✅ **公開 URL**：自動提供公開的 Webhook URL
- ✅ **24/7 運行**：機器人全天候在線

## 📋 部署步驟

### 步驟 1：創建 Replit 帳號

1. 前往 [Replit 官網](https://replit.com/)
2. 點擊「Sign up」
3. 使用 Google、GitHub 或郵箱註冊（推薦使用 Google）
4. 完成註冊

### 步驟 2：創建新的 Replit 項目

1. 登入 Replit 後，點擊「+ Create」
2. 選擇「Import from GitHub」
3. 如果您有 GitHub 帳號，可以先將項目上傳到 GitHub，然後導入
4. 或者，選擇「Create Repl」，然後選擇「Python」

### 步驟 3：上傳項目文件

如果您選擇了「Create Repl」：

1. 在 Replit 編輯器中，您會看到左側的文件列表
2. 創建以下文件：

#### 文件 1：app.py

```python
import os
from dotenv import load_dotenv
from google.genai import Client
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

# 初始化 Gemini 客戶端
client = Client(api_key=GEMINI_API_KEY)

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
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_message,
        )
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
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
```

#### 文件 2：requirements.txt

```
flask
line-bot-sdk
google-genai
python-dotenv
gunicorn
```

#### 文件 3：.env

```
LINE_CHANNEL_ACCESS_TOKEN=mqTSRezYxe9qRutdXaxtLH4EaKwS2r2nc6TK2KywlXvwtihXgdFDD8hcCFLTKmwRXaWt5WJ5jfndTLjNL1R6eYMb1vCNXFxXWtH+hIextEhuGCbbc0qL550U8Js9FQHiOYZfqrHq0/RnyCTn0mY/3gdB04t89/1O/w1cDnyilFU=
LINE_CHANNEL_SECRET=2a7e6a3bbdc78945c06ede3a1ec4f0f3
GEMINI_API_KEY=AIzaSyCJT7yh1a3FRVCNJB1FFRc8Y2jYic_uiEw
```

### 步驟 4：設置 Replit 秘密變數（推薦）

為了安全起見，建議使用 Replit 的秘密變數功能，而不是在 `.env` 文件中存儲敏感信息：

1. 在 Replit 編輯器中，點擊左側的「Secrets」（鑰匙圖標）
2. 添加以下秘密變數：
   - `LINE_CHANNEL_ACCESS_TOKEN`: `mqTSRezYxe9qRutdXaxtLH4EaKwS2r2nc6TK2KywlXvwtihXgdFDD8hcCFLTKmwRXaWt5WJ5jfndTLjNL1R6eYMb1vCNXFxXWtH+hIextEhuGCbbc0qL550U8Js9FQHiOYZfqrHq0/RnyCTn0mY/3gdB04t89/1O/w1cDnyilFU=`
   - `LINE_CHANNEL_SECRET`: `2a7e6a3bbdc78945c06ede3a1ec4f0f3`
   - `GEMINI_API_KEY`: `AIzaSyCJT7yh1a3FRVCNJB1FFRc8Y2jYic_uiEw`

### 步驟 5：運行應用

1. 在 Replit 編輯器中，點擊頂部的「Run」按鈕
2. Replit 會自動安裝依賴並運行您的應用
3. 您應該會看到類似的輸出：
   ```
   * Running on http://0.0.0.0:5000
   ```

### 步驟 6：獲取公開 URL

1. 應用運行後，Replit 會在右側顯示一個預覽窗口
2. 點擊預覽窗口頂部的 URL（例如：`https://line-gpt-bot.username.repl.co`）
3. 複製這個 URL

### 步驟 7：配置 LINE Webhook

1. 前往 [LINE Developers Console](https://developers.line.biz/console/)
2. 進入您的 Channel → **Messaging API** 頁籤
3. 在 **Webhook settings** 中，填入：
   ```
   https://line-gpt-bot.username.repl.co/callback
   ```
   （將 `line-gpt-bot.username` 替換為您的 Replit URL）

4. 點擊 **Verify**，應該會看到 `Success`
5. 啟用 **Use webhook**

### 步驟 8：開始測試

1. 打開 LINE，添加您的機器人為好友
2. 發送任何消息
3. 機器人應該會用 Gemini AI 生成的回覆回應您

---

## 🎉 完成！

您的 Line GPT 聊天機器人現在已經部署到 Replit，並且可以 24/7 全天候運行！

---

## 📝 常見問題

### Q：如何查看應用日誌？

A：在 Replit 編輯器中，點擊「Console」標籤，您可以看到所有的日誌輸出。

### Q：如何更新代碼？

A：在 Replit 中編輯代碼後，點擊「Run」按鈕重新啟動應用。

### Q：Webhook URL 會改變嗎？

A：不會。Replit 提供的 URL 是永久的，不會改變。

### Q：機器人會一直在線嗎？

A：是的，Replit 的免費方案會保持您的應用在線。

---

## 🚀 下一步

- **自定義機器人**：修改 `app.py` 中的代碼
- **添加更多功能**：實現對話歷史、特殊命令等
- **監控性能**：使用 Replit 的分析工具

祝您使用愉快！🎉
