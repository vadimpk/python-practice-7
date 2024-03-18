import pytest
import app.io.input as input

def test_read_from_file_builtin_exists():
    """Перевіряє, чи функція коректно зчитує існуючий файл."""
    result = input.read_from_file_builtin('tests/test_data/test.txt')
    assert result == "this is a test file!"

def test_read_from_file_builtin_not_exists():
    """Перевіряє, чи функція поводить себе коректно, коли файл не існує."""
    with pytest.raises(FileNotFoundError):
        input.read_from_file_builtin('tests/test_data/nonexistent.txt')

def test_read_from_file_pandas_csv_exists():
    """Перевіряє, чи pandas коректно зчитує існуючий CSV файл."""
    result = input.read_from_file_pandas('tests/test_data/test.csv')
    assert not result.empty  # Перевіряємо, що DataFrame не пустий

def test_read_from_file_pandas_csv_columns():
    """Перевіряє, чи структура DataFrame відповідає очікуваній."""
    result = input.read_from_file_pandas('tests/test_data/test.csv')
    expected_columns = ['Name', 'Age']
    assert list(result.columns) == expected_columns

def test_read_from_file_pandas_not_exists():
    """Перевіряє, чи функція pandas поводить себе коректно, коли файл не існує."""
    with pytest.raises(FileNotFoundError):
        input.read_from_file_pandas('tests/test_data/nonexistent.csv')
