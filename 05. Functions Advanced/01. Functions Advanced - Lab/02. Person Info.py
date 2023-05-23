def get_info(name, age, town):
    return f"This is {name} from {town} and he is {age} years old"


kwargs = {'name': "Pesho", 'age': "hmai", "town": "lOOOOL"}
print(get_info(**kwargs))