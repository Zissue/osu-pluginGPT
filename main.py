import quart
import quart_cors
from quart import jsonify

app = quart_cors.cors(quart.Quart(__name__),
                      allow_origin="https://chat.openai.com")


async def get_top_players():
    # Here the code to obtain information about the top players in the game 'osu!' would go
    # But since this is just a skeleton, I will return an example dictionary
    return {
        "players": [
            {"name": "player1", "rank": 1},
            {"name": "player2", "rank": 2},
            {"name": "player3", "rank": 3},
        ]
    }


@app.get("/players")
async def players():
    data = await get_top_players()
    return jsonify(data)


@app.get("/logo.png")
async def plugin_logo():
    filename = 'logo.png'
    return await quart.send_file(filename, mimetype='image/png')


@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    with open("./.well-known/ai-plugin.json") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/json")


@app.get("/openapi.yaml")
async def openapi_spec():
    with open("openapi.yaml") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/yaml")


@app.route('/ping', methods=['GET'])
async def ping():
    return "pong"


def main():
    app.run(debug=True, host="0.0.0.0", port=5003)


if __name__ == "__main__":
    main()
