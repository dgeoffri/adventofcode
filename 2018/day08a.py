#!/usr/bin/env python
# coding: utf-8

class Node(object):
    def __init__(self, data):
        self.children=[]
        self.metadata=[]
        self.childrenCount = data.pop(0)
        self.metadataCount = data.pop(0)
        for x in xrange(self.childrenCount):
            self.children.append(Node(data))
        for x in xrange(self.metadataCount):
            self.metadata.append(data.pop(0))
    	self.metadataSum=sum(self.metadata) + sum([x.metadataSum for x in self.children])
    
license = map(int,open('day08.txt','r').read().splitlines()[0].split(' '))
root = Node(license)
print root.metadataSum
