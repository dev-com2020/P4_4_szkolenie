def mutli(a, b):
    try:
        return int(a) * int(b)
    except (TypeError, ValueError):
        return "operacja nieudana!"


print(mutli("a", "b"))

print("tutaj kolejne instrukcje programu")

valid_data = [
    {'name': 'Adam', 'age': '10'},
    {'name': 'Dawid', 'age': '17'},
    {'name': 'Marcin', 'age': '19'},
]

invalid_data = [
    {},
    {'name': 'Dawid', 'age': '17'},
    {'name': 'Marcin', 'age': '19'},
]

invalid_data2 = [
    {'name': 'Adam', 'age': 'f10da'},
    {'name': 'Dawid', 'age': '17'},
    {'name': 'Marcin', 'age': '19'},
]


def check_age(users, age):
    count = 0
    for user in users:
        try:
            if int(user['age']) < age:
                count += 1
        except KeyError:
            print(f"Niepoprawny słownik: {user}")
        except ValueError:
            print(f"Niepoprawna wartość: {user}")
        else:
            print("Jeśli wszystko jest ok, to ja tu się wykonam!")
        finally:
            print(invalid_data2)
    return count


print(check_age(valid_data, 18))
print(check_age(invalid_data2, 18))
