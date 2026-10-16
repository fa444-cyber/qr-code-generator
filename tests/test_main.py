"""Tests for the QR Code Generator."""

import pytest

from main import create_directory, generate_qr_code, is_valid_url


@pytest.mark.parametrize("url, expected", [
    ("http://www.njit.edu", True),
    ("https://github.com/kaw393939", True),
    ("not a url", False),
    ("", False),
])
def test_is_valid_url(url, expected):
    assert is_valid_url(url) is expected


def test_generate_qr_code_creates_a_png_file(tmp_path):
    target = tmp_path / "code.png"
    generate_qr_code("http://www.njit.edu", target)
    assert target.exists()
    assert target.stat().st_size > 0


def test_generate_qr_code_skips_invalid_urls(tmp_path):
    target = tmp_path / "code.png"
    generate_qr_code("not a url", target)
    assert not target.exists()


def test_create_directory_makes_missing_folders(tmp_path):
    target = tmp_path / "a" / "b"
    create_directory(target)
    assert target.is_dir()