#!python
# coding: utf-8

"""
Tests for Main.py
"""

import pytest
# other imports


# Fixtures


@pytest.fixture()
def fixture_name():
    return ''


# Tests


class TestCase1:
    def test_situation_1(self, fixture_name):
        assert fixture_name == ''

    def test_situation_1_error(self, fixture_name):
        with pytest.raises(ValueError):
            int(fixture_name)
