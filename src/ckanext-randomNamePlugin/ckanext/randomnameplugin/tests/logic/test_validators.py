"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.randomnameplugin.logic import validators


def test_randomnameplugin_reauired_with_valid_value():
    assert validators.randomnameplugin_required("value") == "value"


def test_randomnameplugin_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.randomnameplugin_required(None)
