import numpy as np
from PIL import Image


def image_to_vector(img, vector):

    # Get the width and height of the image
    width, height = img.size

    # Calculate the size of each grid square
    grid_size = (width // 10, height // 10)

    # Loop over the grid squares
    for j in range(10):
        for i in range(10):
            # Get the coordinates of the top-left corner of this grid square
            x = i * grid_size[0]
            y = j * grid_size[1]

            # Get the color of the pixels in this grid square
            pixels = img.crop((x, y, x + grid_size[0], y + grid_size[1])).getdata()

            # Check if any pixels in this grid square are black
            if 255 in pixels:
                vector.append(1)
            else:
                vector.append(-1)

    return vector


def vector_to_image(vector):
    # Reshape the vector into a 10x10 grid
    grid = np.reshape(vector, (10, 10))

    # Scale up the grid so that each square is 50x50 pixels
    scaled_grid = np.kron(grid, np.ones((100, 100)))

    # Create an image from the grid
    image = Image.fromarray(np.uint8(scaled_grid * 255))

    return image


def main():
    # for img in ["new.png"]:
    for img in ["b1.png", "b2.png", "b3.png", "l1.png", "l2.png", "l3.png", "m1.png", "m2.png", "m3.png"]:
        # Open an image file
        im = Image.open(img)

        # Convert the image to black and white
        im_bw = im.convert("1")

        # Invert the colors of the black and white image
        inverted_im_bw = im_bw.point(lambda x: 0 if x == 255 else 255)
        inverted_im_bw.show()

        # Initialize an empty vector
        vector = []

        if img.startswith("b"):
            filename = "b"
            vector.append(1)
        elif img.startswith("l"):
            filename = "l"
            vector.append(2)
        elif img.startswith("m"):
            filename = "m"
            vector.append(3)
        returned_vector = image_to_vector(inverted_im_bw, vector)

        # Convert the list to a string with parentheses
        my_string = '(' + ', '.join(str(i) for i in returned_vector) + ')'

        # Open a text file in write mode
        with open(filename, 'a+') as file:
            # Add a string to the file
            file.write(my_string + "\n")
        image = vector_to_image(returned_vector[1:])
        image.show()

    # rotate left
    for img in ["b1.png", "b2.png", "b3.png", "l1.png", "l2.png", "l3.png", "m1.png", "m2.png", "m3.png"]:
        # Open an image file
        im = Image.open(img)

        # Convert the image to black and white
        im_bw = im.convert("1")

        # Invert the colors of the black and white image
        inverted_im_bw = im_bw.point(lambda x: 0 if x == 255 else 255)

        # Rotate the image
        left_rotated_image = inverted_im_bw.rotate(15, expand=True)
        left_rotated_image.show()

        # Initialize an empty vector
        vector = []

        if img.startswith("b"):
            filename = "bLeft"
            vector.append(1)
        elif img.startswith("l"):
            filename = "lLeft"
            vector.append(2)
        elif img.startswith("m"):
            filename = "mLeft"
            vector.append(3)
        returned_vector = image_to_vector(left_rotated_image, vector)

        # Convert the list to a string with parentheses
        my_string = '(' + ', '.join(str(i) for i in returned_vector) + ')'

        # Open a text file in write mode
        with open(filename, 'a+') as file:
            # Add a string to the file
            file.write(my_string + "\n")
        image = vector_to_image(returned_vector[1:])
        image.show()

    # rotate right
    for img in ["b1.png", "b2.png", "b3.png", "l1.png", "l2.png", "l3.png", "m1.png", "m2.png", "m3.png"]:
        # Open an image file
        im = Image.open(img)

        # Convert the image to black and white
        im_bw = im.convert("1")

        # Invert the colors of the black and white image
        inverted_im_bw = im_bw.point(lambda x: 0 if x == 255 else 255)

        # Rotate the image
        right_rotated_image = inverted_im_bw.rotate(-15, expand=True)
        right_rotated_image.show()

        # Initialize an empty vector
        vector = []

        if img.startswith("b"):
            filename = "bRight"
            vector.append(1)
        elif img.startswith("l"):
            filename = "lRight"
            vector.append(2)
        elif img.startswith("m"):
            filename = "mRight"
            vector.append(3)
        returned_vector = image_to_vector(right_rotated_image, vector)

        # Convert the list to a string with parentheses
        my_string = '(' + ', '.join(str(i) for i in returned_vector) + ')'

        # Open a text file in write mode
        with open(filename, 'a+') as file:
            # Add a string to the file
            file.write(my_string + "\n")
        image = vector_to_image(returned_vector[1:])
        image.show()


if __name__ == "__main__":
    main()
