import matplotlib.pyplot as plt
from matplotlib import patches

# Plotting bbox ffrom the .txt file output from yolo #

## Provide the location of the output .txt file ##
a_file = open("runs/detect/exp5/labels/DJI_0363.txt", "r")

# Stripping data from the txt file into a list #
list_of_lists = []
for line in a_file:
    stripped_line = line.strip()
    line_list = stripped_line.split()
    list_of_lists.append(line_list)
a_file.close()

# Conversion of str to int #
stage1 = []
for i in range(0, len(list_of_lists)):
    test_list = list(map(float, list_of_lists[i]))
    stage1.append(test_list)

# Denormalizing #
stage2 = []
mul = [1, 4056, 2280, 4056, 2280]  # [constant, image_width, image_height, image_width, image_height]
for x in stage1:
    c, xx, yy, w, h = x[0] * mul[0], x[1] * mul[1], x[2] * mul[2], x[3] * mul[3], x[4] * mul[4]
    stage2.append([c, xx, yy, w, h])

# Convert (x_center, y_center, width, height) --> (x_min, y_min, width, height) #
stage_final = []
for x in stage2:
    c, xx, yy, w, h = x[0] * 1, (x[1] - (x[3] / 2)), (x[2] - (x[4] / 2)), x[3] * 1, x[4] * 1
    stage_final.append([c, xx, yy, w, h])

fig = plt.figure()

# add axes to the image
ax = fig.add_axes([0, 0, 1, 1])

# read and plot the image

## Location of the input image which is sent to model's prediction ##
image = plt.imread('Meta_data/images/train/DJI_0363.JPG')
plt.imshow(image)

# iterating over the image for different objects
for x in stage_final:
    class_ = int(x[0])
    xmin = x[1]
    ymin = x[2]
    width = x[3]
    height = x[4]
    xmax = width + xmin
    ymax = height + ymin

    # assign different color to different classes of objects
    if class_ == 1:
        edgecolor = 'y'
        ax.annotate('khoa_neo', xy=(xmax - 40, ymin + 20))
    elif class_ == 2:
        edgecolor = 'b'
        ax.annotate('tru_su', xy=(xmax - 40, ymin + 20))
    elif class_ == 0:
        edgecolor = 'g'
        ax.annotate('ong_noi', xy=(xmax - 40, ymin + 20))

        # add bounding boxes to the image
    rect = patches.Rectangle((xmin, ymin), width, height, edgecolor=edgecolor, facecolor='none')

    ax.add_patch(rect)

plt.show()