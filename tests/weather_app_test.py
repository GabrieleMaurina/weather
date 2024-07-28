import flet
import pytest_mock

import weather_desktop


def test_weather_app(mocker: pytest_mock.MockFixture) -> None:
    page = mocker.Mock(spec=flet.Page)
    weather_desktop.weather_app(page)
    assert page.title == "Weather Desktop"
    assert page.vertical_alignment == flet.MainAxisAlignment.CENTER
    assert page.add.call_args[0][0].controls[0].value
