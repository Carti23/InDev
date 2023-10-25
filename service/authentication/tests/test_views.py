import pytest
from rest_framework import Api


@pytest.mark.django()
def test_register_view():
    payload = dict(
        useraname="harry",
        password1="Dadefo95",
        password2="Dadefo95",
        email="harry@gmail.com",
        first_name="Harry",
        last_name="Potter",
    )

    response = 