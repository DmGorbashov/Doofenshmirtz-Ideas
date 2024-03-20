import random
import csv


def main():
    print("Добро пожаловать в Имявыбиратор3000\n")
    print("Вот один из вариантов вашего инатора:")
    first = ()
    with open('words.csv', newline='', encoding='UTF8') as my_file:
        words_file = csv.reader(my_file)
        for word in words_file:
            first += (word[0],)

    second = ('MEGA', 'MAX', 'SUPER', 'Ultra')

    while True:
        first_part = random.choice(first)
        second_part = random.choice(second)

        print("")
        print(f"{second_part} {first_part}инатор")

        try_again = input("\n\nДругой? (нажми Enter, чтобы продолжить; либо n, чтобы выйти)")

        if try_again.lower() == "n":
            break

    input("\nНажми Enter для завершения работы.")


if __name__ == "__main__":
    main()
