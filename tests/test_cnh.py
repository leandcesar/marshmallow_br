# -*- coding: utf-8 -*-
import pytest
from marshmallow import Schema, ValidationError

from marshmallow_br.fields import CNH


class SchemaCNH(Schema):
    cnh_default = CNH()
    cnh_with_mask = CNH(mask=True)
    cnh_without_mask = CNH(mask=False)


def test_cnh() -> None:
    fake_cnh = "64076917022"  # from https://www.4devs.com.br/gerador_de_cnh
    fake_cnh_mask = "64076917022"

    data = {
        "cnh_default": fake_cnh,
        "cnh_with_mask": fake_cnh,
        "cnh_without_mask": fake_cnh,
    }
    assert SchemaCNH().load(data) == {
        "cnh_default": fake_cnh_mask,
        "cnh_with_mask": fake_cnh_mask,
        "cnh_without_mask": fake_cnh,
    }

    data = {
        "cnh_default": fake_cnh_mask,
        "cnh_with_mask": fake_cnh_mask,
        "cnh_without_mask": fake_cnh_mask,
    }
    assert SchemaCNH().load(data) == {
        "cnh_default": fake_cnh_mask,
        "cnh_with_mask": fake_cnh_mask,
        "cnh_without_mask": fake_cnh,
    }

    data = {
        "cnh_default": "123",
        "cnh_with_mask": "123",
        "cnh_without_mask": "123",
    }
    with pytest.raises(ValidationError):
        SchemaCNH().load(data)
