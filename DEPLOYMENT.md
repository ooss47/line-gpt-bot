'''
# Line GPT 聊天機器人部署指南

本指南將引導您將 Line GPT 聊天機器人部署到雲端平台，以便 24/7 全天候運行。

## 部署平台選擇

您可以選擇多種雲端平台來部署您的機器人，以下是幾個常見的選擇：

- **Heroku**：非常適合初學者，提供簡單的部署流程和免費方案。
- **Google Cloud Run**：基於容器的無伺服器平台，按需付費，擴展性好。
- **AWS Elastic Beanstalk**：功能強大的平台即服務（PaaS），支持多種語言和框架。

本指南將以 **Heroku** 為例進行詳細說明。

## 使用 Heroku 部署

### 1. 準備工作

- **註冊 Heroku 帳戶**：前往 [Heroku 官網](https://www.heroku.com/) 創建一個免費帳戶。
- **安裝 Heroku CLI**：根據您的操作系統，[安裝 Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)。
- **安裝 Git**：確保您的系統已安裝 [Git](https://git-scm.com/downloads)。

### 2. 項目準備

#### A. Procfile

在您的項目根目錄下創建一個名為 `Procfile` 的文件（沒有擴展名），並添加以下內容：

```
web: gunicorn app:app
```

這個文件告訴 Heroku 如何啟動您的 Web 應用程式。

#### B. requirements.txt

確保您的 `requirements.txt` 文件包含所有必要的依賴：

```
flask
line-bot-sdk
openai
gunicorn
```

#### C. Git 初始化

在項目根目錄下初始化 Git 倉庫：

```bash
git init
git add .
git commit -m "Initial commit"
```

### 3. 部署到 Heroku

#### A. 登錄 Heroku

在終端中運行以下命令並按照提示登錄：

```bash
heroku login
```

#### B. 創建 Heroku 應用

```bash
heroku create your-unique-app-name
```

如果您不指定名稱，Heroku 會為您隨機生成一個。

#### C. 設置環境變數

在 Heroku 上設置您的憑證，而不是將它們硬編碼在代碼中：

```bash
heroku config:set LINE_CHANNEL_ACCESS_TOKEN="YOUR_LINE_CHANNEL_ACCESS_TOKEN"
heroku config:set LINE_CHANNEL_SECRET="YOUR_LINE_CHANNEL_SECRET"
heroku config:set OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
```

#### D. 推送到 Heroku

```bash
git push heroku main
```

Heroku 將會自動檢測到您的 Python 應用，安裝依賴，並啟動您的機器人。

### 4. 更新 LINE Webhook

1.  部署完成後，Heroku 會為您提供一個公開的 URL，例如 `https://your-unique-app-name.herokuapp.com/`。
2.  回到 [LINE Developers Console](https://developers.line.biz/console/)。
3.  在您的 Channel 的 **Messaging API** 頁籤下，將 **Webhook URL** 更新為您的 Heroku URL，並在後面加上 `/callback`。
    例如：`https://your-unique-app-name.herokuapp.com/callback`
4.  點擊 **Verify** 確保一切正常。

## 其他部署選項

### Google Cloud Run

1.  **容器化您的應用**：創建一個 `Dockerfile`。
2.  **構建並推送鏡像**：將您的容器鏡像推送到 Google Container Registry (GCR)。
3.  **部署到 Cloud Run**：從 GCR 部署您的鏡像，並設置環境變數。

### AWS Elastic Beanstalk

1.  **安裝 EB CLI**：安裝 AWS Elastic Beanstalk 的命令行工具。
2.  **初始化 EB 應用**：在您的項目目錄中運行 `eb init`。
3.  **創建環境**：運行 `eb create` 來創建您的部署環境。
4.  **設置環境變數**：在 Elastic Beanstalk 控制台中配置您的環境變數。

## 結論

部署完成後，您的 Line 聊天機器人就可以 24/7 不間斷地為用戶提供服務了。如果您在部署過程中遇到任何問題，請查閱相應平台的官方文檔。
'''
