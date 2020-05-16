import piecash
import glob
import os
import xml
import xml.etree
import csv
import xml.etree.ElementTree
# from xml.etree import ElementTree

GNUCASH_DIR = '/home/me/Nextcloud/GnuCash/*.gnca'
list_of_files = glob.glob(GNUCASH_DIR) # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)

context = xml.etree.ElementTree.iterparse(latest_file, events=("start", "end"))

for event,elem in context:
    tag = elem.tag
    if tag == '{http://www.gnucash.org/XML/gnc}account':
        print(tag)
    # text = elem.text

    # print(elem.tag)
    # print(elem.text)
    elem.clear()


