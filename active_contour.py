import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage.color import rgb2gray
from skimage.filters import gaussian
from skimage.segmentation import active_contour
from matplotlib.widgets import LassoSelector
from matplotlib.path import Path


img = mpimg.imread('input_photos/interest_points/4.jpeg') 
if img.ndim == 3:
    img = rgb2gray(img) 
fig, ax = plt.subplots(figsize=(7, 7))
ax.imshow(img, cmap=plt.cm.gray)
ax.set_title("Draw the initial snake contour using Lasso tool")

class SelectFromCollection:
    def __init__(self, ax, collection):
        self.canvas = ax.figure.canvas
        self.collection = collection
        self.xys = collection.get_offsets()
        self.Npts = len(self.xys)
        self.fc = collection.get_facecolors()
        if len(self.fc) == 0:
            raise ValueError('Collection must have a facecolor')
        elif len(self.fc) == 1:
            self.fc = np.tile(self.fc, (self.Npts, 1))
        self.lasso = LassoSelector(ax, onselect=self.onselect)
        self.ind = []

    def onselect(self, verts):
        path = Path(verts)
        self.ind = np.nonzero([path.contains_point(xy) for xy in self.xys])[0]
        self.fc[:, -1] = 0.3 
        self.fc[self.ind, -1] = 1
        self.collection.set_facecolors(self.fc)
        self.canvas.draw_idle()
        init = np.array([[xy[1], xy[0]] for xy in verts]) 
        snake = active_contour(
            gaussian(img, sigma=3, preserve_range=False),
            init,
            alpha=0.015,
            beta=10,
            gamma=0.001
        )
        ax.clear()
        ax.imshow(img, cmap=plt.cm.gray)
        ax.plot(init[:, 1], init[:, 0], '--r', lw=3, alpha=0.5)
        ax.plot(snake[:, 1], snake[:, 0], '-b', lw=3)
        ax.set_xticks([]), ax.set_yticks([])
        ax.axis([0, img.shape[1], img.shape[0], 0])
        plt.draw()
pts = ax.scatter([], [])
selector = SelectFromCollection(ax, pts)
plt.show()