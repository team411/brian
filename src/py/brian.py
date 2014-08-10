from flask import Flask, url_for, request
import re
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


app = Flask(__name__)


class Renderer:

  def __init__(self, src):
    self.raw = src

  def render(self):
    lines = filter(
      lambda x: not re.match(r'^\s*$', x),
      self.raw.split("\n")
    )
    lines = map(lambda s: s.strip(), lines)

    code = "\n".join(lines[:-1])
    expr = lines[-1].split("=")[-1]
    gl = {}
    loc = {}

    exec code in gl,loc
    result = eval(expr,loc)

    plt.bar(range(len(result)),result)
    plt.savefig('static/figure.svg')

    print lines
    return 'static/figure.svg'




@app.route("/eval", methods=['GET', 'POST'])
def evaluate():
  if request.method == 'POST':
    src = request.form['src']
  else:
    src = request.args.get('src')

  r = Renderer(src)
  out = r.render()

  return out

@app.route("/form")
def form():
  return """
  <form action="eval" method="post">
    <textarea name="src" rows="30" cols="90"></textarea >
    <br>
    <input type="submit">
  </form>
  """

if __name__ == "__main__":
  app.debug = True
  app.run(host='0.0.0.0')
