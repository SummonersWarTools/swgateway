from swgateway.crypto import SWCryptoMgr
from swgateway.api.constants import SWGATEWAY_VERSION_IDX

import json
import requests
import math
import time
from base64 import b64encode, b64decode

def smon_req_json(endpoint, data):
    data["swgateway_version"] = SWGATEWAY_VERSION_IDX
    request_encrypted =  b64encode(SWCryptoMgr.Encrypt(SWCryptoMgr.DEFAULT, json.dumps(data).encode('utf-8'))).decode('utf-8')
    response = requests.post(endpoint, data = request_encrypted)
    return {
        "status": response.status_code,
        "data": json.loads(SWCryptoMgr.Decrypt(SWCryptoMgr.DEFAULT, b64decode(response.content)))
    }

def make_smon_gw_request(command, wizard):
    body = {
        "command": command,
        "proto_ver": wizard.VERSION_DATA['protocol'],
        "infocsv": wizard.VERSION_DATA['infocsv'],
        "channel_uid": wizard.HIVE_USER.HIVE_UID,
        "ts_val": math.floor(time.time())
    }
    if wizard.WIZARD_ID != None: body.update({ "wizard_id": wizard.WIZARD_ID })
    if wizard.SESSION_TOKEN != None: body.update({ "session_key": wizard.SESSION_TOKEN })
    return body