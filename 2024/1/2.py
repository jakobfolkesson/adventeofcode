# real input in file ./input.txt
input = open('input.txt').read()

input = input.split("\n")
input = [i.split() for i in input]

list1 = [int(i[0]) for i in input]
list2 = [int(i[1]) for i in input]

list1=sorted(list1)
list2=sorted(list2)

d = {}
for nr in list2:
    d[nr] = d.get(nr, 0) + 1

similarity_score = 0
for nr in list1:
    similarity_score += nr * d.get(nr, 0)

print(similarity_score)