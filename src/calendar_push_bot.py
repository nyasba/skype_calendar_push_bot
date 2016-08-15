# -*- coding: utf-8 -*-

from skype_adapter import SkypeAdapter
from ical_adapter import ICalAdapter
from datetime import date

def lambda_handler(event, context):
	"""Lambda使う場合のエントリポイント"""
	
	today = date.today()
	message_list =  ICalAdapter().getTodaysInternalEventList(today)

	if message_list:
		message = "ズバリ、今日はこのイベントがあるでしょう！" + reduce( lambda x,y: x+y, message_list)
		print message
		SkypeAdapter().postConversation(message)


if __name__ == "__main__":
	"""コマンド実行のエントリポイント"""
	
	today = date(2016, 8, 16)
	message_list =  ICalAdapter().getTodaysInternalEventList(today)

	if message_list:
		message = "ズバリ、今日はこのイベントがあるでしょう！" + reduce( lambda x,y: x+y, message_list)
		print message
		SkypeAdapter().postConversation(message)

