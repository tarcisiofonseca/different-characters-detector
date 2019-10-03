character1 = []
character2 = []
list1 = []
list2 = []
list3 = []
s = 0
ignore_spaces = 0
ignore_commas = 0
ignore_dots = 0

a = "Insert your string here, but keeping quotation marks"
b = "Insert your another string here, keeping quotation marks too"

a = a.split(" ")
a = " ".join(a)
b = b.split(" ")
b = " ".join(b)

if ignore_spaces == 1:
    a = a.replace(' ','')
    b = b.replace(' ','')
else:
    pass
if ignore_commas == 1:
    a = a.replace(',','')
    b = b.replace(',','')
else:
    pass
if ignore_dots == 1:
    a = a.replace('.','')
    b = b.replace('.','')
else:
    pass

if a == b:
    print("All characters are the same.")
else:
    for (character1, character2) in zip(a, b):
        s = s+1
        if character1 != character2:
            g = s
            list1.append(character1)
            list2.append(character2)
            list3.append(g)

for p in range(0, len(list3)):
    print("In position", list3[p], ", the characters", list1[p], " and ", list2[p], "are, respectively, differents.")
if len(a) > len(b):
    print("\nThe first string have more characters than the second string. The text left over is:", a[len(b):])
if len(b) > len(a):
    print("\nThe second string have more characters than the first string. The text left over is:", b[len(a):])
