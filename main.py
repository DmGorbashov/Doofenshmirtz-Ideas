"""Программа генерации идей для Фуфелшмерца"""
import random
import csv


def idea_generator():
    """Метод генерации идеи"""

    first = ()
    with open('words.csv', newline='', encoding='UTF8') as my_file:
        words_file = csv.reader(my_file)
        for word in words_file:
            first += (word[0],)

    second = ('MEGA', 'MAX', 'SUPER', 'Ultra')
    first_part = random.choice(first)
    second_part = random.choice(second)
    return first_part, second_part


def main():
    """Основной метод main"""

    print("Добро пожаловать в Имявыбиратор3000\n")
    print("Вот один из вариантов вашего инатора:")

    while True:
        new_idea = idea_generator()
        print(f"{new_idea[1]} {new_idea[0]}инатор")

        try_again = input("\n\nДругой? (нажми Enter, чтобы продолжить; либо n, чтобы выйти)")

        if try_again.lower() == "n":
            break

    input("\nНажми Enter для завершения работы.")

if __name__ == "__main__":
    main()
