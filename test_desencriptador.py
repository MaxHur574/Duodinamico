import pytest
from aes_utils import encriptar, desencriptar


def test_desencriptar_con_llave_correcta():
    texto = "probando desencriptador"
    llave = "llave123"
    cifrado = encriptar(texto, llave)
    assert desencriptar(cifrado, llave) == texto


def test_desencriptar_con_llave_incorrecta():
    texto = "otro mensaje"
    llave_correcta = "llave_ok"
    llave_incorrecta = "llave_fail"
    cifrado = encriptar(texto, llave_correcta)
    with pytest.raises(ValueError):
        desencriptar(cifrado, llave_incorrecta)
