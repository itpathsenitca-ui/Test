import random
import turtle

# Настройка окна
wn = turtle.Screen()
wn.title("Угадай число")
wn.bgcolor("lightblue")
wn.setup(width=700, height=500)

# Создаём черепашку для текста
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.speed(0)

# Создаём черепашку для кнопок
button_pen = turtle.Turtle()
button_pen.hideturtle()
button_pen.penup()

try_history = []

def draw_text(text, y_offset=0, color="black"):
    """Отрисовка текста."""
    pen.clear()
    pen.goto(0, y_offset)
    pen.color(color)
    pen.write(text, align="center", font=("Arial", 16, "normal"))

def draw_try_history():
    """Показать все предыдущие попытки."""
    if try_history:
        history_str = "Попытки: " + ", ".join(map(str, try_history))
        draw_text(history_str, y_offset=-150, color="darkgreen")
    else:
        draw_text("Нет предыдущих попыток.", y_offset=-150, color="gray")

def reset_game():
    """Начинаем новую игру."""
    global secret_number, attempts_left, try_history
    secret_number = random.randint(1, 100)
    attempts_left = 10
    try_history.clear()
    wn.bgcolor("lightblue")
    draw_text("Я загадал число от 1 до 100.\nУ вас 10 попыток.\nПопробуйте угадать!\n\nНажмите ПРОБЕЛ для попытки.")
    draw_try_history()

def game():
    reset_game()

    def guess():
        """Обработчик для угадывания числа."""
        nonlocal attempts_left
        guess_num = wn.numinput("Попытка", "Введите число (от 1 до 100):", minval=1, maxval=100)
        if guess_num is None:
            # Игрок закрыл окно или отменил ввод
            draw_text("Игра прервана. Чтобы начать заново, нажмите РАЗВОРОТ (зеленую кнопку).", y_offset=0, color="red")
            return
        guess_num = int(guess_num)
        try_history.append(guess_num)
        attempts_left -= 1

        if guess_num == secret_number:
            wn.bgcolor("lightgreen")
            draw_text(f"Поздравляю! Вы угадали число {secret_number}!\n\nНажмите кнопку 'Играть снова' или ПРОБЕЛ.", y_offset=50)
            draw_restart_button()
            return
        elif guess_num < secret_number:
            draw_text(f"Слишком мало! Осталось попыток: {attempts_left}", y_offset=0)
        else:
            draw_text(f"Слишком много! Осталось попыток: {attempts_left}", y_offset=0)

        draw_try_history()

        if attempts_left == 0:
            wn.bgcolor("salmon")
            draw_text(f"Игра окончена! Загаданное число было {secret_number}.", y_offset=50)
            draw_restart_button()

    def draw_restart_button():
        """Рисуем кнопку для нового запуска."""
        button_pen.clear()
        button_pen.goto(0, -200)
        button_pen.color("blue")
        button_pen.write("Нажмите 'Y' или клик для новой игры", align="center", font=("Arial", 14, "bold"))
        # Назначим обработчик
        wn.onkey(reset_game, "Y")
        wn.onclick(lambda x, y: reset_game() if -50 < y < 50 and -200 < x < 200 else None)

    # Назначаем событий
    wn.onkey(guess, "space")
    wn.listen()
    wn.setup(0, 0)  # Обновления для интерфейса
    draw_text("Нажмите ПРОБЕЛ и вводите число для угадывания.\n\nДля новой игры нажмите 'Y' или кликните ниже.", y_offset=150)
    draw_try_history()

    wn.mainloop()

if __name__ == "__main__":
    game()