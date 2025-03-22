# Telegram Music Search Bot 🎵

A professional Telegram bot for searching songs and lyrics. This bot allows users to search for songs using Spotify API and fetch lyrics using Genius API. It is built with Python and the `python-telegram-bot` library.

---

## Features 🌟

- **Search Songs**: Search for songs using Spotify API.
- **Fetch Lyrics**: Get song lyrics using Genius API.
- **Inline Buttons**: Users can directly access song links via inline buttons.
- **Error Handling**: User-friendly error messages for invalid queries or API failures.
- **Easy Setup**: Simple configuration using environment variables.

---

## Prerequisites 📋

Before running the bot, ensure you have the following:

1. **Python 3.7 or higher** installed.
2. A **Telegram Bot Token** from [BotFather](https://t.me/BotFather).
3. **Spotify API Credentials** (Client ID and Client Secret) from the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
4. **Genius API Token** from the [Genius API](https://genius.com/api-clients).

---

## Installation 🛠️

1. Clone the repository or download the source code:
   ```bash
   git clone https://github.com/your-username/telegram-music-bot.git
   cd telegram-music-bot
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your API tokens:
   ```plaintext
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   GENIUS_API_TOKEN=your_genius_api_token
   SPOTIFY_CLIENT_ID=your_spotify_client_id
   SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
   ```

4. Run the bot:
   ```bash
   python bot.py
   ```

---

## Usage 🤖

Once the bot is running, you can interact with it using the following commands:

- **/start**: Start the bot and see a welcome message.
- **/search <song name>**: Search for a song on Spotify.
- **/lyrics <song name>**: Fetch lyrics for a song.

Example:
```
/search Shape of You
/lyrics Bohemian Rhapsody
```

---

## API Integration 🔗

This bot uses the following APIs:

1. **Spotify API**: For searching songs.
   - Documentation: [Spotify API Docs](https://developer.spotify.com/documentation/web-api/)
2. **Genius API**: For fetching song lyrics.
   - Documentation: [Genius API Docs](https://docs.genius.com/)

---

## Contributing 🙌

Contributions are welcome! If you'd like to improve this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

---

## License 📄

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Support 💬

If you have any questions or need help, feel free to open an issue or contact me at [sajjadakbari](sajjadakbari.ir).

---

Enjoy your music journey with this bot! 🎶
```

