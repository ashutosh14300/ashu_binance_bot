# 🪙 Ashu Binance Bot

A simple Binance **testnet trading bot** written in Python.

This project helps you learn:

- Binance API usage (testnet)
- Market and limit orders
- Safe API key handling using `.env`
- Python project structure
- Git / GitHub workflow

> ⚠️ **NOTE:** This bot is for educational purposes only. It runs on **Binance Testnet**, NOT real money.

---

## ✅ 1. Requirements

Make sure you have:

- Python **3.10+**
- Git installed
- Binance Testnet API keys  
Create keys here:  
🔗 https://testnet.binance.vision/

---

## 📁 2. Project Structure

```
ashu_binance_bot/
├─ main.py
├─ README.md
├─ .gitignore
├─ .env               (not uploaded)
├─ src/
│  ├─ bot_instance.py
│  ├─ limit_orders.py
│  ├─ market_orders.py
│  ├─ utils.py
│  └─ advanced/
│     ├─ stop_loss.py
│     └─ twap.py
└─ bot.log            (generated automatically)
```

---

## 🧬 3. Clone the Repository

```bash
git clone https://github.com/ashutosh14300/ashu_binance_bot.git
cd ashu_binance_bot
```

---

## 🧱 4. Create Python Virtual Environment

### Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 📦 5. Install Dependencies

If you have `requirements.txt`:

```bash
pip install -r requirements.txt
```

If not, install manually:

```bash
pip install python-binance python-dotenv
```

---

## 🔑 6. Create `.env` File

> ⚠️ Never upload `.env` to GitHub (your keys must stay private).

Create the file:

```bash
notepad .env
```

Paste:

```
API_KEY=your_testnet_api_key
API_SECRET=your_testnet_secret_key
USE_TESTNET=True
SYMBOL=BTCUSDT
```

Save and close.

---

## 🚫 7. `.gitignore` Example

Make sure `.gitignore` contains:

```
.env
*.env
__pycache__/
*.log
*.pyc
venv/
env/
```

---

## ▶️ 8. Run the Bot

```bash
python main.py
```

If everything is correct, you should see messages like:

```
INFO - Binance Client Initialized on Testnet
INFO - Submitting market order...
```

---

## 🧪 9. Test API Connection (Optional)

Run this snippet to verify API key works:

```python
from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

client = Client(os.getenv("API_KEY"), os.getenv("API_SECRET"), testnet=True)
print(client.get_account())
```

---

## 🧠 10. Features

| Feature | Status |
|--------|--------|
| Market Orders | ✅ |
| Limit Orders | ✅ |
| Stop Loss | ⚠️ Experimental |
| TWAP Strategy | ⚠️ Experimental |
| Logging | ✅ |

---

## 🛡 Security Rules

- Do **NOT** share `.env`
- If you accidentally commit it → **delete and regenerate your API key**
- Always use **testnet** unless fully confident

---

## 🚀 Future Upgrades

- Docker support
- Telegram alerts
- Grid trading mode
- CI/CD deployment

---

## 🤝 Contributing

To contribute:

```bash
git branch feature-name
git commit -m "Message"
git push
```

Submit a Pull Request.

---

## 📞 Support

If you run into issues:

- Check `.env`
- Check API permissions
- Ensure testnet mode is enabled

---

Happy coding! 🎯  
Trade smart, not blindly. 🚀

