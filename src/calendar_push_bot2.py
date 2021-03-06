﻿# -*- coding: utf-8 -*-

from skype_adapter import SkypeAdapter
from ical_adapter import ICalAdapter
from datetime import date
import skype_config2 as s

def lambda_handler(event, context):
	"""Lambda使う場合のエントリポイント"""
	
	today = date.today()
	message_list =  ICalAdapter().getTodaysExternalEventList(today)

	if message_list:
		message = """今日は君にグッドニュースがあるんだよ ベイビー
チェックしておいてくれたまえ""" + reduce( lambda x,y: x+y, message_list)
		print message
		SkypeAdapter(s).postConversation(message)


if __name__ == "__main__":
	"""コマンド実行のエントリポイント"""
	
	today = date(2016, 8, 1)
	message_list =  ICalAdapter().getTodaysExternalEventList(today)

	if message_list:
		message = """今日は君にグッドニュースがあるんだよ ベイビー
チェックしておいてくれたまえ""" + reduce( lambda x,y: x+y, message_list)
		print message
		SkypeAdapter(s).postConversation(message)

