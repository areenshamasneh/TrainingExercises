import re
from django.urls import register_converter


class YearConverter:
    regex = r'(\d{1,2}|\d{4})'

    def to_python(self, value):
        year = int(value)
        if year < 100:
            year += 2000
        return year

    def to_url(self, value):
        return str(value)


register_converter(YearConverter, 'yyyy')
