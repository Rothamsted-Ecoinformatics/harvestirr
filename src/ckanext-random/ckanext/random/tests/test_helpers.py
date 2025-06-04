"""Tests for helpers.py."""

import ckanext.random.helpers as helpers


def test_random_hello():
    assert helpers.random_hello() == "Hello, random!"
