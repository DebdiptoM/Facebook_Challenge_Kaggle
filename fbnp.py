# Load the Pima Indians diabetes dataset from CSV URL
import numpy as np
# import urllib
# URL for the Pima Indians Diabetes dataset (UCI Machine Learning Repository)
# url = "http://goo.gl/j0Rvxq"
# download the file
# raw_data = urllib.urlopen(url)
csv_path = "train.csv"
bid_file="bid-small.csv"
# f_obj= open(csv_path, "rb")
# load the CSV file as a numpy matrix
# dataset = np.loadtxt(csv_path, delimiter=",")
train = np.genfromtxt(csv_path, delimiter=',',filling_values=0)
bids=np.genfromtxt(bid_file,delimiter=',',filling_values=0)
# print "Bids=",bids.shape,"\nHeader=",bids[1,:]
# separate the data from the target attributes
X = dataset[1]
y = dataset[2]