from sanic import Sanic
# from sanic.response import text
from sanic.response import json
from get_quake_data import get_quake_data

app = Sanic(__name__)

@app.route("/")
async def test(request):
    # app.static('/', './static/html/landing.html')
    return json(get_quake_data())


app.run(host="0.0.0.0", port=8000, debug=True)
