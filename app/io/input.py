import pandas as pd


def read_from_console():
    """Зчитує текст, введений користувачем з консолі."""
    return input("Будь ласка, введіть текст: ")


def read_from_file_builtin(filepath):
    """Зчитує текст з файлу за допомогою вбудованих можливостей Python.

    Args:
        filepath (str): Шлях до файлу для зчитування.
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()


def read_from_file_pandas(filepath):
    """Зчитує дані з файлу у форматі CSV за допомогою бібліотеки pandas.

    Args:
        filepath (str): Шлях до файлу CSV для зчитування.
    """
    return pd.read_csv(filepath)
