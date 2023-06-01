import pandas as pd
import json
import numpy as np
import os

an = json.load(open('')) # link to json file from COCO official website
an = an['annotations']  # annotations hold category information

# create a new data frame to hold information on images and corresponding categories 
col = ['image-id', 'category-id']
data = pd.DataFrame(columns=col) 

for i in range(len(an)):
    id = an[i]['image_id']
    imgname = str(id).zfill(12)   # pad with zeros to match image name in COCO folder
    data = data.append( {'image-id' : imgname,
                     'category-id' : an[i]['category-id']}, ignore_index=True)  
                      #add a row to a data frame
    
# Multiple instances of the same object category in an image are stored as separate rows
# deleting them
data = data.drop_duplicates(data.columns)

# Cleaning the data frame content
img_names = np.unique(data['image-id']) # get set of image names

for i in img_names:
    # If the image contains an element under the person category (category #1)
    if len(data[(data['image-id'] == str(i)) & (data['category-id'] == 1)]) != 0:
        # Remove rows that indicate the presence of other category elements in the image 
        indices = data[(data['image-id'] == str(i)) & (data['category-id'] != 1)].index
        if(len(indices) != 0):
            data = data.drop(index=indices)

# separate into 2 dataframes
data_person = data[data['category-id'] == 1]
data_not = data[data['category-id'] != 1]

# set category_id = 0 to indicate not_person
data_not['category-id'] = 0

# there may be several not_person elements leading to redundant rows, eliminating them
data_not = data_not.drop_duplicates()

path = ''   # path to store the categorized image files
curpath = ''    # path to COCO image files

# make appropriate folders
os.mkdir(path + 'vww')
os.mkdir(path + 'vww/person')
os.mkdir(path + 'vww/notperson')

pt = path + 'vww/person/'
npt = path + 'vww/notperson/'

datap = list(data_person['image-id'])
datanp = list(data_not['image-id'])

n = 300 # number of images to pick from each category

for i in range(n):
   os.rename(curpath + str(dfp[i]).zfill(12) + '.jpg', 
													pt + str(dfp[i]).zfill(12) + '.jpg')
	 os.rename(curpath + str(dfnp[i]).zfill(12) + '.jpg', 
													npt + str(dfnp[i]).zfill(12) + '.jpg')