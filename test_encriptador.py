import pytest
from aes_utils import encriptar, desencriptar


def test_encriptar_devuelve_hex():
    resultado = encriptar("hola mundo", "mi_llave")
    # Debe ser un string hex válido
    assert isinstance(resultado, str)
    assert all(c in "0123456789abcdef" for c in resultado.lower())


def test_encriptar_y_desencriptar():
    texto = "mensaje secreto con acentos áéíóú"
    llave = "clave_segura"
    cifrado = encriptar(texto, llave)
    descifrado = desencriptar(cifrado, llave)
    assert descifrado == texto
