import flet


def weather(page: flet.Page) -> None:
    page.title = "Weather"
    page.vertical_alignment = flet.MainAxisAlignment.CENTER
    page.add(flet.Row([flet.Text("Weather")], alignment=flet.MainAxisAlignment.CENTER))
