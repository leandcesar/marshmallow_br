# -*- coding: utf-8 -*-
import pytest
from marshmallow import Schema, ValidationError

from marshmallow_br.fields import CNPJ


class SchemaCNPJ(Schema):
    cnpj_default = CNPJ()
    cnpj_with_mask = CNPJ(mask=True)
    cnpj_without_mask = CNPJ(mask=False)


def test_cnpj() -> None:
    fake_cnpj = "52203670000109"  # from https://www.4devs.com.br/gerador_de_cnpj
    fake_cnpj_mask = "52.203.670/0001-09"

    data = {
        "cnpj_default": fake_cnpj,
        "cnpj_with_mask": fake_cnpj,
        "cnpj_without_mask": fake_cnpj,
    }
    assert SchemaCNPJ().load(data) == {
        "cnpj_default": fake_cnpj_mask,
        "cnpj_with_mask": fake_cnpj_mask,
        "cnpj_without_mask": fake_cnpj,
    }

    data = {
        "cnpj_default": fake_cnpj_mask,
        "cnpj_with_mask": fake_cnpj_mask,
        "cnpj_without_mask": fake_cnpj_mask,
    }
    assert SchemaCNPJ().load(data) == {
        "cnpj_default": fake_cnpj_mask,
        "cnpj_with_mask": fake_cnpj_mask,
        "cnpj_without_mask": fake_cnpj,
    }

    data = {
        "cnpj_default": "123",
        "cnpj_with_mask": "123",
        "cnpj_without_mask": "123",
    }
    with pytest.raises(ValidationError):
        SchemaCNPJ().load(data)
