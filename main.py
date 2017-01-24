from sanic import Sanic
from sanic.response import json, html
import os
from get_quake_data import get_quake_data

app = Sanic(__name__)

@app.route("/")
async def test(request):
    template = open(os.getcwd() + "/index.html")
    return html(template.read())

@app.route("/json")
async def test(request):
    return json(get_quake_data())


app.run(host="0.0.0.0", port=8000, debug=True)
