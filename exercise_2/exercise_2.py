from collections import Counter
import re

pattern = r"(?<=switchport trunk allowed vlan )[\d,]+"
list_aux = list()  # Aux list for collecting data purposes
number_of_lines =0 # Counter of number of lines of the file
List1 = list()
List2 = list()

for i, line in enumerate(open('commands.txt')):
    for match in re.finditer(pattern, line, re.MULTILINE):  # We apply the regex in every line
        splitted_line = match.group().split(',')
        n = 0  # Counter = 0
        for i in splitted_line:
            if i.isdigit():
                list_aux.append(splitted_line[n])
            n += 1
        number_of_lines += 1  # We keep counting the number of lines read of the file.

# After inserting all items, we start treating the auxiliar list
cnt = Counter(list_aux)
for v in cnt.iteritems():
    if v[1] == number_of_lines:  # If an item appears in every line, it will be a common VLAN
        List1.append(v[0])
    if v[1] == 1:
        List2.append(v[0])  # If an item appears just one time, it will be a unique VLAN

List1.sort(key=int)  # We sort lists in ascending order
List2.sort(key=int)
print "List_1 =", List1
print "List_2 =", List2