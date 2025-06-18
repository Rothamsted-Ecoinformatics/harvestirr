"""Tests for helpers.py."""

import ckanext.random_name.helpers as helpers


def test_random_name_hello():
    assert helpers.random_name_hello() == "Hello, random_name!"
