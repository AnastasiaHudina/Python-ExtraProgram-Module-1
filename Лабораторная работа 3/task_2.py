# TODO Напишите функцию find_common_participants
def find_common_participants(a,b, arg=','):
    first = set(a.split(arg))
    second = set(b.split(arg))
    new = list(first.intersection(second))
    return sorted(new)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(a=participants_first_group, b=participants_second_group,arg='|'))

