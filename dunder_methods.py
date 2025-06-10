class Robots:
    def __init__(self, name, material, weight):
        self.name = name
        self.material = material
        self.weight = weight

        self.model = {}

    def __str__(self):
        return f"My name is {self.name}, I am made up of {self.material} and I weight {self.weight}kg"

    def __repr__(self):
        return f"Robot('{self.name}', '{self.material}', {self.weight})"

    def __setitem__(self, name, model):
        if self.name == name:
            self.model[name] = model

        else:
            print(f"{name} doesn't exists!")

    def __getitem__(self, item):
        if self.name == item:
            for k, v in self.model.items():
                return f"{k} : {v}"

    def __eq__(self, other):
        if self.material == other.material:
            return True

        else:
            return False

    def __hash__(self):
        return hash(self.material)


r1 = Robots("R2D2", "Aluminium", 56)
r1["R2D2"] = 2019
print(r1["R2D2"])

r2 = Robots("Bloob", "Aluminium", 65)
r2["Bloob"] = 2020
print(r2["Bloob"])

print(r1 == r2)
print(hash(r1) == hash(r2))

print("\n\n")


class Loop:
    def __init__(self, list):
        self.list = list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.list) > self.index:
            result = self.list[self.index]
            self.index += 1
            return result

        else:
            raise StopIteration


stds = ["hassan", "ahmed", "shunan", "kinza"]

list1 = Loop(stds)

for i in list1:
    print(i)


print("\n\n")


# with open("dundermethod.txt", newline="") as file:
#     reader = file.read()
#     print(reader)


class FileReader:
    def __init__(self, name, method):
        self.file = open(name, method)

    def __enter__(self):
        return self.file

    def __exit__(self, exptype, expvalue, traceback):
        self.file.close()

        if exptype == FileNotFoundError:
            return True


print("Hello")

with FileReader("dundermethod.txt", "r") as file:
    reader = file.read()
    print(reader)

    raise FileNotFoundError


print("\n\n")