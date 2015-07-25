#!/usr/bin/python
import csv
train_file='train.csv'
bid_file='bid-small.csv'
output_file='hash.csv'
def hash_from_file(input_file):
    RH=open(input_file,'r')
    lines=csv.DictReader(RH)
    RH.close
    hash_val=dict()
    for rows in lines:
        current_bidder_id=rows['bidder_id']
        str_val=""
        for keys in rows:
            if (keys!='bidder_id'):
                str_val=str_val,',',rows[keys]
        hash_val[current_bidder_id]=str_val
    return hash_val

def merge_hash(h1,h2):
    return_hash=dict()
    for k2 in h2:
        return_hash[k2]=k2,",",h2.get(k2,"na"),",",h1.get(k2,"na")
        # strv=strv,",",h1[k2]
    return return_hash
def write_file(whash,fieldnames,output_file):
    csvfile=open(output_file, 'w')
    # fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    strv=""
    for wkey in whash:
        for names in fieldnames:
            writer.writerow(["names:wkey whash[wkey]])
    csvfile.close

# small_hash=hash_from_file(bid_file)
# big_hash=hash_from_file(train_file)
fh=merge_hash(hash_from_file(train_file),hash_from_file(bid_file))
write_file(fh,fh.keys(),output_file)
# print small_hash["7d3c649e6dfcc7773703b5ce789c1202wehdy"]
# for k in small_hash:
#     print "Key=%s\t%s\n",k,small_hash[k]

# with open(train, mode='r') as infile:

#     train_dataset = csv.DictReader(train_file)
#     infile.close()
# with open(input_file,mode='r') as infile:
#     bid_dataset=csv.DictReader(infile)
#     infile.close()
# bidder_hash=dict()
# feature_hash=dict()
# # str2='abc'
# for bidder_rows in train_dataset:
#     str2=""
#     print bidder_rows.has_keys('bidder_id')
#     for header in bidder_rows:
#         if(header!='bidder_id'):
#             str2=str2,",",bidder_rows[header]
#     # string1=bidder_rows['payment_account'],',',bidder_rows['address'],",",bidder_rows['outcome']

#     bidder_hash[bidder_rows['bidder_id']]=str2
#     #bid_id,bidder_id,auction,merchandise,device,time,country,ip,url
# # bidder_id,payment_account,address,outcome
# # for bid_rows in bid_dataset:
# #     bid_rows['bidder_id']

#  #    with open(output_file, mode='w') as outfile:
#  #   	 writer = csv.writer(out_file)
#  #    for rows in reader:
#  #        k = rows['bid_id']
# 	# v.clear()
#  #    	for key in rows:
#  #            if (key != 'bidder_id'):
#  #        	   v = join (','.([v key]))    
#  #        mydict = {k:v for k, v in rows}
#  #    print(mydict)

