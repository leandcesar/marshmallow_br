# -*- coding: utf-8 -*-
import pytest
from marshmallow import Schema, ValidationError

from marshmallow_br.fields import Certificate


class SchemaCertificate(Schema):
    certificate_default = Certificate()
    certificate_with_mask = Certificate(mask=True)
    certificate_without_mask = Certificate(mask=False)


def test_certificate() -> None:
    fake_certificate = "12173901552014167634174940702955"  # from https://www.4devs.com.br/gerador_numero_certidoes
    fake_certificate_mask = "121739.01.55.2014.1.67634.174.9407029-55"

    data = {
        "certificate_default": fake_certificate,
        "certificate_with_mask": fake_certificate,
        "certificate_without_mask": fake_certificate,
    }
    assert SchemaCertificate().load(data) == {
        "certificate_default": fake_certificate_mask,
        "certificate_with_mask": fake_certificate_mask,
        "certificate_without_mask": fake_certificate,
    }

    data = {
        "certificate_default": fake_certificate_mask,
        "certificate_with_mask": fake_certificate_mask,
        "certificate_without_mask": fake_certificate_mask,
    }
    assert SchemaCertificate().load(data) == {
        "certificate_default": fake_certificate_mask,
        "certificate_with_mask": fake_certificate_mask,
        "certificate_without_mask": fake_certificate,
    }

    data = {
        "certificate_default": "123",
        "certificate_with_mask": "123",
        "certificate_without_mask": "123",
    }
    with pytest.raises(ValidationError):
        SchemaCertificate().load(data)
