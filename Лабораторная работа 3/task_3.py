# TODO  Напишите функцию count_letters
def count_letters(ar):
    ar_low = ar.lower()
    dict_={
        'а': ar.count('а'),
        'б': ar.count('б'),
        'в': ar.count('в'),
        'г': ar.count('г'),
        'д': ar.count('д'),
        'е': ar.count('е'),
        'ё': ar.count('ё'),
        'ж': ar.count('ж'),
        'з': ar.count('з'),
        'и': ar.count('и'),
        'й': ar.count('й'),
        'к': ar.count('к'),
        'л': ar.count('л'),
        'м': ar.count('м'),
        'н': ar.count('н'),
        'о': ar.count('о'),
        'п': ar.count('п'),
        'р': ar.count('р'),
        'с': ar.count('с'),
        'т': ar.count('т'),
        'у': ar.count('у'),
        'ф': ar.count('ф'),
        'х': ar.count('х'),
        'ц': ar.count('ц'),
        'ч': ar.count('ч'),
        'ш': ar.count('ш'),
        'щ': ar.count('щ'),
        'ъ': ar.count('ъ'),
        'ы': ar.count('ы'),
        'ь': ar.count('ь'),
        'э': ar.count('э'),
        'ю': ar.count('ю'),
        'я': ar.count('я')
 }

# TODO Напишите функцию calculate_frequency
def calculate_frequency(ar):
    ar_low = ar.lower()
    general_count = 0
    for i in ar_low:
        if i.isalpha():
            general_count += 1

    new_dict_={
        'а': round(ar.count('а')/general_count, 2),
        'б': round(ar.count('б')/general_count, 2),
        'в': round(ar.count('в')/general_count,2),
        'г': round(ar.count('г')/general_count,2),
        'д': round(ar.count('д')/general_count,2),
        'е': round(ar.count('е')/general_count,2),
        'ё': round(ar.count('ё')/general_count,2),
        'ж': round(ar.count('ж')/general_count,2),
        'з': round(ar.count('з')/general_count,2),
        'и': round(ar.count('и')/general_count,2),
        'й': round(ar.count('й')/general_count,2),
        'к': round(ar.count('к')/general_count,2),
        'л': round(ar.count('л')/general_count,2),
        'м': round(ar.count('м')/general_count,2),
        'н': round(ar.count('н')/general_count,2),
        'о': round(ar.count('о')/general_count,2),
        'п': round(ar.count('п')/general_count,2),
        'р': round(ar.count('р')/general_count,2),
        'с': round(ar.count('с')/general_count,2),
        'т': round(ar.count('т')/general_count,2),
        'у': round(ar.count('у')/general_count,2),
        'ф': round(ar.count('ф')/general_count,2),
        'х': round(ar.count('х')/general_count,2),
        'ц': round(ar.count('ц')/general_count,2),
        'ч': round(ar.count('ч')/general_count,2),
        'ш': round(ar.count('ш')/general_count,2),
        'щ': round(ar.count('щ')/general_count,2),
        'ъ': round(ar.count('ъ')/general_count,2),
        'ы': round(ar.count('ы')/general_count,2),
        'ь': round(ar.count('ь')/general_count,2),
        'э': round(ar.count('э')/general_count,2),
        'ю': round(ar.count('ю')/general_count,2),
        'я': round(ar.count('я')/general_count,2)
    }
    return new_dict_

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
count_letters(ar=main_str)
result = calculate_frequency(ar=main_str)
list1= list(result.keys())
list2=list(result.values())
for j in range(len(list2)):
    print(f'{list1[j]}: {list2[j]}')


