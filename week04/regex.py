import re


def find_names(line):
    pattern = r"[a-zA-Z]"
    result = re.findall(pattern,line)

    pattern=r'(October|Oct|November|Nov)( [0-9]{1,2}, [0-9]{4})'
    result = result + re.findall(pattern,line)
    return result


f = open("names.txt")
for line in f.readlines():
    #print(line)
    result = find_names(line)
    if (len(result)>0):
        print(result)