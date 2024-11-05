# TODO  Напишите функцию count_letters
def count_letters(ar):
    list1 = []
    count = 0
    for i in ar:
        if i not in list1:
            if i.isalpha():
                list1.append((i, ar.count(i)))
    return dict(list1)

# TODO Напишите функцию calculate_frequency
def calculate_frequency(ar, arr):
    letters = list(arr.keys())
    counting = list(arr.values())
    list2 = []
    general_count = 0
    for i in ar:
        if i.isalpha():
            general_count += 1
    for g in range(len(counting)):
        frequency = round(counting[g] / general_count, 2)
        list2.append((letters[g], "{:,.2f}".format(frequency)))
    return dict(list2)

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
result1 = count_letters(ar=main_str.lower())
# print(result1)
result2 = calculate_frequency(ar=main_str.lower(), arr=result1)
# print(result2)
list_1 = list(result2.keys())
list_2 = list(result2.values())
for j in range(len(list_2)):
    print(f'{list_1[j]}: {list_2[j]}')
