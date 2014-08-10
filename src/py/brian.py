from flask import Flask, url_for, request
import re
import time
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


app = Flask(__name__)


class Renderer:

  def __init__(self, src, line):
    self.raw = src
    self.line = int(line)

  def render(self):
    lines = filter(
      lambda x: not re.match(r'^\s*$', x),
      self.raw.split("\n")[:(self.line + 1)]
    )
    lines = map(lambda s: s.strip(), lines)

    code = "\n".join(lines[:-1])
    expr = lines[-1].split("=")[-1]
    gl = {}
    loc = {}

    print lines

    exec code in gl,loc
    result = eval(expr, loc)

    #os.remove('static/figure.svg')

    plt.bar(range(len(result)),result)
    plt.savefig('static/figure.svg', transparent=True)

    print lines
    return '<html><body style="background-color: rgb(59, 63, 65);"><img style="width:100%;" src="static/figure.svg?' + str(time.time()) + '" /></body></html>'




@app.route("/eval", methods=['GET', 'POST'])
def evaluate():
  if request.method == 'POST':
    src = request.form['src']
  else:
    src = request.args.get('code')

  r = Renderer(src, request.args.get('line'))
  out = r.render()

  return out

@app.route("/form")
def form():
  return """
  <form action="eval" method="post">
    <textarea name="src" rows="30" cols="90"></textarea>
    <br>
    <input type="submit">
  </form>
  """

if __name__ == "__main__":
  app.debug = True
  app.run(host='0.0.0.0')
