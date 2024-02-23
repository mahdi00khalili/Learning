import random
from math import sqrt
from PIL import Image, ImageDraw

# Define the dimensions of the image
width = 800
height = 800

# Create a new image with white background
image = Image.new("RGB", (width, height), "white")

# Create a drawing object
draw = ImageDraw.Draw(image)


# Calculate the coordinates of the center
center_x = width // 2
center_y = height // 2

# Define the size of the points
# radius
point_size = 2


# Define the bounding box of the ellipse (left, top, right, bottom)
bbox = (
    center_x - point_size,
    center_y - point_size,
    center_x + point_size,
    center_y + point_size,
)

# Define point one as a red point in the center
draw.ellipse(bbox, fill="red")


# distance calculation
def dist(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# functions to handle random finder~~~~~~~~~


# find the random point
def find_random_x_y(x, y):
    if y == center_y and x > center_x:
        current_point_x = random.randint(center_x, width)
        current_point_y = random.randint(0, height)

    elif y > center_y and x > center_x:
        current_point_x = random.randint(center_x, width)
        current_point_y = random.randint(center_y, height)

    elif y > center_y and x == center_x:
        current_point_x = random.randint(0, width)
        current_point_y = random.randint(center_y, height)

    elif y > center_y and x < center_x:
        current_point_x = random.randint(0, center_x)
        current_point_y = random.randint(center_y, height)

    elif y == center_y and x < center_x:
        current_point_x = random.randint(0, center_x)
        current_point_y = random.randint(0, height)

    elif y < center_y and x < center_x:
        current_point_x = random.randint(0, center_x)
        current_point_y = random.randint(0, center_y)

    elif y < center_y and x == center_x:
        current_point_x = random.randint(0, width)
        current_point_y = random.randint(0, center_y)
    else:
        current_point_x = random.randint(center_x, width)
        current_point_y = random.randint(0, center_y)

    return (current_point_x, current_point_y)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# draw line between lines
def draw_line_between_points(x1, y1, x2, y2):
    line_color = "blue"
    line_width = 1

    # Draw a line on the image
    draw = ImageDraw.Draw(image)
    draw.line([(x1, y1), (x2, y2)], fill=line_color, width=line_width)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


for line in range(50):
    loop_counter = 1

    while True:

        # define a temp  distance
        if loop_counter == 1:  # for first loop

            prev_distance_from_center = 0
            current_distance_from_center = 1

            # the first point is the center point
            current_point_x = random.randint(0, width)
            current_point_y = random.randint(0, height)

            draw_line_between_points(
                center_x, center_y, current_point_x, current_point_y
            )

            # define a temp  point to save the previous point
            prev_point_x = current_point_x
            prev_point_y = current_point_y

        # find the random point
        (current_point_x, current_point_y) = find_random_x_y(prev_point_x, prev_point_y)

        current_distance_from_center = dist(
            current_point_x, current_point_y, center_x, center_y
        )

        if current_distance_from_center > prev_distance_from_center:

            if (
                current_point_x == width
                or current_point_y == height
                or current_point_x == 0
                or current_point_y == 0
            ):  # stop the operation if the point reaches the edge of the image

                # Define the bounding box of the ellipse (left, top, right, bottom)
                bbox = (
                    current_point_x - point_size,
                    current_point_y - point_size,
                    current_point_x + point_size,
                    current_point_y + point_size,
                )

                # Define point one as a red point in the point
                draw.ellipse(bbox, fill="red")
                draw_line_between_points(
                    prev_point_x, prev_point_y, current_point_x, current_point_y
                )
                print(
                    "......................................................................."
                )
                print("\n")
                print(f"current_point: ({current_point_x},{current_point_y})")
                print(f"prev_point: ({prev_point_x},{prev_point_y})")
                print(f"current distance from center: {current_distance_from_center}")
                print(f"prev distance from center: {prev_distance_from_center}")

                break

            # Define the bounding box of the ellipse (left, top, right, bottom)
            bbox = (
                current_point_x - point_size,
                current_point_y - point_size,
                current_point_x + point_size,
                current_point_y + point_size,
            )

            # Define point one as a red point in the point
            draw.ellipse(bbox, fill="red")
            draw_line_between_points(
                prev_point_x, prev_point_y, current_point_x, current_point_y
            )

            # update the temp  distances
            prev_distance_from_center = current_distance_from_center

            # update the temp  prev point
            prev_point_x = current_point_x
            prev_point_y = current_point_y

            loop_counter += 1

        else:
            continue

    # Save the image
    image.save("page_with_points_and_line.png")

# Display the image
image.show()
