import os
import re

import numpy as np

import settings


def export_image(image, path):
    """
    Exports the desired 4D image into the specified file path.
    :param image: A 4D numpy array containing the binary image.
    :param path: The file's path. A file with the same path will be overwritten.
    :return: Returns nothing
    """
    with open(path, mode="w") as f:
        """
        The first line of our file will inform about the array's shape
        so it could be read from our read method.
        """
        f.write("# Array shape: {}\n".format(image.shape))

        """
        As there is no standard way to export 4D data we will slice
        the image in 2D slices so it can be human readable.
        This is why the first line must indicate the array's shape, because we
        lose that information during the exportation.
        """
        for slice_3d in image:
            for slice_2d in slice_3d:
                # Store the slice into the file. Numbers will be left aligned.
                np.savetxt(f, slice_2d, fmt="%-d")

                # Add a new line break in order to ease readability
                f.write("# New slice \n")


def generate_random_img(path=None):
    """
    Generates a random 5x5x5x5 image and exports it into the desired file.
    :param path: The filepath. A file with the same path will be overwritten.
                 If path is None a file will be generated in the root directory.
    :return: A numpy 4D array with the generated image.
    """
    if path is None:
        path = os.path.join(settings.BASE_DIR, "4d_img.txt")

    """
    4D array generation. We create a 5x5x5x5 binary image, we also
    use the less memory hungry version of the integer type.
    """
    img = np.random.randint(2, size=(5, 5, 5, 5), dtype=np.int8)
    export_image(img, path)
    return img


def load_image(path):
    """
    Loads an image from the specified path. The file must contain information
    about the array shape in its first line, otherwise the file will not be
    read.
    :param path: The file's path containing the image's information.
    :return: A numpy 4D array with the specified shape.
    """
    shape = None

    """
    We define a regular expression in order to extract the shape from the
    first line. This will work with any of the following examples:
    # Array shape: (3, 23, 1, 2)
    # Shape: (2, 2, 3, 2)
    """
    shape_pattern = "^.*\((\d{1,}),\s(\d{1,}),\s(\d{1,}),\s(\d{1,})\)"

    # Pattern compilation
    regex = re.compile(shape_pattern)

    with open(path, mode="r") as f:
        first_line = f.readline()
        matches = regex.findall(first_line)
        assert len(matches) == 1, "File does not specify the array shape"

        # If our regex produced a match then we can retrieve the shape
        if len(matches) == 1:
            """
            As each number is contained in a different capturing group
            we have to go through the first match tuple and convert the
            numbers from strings to integers.
            """
            shape = [int(matches[0][_]) for _ in range(4)]

    """
    Load the image from the path. This will return a 2D array, we must
    recover its original shape.
    """
    image = np.loadtxt(path, dtype=np.int8)

    # Apply the shape
    image = image.reshape(shape)

    return image
