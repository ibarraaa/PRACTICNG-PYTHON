THISSET = {1, 2, 3, 4, 5, 0}
for x in THISSET:
    print(x)
    print(1 in THISSET)
    print(1 not in THISSET)
    
THISSET.add(90)
print(THISSET)  

data_1 = {1000,1111, 10101, 1001}
data_2 = {1011, 1000, 111, 1110}
data_1.update(data_2)
print(data_1)

set_1 = {"ds", "ov", "preamp"}
list_1 = ["mvave", "joyo"]
set_1.update(list_1)
THISSET.remove(1)

print('JOIN SETS_')
# join sets ''

set_2 = {"compress", "IR", "EQ" "ds"}

set_3 = set_1.union(set_2)
print(set_3)
sett = set_1 | set_2
print(sett)

allset = set_1.union(set_2, set_3, data_1, data_2)
print(allset)
allsetset = set_1 | set_2 |set_3
print(allsetset)

z = set_1.union(list_1)
print("tuple and set: ", z)


set_4 = set_1.intersection(set_2)
print(set_4)
set_1 = set_1.intersection_update(set_2)
print(set_1)

set_5 = data_1.difference(data_2)
print(set_5)

# frozenset
print("FROZENSET___")


x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
