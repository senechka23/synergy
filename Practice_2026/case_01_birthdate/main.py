from datetime import date
import calendar


STAR_GLYPHS = {
    "0": [" *** ", "*   *", "*   *", "*   *", " *** "],
    "1": ["  *  ", " **  ", "  *  ", "  *  ", " *** "],
    "2": [" *** ", "*   *", "   * ", "  *  ", "*****"],
    "3": ["**** ", "    *", " *** ", "    *", "**** "],
    "4": ["*  * ", "*  * ", "*****", "   * ", "   * "],
    "5": ["*****", "*    ", "**** ", "    *", "**** "],
    "6": [" *** ", "*    ", "**** ", "*   *", " *** "],
    "7": ["*****", "   * ", "  *  ", " *   ", "*    "],
    "8": [" *** ", "*   *", " *** ", "*   *", " *** "],
    "9": [" *** ", "*   *", " ****", "    *", " *** "],
    " ": ["   ", "   ", "   ", "   ", "   "],
}

DAY_NAMES = [
    "понедельник",
    "вторник",
    "среда",
    "четверг",
    "пятница",
    "суббота",
    "воскресенье",
]


def ask_for_birthday():
    """Запрашивает дату рождения и проверяет корректность введённой даты."""
    while True:
        try:
            day = int(input("Введите день рождения: "))
            month = int(input("Введите месяц рождения: "))
            year = int(input("Введите год рождения: "))

            birthday = date(year, month, day)

            if birthday > date.today():
                print("Дата рождения не может быть в будущем. Попробуйте ещё раз.\n")
                continue

            return birthday
        except ValueError:
            print("Введена некорректная дата. Попробуйте ещё раз.\n")


def weekday_label(birthday):
    """Возвращает название дня недели для указанной даты."""
    return DAY_NAMES[birthday.weekday()]


def check_leap_year(year):
    """Определяет, является ли год високосным."""
    return calendar.isleap(year)


def years_elapsed(birthday):
    """Вычисляет полный возраст пользователя на текущую дату."""
    today = date.today()
    age = today.year - birthday.year

    if (today.month, today.day) < (birthday.month, birthday.day):
        age -= 1

    return age


def draw_date_in_stars(birthday):
    """Печатает дату рождения цифрами, составленными из звёздочек."""
    formatted_date = birthday.strftime("%d %m %Y")
    print("\nДата рождения в формате электронного табло:\n")

    for line_index in range(5):
        star_line = "  ".join(STAR_GLYPHS[symbol][line_index] for symbol in formatted_date)
        print(star_line)


def run_birthdate_app():
    print("Программа работы с датой рождения")
    print("-" * 36)

    birthday = ask_for_birthday()
    print(f"\nДень недели: {weekday_label(birthday)}")

    if check_leap_year(birthday.year):
        print(f"{birthday.year} год был високосным.")
    else:
        print(f"{birthday.year} год не был високосным.")

    print(f"Возраст пользователя: {years_elapsed(birthday)}")
    draw_date_in_stars(birthday)


if __name__ == "__main__":
    run_birthdate_app()
