import re

mylist = ["А123АА11", "А222АА123", "A12AA123", "A123CC1234", "AA123A12", "Т322ЛЛ11", "а123сс123", "f123ff1234"]

r = re.compile("^[АВЕКМНОРСТУХавекмнорстух]\d{3}(?<!000)[АВЕКМНОРСТУХавекмнорстух]{2}\d{2,3}$")
newlist = list(filter(r.match, mylist))
print(newlist)
