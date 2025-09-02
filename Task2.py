import turtle

def koch_curve(t, length, level):
    """
    Рекурсивно малює одну сторону фрактала Коха.

    :param t: Об'єкт черепашки (turtle).
    :param length: Довжина поточної лінії.
    :param level: Поточний рівень рекурсії.
    """
    if level == 0:
        # Базовий випадок: малюємо пряму лінію
        t.forward(length)
    else:
        # Рекурсивний крок: ділимо лінію на 4 сегменти
        # з довжиною, що дорівнює 1/3 від початкової
        segment_length = length / 3
        new_level = level - 1

        koch_curve(t, segment_length, new_level)
        t.left(60)
        koch_curve(t, segment_length, new_level)
        t.right(120)
        koch_curve(t, segment_length, new_level)
        t.left(60)
        koch_curve(t, segment_length, new_level)

def draw_koch_snowflake(t, length, level):
    """
    Малює повну сніжинку Коха, що складається з трьох сторін.

    :param t: Об'єкт черепашки (turtle).
    :param length: Довжина сторони початкового трикутника.
    :param level: Рівень рекурсії.
    """
    # Малюємо три сторони сніжинки
    for _ in range(3):
        koch_curve(t, length, level)
        t.right(120)

def main():
    """
    Основна функція для налаштування та запуску програми.
    """
    try:
        # Запит рівня рекурсії у користувача
        user_level = int(input("Введіть рівень рекурсії (наприклад, 1, 2, 3): "))
        if user_level < 0:
            print("Рівень рекурсії не може бути від'ємним.")
            return
    except ValueError:
        print("Неправильне введення. Будь ласка, введіть ціле число.")
        return

    # Налаштування вікна та черепашки
    window = turtle.Screen()
    window.bgcolor("white")
    snowflake_turtle = turtle.Turtle()
    snowflake_turtle.speed("fastest")
    snowflake_turtle.color("blue")

    # Переміщення черепашки до початкової позиції, щоб сніжинка була по центру
    snowflake_turtle.penup()
    snowflake_turtle.goto(-150, 90)
    snowflake_turtle.pendown()

    # Малюємо сніжинку
    initial_length = 300
    draw_koch_snowflake(snowflake_turtle, initial_length, user_level)

    # Приховуємо черепашку після завершення малювання
    snowflake_turtle.hideturtle()
    
    # Тримаємо вікно відкритим, доки його не закриє користувач
    window.exitonclick()

if __name__ == "__main__":
    main()