# 6.	Unpack a tuple into variables and print each variable.

def unpa():
    name = "pravin"
    age = 23
    city = "mumbai"
    pack = name, age, city

    name, age, city = pack
    print(name)
    print(age)
    print(city)

unpa()