# Please change your setting. 
CLIENT_ID = '** YOUR CLIENT_ID **'
CLIENT_SECRET = '** YOUR CLIENT_SECRET **'
TARGET_CHAT = '** YOUR CHATROOM **'

AUTH_URL = 'https://login.microsoftonline.com/common/oauth2/v2.0/token'
SCOPE = 'https://graph.microsoft.com/.default'
POST_URL = 'https://api.skype.net/v3/conversations/' + TARGET_CHAT + '/activities/'