from hive.auth import HiveGuestUser
from . import regions
from . import api
from .exceptions import SmonException

# base class for different wizard authentication methods
class Wizard:
    SESSION_TOKEN = None
    WIZARD_ID = None
    REGION = regions.GLOBAL
    HIVE_USER = None

    GATEWAY_PATH = None
    VERSION_PATH = None
    STATUS_PATH = None

    VERSION_DATA = None

    def __init__(self, hive_user, token = None, wizard_id = None):
        self.HIVE_USER = hive_user
        self.SESSION_TOKEN = token
        self.WIZARD_ID = wizard_id

    def set_region(self, region):
        self.REGION = region

    def fetch_urls(self):
        if self.REGION == None: raise Exception("Attempted to fetch URLs for a Wizard with an invalid region")
        # fetch location data
        locations_data = api.location()
        if locations_data['status'] != 200: raise SmonException("Failed to execute request to fetch URLs from location_c2")
        locations_data = locations_data['data']
        # fetch data for specified region
        region_data = list(filter(lambda x: x['server_id'] == self.REGION, locations_data['server_url_list']))
        if len(region_data) == 0: raise SmonException(f"Could not retrieve server base URLs for region {self.REGION}")
        # save paths for API calls in this region
        self.GATEWAY_PATH = region_data[0]['gateway']
        self.VERSION_PATH = region_data[0]['version']
        self.STATUS_PATH = region_data[0]['status']

    def fetch_versions(self):
        # pull version information
        versions_data = api.version_info(path = self.VERSION_PATH)
        if versions_data['status'] != 200: raise SmonException("Failed to execute request to check game versions during authenticate()")
        versions_data = versions_data['data']['version_data']
        # save version information for future requests
        self.VERSION_DATA = {}
        for data in versions_data:
            self.VERSION_DATA[data['topic']] = data['version']

    def authenticate(self):
        raise NotImplementedError

# represents a wizard which will authenticate to SW using GuestLogin
class WizardGuest(Wizard):

    def __init__(self, hive_user, token = None, wizard_id = None):
        if not isinstance(hive_user, HiveGuestUser): raise Exception("WizardGuest must be backed by a HiveGuestUser")
        super().__init__(hive_user, token, wizard_id)
    
    # authentication using GuestLogin
    def authenticate(self):
        # retrieve URLs for specified region if not already pulled
        if self.GATEWAY_PATH == None: super().fetch_urls()
        # retrieve version information if not already pulled
        if self.VERSION_DATA == None: super().fetch_versions()

        # execute GuestLogin API call
        login_data = api.gateway.GuestLogin(self)
        if login_data['status'] != 200 or login_data['data']['ret_code'] != 0: raise SmonException(f"Failed to login to Summoners War API via GuestLogin method, status={login_data['status']}, return={login_data['data']['ret_code']}")
        self.SESSION_TOKEN = login_data['data']['session_key']
        self.WIZARD_ID = login_data['data']['wizard_id']