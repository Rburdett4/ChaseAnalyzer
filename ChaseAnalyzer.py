#!/usr/bin/env python3
# Author = Ryan Burdett
# Contact = rburdett4@gmail.com
import csv


csvstring = "./Chase7917_Activity_20190504.CSV"        #in the future, this should be a GUI selection to make sure you can get any desired file.
with open(csvstring, "r") as readfile:
    reader = csv.reader(readfile)
    for x in reader:
        print(x)

