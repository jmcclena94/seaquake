from sanic import Sanic
# from sanic.response import text
from sanic.response import json

app = Sanic(__name__)
app.static('/', './static/html/landing.html')

# @app.route("/")
# async def test(request):
#     return json({"hello":"world"})


app.run(host="0.0.0.0", port=8000, debug=True)
