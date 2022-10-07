###XML 1 - Find the Score###

    return sum([len(i.keys()) for i in  node.iter() ])


###XML2 - Find the Maximum Depth###

import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    if (level == maxdepth):
        maxdepth += 1
    for child in elem:
        depth(child, level + 1)
