'''
Created on Aug 28, 2013

@author: ishaansutaria
'''

from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as etree

#XML has a root and 
#Basic Example
'''
root = Element('devices')
tree = ElementTree(root)
name = Element('name')
root.append(name)
name.text = 'Ihsaan'
print etree.tostring(root)
'''


#Updated this function to support array inside an xml
'''
def getXML(**dic):
    root = Element(dic['root'])
    tree = ElementTree(root)
    del dic['root']
    
    for key in dic:
        name = Element(key)
        root.append(name)
        name.text = dic[key]
       
    return etree.tostring(root)
'''

'''
Here to create an xml that has a root and a child which has nodes inside
1) Fuction accepts a dictionary in which another dictionary is passed for creating child nodes.
2) Root is searched and assigned and then deleted from the dictionary
3) We check if the next node selected is a dictionary or a normal child as there is a possibility of both existing in the same XML
4) If the key is a dictionary then create that node as a subroot and loop through the dictionary to create child node for that subroot.
5) Else treat is as a normal child node.
'''
def getXML(**dic):
    root = Element(dic['root'])
    tree = ElementTree(root)
    del dic['root']
    for key in dic:
        
        if isinstance(dic[key],dict):
            k1 = etree.SubElement(root, key)
            child = dic[key]
            for subKeys in child:
                k2 = etree.SubElement(k1,subKeys)
                k2.text = child[subKeys]
        else:           
            name = Element(key)
            root.append(name)
            name.text = dic[key]
    
    return etree.tostring(root)

def main():
    dic = {'root':'user','email':'ishaads','password':'asdad','app':{'as0':'1'}}
    k = getXML(**dic)
    print k

if __name__ == "__main__":main()