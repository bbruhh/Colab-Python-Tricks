# Imports
import os
import keras
import numpy as np
from matplotlib.image import imread
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
import csv
from PIL import Image
import time


# Function to decide if a stirng is a number with 2 digits
def IsLabel(input_text):
    dominos = input_text.split(' ')
    for domino in dominos:
        # if number enter does not have 2 digits
        if len(domino) != 2:
            print 'Wrong pips count. Need 2 digit numbers. Try again!'
            return False
        try:
            int(domino)
            continue
        except ValueError:
            print 'Invalid number/s! Try again!'
            return False
    return True

# need to import matplotlib
# path CSV file

plot_size = 15    # I think 20 is too big. you can change it to what is more comfortable

print 'Labeing started...\n'

path = '../labeled_imaged.csv'      # path of CSV files where store labeles

# current path get files list
im_names =  os.listdir('./')

# array of already labeled images
im_labeled = []

# append
with open(path, "a+w") as f:
    writer = csv.writer(f)

    # create array of already labeled images
    readCSV = csv.reader(f)
    for row in readCSV:
        im_labeled.append(row[0])

    print '\nSo far you labeled: %s images, out of %s\nKeep up the good work!\n'%(len(im_labeled), len(im_names))

    # look in each image in directory
    for im in im_names:
        # avoid labeling already labeled
        if im in im_labeled:
            continue
        # read image to array
        image = imread(im)

        # plot the image
        plt.figure(figsize=(plot_size, plot_size))
        graph = plt.imshow(image)

        plt.grid(False)
        plt.show()
        time.sleep(2)

        text = None  # what ever the user enters

        while(True):
            # get user input
            text = raw_input('%s has: '%im)
            # if no anotaiton was enter, keep asking user for it
            if text == '':
                continue
            # if need to break
            if text == 'q':
                break
            # white space split and check if there each 2 digit numbers
            if IsLabel(text):
                writer.writerows([[im , text]])
                break
            if text == 'q':
                print '\nTerminating...'
                break

print '\nProgram Finished!'
