import re

# Names can contain:
# A-Z, a-z ([A-Za-z]+)
# spaces \s
# .  (will have letters before, space after):  ([A-Z]([a-z]*)\.)
# ' (letters before & after): ([A-Za-z]+\'[A-Za-z]+)
# - (lowercase letters before, upper case right after) ([a-z]+\-[A-Z][a-z]+)

# Names do not contain:
# 0-9
# ! @ # $ % ^ & * () + =
# [] {} | \
# : ; " 
# / ? 
# "Robert'); DROP TABLE Students;--" notwithstanding

def find_names(line):
    pattern = r"([A-Z][a-z]+\s[A-Za-z]+)|([A-Z][a-z]+\.)"
    result = re.findall(pattern,line)
    return result


f = open("names.txt")
for line in f.readlines():
    #print(line)
    result = find_names(line)
    if (len(result)>0):
        print(result)