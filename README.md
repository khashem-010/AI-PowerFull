# AI-PowerFull :robot: :earth_africa:

An Enigma2 plugin that translates TV subtitles to Arabic in real-time using AI, with Egyptian voice dubbing support.

![Plugin Screenshot](skin/images/screenshot.png)

## Features
- :arabic: **Auto-translate subtitles** to Arabic (or any language)
- :microphone: **Voice dubbing** with Egyptian dialect options
- :zap: **Fast caching** system for smooth performance
- :tv: Works with **all Enigma2 boxes** (Egami, OpenATV, etc.)

## Installation

### 1. Dependencies
```bash
opkg update
opkg install python3-requests python3-langdetect
pip3 install openai --user
