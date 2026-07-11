def greeting(name):
    return f"Hello,{name}"

def displayInfo(name, age, *skills):
    print(f"Hello, {name}")
    print(f"Your age is, {age}")
    for i in skills:
        print(f"- {i}", sep=" | ")

def byeBye():
    return "see You next day😁😁"