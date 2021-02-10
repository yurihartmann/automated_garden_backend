from tortoise.fields import *


class TimestampMixin:
    created_at = DatetimeField(null=True, auto_now_add=True)
    modified_at = DatetimeField(null=True, auto_now=True)
