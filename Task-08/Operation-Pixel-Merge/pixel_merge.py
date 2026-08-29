import cv2
import glob
import re
import numpy as np
from PIL import Image, ImageDraw

files = glob.glob("assets/*.png")

files.sort(
    key=lambda f: int(re.search(r"Layer (\d+)", f).group(1))
)

output = Image.new("RGB", (512, 512), "white")
draw = ImageDraw.Draw(output)

previous_point = None
previous_color = None

for file in files:

    image = cv2.imread(file)

    if image is None:
        print("Could not load:", file)
        continue

    # Find coloured pixels
    coloured_mask = (
        (image[:, :, 0] != image[:, :, 1]) |
        (image[:, :, 1] != image[:, :, 2]) |
        (image[:, :, 0] != image[:, :, 2])
    )

    coloured_pixels = image[coloured_mask]

    # ----------------------------------------
    # COLOURED DOT
    # ----------------------------------------

    if len(coloured_pixels) > 0:

        # Coordinates of coloured pixels
        ys, xs = np.where(coloured_mask)

        x = int(xs.mean())
        y = int(ys.mean())

        # Average colour of ONLY coloured pixels
        b, g, r = coloured_pixels.mean(axis=0)

        current_color = (
            int(r),
            int(g),
            int(b)
        )

    # ----------------------------------------
    # GRAYSCALE DOT
    # ----------------------------------------

    else:

        mask = cv2.inRange(
            image,
            (0, 0, 0),
            (254, 254, 254)
        )

        points = cv2.findNonZero(mask)

        # Completely white image
        if points is None:
            previous_point = None
            previous_color = None
            continue

        points = points.reshape(-1, 2)

        xs = points[:, 0]
        ys = points[:, 1]

        x = int(xs.mean())
        y = int(ys.mean())

        # Get grayscale colour
        b, g, r = image[y, x]

        current_color = (
            int(r),
            int(g),
            int(b)
        )

    current_point = (x, y)

    print(
        file,
        "Point:",
        current_point,
        "Color:",
        current_color
    )

    # Connect to previous dot
    if previous_point is not None:

        draw.line(
            [previous_point, current_point],
            fill=previous_color,
            width=5
        )

    previous_point = current_point
    previous_color = current_color


output.save("pixel_merge_output.png")

print("Done!")
print("Output saved as pixel_merge_output.png")