from django.urls import resolve, Resolver404
from django.test import TestCase
import pytest


class HomePageTest(TestCase):
    def test_not_exist_url(self):
        with pytest.raises(Resolver404):
            resolve('/cms/hoge/')

    def test_index_url(self):
        result = resolve('/cms/')
        assert result.url_name == 'index'

    def test_exist_url(self):
        result = resolve('/cms/logs/')
        assert result.url_name == 'life_logs'
