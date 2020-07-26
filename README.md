# husker
cropping dark headers and footers from images

### Use Case
This algorithm was developed for a particular use name, namely lots of images that are framed at top and bottom by blocks of darkness.  The husker will crop off these blocks so that the central image remains unframed.  

### Basic Use
Given an image directory path, the husker will crop all images and send them to an outbound directory:

```husker.husk('/Users/moebiusthrip/Desktop/Images')```

will place a cropped copy of every image in the /Images folder into /Images_cropped.

### Basic Algorithm
The idea is to crop off regions that are nearly solid dark from the top and bottom of the image.  The husker looks from the top of the image to the middle of the image and finds the lowest block of all dark rows it can find.  Then it does the same for the bottom of the image.  The assumption is made that the headers are of roughly equal size, and this was sufficient for my use case.

### Parameters
The other parameters and defaults are as follows:

```husker.husk(directory, outgoing='/Specific/Directory')```

will place the new images into a directory at this specific path, and will create the directory if it does not yet exist.  The default directory is the incoming directory name tagged with '_cropped'.

```husker.husk(directory, darkness=200)```

sets the highest intensity considered dark at 200, based on the RGB system.  Pitch black is 0, and pure white is 765 (255 for red + 255 for green + 255 for blue).  The impulse was to set this around 50 or so because I was expecting more or less pitch black headings, but I found I needed to raise this to 200 (dark brown) for my use case.  Setting this too high risks actual content being mistaken for the headings to crop.

```husker.husk(directory, block=40)```

looks for a block of 40 consecutive all dark rows before it will crop it from the image.  Lower values risk that a thin dark horizontal line in the content itself will cause it to crop there instead.

```husker.husk(directory, thoroughness=100)```

checks 100 random points along a row before determining it is all dark.  All pixels could be checked, but it is much quicker to only check a few.  The assumption is that a row of desired content will likely have at least one light pixel amongst 100.

```husker.husk(directory, extensions=('.jpg', '.png')```

only attempts the process on a file ending with .jpg or .png.  Otherwise it skips.

### Thanks!

