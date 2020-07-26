# import reload
from importlib import reload

# import os
import os

# import images
from PIL import Image

# import numpy
import numpy

# import choice
from random import choice


# crop function
def husk(incoming, outgoing=None, darkness=200, block=40, thoroughness=100, extensions=('.jpg', '.png')):
    """Crop dark space from top and bottom of an image.

    Arguments:
        incoming: str, directory for images to be cropped
        outgoing: str, directory for cropped images
        darkness=200: int, maximuum sum of RGB intensities considered dark enough
        block=40: number of consecutive all dark rows
        thoroughness=100: int, number of random pixels to test
        extensions=('.jpg', '.png'): tuple of extension strings that will be tried

    Returns:
        None
    """

    # set default outgoing
    if not outgoing:

        # add cropped
        outgoing = incoming + '_cropped'

    # try to find outgoing directory
    try:

        # to find outgoing directory
        contents = os.listdir(outgoing)

    # otherwise
    except FileNotFoundError:

        # make directory

        print('better make it then')

        os.mkdir(outgoing)

    # get paths
    paths = [incoming + '/' + path for path in os.listdir(incoming)]

    # crop each path
    for path in paths:

        # check for extension
        if any([extension in path for extension in extensions]):

            # status
            print('cropping {}...'.format(path))

            # get image and change to array
            image = Image.open(path)
            array = numpy.array(image)

            # get height
            height = len(array)

            # get indices of black lines
            indices = []
            array = array.tolist()
            for index, row in enumerate(array):

                # check for black line
                choices = [choice(row) for _ in range(thoroughness)]
                if all([sum(pixel[:3]) < darkness for pixel in choices]):

                    # add to indices
                    indices.append(index)

            # get top row
            tops = [index for index in indices if index < height / 2]
            tops = [index for index in tops if all([index - n in indices for n in range(block)])] + [0]
            top = max(tops)

            # get bottom row
            bottoms = [index for index in indices if index > height / 2]
            bottoms = [index for index in bottoms if all([index + n in indices for n in range(block)])] + [height]
            bottom = min(bottoms)

            # crop
            cropped = Image.fromarray(numpy.array(array[top:bottom], dtype='uint8'))

            # deposit
            deposit = path.replace(incoming, outgoing)
            cropped.save(deposit)

        # otherwise
        else:

            # ignore
            print('skipped {}.'.format(path))

    return None
