"""
auth spencer-maaaaan
desc takes master.csv and generates/writes tables to webpages for walkies
"""
import csv

from to_table import to_table
from make_index_arrays import make_index_arrays

# reading the current html file
with open("../index.html","r") as f:
    html=f.readlines()

# inserting new lines into html doc from csv file
with open("../master.csv", "r") as data:
    csv_reader=csv.reader(data)
    
    # putting fields and rows into lists
    fields=next(csv_reader)
    rows=[row for row in csv_reader]

# finding where the text should be inserted
insert_pos=html.index(" "*16+"<table>\n")+1
end_pos=html.index(" "*16+"</table>\n")

# clearing existing table
del html[insert_pos:end_pos]

# generating the index table
index_arrays=make_index_arrays(rows)

# converting index table into html table string
index_table=to_table(index_arrays)

# writing over new lines to old file
html.insert(insert_pos, index_table)

with open("../index.html","w") as f:
    f.writelines(html)
