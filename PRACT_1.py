THISSET = {1, 2, 3, 4, 5, 0}
for x in THISSET:
    print(x)
    print(1 in THISSET)
    print(1 not in THISSET)
    
THISSET.add(90)
print(THISSET)

data_1 = {1000,1111, 10101, 1001}
data_2 = {1011, 10101, 111, 1110}
data_1.update(data_2)
print(data_1)

set_1 = {"ds", "ov", "preamp"}
list_1 = ["mvave", "joyo"]
set_1.update(list_1)
THISSET.remove(1)

print('JOIN SETS_')
# join sets ''

set_2 = {"compress", "IR", "EQ"}

set_3 = set_1.union(set_2)
print(set_3)
sett = set_1 | set_2
print(sett)

allset = set_1.union(set_2, set_3, data_1, data_2)
print(allset)
allsetset = set_1 | set_2 |set_3
print(allsetset)

z = set_1.union(list_1)
print(z)













