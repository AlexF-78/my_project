import os

import pytest

from src.decorators import log

LOG_FILE = "test_log.txt"


@pytest.fixture(autouse=True)
def cleanup_log():
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
    yield
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)


def test_success_and_error(capsys):
    # Успешный вызов без файла (лог в консоль)
    @log()
    def f1(x):
        print("Inside f1")
        return x + 1

    result = f1(10)
    assert result == 11
    out = capsys.readouterr().out
    assert "Inside f1" in out

    # Вызов с файлом, успешный вызов
    @log(filename=LOG_FILE)
    def f2(x):
        return x * 2

    assert f2(5) == 10
    with open(LOG_FILE) as f:
        logs = f.read()
    assert "f2 ok" in logs

    # Вызов с исключением, лог ошибки
    @log(filename=LOG_FILE)
    def f3():
        raise ValueError("err")

    with pytest.raises(ValueError):
        f3()

    with open(LOG_FILE) as f:
        logs = f.read()
    assert "f3 error" in logs


def test_console_output_on_error(capsys):
    @log()
    def g():
        raise RuntimeError()

    with pytest.raises(RuntimeError):
        g()
