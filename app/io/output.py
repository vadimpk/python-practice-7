def print_to_console(text):
    """Виводить текст у консоль.

    Args:
        text (str): Текст для виводу.
    """
    print(text)


def write_to_file_builtin(filepath, text):
    """Записує текст до файлу за допомогою вбудованих можливостей Python.

    Args:
        filepath (str): Шлях до файлу для запису.
        text (str): Текст, який потрібно записати.
    """
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(text)
