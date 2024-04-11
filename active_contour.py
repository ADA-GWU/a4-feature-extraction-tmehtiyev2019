import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage.color import rgb2gray
from skimage.filters import gaussian
from skimage.segmentation import active_contour
from matplotlib.widgets import LassoSelector
from matplotlib.path import Path

def load_and_preprocess_image(image_path):
    img = mpimg.imread(image_path)
    if img.ndim == 3:
        img = rgb2gray(img)
    return img

def initialize_plot(img):
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.imshow(img, cmap=plt.cm.gray)
    ax.set_title("Draw the initial contour ")
    return fig, ax

class InteractiveSnake:
    def __init__(self, ax, img):
        self.ax = ax
        self.img = img
        self.lasso = LassoSelector(ax, onselect=self.on_select)
        self.init = None
        self.snake = None

    def on_select(self, verts):
        self.init = np.array([[xy[1], xy[0]] for xy in verts])
        self.snake = active_contour(
            gaussian(self.img, sigma=3, preserve_range=False),
            self.init,
            alpha=0.015,
            beta=10,
            gamma=0.001
        )
        self.update_plot()

    def update_plot(self):
        self.ax.clear()
        self.ax.imshow(self.img, cmap=plt.cm.gray)
        if self.init is not None:
            self.ax.plot(self.init[:, 1], self.init[:, 0], '--r', lw=3, alpha=0.5)
        if self.snake is not None:
            self.ax.plot(self.snake[:, 1], self.snake[:, 0], '-b', lw=3)
        self.ax.set_xticks([]), self.ax.set_yticks([])
        self.ax.axis([0, self.img.shape[1], self.img.shape[0], 0])
        plt.draw()

if __name__ == '__main__':
    image_path = 'input_photos/active_contour/1.jpeg'
    img = load_and_preprocess_image(image_path)
    fig, ax = initialize_plot(img)
    interactive_snake = InteractiveSnake(ax, img)
    plt.show()
