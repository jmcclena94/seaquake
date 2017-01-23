from sanic import Sanic
# from sanic.response import text
from sanic.response import json

app = Sanic(__name__)

@app.middleware('request')
async def print_on_request(request):
    print("I print when a request is received by the server.")

@app.middleware('response')
async def print_on_request(request, response):
    print("I print when a response is returned by the server.")

@app.route("/")
async def test(request):
    return json({"hello":"world"})


app.run(host="0.0.0.0", port=8000, debug=True)
