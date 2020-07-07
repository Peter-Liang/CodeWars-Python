"""
3 kyu Metaclasses - Simple Django Models
https://www.codewars.com/kata/54b26b130786c9f7ed000555/train/python
"""

import datetime
import re
from typing import Any


class ValidationError(Exception):
    pass


class ValidationField:
    def __init__(self, default=None, blank=False, **kwargs):
        self.default = default
        self.blank = blank
        self.__dict__.update(kwargs)

    def validate(self, val):
        if val is None and self.blank is False:
            raise ValidationError


class CharField(ValidationField):
    def __init__(self, min_length=0, max_length=None, **kwargs):
        super().__init__(**kwargs)
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, val):
        super().validate(val)

        if val is None:
            return

        if not isinstance(val, str):
            raise ValidationError

        if self.min_length is not None and len(val) < self.min_length:
            raise ValidationError

        if self.max_length is not None and self.max_length < len(val):
            raise ValidationError


class IntegerField(ValidationField):
    def __init__(self, min_value=None, max_value=None, **kwargs):
        super().__init__(**kwargs)
        self.min_value = min_value
        self.max_value = max_value

    def validate(self, val):
        super().validate(val)

        if val is None:
            return

        if isinstance(val, bool):
            raise ValidationError

        if not isinstance(val, int):
            raise ValidationError

        if self.min_value is not None and val < self.min_value:
            raise ValidationError

        if self.max_value is not None and self.max_value < val:
            raise ValidationError


class BooleanField(ValidationField):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate(self, val):
        super().validate(val)

        if val is None:
            return

        if not isinstance(val, bool):
            raise ValidationError


class DateTimeField(ValidationField):
    def __init__(self, default=None, auto_now=False, **kwargs):
        super().__init__(**kwargs)
        self.auto_now = auto_now
        self._default = default

    def __getattribute__(self, name: str) -> Any:
        if name == 'default':
            if self._default is None and self.auto_now is True:
                return datetime.datetime.now()
            else:
                return self._default
        return super().__getattribute__(name)

    def validate(self, val):
        super().validate(val)

        if val is None:
            return

        if not isinstance(val, datetime.datetime):
            raise ValidationError


class EmailField(ValidationField):
    def __init__(self, min_length=0, max_length=None, **kwargs):
        super().__init__(**kwargs)
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, val):
        super().validate(val)

        if val is None:
            return

        if not isinstance(val, str):
            raise ValidationError

        if self.min_length is not None and len(val) < self.min_length:
            raise ValidationError

        if self.max_length is not None and self.max_length < len(val):
            raise ValidationError

        if not re.match(r"[^@]+@[^@]+\.[^@]+", val):
            raise ValidationError


class Model:
    def __init__(self, **kwargs):
        for d in [d for d in dir(self.__class__) if d.startswith('_f_')]:
            attr = getattr(self.__class__, d)
            setattr(self, d[3:], attr.default)

        for k, v in kwargs.items():
            setattr(self, k, v)

    def __init_subclass__(cls) -> None:
        for d in [d for d in dir(cls) if not d.startswith('_')]:
            attr = getattr(cls, d)
            if isinstance(attr, (CharField, EmailField,
                                 IntegerField, BooleanField, DateTimeField)):
                delattr(cls, d)
                setattr(cls, '_f_' + d, attr)
        super().__init_subclass__()

    def validate(self):
        for d in [d for d in dir(self.__class__) if d.startswith('_f_') and hasattr(self, d[3:])]:
            class_attr = getattr(self.__class__, d)
            instance_attr = getattr(self, d[3:])
            class_attr.validate(instance_attr)
