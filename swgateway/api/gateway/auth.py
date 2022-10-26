from ..utils import smon_req_json, make_smon_gw_request
from ..constants import SMON_GAME_INDEX, SMON_APP_VERSION, SMON_BATTLE_VERSION

def GuestLogin(wizard):
    login_body = make_smon_gw_request("GuestLogin", wizard)
    login_body.update({
        "game_index": SMON_GAME_INDEX,
        "app_version": SMON_APP_VERSION,
        "uid": wizard.HIVE_USER.HIVE_UID,
        "did": 0,
        "push": 1,
        "is_emulator": 0,
        "is_rooting": 0,
        "is_aop": 0,
        "country": "US",
        "lang": "eng",
        "lang_game": 1,
        "mac_address": "",
        "device_name": "",
        "os_version": "",
        "token": "",
        "idfv": "",
        "adid": "",
        "create_if_not_exist": 1,
        "is_jailbroken": 0,
        "ag_cert_result": 2,
        "ag_ucid": "",
        "app_s_key": "",
        "battle_version": SMON_BATTLE_VERSION
    })
    login_response = smon_req_json(wizard.GATEWAY_PATH, login_body)
    return login_response