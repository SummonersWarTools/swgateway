from .utils import smon_req_json
from .constants import SMON_API_LOCATIONS, SMON_API_VERSIONS_DEFAULT, SMON_API_SERVER_STATUS_DEFAULT, SMON_GAME_INDEX

from . import gateway

def location():
    locations_data = smon_req_json(SMON_API_LOCATIONS, {})
    return locations_data

def server_status(path = SMON_API_SERVER_STATUS_DEFAULT):
    pass

def version_info(path = SMON_API_VERSIONS_DEFAULT):
    version_data = smon_req_json(path, { "game_index": SMON_GAME_INDEX })
    return version_data