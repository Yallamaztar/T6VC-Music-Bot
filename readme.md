# T6VC Music Bot

![https://github.com/Yallamaztar/T6VC-Music-Bot](./image.png)

A voice chat music bot for Plutonium T6 (Black Ops II) that allows players to play YouTube music through in-game voice chat using a virtual microphone setup.

## ⚠️ Requirements

**VB-Cable is REQUIRED to use this bot!**

You need to install [VB-Cable Virtual Audio Device](https://vb-audio.com/Cable/) to route audio from the bot to your game's voice chat. The bot uses a virtual microphone to play audio that gets transmitted through your voice channel.

### Setup Steps:
1. Download and install VB-Cable from the official website
2. Set VB-Cable as your default microphone in Windows
3. Configure your game to use VB-Cable as the microphone input
4. The bot will automatically detect and use the virtual audio device

## 🎮 **IMPORTANT: Bot Deployment Requirements**

**This bot must run as an actual game client to function properly!**

The bot needs to be running **inside the Plutonium T6 game client** as a connected player to interact with the server's voice chat system. Here's why:

- **Voice Chat Integration**: The bot simulates pressing the voice chat key while playing music, which only works when connected as a game client
- **Audio Routing**: Music is played through the virtual microphone and transmitted via the game's voice chat to other players

**What this means:**
- You need a dedicated computer/account that stays connected to your T6 server
- The bot account must remain in-game as a player
- This is not a standalone server application - it requires an active game client

## Features

- 🎵 Play YouTube music through voice chat
- 📋 Queue system for multiple songs
- ⏸️ Pause/Resume functionality
- ⏭️ Skip to next song
- 📏 File size limits (100MB max)
- 🎮 T6VC server integration via RCON
- 🔧 Automatic audio device detection

## Commands

- `!play <youtube_url>` or `!ply <youtube_url>` - Add a song to the queue
- `!pause` or `!pa` - Pause the current song
- `!unpause` or `!up` - Unpause the current song
- `!next` or `!nxt` - Skip to the next song

## Installation

1. Clone this repository
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables in your system:
   ```
   IW4M_URL=your_iw4m_server_url
   IW4M_ID=your_server_id
   IW4M_HEADER=your_iw4m_cookie
   
   RCON_IP=your_rcon_ip
   RCON_PORT=your_rcon_port
   RCON_PASSWORD=your_rcon_password
   ```

4. Run the bot:
   ```bash
   python main.py
   ```

## Configuration

The bot automatically detects your audio device. If you need to change the virtual microphone device name, edit `core/virtual_mic.py` and update the `device_name` parameter in the `VirtualMic` class constructor.

## How It Works

1. The bot monitors T6VC server chat for music commands
2. When a `!play` command is received, it downloads the YouTube audio using yt-dlp
3. Audio is played through the virtual microphone device (VB-Cable)
4. The bot simulates holding down the voice chat key while music plays
5. Audio is routed through your game's voice chat to other players

## Dependencies

- pygame (audio playback)
- yt-dlp (YouTube audio downloading)
- iw4m (T6VC server integration)
- t6rcon (RCON communication)
- keyboard (voice chat key simulation)

## Troubleshooting

- **No audio in game**: Make sure VB-Cable is installed and set as your default microphone
- **Bot not responding**: Check your environment variables and RCON connection
- **Download failures**: Ensure the YouTube URL is valid and the video is not restricted
- **Device not found**: Update the device name in `virtual_mic.py` to match your audio setup

----

# Come Play on Brownies SND 🍰
### Why Brownies? 🤔
- **Stability:** Brownies delivers a consistent, lag-free experience, making it the perfect choice for players who demand uninterrupted action
- **Community:** The players at Brownies are known for being helpful, competitive, and fun—something Orion can only dream of
- **Events & Features:** Brownies is constantly running unique events and offers more server-side customization options than Orion, ensuring every game feels fresh

---

#### [Brownies Discord](https://discord.gg/DtktFBNf5T) | [Brownies IW4M](http://193.23.160.188:1624/) | Made With ❤️ By Budiworld
