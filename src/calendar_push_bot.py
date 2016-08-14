# -*- coding: utf-8 -*-

from skype_adapter import SkypeAdapter
from gcal_adapter import GoogleCalendarAdapter

#-----------------------------------------------------------------
# Lambda使う場合のエントリポイント
#-----------------------------------------------------------------
def lambda_handler(event, context):

	return

#-----------------------------------------------------------------
# コマンド実行のエントリポイント
#-----------------------------------------------------------------
if __name__ == "__main__":
	GoogleCalendarAdapter().getTodaysEventList()
	#SkypeAdapter().postConversation('やっとできたぞー！')

