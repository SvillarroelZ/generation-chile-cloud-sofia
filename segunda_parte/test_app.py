import pytest
from app import suma

def test_suma_valores_validos():
    assert suma(2, 3) == 5
    assert suma(0, 5) == 5
    assert suma(1.5, 2.5) == 4.0


def test_suma_tipo_invalido():
    with pytest.raises(TypeError):
        suma("2", 3)

    with pytest.raises(TypeError):
        suma(2, "3")

    with pytest.raises(TypeError):
        suma("hola", "mundo")


def test_suma_valores_negativos():
    with pytest.raises(ValueError):
        suma(-1, 3)

    with pytest.raises(ValueError):
        suma(2, -5)

    with pytest.raises(ValueError):
        suma(-1, -1)