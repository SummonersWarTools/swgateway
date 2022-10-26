from . import constants
from . import utils
from . import gateway

def location():
    locations_data = utils.smon_req_json(constants.SMON_API_LOCATIONS, {})
    return locations_data

def server_status(path = constants.SMON_API_SERVER_STATUS_DEFAULT):
    pass

def version_info(path = constants.SMON_API_VERSIONS_DEFAULT):
    version_data = utils.smon_req_json(path, { "game_index": constants.SMON_GAME_INDEX })
    return version_data