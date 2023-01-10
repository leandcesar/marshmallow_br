# -*- coding: utf-8 -*-
import pytest
from marshmallow import Schema, ValidationError

from marshmallow_br.fields import CPF


class SchemaCPF(Schema):
    cpf_default = CPF()
    cpf_with_mask = CPF(mask=True)
    cpf_without_mask = CPF(mask=False)


def test_cpf() -> None:
    fake_cpf = "98008862068"  # from https://www.4devs.com.br/gerador_de_cpf
    fake_cpf_mask = "980.088.620-68"

    data = {
        "cpf_default": fake_cpf,
        "cpf_with_mask": fake_cpf,
        "cpf_without_mask": fake_cpf,
    }
    assert SchemaCPF().load(data) == {
        "cpf_default": fake_cpf_mask,
        "cpf_with_mask": fake_cpf_mask,
        "cpf_without_mask": fake_cpf,
    }

    data = {
        "cpf_default": fake_cpf_mask,
        "cpf_with_mask": fake_cpf_mask,
        "cpf_without_mask": fake_cpf_mask,
    }
    assert SchemaCPF().load(data) == {
        "cpf_default": fake_cpf_mask,
        "cpf_with_mask": fake_cpf_mask,
        "cpf_without_mask": fake_cpf,
    }

    data = {
        "cpf_default": "123",
        "cpf_with_mask": "123",
        "cpf_without_mask": "123",
    }
    with pytest.raises(ValidationError):
        SchemaCPF().load(data)
