import os, io, json, math, re, importlib
import pytest
mod = importlib.import_module('main')


@pytest.mark.parametrize("s,esperado", [
    ("  hola   mundo  ", "hola mundo"),
    ("\n\t  ", ""),
    (None, ""),
])
def test_normalizar_espacios(s, esperado):
    assert mod.normalizar_espacios(s) == esperado
