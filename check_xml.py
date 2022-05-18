#####################################
## BN ##
import xml.etree.ElementTree as ET
import os
# the path of the input xml file (path_xml) is given by user
path_xml = r'C:\Users\24979\OneDrive\桌面\UROP\PyCHAM_3.5.3_single_terminal_only\PyCHAM\input\try_10bins'
os.chdir(path_xml)

# name of the input xml file is given by user
name = "Chemical xml file.xml"

list_need_change = []
list_index = []
xml = open(name, "r+")
xml = xml.readlines()
for i in xml:
    if ("species_name" in i) and (i[-3] == "/"):
        list_need_change.append(i)

list_index = [int(i.split('"')[1][1:])-1 for i in list_need_change]
list_need_change = [i.split('"')[3] for i in list_need_change]

# set a flag, flag == 0 means there is no missing data in xml file and no need to run modify_xml.py, \
# flag == 1 means there are missing data in xml file and need to run modify_xml.py to add the missing data
flag = 0
if len(list_need_change) > 0:
    flag = 1

# print list_need_change which contains all the components whose smile strings are missing\
# then user can find missing smile strings manually according to the list_need_change
print(list_need_change)
