#!/usr/bin/python
import csv
 
#----------------------------------------------------------------------
def csv_reader(file_obj):
    """
    Read a csv file
    """
    reader = csv.reader(file_obj)
    for row in reader:
        i=1
        # print(" ".join(row))
 
#----------------------------------------------------------------------
def csv_dict_writer(path, fieldnames, data):
    """
    Writes a CSV file using DictWriter
    """
    with open(path, "wb") as out_file:
        writer = csv.DictWriter(out_file, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
# -------------------------------------------------------------------------
def put_csv_data_hash(file_obj):
     	"""
        Read a csv file
        """
        bidder_id_hash=dict()
        reader = csv.DictReader(file_obj)
        for row in reader:
            for key_id in row.iterkeys:
                string.clear()
                if(key_id!='bidder_id'):
                    string=','.join(row[key_id])
            bidder_id_hash[row['bidder_id']]=string#','.join(value) for key in row.iterkeys() if (row[key]~='bidder_id')
            # print (row['bidder_id'])
            #print(" ".join(row))

if __name__ == "__main__":
    csv_path = "train.csv"
    with open(csv_path, "rb") as f_obj:
        # csv_reader(f_obj)
        put_csv_data_hash(f_obj)