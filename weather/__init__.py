import flet

import weather.forecast
import weather.location


def weather_app(page: flet.Page) -> None:
    lat, lon, address = weather.location.get_lat_lon()
    curr_temp, min_temp, max_temp = weather.forecast.get_forecast(lat, lon)
    page.title = "Weather"
    page.vertical_alignment = flet.MainAxisAlignment.CENTER
    page.add(
        flet.Row([flet.Text(address, size=50)], alignment=flet.MainAxisAlignment.CENTER)
    )
    page.add(
        flet.Row(
            [flet.Text(f"Temperature: {curr_temp}°F", size=50)],
            alignment=flet.MainAxisAlignment.CENTER,
        )
    )
    page.add(
        flet.Row(
            [flet.Text(f"Min: {min_temp}°F", size=30)],
            alignment=flet.MainAxisAlignment.CENTER,
        )
    )
    page.add(
        flet.Row(
            [flet.Text(f"Max: {max_temp}°F", size=30)],
            alignment=flet.MainAxisAlignment.CENTER,
        )
    )
