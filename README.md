# Line GPT 聊天機器人

這是一個整合了 OpenAI GPT-4.1-mini 的 Line 聊天機器人，可以與用戶進行智能對話。

## 功能

- 接收 Line 用戶消息
- 調用 OpenAI GPT-4.1-mini 模型生成回覆
- 將 AI 生成的回覆發送回 Line

## 項目結構

```
line-gpt-bot/
├── app.py           # Flask 應用程式主文件
├── requirements.txt   # Python 依賴列表
├── README.md        # 項目說明文件
└── .env.example     # 環境變數範例文件
```

## 設置步驟

### 1. 獲取必要的憑證

在開始之前，您需要獲取以下三項憑證：

- **LINE Channel Access Token**
- **LINE Channel Secret**
- **OpenAI API Key**

#### A. 設置 LINE 機器人

根據最新的（2024年9月後）申請流程，您需要先創建一個 LINE 官方帳號，然後啟用 Messaging API。

1.  **創建 LINE 官方帳號**：前往 [LINE Official Account Manager](https://manager.line.biz/) 創建一個新的官方帳號。
2.  **啟用 Messaging API**：在官方帳號的「設定」頁面中，找到「Messaging API」並啟用它。
3.  **創建 Provider 和 Channel**：按照提示創建一個新的 Provider 和 Messaging API Channel。
4.  **獲取憑證**：
    - 在 [LINE Developers Console](https://developers.line.biz/console/) 中，進入您的 Channel。
    - 在 **Messaging API** 頁籤下，發行一個 **Channel access token (long-lived)**。
    - 在 **Basic settings** 頁籤下，找到您的 **Channel secret**。

#### B. 獲取 OpenAI API Key

1.  前往 [OpenAI Platform](https://platform.openai.com/) 註冊或登錄。
2.  在 API Keys 頁面創建一個新的 Secret Key。

### 2. 設置本地開發環境

#### A. 克隆或下載項目

將此項目文件下載到您的本地電腦。

#### B. 安裝 Python 和 Pip

確保您的系統已安裝 Python 3.7+ 和 pip。

#### C. 創建並激活虛擬環境（推薦）

```bash
python -m venv venv
source venv/bin/activate  # 在 Windows 上使用 `venv\Scripts\activate`
```

#### D. 安裝依賴

```bash
pip install -r requirements.txt
```

#### E. 設置環境變數

創建一個 `.env` 文件，並將您的憑證填寫進去：

```
LINE_CHANNEL_ACCESS_TOKEN=YOUR_LINE_CHANNEL_ACCESS_TOKEN
LINE_CHANNEL_SECRET=YOUR_LINE_CHANNEL_SECRET
OPENAI_API_KEY=YOUR_OPENAI_API_KEY
```

`app.py` 將會自動讀取這些環境變數。

### 3. 運行本地伺服器

在項目根目錄下運行以下命令：

```bash
python app.py
```

您的本地伺服器將在 `http://127.0.0.1:5000` 上運行。

### 4. 使用 ngrok 暴露本地伺服器

LINE 的 Webhook 需要一個公開的 HTTPS URL。在本地開發時，您可以使用 `ngrok` 來實現這一點。

1.  [下載並安裝 ngrok](https://ngrok.com/download)。
2.  運行以下命令將您的本地伺服器暴露到公網：

    ```bash
    ngrok http 5000
    ```

3.  複製 ngrok 提供的 `https` 開頭的 Forwarding URL。

### 5. 配置 LINE Webhook

1.  回到 [LINE Developers Console](https://developers.line.biz/console/)。
2.  在您的 Channel 的 **Messaging API** 頁籤下，找到 **Webhook settings**。
3.  將 ngrok 提供的 URL 貼到 **Webhook URL** 欄位，並在後面加上 `/callback`。
    例如：`https://your-ngrok-url.ngrok.io/callback`
4.  啟用 **Use webhook**。
5.  點擊 **Verify** 按鈕，您應該會看到 `Success` 的提示。

## 開始測試

現在，您可以打開 LINE，添加您的機器人為好友，然後開始與它對話了！

## 部署到雲端（可選）

當您準備好將機器人部署到生產環境時，可以考慮以下平台：

- **Heroku**
- **Google Cloud Run**
- **AWS Elastic Beanstalk**

部署時，請確保將環境變數（`LINE_CHANNEL_ACCESS_TOKEN`, `LINE_CHANNEL_SECRET`, `OPENAI_API_KEY`）設置在您的雲端服務上。
