from swgateway.api.utils import smon_req_json, make_smon_gw_request

def SetWizardName(wizard, wizard_name):
    body = make_smon_gw_request("SetWizardName", wizard)
    body['wizard_name'] = wizard_name
    response = smon_req_json(wizard.GATEWAY_PATH, body)
    return response

def GetWizardInfo(wizard, wizard_id = None):
    body = make_smon_gw_request("GetWizardInfo", wizard)
    if wizard_id != None: body['wizard_id'] = wizard_id
    response = smon_req_json(wizard.GATEWAY_PATH, body)
    return response
    
def GetDailyQuests(wizard):
    body = make_smon_gw_request("GetDailyQuests", wizard)
    response = smon_req_json(wizard.GATEWAY_PATH, body)
    return response
    
def GetCostumeCollectionList(wizard):
    body = make_smon_gw_request("GetCostumeCollectionList", wizard)
    response = smon_req_json(wizard.GATEWAY_PATH, body)
    return response
    
def GetBlockUserList(wizard):
    body = make_smon_gw_request("getBlockUserList", wizard)
    response = smon_req_json(wizard.GATEWAY_PATH, body)
    return response
    
def GetUpdatedDataBeforeWebEvent(wizard):
    body = make_smon_gw_request("getUpdatedDataBeforeWebEvent", wizard)
    response = smon_req_json(wizard.GATEWAY_PATH, body)
    return response
    
def UpdateAchievement(wizard, ach_list):
    body = make_smon_gw_request("UpdateAchievement", wizard)
    body["ach_list"] = ach_list
    response = smon_req_json(wizard.GATEWAY_PATH, body)
    return response
    
def GetUnitStorageList(wizard):
    body = make_smon_gw_request("getUnitStorageList", wizard)
    response = smon_req_json(wizard.GATEWAY_PATH, body)
    return response