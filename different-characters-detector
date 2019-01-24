import itertools

character1 = []
character2 = []
list1 = []
list2 = []
list3 = []
s = 0

a = "Insert your string here, but keeping quotation marks"
b = "Insert your another string here, keeping quotation marks too"

a = " ".join(a)
a = a.split(" ")

b = " ".join(b)
b = b.split(" ")

if a == b:
    print("All characters are the same")
else:
    for (character1,character2) in zip(a,b):
        s = s+1
        if character1!=character2:
            g = s
            list1.append(character1)
            list2.append(character2)
            list3.append(g)

print("In position {}, the characters {} and {} are, respectively, different".format(list3,list1,list2))
