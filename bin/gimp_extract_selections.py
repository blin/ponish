# This code works on GIMP 2.10 via python-fu console
# Populate `names` with ordered list of file names to get a
# outpath,x,y,width,height
# list suitable for use with imagemagick.
# Note that GIMP 2.10 python is Python 2.7

infile = "051.png"
names = ["part-2/passage-4-line-{:02}.png".format(i) for i in range(1,6)]


def print_selection_channels(image):
    for i, ch in enumerate(reversed(image.channels)):
        pdb.gimp_image_select_item(image, CHANNEL_OP_REPLACE, ch)
        _, x1, y1, x2, y2 = pdb.gimp_selection_bounds(image)
        width = x2 - x1
        height = y2 - y1
        print("{},{},{},{},{},{}".format(infile, names[i], x1, y1, width, height))


print_selection_channels(gimp.image_list()[0])
