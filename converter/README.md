 your Telegram file conversion bot:

---

# Telegram File Conversion Bot

A powerful and versatile Telegram bot designed to convert files between various formats. This bot supports audio, image, video, and document conversions with an intuitive user interface.

---

## Features

- **Audio Conversion**: Convert audio files between formats like MP3, WAV, OGG, and FLAC.
- **Image Conversion**: Convert images between formats like JPG, PNG, BMP, and WEBP.
- **Video Conversion**: Convert videos between formats like MP4, AVI, MOV, and MKV.
- **Document Conversion**: Convert documents between formats like PDF, DOCX, and TXT.
- **User-Friendly Interface**: Interactive buttons for selecting file types and output formats.
- **Efficient File Handling**: Temporary files are deleted after conversion to save storage.

---

## Supported Formats

### Audio
- **Input Formats**: MP3, WAV, OGG, FLAC
- **Output Formats**: MP3, WAV, OGG, FLAC

### Image
- **Input Formats**: JPG, PNG, BMP, WEBP
- **Output Formats**: JPG, PNG, BMP, WEBP

### Video
- **Input Formats**: MP4, AVI, MOV, MKV
- **Output Formats**: MP4, AVI, MOV, MKV

### Documents
- **Input Formats**: PDF, DOCX, TXT
- **Output Formats**: PDF, DOCX, TXT

---

## How It Works

1. Start the bot by sending `/start`.
2. Select the type of file you want to convert (audio, image, video, or document).
3. Choose the desired output format.
4. Upload the file you want to convert.
5. The bot will process the file and send back the converted version.

---

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- A Telegram bot token (obtain from [BotFather](https://t.me/BotFather))
- Required Python libraries

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/telegram-file-conversion-bot.git
   cd telegram-file-conversion-bot
   ```

2. Install the required dependencies:
   ```bash
   pip install python-telegram-bot pydub pillow moviepy pdf2image pdf2docx PyPDF2
   ```

3. Set up your Telegram bot token:
   - Replace `YOUR_TELEGRAM_BOT_TOKEN` in the `bot.py` file with your actual bot token.

4. Run the bot:
   ```bash
   python bot.py
   ```

---

## Code Structure

- `bot.py`: The main script that handles the bot's functionality.
- `temp/`: A temporary directory for storing uploaded and converted files (automatically created if it doesn't exist).

---

## Dependencies

- `python-telegram-bot`: For interacting with the Telegram Bot API.
- `pydub`: For audio file conversions.
- `pillow`: For image file conversions.
- `moviepy`: For video file conversions.
- `pdf2image`, `pdf2docx`, `PyPDF2`: For document conversions.

---

## Contributing

Contributions are welcome! If you'd like to add new features, improve the code, or fix bugs, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For questions or support, feel free to reach out:

- **Email**: your-email@example.com
- **Telegram**: [@YourTelegramHandle](https://t.me/YourTelegramHandle)

---

Enjoy using the Telegram File Conversion Bot! 🚀
