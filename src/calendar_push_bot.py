# -*- coding: utf-8 -*-

from skype_adapter import SkypeAdapter
from ical_adapter import ICalAdapter
from datetime import date

#-----------------------------------------------------------------
# Lambda使う場合のエントリポイント
#-----------------------------------------------------------------
def lambda_handler(event, context):

	today = date.today
	message_list =  ICalAdapter().getTodaysInternalEventList(today)

	if message_list:
		message = "ズバリ、今日はこのイベントがあるでしょう！" + reduce( lambda x,y: x+y, message_list)
		print message
		SkypeAdapter().postConversation(message)

#-----------------------------------------------------------------
# コマンド実行のエントリポイント
#-----------------------------------------------------------------
if __name__ == "__main__":
	
	today = date(2016, 8, 16)
	message_list =  ICalAdapter().getTodaysInternalEventList(today)

	if message_list:
		message = "ズバリ、今日はこのイベントがあるでしょう！" + reduce( lambda x,y: x+y, message_list)
		print message
		SkypeAdapter().postConversation(message)

