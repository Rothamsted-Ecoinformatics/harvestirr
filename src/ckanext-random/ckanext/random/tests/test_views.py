"""Tests for views.py."""

import pytest

import ckanext.random.validators as validators


import ckan.plugins.toolkit as tk


@pytest.mark.ckan_config("ckan.plugins", "random")
@pytest.mark.usefixtures("with_plugins")
def test_random_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("random.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, random!"
