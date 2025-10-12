import os
from iw4m import IW4MWrapper
from t6rcon import PlutoRCON

iw4m = IW4MWrapper(
    base_url  = os.environ["IW4M_URL"],
    server_id = os.environ["IW4M_ID"],
    cookie    = os.environ["IW4M_HEADER"])

server   = iw4m.Server(iw4m)
player   = iw4m.Player(iw4m)
commands = iw4m.Commands(iw4m)

rcon = PlutoRCON(
    ip_addr  = os.environ["RCON_IP"],
    port     = int(os.environ["RCON_PORT"]),
    password = os.environ["RCON_PASSWORD"])