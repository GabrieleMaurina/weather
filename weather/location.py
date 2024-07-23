import typing

import geocoder


def get_lat_lon() -> typing.Any:
    res = geocoder.ip("me")
    return res.latlng[0], res.latlng[1], res.address
