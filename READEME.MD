# Instagram Phishing Page

This project demonstrates a **real-time phishing attack simulation** using a fake Instagram login page. It is designed purely for **ethical hacking, awareness, and educational purposes**. The page captures login credentials (username and password) and stores them in a local log file. The project uses **Ngrok** to expose the local server to the internet, enabling real-time data collection even from mobile devices.

⚠️ Warning
This project is for educational and ethical hacking purposes only. Do NOT use this script to target or collect data from real users without their explicit consent. Unauthorized phishing is illegal and punishable under cybercrime laws.

## 📀 Project Overview

This Instagram phishing page mimics the official login interface to trick the user into entering their credentials. When the user submits the form, the credentials are captured via a PHP script and logged into a file stored locally on the attacker’s machine.

---

## 🛠️ Setup Instructions

### Step-by-step Guide:

1. **Clone or download the repository**
  
   git clone https://github.com/yourusername/Instagram-Phishing.git
   cd Instagram-Phishing
   ```

2. **Start a local PHP server**
 
   php -S 127.0.0.1:8080
   ```

3. **Start Ngrok tunnel**
  
   ngrok http 8080
   ```
   > Copy the HTTPS link Ngrok provides (e.g., https://abc123.ngrok.io)

4. **Open the Ngrok URL on any device (mobile/PC)** and test.

5. **Captured credentials** will be saved in the `logs.txt` file on your local machine.

---

## 🧰 Requirements

- PHP installed
- Ngrok account and executable
- Web browser
- Basic terminal usage

> Note: No external Python or pip packages are needed.

---

## 🧠 How It Works

- The `index.html` page is a fake Instagram login page.
- When a user enters data, it is sent to `login.php`.
- The PHP script saves the credentials to `logs.txt`.
- Ngrok provides a secure public URL that tunnels requests to your local server.
- All credential logs are visible **instantly on your laptop**, even when accessed via phone.

---

## ⚠️ Legal & Ethical Warning

This tool is made for **educational use only** to spread cybersecurity awareness.

> 🚨 Unauthorized use of this phishing simulation for real-world attacks is **strictly illegal** and unethical.

Use it only on systems you own or have explicit permission to test.

---

## 🚀 Future Enhancement Ideas

- Implement OTP (2FA) simulation
- Add IP and geolocation tracking
- Log browser/device info
- Create a dashboard for live monitoring
- Setup email or Telegram alerts

---

## 📂 Folder Structure

```
Instagram-Phishing/
├── index.html         # Fake Instagram login page
├── login.php          # Handles form data and stores credentials
├── logs.txt           # Stores captured usernames and passwords
├── phishing.zip       # Archive for deployment
└── README.md          # Complete guide and documentation
```

✍️ Author
Yash Khedkar
Cybersecurity Enthusiast | Ethical Hacker
💼 Project created for demonstration and learning purposes.

> ✨ "Learn to hack ethically and responsibly. Spread awareness, not fear!" ✨

