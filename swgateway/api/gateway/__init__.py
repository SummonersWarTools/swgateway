from .auth import GuestLogin, CheckLoginBlock
from .chat import GetChatServerInfo
from .wizard import GetWizardInfo, GetDailyQuests, GetCostumeCollectionList, GetBlockUserList, GetUpdatedDataBeforeWebEvent, GetUnitStorageList, UpdateAchievement, SetWizardName
from .dungeon import CheckDarkPortalStatus, GetDimensionHolePortalInfo
from .reward import ReceiveDailyRewardSpecial, ReceiveDailyRewardInactive, GetMiscReward, ReceiveDailyRewardNewUser
from .arena import GetArenaLog
from .collection import GetUnitRecommendPage_V2, GetUnitRecommendFriendUnitList, getUnitRecommendRecentDeckList, getUnitStatsRuneInfo
from .rtpvp import getRtpvpReplayData, getRtpvpReplayList