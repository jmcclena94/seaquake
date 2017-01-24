from sanic import Sanic
from sanic.response import json, html
import os
from get_quake_data import get_quake_data
import settings

app = Sanic(__name__)
app.static('/static', settings.STATIC_DIR)


@app.route("/")
async def test(request):
    template = open(os.getcwd() + "/project/index.html")
    return html(template.read())

@app.route("/json")
async def test(request):
    return json(get_quake_data())


app.run(host="127.0.0.1", port=8000, debug=True)
