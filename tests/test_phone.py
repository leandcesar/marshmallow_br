# -*- coding: utf-8 -*-
import pytest
from marshmallow import Schema, ValidationError

from marshmallow_br.fields import Phone


class SchemaPhone(Schema):
    phone_default = Phone(require_ddi=False, require_ddd=False)
    phone_with_mask = Phone(require_ddi=False, require_ddd=False, mask=True)
    phone_without_mask = Phone(require_ddi=False, require_ddd=False, mask=False)


class SchemaPhoneRequiredDDD(Schema):
    phone_default = Phone(require_ddi=False, require_ddd=True)
    phone_with_mask = Phone(require_ddi=False, require_ddd=True, mask=True)
    phone_without_mask = Phone(require_ddi=False, require_ddd=True, mask=False)


class SchemaPhoneFullRequired(Schema):
    phone_default = Phone(require_ddi=True, require_ddd=True)
    phone_with_mask = Phone(require_ddi=True, require_ddd=True, mask=True)
    phone_without_mask = Phone(require_ddi=True, require_ddd=True, mask=False)


def test_phone() -> None:
    fake_phone = "999999999"
    fake_phone_mask = "99999-9999"

    data = {
        "phone_default": fake_phone,
        "phone_with_mask": fake_phone,
        "phone_without_mask": fake_phone,
    }
    assert SchemaPhone().load(data) == {
        "phone_default": fake_phone_mask,
        "phone_with_mask": fake_phone_mask,
        "phone_without_mask": fake_phone,
    }

    data = {
        "phone_default": fake_phone_mask,
        "phone_with_mask": fake_phone_mask,
        "phone_without_mask": fake_phone_mask,
    }
    assert SchemaPhone().load(data) == {
        "phone_default": fake_phone_mask,
        "phone_with_mask": fake_phone_mask,
        "phone_without_mask": fake_phone,
    }

    data = {
        "phone_default": "123",
        "phone_with_mask": "123",
        "phone_without_mask": "123",
    }
    with pytest.raises(ValidationError):
        SchemaPhone().load(data)


def test_phone_required_ddd() -> None:
    fake_phone = "11999999999"
    fake_phone_mask = "(11) 99999-9999"

    data = {
        "phone_default": fake_phone,
        "phone_with_mask": fake_phone,
        "phone_without_mask": fake_phone,
    }
    assert SchemaPhoneRequiredDDD().load(data) == {
        "phone_default": fake_phone_mask,
        "phone_with_mask": fake_phone_mask,
        "phone_without_mask": fake_phone,
    }

    data = {
        "phone_default": fake_phone_mask,
        "phone_with_mask": fake_phone_mask,
        "phone_without_mask": fake_phone_mask,
    }
    assert SchemaPhoneRequiredDDD().load(data) == {
        "phone_default": fake_phone_mask,
        "phone_with_mask": fake_phone_mask,
        "phone_without_mask": fake_phone,
    }

    data = {
        "phone_default": "123",
        "phone_with_mask": "123",
        "phone_without_mask": "123",
    }
    with pytest.raises(ValidationError):
        SchemaPhoneRequiredDDD().load(data)


def test_phone_full_required() -> None:
    fake_phone = "5511999999999"
    fake_phone_mask = "+55 (11) 99999-9999"

    data = {
        "phone_default": fake_phone,
        "phone_with_mask": fake_phone,
        "phone_without_mask": fake_phone,
    }
    assert SchemaPhoneFullRequired().load(data) == {
        "phone_default": fake_phone_mask,
        "phone_with_mask": fake_phone_mask,
        "phone_without_mask": fake_phone,
    }

    data = {
        "phone_default": fake_phone_mask,
        "phone_with_mask": fake_phone_mask,
        "phone_without_mask": fake_phone_mask,
    }
    assert SchemaPhoneFullRequired().load(data) == {
        "phone_default": fake_phone_mask,
        "phone_with_mask": fake_phone_mask,
        "phone_without_mask": fake_phone,
    }

    data = {
        "phone_default": "123",
        "phone_with_mask": "123",
        "phone_without_mask": "123",
    }
    with pytest.raises(ValidationError):
        SchemaPhoneFullRequired().load(data)
