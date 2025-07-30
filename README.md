# WhatsApp Message Automation

A Python application that allows you to schedule and send automated WhatsApp messages using the Twilio API. This tool is perfect for sending reminders, birthday messages, or any scheduled notifications through WhatsApp.

## 🚀 Features

- **Scheduled Messaging**: Send WhatsApp messages at a specific date and time
- **User-Friendly Interface**: Simple command-line interface for easy interaction
- **Secure Credentials**: Environment variable support for API security
- **Message Status Tracking**: Real-time message delivery status monitoring
- **Error Handling**: Comprehensive error handling and user feedback

## 📋 Prerequisites

Before you begin, ensure you have:

- Python 3.7 or higher installed
- A Twilio account with WhatsApp API access
- WhatsApp Sandbox setup (for testing) or approved WhatsApp Business Account

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/whatsapp-message-automation.git
   cd whatsapp-message-automation
   ```

2. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   - Copy the example environment file:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` file with your Twilio credentials:
     ```
     TWILIO_ACCOUNT_SID=your_account_sid_here
     TWILIO_AUTH_TOKEN=your_auth_token_here
     TWILIO_WHATSAPP_NUMBER=your_whatsapp_sandbox_number_here
     ```

## 🔧 Twilio Setup

### Option 1: WhatsApp Sandbox (Free - For Testing)

1. **Create a Twilio Account**
   - Sign up at [Twilio Console](https://console.twilio.com/)
   - Navigate to Messaging → Try it out → Send a WhatsApp message

2. **Get Your Sandbox Details**
   - Find your Account SID and Auth Token in the Twilio Console
   - Note your WhatsApp Sandbox number (usually `+14155238886`)
   - Get your sandbox join code

3. **Add Recipients to Sandbox**
   - Recipients must send your join code to your sandbox number
   - Example: Send `join your-sandbox-code` to `+14155238886`

### Option 2: WhatsApp Business API (Production)

1. **Apply for WhatsApp Business Account**
   - Submit business verification through Twilio
   - Wait for approval (can take several days)
   - Once approved, you can send messages to any WhatsApp number

## 🎯 Usage

1. **Run the application**
   ```bash
   python main.py
   ```

2. **Follow the prompts**
   ```
   Enter your name: John Doe
   Enter your WhatsApp number (in E.164 format, e.g., +1234567890): +1234567890
   Enter the message you want to send: Hello! This is a scheduled message.
   Enter the date (YYYY-MM-DD): 2025-12-25
   Enter the time (HH:MM): 09:30
   ```

3. **Wait for scheduled delivery**
   - The application will calculate the delay and wait
   - Message will be sent automatically at the specified time
   - You'll see delivery status and confirmation

## 📱 Message Status Codes

- **`queued`** - Message is waiting to be sent
- **`sent`** - Message has been dispatched to WhatsApp
- **`delivered`** - Message successfully delivered to recipient
- **`failed`** - Message delivery failed
- **`undelivered`** - Message could not be delivered

## ⚠️ Important Notes

### Sandbox Limitations
- Recipients must join your sandbox before receiving messages
- Sandbox sessions expire after 24 hours of inactivity
- Limited to pre-approved numbers only

### Phone Number Format
- Always use E.164 format: `+[country code][phone number]`
- Examples: `+1234567890`, `+919876543210`, `+447911123456`

### Rate Limits
- Twilio has rate limits for message sending
- For high-volume usage, consider upgrading to a paid plan

## 🔒 Security Best Practices

1. **Never commit credentials to version control**
   - The `.env` file is in `.gitignore` for security
   - Use the `.env.example` file as a template

2. **Environment Variables**
   - Always use environment variables for sensitive data
   - Consider using a secrets manager for production deployments

3. **API Key Security**
   - Regularly rotate your Twilio API keys
   - Monitor usage in Twilio Console

## 🐛 Troubleshooting

### Common Issues

1. **"Missing Twilio credentials" Error**
   - Check if `.env` file exists and contains valid credentials
   - Verify environment variable names match exactly

2. **"Content Variables parameter is invalid" Error**
   - This usually means you're using a content template incorrectly
   - For simple messages, remove `content_sid` and `content_variables`

3. **Messages not being delivered**
   - Verify recipient has joined your WhatsApp sandbox
   - Check message status using the enhanced debugging output
   - Ensure phone number is in correct E.164 format

4. **"Import dotenv could not be resolved" Error**
   - Install python-dotenv: `pip install python-dotenv`
   - Or install all requirements: `pip install -r requirements.txt`

### Getting Help

- Check [Twilio WhatsApp Documentation](https://www.twilio.com/docs/whatsapp)
- Review [Twilio Error Codes](https://www.twilio.com/docs/api/errors)
- Visit [Twilio Support](https://support.twilio.com/)

## 📁 Project Structure

```
whatsapp-message-automation/
├── main.py                 # Main application file
├── requirements.txt        # Python dependencies
├── .env                   # Environment variables (not in repo)
├── .env.example          # Example environment file
├── .gitignore           # Git ignore rules
└── README.md           # Project documentation
```

## 🚀 Future Enhancements

- [ ] GUI interface using tkinter or PyQt
- [ ] Multiple recipient support
- [ ] Message templates and personalization
- [ ] Recurring message scheduling
- [ ] Message history and logging
- [ ] Integration with calendar applications
- [ ] Bulk message import from CSV/Excel

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚖️ Disclaimer

- This tool is for educational and personal use
- Respect WhatsApp's Terms of Service and anti-spam policies
- Ensure you have consent before sending automated messages
- Be mindful of message frequency and recipient preferences

## 👨‍💻 Author

**Jeevan Kushwaha**
- GitHub: [@zione-kushwaha](https://github.com/zione-kushwaha)
- LinkedIn: [zi-one](https://linkedin.com/in/zione)

## 🙏 Acknowledgments

- [Twilio](https://www.twilio.com/) for providing the WhatsApp API
- [Python-dotenv](https://github.com/theskumar/python-dotenv) for environment variable management
- The Python community for excellent documentation and support

---

**⭐ Star this repository if you found it helpful!**
