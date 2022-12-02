from swgateway.api.utils import smon_req_json, make_smon_gw_request

def CheckDarkPortalStatus(wizard):
    chat_body = make_smon_gw_request("CheckDarkPortalStatus", wizard)
    chat_response = smon_req_json(wizard.GATEWAY_PATH, chat_body)
    return chat_response
    
def GetDimensionHolePortalInfo(wizard):
    chat_body = make_smon_gw_request("getDimensionHolePortalInfo", wizard)
    chat_response = smon_req_json(wizard.GATEWAY_PATH, chat_body)
    return chat_response