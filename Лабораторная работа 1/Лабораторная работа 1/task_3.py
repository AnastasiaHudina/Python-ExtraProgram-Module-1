list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"] #исходный список
number_of_players = len(list_players) #общее количество игроков
middle_index = len(list_players) // 2 #середина списка
first_team = list_players[:middle_index]
print(first_team)
second_team = list_players[middle_index:]
print(second_team)