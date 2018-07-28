#!/usr/bin/python

# Aditya Subramanian Muralidaran


import sys
import functools

def compare_using(line1,line2):
    arr1 = line1.split('\t',1)
    arr2 = line2.split('\t',1)
    val1 = int(arr1[1])
    val2 = int(arr2[1])
    if(val1 > val2):
        return -1
    elif(val1 < val2):
        return 1
    else:
        if(str(arr1[0]) > str(arr2[0])):
            return -1
        elif(str(arr1[0]) < str(arr2[0])):
            return 1
        else:
            return 0

StopWords = ['https']
lines = list(open('Twitter_WordCount.txt', 'r'))
lines.sort(key=functools.cmp_to_key(compare_using))
print(lines)
writeFile = open("Twitter_TopWords.txt", "a", encoding='utf-8')
for line in lines:
    lsplit = line.split('\t',1)
    if(len(lsplit[0]) > 2 and lsplit[0].isalpha() and lsplit[0] not in StopWords):
        writeFile.write(line)

writeFile.close()
