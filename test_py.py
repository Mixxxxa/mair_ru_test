import pytest


@pytest.fixture
def text_for_str_tests() -> str:
    """
    Фикстура для тестов типа str
    """
    return 'TestTesttesT'
    

def test_str_members(text_for_str_tests) -> None:
    """
    Обычный тест проверяющий наиболее используемые функции типа str
    """
    # замена символов
    assert text_for_str_tests.replace('Test', 'AAA') == 'AAAAAAtesT'
    # разбиение строки
    assert text_for_str_tests.split('T') == ['', 'est', 'esttes', '']
    # конкатенация и умножение строк
    assert (text_for_str_tests * 2) == (text_for_str_tests + text_for_str_tests)
    # соответствие начала и конца строки
    assert text_for_str_tests.startswith('Te') and text_for_str_tests.endswith('sT')
    # приведение к нижнему регистру
    assert text_for_str_tests.lower() == 'testtesttest'


@pytest.mark.parametrize("input,expected", [
    ("test", 4),    # обычный текст (латиница)
    ("привет", 6),  # обычный текст (кирилица)
    ("👋🏼", 2),      # составной юникод символ 
    ("", 0),        # пустой текст
    ("\t", 1)       # текст с управляющими последовательностями
    ])   
def test_str_len(input: str, expected: int) -> None:
    """
    Параметризованный тест, проверяющий корректную работу функции len для строк
    """
    assert len(input) == expected


def test_str_expected_fail(text_for_str_tests) -> None:
    """
    Негативный тест без ошибки с использованием фикстуры
    """
    try:
        # Получение отсутствующего элемента массива
        check = text_for_str_tests[100]
    except IndexError:
        pass
    