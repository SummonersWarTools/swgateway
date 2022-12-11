from swgateway.api.utils import smon_req_json, make_smon_gw_request

def CheckDarkPortalStatus(wizard):
    body = make_smon_gw_request("CheckDarkPortalStatus", wizard)
    response = smon_req_json(wizard.GATEWAY_PATH, body)
    return response
    
def GetDimensionHolePortalInfo(wizard):
    body = make_smon_gw_request("getDimensionHolePortalInfo", wizard)
    response = smon_req_json(wizard.GATEWAY_PATH, body)
    return response