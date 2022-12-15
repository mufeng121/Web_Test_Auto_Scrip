# SOURCE FILE:    Labelling.py
# PROGRAM:        JuiceShop automating attack application -- Plugin
# FUNCTIONS:      Labelling each pcap traffic with the attack name recorded by logging
#                
#                  
# DATE:           Dec 8, 2022
# REVISIONS:      N/A
# PROGRAMMER:     River Chen
#
# NOTES
# We need to finish all the attacks and have pcap collected first
# Then have the pcap CSV and logging file 'test_logging_info.log' ready
# Then run this function to do the labelling
# The labeled file will be write to a new CSV file named labeled.csv
# Please modify pcap_file_name with the pcap that need to be labeled
#--------------------------------------------------------------------------------------
import datetime
import logging
from typing import List, Iterable
import csv
import pandas as pd


#Need to modify the pcap file's name to the pcap that we wanted to label
pcap_file_name = "./pcap_2022-12-11_UTC.csv"

#--------------------------------------------------------------------------------------
#FUNCTION read
#ARGUMENTS: fp: str --> file name
#RETURNS: array of strings  --> will be used for extracting labelling features
#Description: This function is used to return two lines when reading files
#               Because Python only provides function for reading line by line 
#               We need to read two lines at a time to get the start time and end time for one attack
#             
#NOTES:
# None
#--------------------------------------------------------------------------------------
def read(fp: str) -> Iterable[List[str]]:
    i = 0
    # a buffer to cache lines
    lines = []

    with open(fp) as f:
        for line in f:
            i += 1
            # append a line
            lines.append(line.strip())

            if i >= 2:
                yield lines

                # reset buffer
                i = 0
                lines.clear()

    # remaining lines
    if i > 0:
        yield lines


# Read pcap.csv file and format time
df = pd.read_csv(pcap_file_name, index_col=False)
df['Time'] = pd.to_datetime(df['Time'])

# Read two lines from logging file
lines_gen = read("./test_logging_info.log")
for lines in lines_gen:

    # Get start time, end time, attack name from two lines of log
    # Read first line as an array
    start = lines[0].split('#')
    # Start time is the first element in the array
    start_time = pd.to_datetime(start[0])
    # Name of the attack is the second element in the array
    attack_name = start[1][:-7]
    end = lines[1].split('#')
    end_time = pd.to_datetime(end[0])
    # print(attack_name)
    # Use pandas.Series.between fucntion to get cooresponding dataframe and stored in temp
    df_temp = df[df['Time'].between(start_time, end_time,inclusive="both")]
    # Drop the first column
    df_temp = df_temp.iloc[:, 1:]
    # Append the name of the attack to cooresponding dataframe
    # Append data frame to CSV file
    df_temp.assign(label=attack_name).to_csv('labeled.csv', mode='a')
