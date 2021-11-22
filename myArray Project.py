my_array = ['Festus Ijalana', '9lakes']


def cut_name(name):
    name_list = []
    for word in name:
        print(name.split(','))
        print(word)
        name_list.append(word)
        return name_list


name = input("Name: ")
print(cut_name(name))