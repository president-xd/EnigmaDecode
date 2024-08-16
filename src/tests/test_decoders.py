# src/tests/test_decoders.py

import pytest
from src.EnigmaDecode import (binary_decode, hexadecimal_decode, octal_decode,
                               ascii_decode, url_decode, unicode_point_decode,
                               base32_decode, base64_decode)

def test_binary_decode():
    assert binary_decode("01001000 01100101 01101100 01101100 01101111") == "Hello"
    assert binary_decode("00110001 00110010 00110011") == "123"

def test_hexadecimal_decode():
    assert hexadecimal_decode("48 65 6c 6c 6f") == "Hello"
    assert hexadecimal_decode("31 32 33") == "123"

def test_octal_decode():
    assert octal_decode("110 145 154 154 157") == "Hello"
    assert octal_decode("61 62 63") == "123"

def test_ascii_decode():
    assert ascii_decode("72 101 108 108 111") == "Hello"
    assert ascii_decode("49 50 51") == "123"

def test_url_decode():
    assert url_decode("Hello%20World%21") == "Hello World!"
    assert url_decode("Python%20is%20awesome") == "Python is awesome"

def test_unicode_point_decode():
    assert unicode_point_decode("0048 0065 006c 006c 006f") == "Hello"
    assert unicode_point_decode("0031 0032 0033") == "123"

def test_base32_decode():
    assert base32_decode("JBSWY3DPEBLW64TMMQ====") == "Hello"
    assert base32_decode("MFRGGZDFMZTWQ2LK") == "123"

def test_base64_decode():
    assert base64_decode("SGVsbG8=") == "Hello"
    assert base64_decode("MTIz") == "123"
