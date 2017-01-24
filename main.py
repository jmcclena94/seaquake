from sanic import Sanic
# from sanic.response import text
# from sanic.response import json
from sanic.response import html
from get_quake_data import get_quake_data
from jinja2 import Environment, PackageLoader

env = Environment(
    loader=PackageLoader('main', './static/html'),
)

app = Sanic(__name__)

@app.route("/")
async def test(request):
    template = env.get_template('landing.html')
    data = get_quake_data()
    # import pdb; pdb.set_trace()
    return html(template.render(quakes=data))


app.run(host="0.0.0.0", port=8000, debug=True)
