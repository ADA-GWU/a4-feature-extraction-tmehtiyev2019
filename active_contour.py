import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage.color import rgb2gray
from skimage.filters import gaussian
from skimage.segmentation import active_contour
from matplotlib.widgets import LassoSelector
from matplotlib.path import Path
import os

def load_and_preprocess_image(image_path):
    """ Load and convert the image to grayscale if it's colored. """
    img = mpimg.imread(image_path)
    return rgb2gray(img) if img.ndim == 3 else img

def setup_figure(image):
    """ Set up the matplotlib figure and axes. """
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.imshow(image, cmap='gray')
    ax.set_title("Draw the initial contour with left-click and push the enter button")
    ax.set_xticks([])
    ax.set_yticks([])
    return fig, ax

class InteractiveSnake:
    def __init__(self, image, ax):
        """ Initialize the interactive contour with image and axes. """
        self.image = image
        self.ax = ax
        self.selector = LassoSelector(ax, onselect=self.process_selection, button=1)
        self.initial_contour = None
        self.refined_contour = None

    def process_selection(self, vertices):
        """ Process the selection to create and update contours. """
        initial = np.array([[y, x] for x, y in vertices])
        refined = self.compute_active_contour(initial)
        self.update_plot(initial, refined)

    def compute_active_contour(self, initial):
        """ Compute the active contour using a Gaussian filter. """
        filtered_image = gaussian(self.image, sigma=3, preserve_range=False)
        return active_contour(filtered_image, initial, alpha=0.015, beta=10, gamma=0.001)

    def update_plot(self, initial, refined):
        """ Clear the plot and draw the initial and refined contours. """
        self.ax.clear()
        self.ax.imshow(self.image, cmap='gray')
        self.ax.plot(initial[:, 1], initial[:, 0], '--r', lw=3, alpha=0.5)
        self.ax.plot(refined[:, 1], refined[:, 0], '-r', lw=3)
        plt.draw()

if __name__ == '__main__':
    
    image_path = 'input_photos/active_contour/1.jpeg'
    image = load_and_preprocess_image(image_path)
    fig, ax = setup_figure(image)
    snake_interactive = InteractiveSnake(image, ax)

    plt.connect('key_press_event', lambda event: plt.close(fig) if event.key == 'enter' else None)
    plt.show()

    output_dir = 'output_images'  # Define the output directory
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # Create the output directory if it does not exist

    output_path = os.path.join(output_dir, f'active_contour_{os.path.basename(image_path)}')
    fig.savefig(output_path)  # Save the figure to the file path
    print(f"Result saved as {output_path}")

    # Display the result image after saving
    plt.figure(figsize=(7, 7))
    plt.imshow(mpimg.imread(output_path))
    plt.title("Final Contour Result")
    plt.axis('off')  # Hide axes
    plt.show()
