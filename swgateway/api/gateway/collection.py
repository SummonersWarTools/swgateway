from swgateway.api.utils import smon_req_json, make_smon_gw_request

def GetUnitRecommendPage_V2(wizard, unit_master_id, page_number, best):
    body = make_smon_gw_request("GetUnitRecommendPage_V2", wizard)
    body.update({
        'unit_master_id': unit_master_id,
        'page_number': page_number,
        'best': best
    })
    response = smon_req_json(wizard.GATEWAY_PATH, body)
    return response

def GetUnitRecommendFriendUnitList(wizard, unit_master_id):
    body = make_smon_gw_request("GetUnitRecommendFriendUnitList", wizard)
    body.update({
        'unit_master_id': unit_master_id
    })
    response = smon_req_json(wizard.GATEWAY_PATH, body)
    return response

def getUnitRecommendRecentDeckList(wizard, unit_master_id):
    body = make_smon_gw_request("getUnitRecommendRecentDeckList", wizard)
    body.update({
        'unit_master_id': unit_master_id
    })
    response = smon_req_json(wizard.GATEWAY_PATH, body)
    return response

def getUnitStatsRuneInfo(wizard, unit_master_id, request_type):
    body = make_smon_gw_request("getUnitStatsRuneInfo", wizard)
    body.update({
        'unit_master_id': unit_master_id,
        'request_type': request_type
    })
    response = smon_req_json(wizard.GATEWAY_PATH, body)
    return response