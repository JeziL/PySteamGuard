# PySteamGuard

Get Steam guard code without the Mobile Authenticator app.

## Usage

First of all, you need to get your **shared secret**. Refer to [this article](https://github.com/SteamTimeIdler/stidler/wiki/Getting-your-%27shared_secret%27-code-for-use-with-Auto-Restarter-on-Mobile-Authentication).

Then put your shared secret to [`config.py`](config.py) and run [`guard.py`](guard.py) to see if it works.

The main logic is in [`utils.py`](utils.py), you can use it in any convenient way (eg. make an [Alfred workflow](https://www.alfredapp.com/workflows/)).

## Thanks to

- [SteamAuth](https://github.com/geel9/SteamAuth)
