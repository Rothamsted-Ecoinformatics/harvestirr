"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.random.logic import validators


def test_random_reauired_with_valid_value():
    assert validators.random_required("value") == "value"


def test_random_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.random_required(None)
