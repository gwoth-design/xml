import os 
from xml.etree import ElementTree

lookFor = input("What company are you looking for? ")

full_file = r"C:/Users/benja/Downloads/testXML/data/ItemData.xml"

dom = ElementTree.parse(full_file)

dat = dom.findall('data/item/column/rawData')

if lookFor == "ACME 1":
    for i in range(1,16):
        print(dat[i].text)