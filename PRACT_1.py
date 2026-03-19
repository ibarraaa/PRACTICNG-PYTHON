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

# join sets 
