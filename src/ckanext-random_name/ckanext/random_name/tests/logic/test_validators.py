"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.random_name.logic import validators


def test_random_name_reauired_with_valid_value():
    assert validators.random_name_required("value") == "value"


def test_random_name_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.random_name_required(None)
