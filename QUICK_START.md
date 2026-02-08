# Line GPT 聊天機器人 - 快速開始指南

## ✅ 安裝已完成！

您的 Line GPT 聊天機器人已經完成了以下配置：

- ✅ 所有依賴已安裝
- ✅ 環境變數已配置（`.env` 文件）
- ✅ 代碼已修改為使用 Gemini AI
- ✅ 所有配置文件已準備好

## 🚀 運行機器人

### 第一步：進入項目目錄

```bash
cd /home/ubuntu/line-gpt-bot
```

### 第二步：運行 Flask 應用

```bash
python app.py
```

您應該會看到類似的輸出：

```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

### 第三步：在另一個終端中運行 ngrok

打開一個新的終端窗口，運行：

```bash
ngrok http 5000
```

您會看到類似的輸出：

```
ngrok                                       (Ctrl+C to quit)

Session Status                online
Account                       <your-account>
Version                       3.x.x
Region                        us (United States)
Forwarding                    https://xxxx-xxx-xxx-xxx.ngrok.io -> http://localhost:5000
```

複製 `https://` 開頭的 URL。

### 第四步：配置 Webhook

1. 前往 [LINE Developers Console](https://developers.line.biz/console/)
2. 進入您的 Channel
3. 在 **Messaging API** 頁籤下，找到 **Webhook settings**
4. 將 ngrok 的 URL 貼到 **Webhook URL** 欄位，並在後面加上 `/callback`
   - 例如：`https://xxxx-xxx-xxx-xxx.ngrok.io/callback`
5. 點擊 **Verify** 按鈕，您應該會看到 `Success` 的提示
6. 啟用 **Use webhook**

### 第五步：開始測試

現在，您可以打開 LINE，添加您的機器人為好友，然後開始與它對話了！

## 📝 配置文件說明

### .env 文件

您的 `.env` 文件包含以下信息：

```
LINE_CHANNEL_ACCESS_TOKEN=<您的 Token>
LINE_CHANNEL_SECRET=<您的 Secret>
GEMINI_API_KEY=<您的 Gemini API Key>
```

**重要提示**：不要將 `.env` 文件提交到 Git 或任何公開的地方！

### app.py

主應用程式文件，包含：

- **Webhook 端點**：`/callback` 路由接收來自 Line 的消息
- **消息處理**：使用 Gemini AI 生成回覆
- **錯誤處理**：捕捉並處理 API 錯誤

## 🔧 故障排除

### 問題 1：Webhook 驗證失敗

**解決方案**：
- 確保 Flask 應用正在運行
- 確保 ngrok 正在運行
- 確保 Webhook URL 正確（包括 `/callback`）
- 檢查 Channel Secret 是否正確

### 問題 2：機器人沒有回覆

**解決方案**：
- 檢查 Flask 應用的日誌輸出
- 確保 Gemini API Key 正確
- 確保 LINE Channel Access Token 正確
- 檢查 ngrok 是否顯示請求

### 問題 3：Gemini API 錯誤

**解決方案**：
- 確保 Gemini API Key 有效
- 確保您的 Google Cloud 項目已啟用 Generative AI API
- 檢查 API 配額和使用限制

## 📚 下一步

1. **自定義系統提示**：修改 `app.py` 中的 system prompt，使機器人更符合您的需求
2. **添加上下文管理**：實現對話歷史記錄，使機器人能夠進行多輪對話
3. **部署到雲端**：參考 `DEPLOYMENT.md` 將機器人部署到 Heroku、Google Cloud Run 等平台

## 💡 提示

- 使用 `Ctrl+C` 停止 Flask 應用
- 使用 `Ctrl+C` 停止 ngrok
- 每次重啟 ngrok 時，Webhook URL 會改變，需要重新配置
- 在生產環境中，建議使用固定的 Webhook URL（部署到雲端）

## 📞 需要幫助？

如果您遇到任何問題，請檢查：
- 終端的錯誤信息
- Flask 應用的日誌輸出
- ngrok 的請求日誌
- LINE Developers Console 的 Webhook 錯誤統計

祝您使用愉快！🎉
