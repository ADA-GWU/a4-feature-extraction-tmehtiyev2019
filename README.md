# Edge Analysis and Active Contour

## Overview
This repository contains Jupyter notebooks for digital image processing with a focus on:

1. Edge analysis, including edge detection, corner detection, and line and circle detection.
2. Active Contour (snakes) algorithm for detecting the contours of objects.
3. Interest Point detection using ORB to locate the same object in different images.

The notebooks are designed to be self-contained, with all necessary interpretations and visual representations included. To reproduce the results, please follow the steps outlined below.

## Prerequisites
- Google Colab account
- Google Drive with sufficient storage space

## Installation

1. **Clone the Repository:**
   Clone this repository to your local machine using `git clone https://github.com/ADA-GWU/a4-feature-extraction-tmehtiyev2019.git`.
   
2. **Upload to Google Drive:**
   Upload the cloned repository folder to your Google Drive in the directory `/content/drive/My Drive/`.

## Usage

1. **Open the Notebook:**
   Navigate to Google Colab and open the `feature_extraction.ipynb` file from the folder you uploaded to Google Drive.

2. **Run the Notebook:**
   Execute the cells in the notebook. The first cell will mount your Google Drive, and you'll need to authorize access to the folder where the repository is located.

   


## Project Repository Structure

This repository is organized into several directories for input and output data, as well as implementation code. Below is a breakdown of the structure and contents.

### Input Pictures

`/input-pictures/` - This directory contains all the input images used for processing.

#### MRI

`/input-pictures/MRI/` - Includes subdirectories named after patient numbers, each containing four categories of DICOM files for MRI scans:
- `FLAIR` - Fluid-attenuated inversion recovery images
- `T1w` - T1-weighted images
- `T1wCE` - T1-weighted contrast-enhanced images
- `T2w` - T2-weighted images

#### Noisy Images

`/input-pictures/noisy/` - Contains two subcategories with input images for noise reduction:
- `chemical` - Images with pepper noise
- `speckle` - Images with speckle noise

### Output Pictures

`/output-pictures/` - Follows the same structure as `input-pictures` with corresponding output images after processing. The outputs are categorized in the same manner, reflecting the changes and enhancements made.

### Implementation Code

`digital_image_pre_processing.ipynb` - This Jupyter notebook contains all the implementation code along with interpretations and visualizations. Refer to this file for a comprehensive explanation of the processing techniques used and the rationale behind them.

For detailed visualizations and explanations of the results and outputs for each data point, please refer to the `digital_image_pre_processing.ipynb` file. It contains all necessary interpretations and visual representations to understand the processing steps and results.



