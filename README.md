# osu! Top Players Plugin

This project provides a simple plugin to fetch the top players' information from the popular rhythm game, 'osu!'. It has been developed as an extension for the OpenAI ChatGPT platform. 

## Features

- Fetches the top 'osu!' players (skeleton data at the moment).
- Includes the plugin manifest under '/.well-known/ai-plugin.json' route.
- Allows for future extensibility to include more data and real-time updates.

## Installation

Clone this repository:

```bash
git clone https://github.com/Zissue/osu-pluginGPT.git
```

Navigate into the project directory:

```bash
cd osu-pluginGPT
```

Install the required Python dependencies:

```bash
pip install quart quart-cors
```

## Usage

Run the `main.py` file:

```bash
python main.py
```

The application will start a server at `http://0.0.0.0:5003`.

## Routes

- `GET /players`: Returns a list of top 'osu!' players.
- `GET /.well-known/ai-plugin.json`: Returns the plugin manifest.
- `GET /logo.png`: Returns the logo of the plugin.
- `GET /openapi.yaml`: Returns the OpenAPI specification of the application.
