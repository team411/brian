import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import StringIO


class Visualizer:
  def __init__(self, obj):
    self.obj = obj
    plt.clf()

    # check avail plot types
    if isinstance(obj, np.ndarray):
      print "---!!! NDARR"
      self.bplot = BList(self.obj)
    elif isinstance(obj, dict):
      print "---!!! DICT"
      self.bplot = BHash(self.obj)

    self.plot_types = self.bplot.plot_types

  def render(self, plot_type):
    self.bplot.prerender()
    imgdata = StringIO.StringIO()
    plt.savefig(imgdata, format='svg', transparent=True)
    imgdata.seek(0)
    return imgdata.buf


# line, points, bars, hist
class BList:
  plot_types = ["line", "points", "bars", "hist"]

  def __init__(self, obj):
    self.obj = obj

  def prerender(self, plot_type = "points"):
    if plot_type == "line":
      plt.plot(self.obj,'-')
    elif plot_type == "points":
      plt.plot(self.obj,'.')
    elif plot_type == "bars":
      plt.bar(range(len(self.obj)),self.obj)
    elif plot_type == "hist":
      plt.hist(self.obj, bins=30)


# bars, pie, values
class BHash:
  plot_types = ["bars", "pie", "values"]

  def __init__(self, obj):
    self.obj = obj

  def prerender(self, plot_type = "pie"):
    if plot_type == "bars":
      x_pos = range(len(self.obj))
      plt.bar(x_pos, self.obj.values() )
      plt.xticks(x_pos, self.obj.keys())
    elif plot_type == "pie":
      plt.pie(self.obj.values(), labels=self.obj.keys())
    elif plot_type == "values":
      plt.plot(self.obj.values())


# scatter, heatmap, surface3D, hist3D
class BPointsList:
  def __init__(self, obj):
    self.obj = obj


# matrix
class BMatrix:
  def __init__(self, obj):
    self.obj = obj


# graph, tree
class BTree:
  def __init__(self, obj):
    self.obj = obj












