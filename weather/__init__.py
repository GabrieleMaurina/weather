import flet

import weather.location


def weather_app(page: flet.Page) -> None:
    lat, lon, address = weather.location.get_lat_lon()
    page.title = "Weather"
    page.vertical_alignment = flet.MainAxisAlignment.CENTER
    page.add(
        flet.Row(
            [flet.Text(f"Weather\n{address}")], alignment=flet.MainAxisAlignment.CENTER
        )
    )
    lat, lon, address = weather.location.get_lat_lon()
