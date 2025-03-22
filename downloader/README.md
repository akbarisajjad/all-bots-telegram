 Telegram bot code. This file provides an overview of the bot, its features, setup instructions, and usage guidelines.

---

# Telegram Video Downloader Bot

A Telegram bot that allows users to download videos from **YouTube**, **Instagram**, and **Twitter** directly through the bot. The bot supports multiple video qualities for YouTube and provides a user-friendly interface with inline buttons.

---

## Features

- **YouTube Video Downloader**: Download videos from YouTube in high or low quality.
- **Instagram Video Downloader**: Download videos from Instagram posts or stories.
- **Twitter Video Downloader**: Download videos from Twitter (formerly X).
- **Inline Buttons**: Easy-to-use interface with inline buttons for platform selection and quality preferences.
- **Error Handling**: Clear error messages for invalid links or unsupported platforms.

---

## Setup Instructions

### Prerequisites

1. **Python 3.8 or higher**: Ensure Python is installed on your system.
2. **Telegram Bot Token**: Obtain a bot token from [BotFather](https://core.telegram.org/bots#botfather).
3. **Required Libraries**: Install the required Python libraries using `pip`.

### Installation

1. Clone the repository or download the bot script:
   ```bash
   git clone https://github.com/your-repo/telegram-video-downloader.git
   cd telegram-video-downloader
   ```

2. Install the required dependencies:
   ```bash
   pip install aiogram pytube yt-dlp instaloader
   ```

3. Replace the `API_TOKEN` in the script with your Telegram bot token:
   ```python
   API_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
   ```

4. Run the bot:
   ```bash
   python bot.py
   ```

---

## Usage

1. Start the bot by sending `/start` in Telegram.
2. Choose the platform (YouTube, Instagram, or Twitter) using the inline buttons.
3. Send the video link to the bot.
4. For YouTube, select the desired video quality (high or low) using the inline buttons.
5. The bot will download and send the video to you.

---

## Supported Platforms

- **YouTube**: Supports `.mp4` format with high and low quality options.
- **Instagram**: Downloads videos from posts and stories.
- **Twitter**: Downloads videos from tweets.

---

## Notes

- Ensure the bot has sufficient permissions to send videos and handle messages.
- The bot uses third-party tools like `pytube`, `yt-dlp`, and `instaloader` for downloading videos. Make sure these tools are installed and up-to-date.
- Large videos may take time to download and upload, depending on the server's speed and Telegram's limitations.

---

## Contributing

Contributions are welcome! If you find any issues or want to add new features, feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For questions or support, contact the developer at [your-email@example.com](mailto:your-email@example.com).

---

Enjoy downloading videos with your Telegram bot! 🚀
