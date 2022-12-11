from swgateway.api.utils import smon_req_json, make_smon_gw_request

def ReceiveDailyRewardInactive(wizard):
    body = make_smon_gw_request("receiveDailyRewardInactive", wizard)
    response = smon_req_json(wizard.GATEWAY_PATH, body)
    return response
    
def ReceiveDailyRewardSpecial(wizard):
    body = make_smon_gw_request("ReceiveDailyRewardSpecial", wizard)
    response = smon_req_json(wizard.GATEWAY_PATH, body)
    return response
    
def ReceiveDailyRewardNewUser(wizard):
    body = make_smon_gw_request("ReceiveDailyRewardNewUser", wizard)
    response = smon_req_json(wizard.GATEWAY_PATH, body)
    return response
    
def GetMiscReward(wizard):
    body = make_smon_gw_request("GetMiscReward", wizard)
    response = smon_req_json(wizard.GATEWAY_PATH, body)
    return response