#!/bin/python
import matplotlib.pyplot as plt
import numpy as np
import math

def generate_functional_form_of_batman_logo() -> tuple:
  """Wow, this needs to be optimized haha

  Returns:
      tuple: X, Y functional forms for plotting logo
  """
  Y = np.arange(-4,4,.005)
  X = np.zeros((0))
  for y in Y:
    X = np.append(X,abs(y/2)- 0.09137*y**2 + math.sqrt(1-(abs(abs(y)-2)-1)**2) -3)
    
  Y1 = np.append(np.arange(-7,-3,.01), np.arange(3,7,.01))
  X1 = np.zeros((0))
  for y in Y1:
    X1 = np.append(X1, 3*math.sqrt(-(y/7)**2+1))
  X = np.append(X,X1)
  Y = np.append(Y, Y1)
  Y1 = np.append(np.arange(-7.,-4,.01), np.arange(4,7.01,.01))
  X1 = np.zeros((0))
  for y in Y1:
    X1 = np.append(X1, -3*math.sqrt(-(y/7)**2+1))
  X = np.append(X,X1)
  Y = np.append(Y, Y1)
  Y1 = np.append(np.arange(-1,-.8,.01), np.arange(.8, 1,.01))
  X1 = np.zeros((0))
  for y in Y1:
    X1 = np.append(X1, 9-8*abs(y))
  X = np.append(X,X1)
  Y = np.append(Y, Y1)
  Y1 = np.arange(-.5,.5,.05)
  X1 = np.zeros((0))
  for y in Y1:
    X1 = np.append(X1,2)
  X = np.append(X,X1)
  Y = np.append(Y, Y1)
  Y1 = np.append(np.arange(-2.9,-1,.01), np.arange(1, 2.9,.01))
  X1 = np.zeros((0))
  for y in Y1:
    X1 = np.append(X1, 1.5 - .5*abs(y) - 1.89736*(math.sqrt(3-y**2+2*abs(y))-2) )
  X = np.append(X,X1)
  Y = np.append(Y, Y1)
  Y1 = np.append(np.arange(-.7,-.45,.01), np.arange(.45, .7,.01))
  X1 = np.zeros((0))
  for y in Y1:
    X1 = np.append(X1, 3*abs(y)+.75)
  X = np.append(X,X1)
  Y = np.append(Y, Y1)
  return (X, Y)

def plot_batman_logo(X: np.ndarray, Y: np.ndarray, facecolor=(0, 0, 0), plt_style=False, savefig=False):
  """Plot the batman logo.

  Args:
      X (np.ndarray): X functional form for plotting logo.
      Y (np.ndarray): Y functional form for plotting logo.
      facecolor (tuple, optional): Facecolor for plot. Defaults to (0, 0, 0).
      savefig (str, optional): Path to save figure. Defaults to False.
  """
  # plt.style.use('')
  if plt_style:
    plt.style.use(plt_style)
  ax = plt.gca()
  ax.set_facecolor(facecolor)
  plt.plot(Y,X, 'yo')
  ax.set_yticklabels([])
  ax.set_xticklabels([])
  plt.tight_layout()
  if savefig:
    plt.savefig(savefig)
  else:
    plt.savefig()
  return

_style_ = "dark_background"
# _style_ = "ggplot"
# _style_ = None
_savefig_ = f"./Batman_logo_with_style_{_style_}.png"

X, Y = generate_functional_form_of_batman_logo()
plot_batman_logo(X, Y, plt_style=_style_, savefig=_savefig_)
