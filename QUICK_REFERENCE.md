# LINE 聊天機器人 - 快速參考卡

## 🎯 關鍵信息

| 項目 | 值 |
|------|-----|
| **Channel ID** | 2009075799 |
| **部署平台** | Render |
| **公開 URL** | https://line-gpt-bot-zi8n.onrender.com |
| **Webhook URL** | https://line-gpt-bot-zi8n.onrender.com/callback |
| **AI 模型** | Google Gemini 2.5 Flash |
| **GitHub** | https://github.com/ooss47/line-gpt-bot |

---

## 🚀 快速命令

### 本地開發

```bash
# 安裝依賴
pip install -r requirements.txt

# 運行應用
python app.py

# 訪問應用
http://127.0.0.1:5000
```

### Git 操作

```bash
# 提交更改
git add .
git commit -m "Your message"
git push origin main

# Render 會自動部署
```

---

## 📱 測試聊天機器人

1. **掃描 QR Code**（在 LINE Developers Console）
2. **或搜索 Channel ID**：`2009075799`
3. **發送測試消息**
4. **等待 AI 回應**

---

## 🔧 環境變數

```env
LINE_CHANNEL_ACCESS_TOKEN=your_token
LINE_CHANNEL_SECRET=your_secret
GEMINI_API_KEY=your_api_key
```

---

## 📊 監控

### Render 日誌

```
Render Dashboard → line-gpt-bot → Logs
```

### 常見日誌

```
✅ Your service is live
❌ ERROR in app: [error message]
```

---

## 🔑 更新 API 密鑰

### 步驟 1：生成新密鑰

- LINE：[LINE Developers Console](https://developers.line.biz/)
- Gemini：[Google AI Studio](https://aistudio.google.com/app/apikey)

### 步驟 2：更新 Render

```
Render Dashboard → Environment → Edit → Update → Save
```

### 步驟 3：應用自動重啟

---

## 🐛 快速故障排除

| 問題 | 解決方案 |
|------|--------|
| 無法接收消息 | 檢查 Webhook URL 和啟用狀態 |
| AI 無回應 | 檢查 Gemini API 密鑰和配額 |
| 應用崩潰 | 查看 Render 日誌 |

---

## 📚 文件位置

```
line-gpt-bot/
├── app.py                    # 主應用
├── requirements.txt          # 依賴
├── .env                      # 密鑰
├── DEPLOYMENT_GUIDE.md       # 完整指南
└── QUICK_REFERENCE.md        # 本文件
```

---

## 🎓 學習資源

- [LINE Messaging API](https://developers.line.biz/)
- [Google Gemini API](https://ai.google.dev/)
- [Flask 教程](https://flask.palletsprojects.com/)

---

**最後更新**：2026年2月8日
