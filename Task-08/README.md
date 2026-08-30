# Operation Pixel Merge

## Overview

Operation Pixel Merge is an image-processing task where a hidden image is divided into multiple layers. Each layer contains a small point, and the objective is to detect these points, determine their positions and colours, and connect them in the correct layer order to reconstruct the final image.

## Approach

The solution was implemented using Python with OpenCV and Pillow.

The program:

1. Loads all PNG files from the `assets` folder.
2. Sorts the layers according to their layer numbers.
3. Reads each image using OpenCV.
4. Detects the non-white pixels in each layer.
5. Calculates the centre position of the detected point.
6. Detects the colour of the point.
7. Converts OpenCV's BGR colour format to Pillow's RGB format.
8. Connects each point to the previous point in layer order.
9. Handles completely white layers as breaks between lines.
10. Saves the reconstructed image as `pixel_merge_output.png`.

## Technologies Used

- Python
- OpenCV (`cv2`)
- Pillow (`PIL`)
- NumPy
- Glob
- Regular Expressions

## Important Concepts Learned

1. Image representation as arrays
Learned that an image is represented as a NumPy array, where each pixel has a position and colour values.

2. Image dimensions and coordinates
Understood the difference between x and y coordinates:
x → horizontal position (columns)
y → vertical position (rows)
In an image array, pixels are accessed as: image[y, x]

3. Pixel detection using masks
Learned how to create a mask to identify non-white pixels and use it to locate the points in each layer.

4. Finding the centre of a group of pixels
Learned how to calculate the centre/average position of multiple detected pixels so that the small dot can be represented by a single (x, y) point.

5. Contours and moments
Learned how OpenCV contours can represent detected objects and how image moments can be used to calculate an object's centre.

6. BGR vs RGB colour formats
One of the most important concepts from this task:
OpenCV uses BGR
Pillow uses RGB
For example:
BGR → (7, 193, 255)
RGB → (255, 193, 7)

6. Handling coloured and grayscale pixels
Learned that detecting only grayscale/non-white pixels can miss coloured information. The solution therefore needed separate handling for coloured pixels.

7. Numerical sorting of filenames
Learned that normal alphabetical sorting doesn't correctly order files such as Layer 9.png and Layer 10.png. A regular expression was used to extract the layer number and sort it numerically.

8. Handling empty/white images
Learned that a completely white layer doesn't necessarily mean an error. It can represent a break between parts of the drawing, so the previous point needs to be reset.

9. Debugging array and OpenCV errors
Learned how errors such as IndexError and OpenCV errors can occur because of incorrect array dimensions, indexing, or attempting to process an image that wasn't loaded correctly.

10. Connecting points to reconstruct an image
Learned how individual coordinates from different layers can be connected sequentially to reconstruct the hidden image.

11. Debugging by testing individual layers
Instead of repeatedly changing the entire program, we learned to test individual layers—such as Layer 51—to verify whether the image loaded correctly and whether its colour values were being detected properly.

## Challenges Faced
During development, several issues were encountered:
Incorrect array indexing when extracting pixel coordinates.
Confusion between x and y coordinates.
OpenCV's BGR format versus Pillow's RGB format.
Completely white layers being mistaken for missing points.
Coloured pixels being incorrectly detected as grayscale pixels.
Some layers being skipped because they contained no detectable non-white pixels.
A nested Git repository inside the task folder causing problems while pushing the project.
These issues were solved by testing individual layers, checking pixel values, separating coloured-pixel detection from grayscale detection, and carefully handling the Git repository structure.

## What I Learned
Through this task, I learned the basics of image processing using Python, OpenCV, and Pillow. I learned how images are represented as NumPy arrays and how to work with image dimensions, pixels, and (x, y) coordinates. I understood how masks, contours, and image moments can be used to detect objects and find their centre points.
I also learned the difference between BGR and RGB colour formats, which was especially important when handling the coloured layers. I learned how to inspect individual pixel values and debug problems by testing individual layers instead of changing the entire program blindly.
Working with the layers taught me how to use glob to find files, regular expressions to extract layer numbers, and numerical sorting to process the layers in the correct order. I also learned how to handle empty or white layers and how to connect detected points to reconstruct an image.
Most importantly, this task improved my debugging and problem-solving skills. I encountered issues such as incorrect array indexing, undefined variables, OpenCV errors, incorrect colour detection, and file-path problems. By investigating each error step by step, I learned how to understand error messages, inspect data, test assumptions, and gradually improve the program until the final image was successfully reconstructed.
I also gained practical experience with Git, including staging specific files, committing changes, handling nested repositories, rebasing with remote changes, using stash, and pushing the completed task to GitHub.
Overall, this task taught me that solving a programming problem is not just about writing code—it is also about understanding the data, testing assumptions, reading errors, and debugging systematically
