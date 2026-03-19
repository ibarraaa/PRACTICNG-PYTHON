thisdict = {
    "brand": "ford",
    "model": "Mustang",
    "year": 1976
}

print(thisdict["brand"])
print(len(thisdict))
print(thisdict)
x = thisdict["model"]
z = thisdict.get("model")
y = thisdict.keys()
car = {
    "brand": "toyata",
    "model": "Vios",
    "year": 2015
}
x_ = car.keys()
print(x_)
car["color"] = "white"
print(x_)
z_ = thisdict.values()
print(z_) #values
print(x_) #keys


y_ = thisdict.items()

print("tuple in a list: ", y_)



