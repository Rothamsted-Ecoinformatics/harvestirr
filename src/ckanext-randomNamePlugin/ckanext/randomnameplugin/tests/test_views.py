"""Tests for views.py."""

import pytest

import ckanext.randomnameplugin.validators as validators


import ckan.plugins.toolkit as tk


@pytest.mark.ckan_config("ckan.plugins", "randomnameplugin")
@pytest.mark.usefixtures("with_plugins")
def test_randomnameplugin_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("randomnameplugin.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, randomnameplugin!"
