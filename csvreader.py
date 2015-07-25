#!/usr/bin/python
import csv 
import sys

def csv_dict_reader(file_obj, keyindex):
    hashf=dict()
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        hashf[line[keyindex]]= line#",".join(line)
    return hashf
label_bidder_id=csv_dict_reader(open("train.csv","rb"),0)
writer=csv.writer(open("fb-data","w"))
reader_bids=csv_dict_reader(open("bid-small.csv","rb"),1)
for bid_id in reader_bids:
	if (label_bidder_id.has_key(bid_id)):
		reader_bids[bid_id]=reader_bids[bid_id].extend(label_bidder_id[bid_id][2:9])
writer.writerows(reader_bids)



# print label_bidder_id