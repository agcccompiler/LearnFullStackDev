#!/opt/anaconda3/bin/python3
import json
import pickle


s = {
    "name": "Alice", 
     "age": 30, 
     "city": "Beijing"
}

with open('test.json', 'w') as f:
    json.dump(s, f)

with open('test.json', 'r') as f:
    loaded_file = json.load(f)
    print(type(loaded_file))
print(loaded_file)

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age}, city={self.city})"

Jincheng = Person("Jincheng", 21, "London")

with open("test.pkl", "wb") as f: 
    pickle.dump(Jincheng, f)

with open('test.pkl', 'rb') as f:
    loaded_file_b = pickle.load(f)
    print(type(loaded_file_b))
print(loaded_file_b)

class Animal:
    def __init__(self, species, age, name):
        self.species = species
        self.age = age
        self.name = name

    def __repr__(self):
        return f"Animal(species={self.species}, age={self.age}, name={self.name})"

cat = Animal("Cat", 3, "Kitty")

cat_bytes = pickle.dumps(cat)
print(cat_bytes)
print(type(cat_bytes))
cat_org = pickle.loads(cat_bytes)
print(cat_org)
print(cat_org.age)