#!/usr/bin/env python3
# Author = Ryan Burdett
# Contact = rburdett4@gmail.com
import csv


class ChaseAnalyzer:
    def __init__:
        # create a hash table for the grocers
        # hash the fast food
        # hash the fuel
        # bills
        # rent
        # utilities
        # paypal
        #



csvstring = "./Chase7917_Activity_20190504.CSV"        #in the future, this should be a GUI selection to make sure you can get any desired file.
firstline = True
with open(csvstring, "r") as readfile:
    reader = csv.reader(readfile)
    for line in reader:
        if firstline:
            firstline = False
        else:
            if float(line[3]) < 0:
                print(line[3] + "  " +  line[2].split("    ")[0])