# TODO Найдите количество книг, которое можно разместить на дискете
disketa = 1.44*1024*1024 #перевели Мб в байты
pages = 100
lines_on_page = 50
symbols_on_line = 25
one_symbol = 4
weight_of_one_book = 4*25*50*100 #вес в байтах одной книги
print("Количество книг, помещающихся на дискету:", int(disketa//weight_of_one_book))
