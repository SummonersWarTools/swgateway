from swgateway.api.utils import smon_req_json, make_smon_gw_request

def getRtpvpReplayList(wizard, replay_path, target_wizard_id = None, target_server_id = None):
    body = make_smon_gw_request("getRtpvpReplayList", wizard)
    body['replay_path'] = replay_path
    if target_wizard_id != None: body['target_wizard_id'] = target_wizard_id
    if target_server_id != None: body['target_server_id'] = target_server_id

    response = smon_req_json(wizard.GATEWAY_PATH, body)
    return response

def getRtpvpReplayData(wizard, path, target_wizard_id, target_server_id, replay_rid_ref, is_ranker):
    body = make_smon_gw_request("getRtpvpReplayData", wizard)
    body.update({
        'path': path,
        'target_wizard_id': target_wizard_id,
        'target_server_id': target_server_id,
        'replay_rid_ref': replay_rid_ref,
        'is_ranker': is_ranker
    })
    response = smon_req_json(wizard.GATEWAY_PATH, body)
    return response