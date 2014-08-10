from flask import Flask, url_for, request
import re
import urllib2
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import os
import sys

sys.path.append(os.getcwd())
from visualizer import *


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

    print "-----"
    print lines
    print "-----"
    print code
    print "-----"
    print expr
    print "-----"

    exec code in gl,loc
    result = eval(expr, loc)

    print result
    print "-----"

    vis = Visualizer(result)
    print vis.plot_types
    result = vis.render("pie")

    return """<html>
      <body style="background-color: rgb(59, 63, 65);">
      <svg style="width:100%; height:100%" src="static/figure.svg">"""+result+"""</svg></body></html>"""




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
  <form action="eval?line=3" method="post">
    <textarea name="src" rows="30" cols="90"></textarea>
    <br>
    <input type="submit">
  </form>
  """

if __name__ == "__main__":
  app.debug = True
  app.run(host='0.0.0.0')
