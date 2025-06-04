"""Tests for helpers.py."""

import ckanext.randomnameplugin.helpers as helpers


def test_randomnameplugin_hello():
    assert helpers.randomnameplugin_hello() == "Hello, randomnameplugin!"
