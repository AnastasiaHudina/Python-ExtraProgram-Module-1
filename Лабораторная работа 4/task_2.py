# TODO импортировать необходимые модули
import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # TODO считать содержимое csv файла
    list1 = []
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as input_file:
        reader = csv.DictReader(input_file)
        # Чтение данных
        for row in reader:
            list1.append(row)

    # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as output_file:
        json.dump(list1, output_file, indent=4)

if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME, 'r', encoding='utf-8') as output_f:
        for line in output_f:
            print(line, end="")
