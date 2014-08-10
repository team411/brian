import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


class Visualizer:
  def __init__(self, obj):
    self.obj = obj

    # check avail plot types
    if False:
      self.bplot = BList(self.obj)
    elif True:
      self.bplot = BHash(self.obj)

    self.plot_types = self.bplot.plot_types

  def render(self, plot_type):
    self.bplot.prerender(plot_type)
    plt.show()


# line, points, bars, hist
class BList:
  plot_types = ["line", "points", "bars", "hist"]

  def __init__(self, obj):
    self.obj = obj

  def prerender(self, plot_type):
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

  def prerender(self, plot_type):
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












