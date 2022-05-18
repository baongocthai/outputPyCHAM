#####################################
## BN ##
import check_xml as cx
import xml.etree.ElementTree as ET
import os
# the path of the input xml file (path_xml) is given by user
path_xml = r'C:\Users\24979\OneDrive\桌面\UROP\PyCHAM_3.5.3_single_terminal_only\PyCHAM\input\try_10bins'
os.chdir(path_xml)

flag = cx.flag
if flag == 0:
    quit()

# list_change contains all the missing smile strings in the original xml file, it is given by user and user should \
# make sure the sequence is corresponding to list_index
list_change = ['[C-]#[O+]', '[N]=O', 'CL']

name = cx.name
tree = ET.parse(name)
root = tree.getroot()
title = str(root).split('{')[1].split('}')[0]

list_index = cx.list_index
for i in range(len(list_index)):
    sub_item = ET.SubElement(root[0][list_index[i]], 'smiles')
    sub_item.text = list_change[i]
ET.register_namespace("", title)
root = ET.tostring(root)
with open(name, "wb") as f:
    f.write(root)