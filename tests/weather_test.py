import flet
import pytest_mock

import weather


def test_weather(mocker: pytest_mock.MockFixture) -> None:
    page = mocker.Mock(spec=flet.Page)
    weather.weather(page)
    assert page.title == "Weather"
    assert page.vertical_alignment == flet.MainAxisAlignment.CENTER
    assert page.add.call_args[0][0].controls[0].value == "Weather"
