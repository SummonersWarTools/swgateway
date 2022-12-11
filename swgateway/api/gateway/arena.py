from swgateway.api.utils import smon_req_json, make_smon_gw_request

def GetArenaLog(wizard):
    body = make_smon_gw_request("GetArenaLog", wizard)
    response = smon_req_json(wizard.GATEWAY_PATH, body)
    return response