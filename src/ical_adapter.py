# -*- coding: utf-8 -*-

import vobject
from datetime import datetime
from datetime import date
from pytz import timezone
import requests
import ical_config as i

class ICalAdapter:
	""" iCalendar形式のデータにアクセスするためのAdapterClass """
	
	def getTodaysInternalEventList(self, today):
		""" 今日開催される内部イベントリストを返却する """
		
		c = vobject.readOne(requests.get(i.URL).text)
		todays_internal_events = [ e for e in c.vevent_list if self.__internal(e) and self.__today(e, today) ]
		for e in todays_internal_events:
			print e.prettyPrint()
		
		return [ self.__convert_message(e)  for e in todays_internal_events ]
	
	def getTodaysExternalEventList(self, today):
		""" 今日開催される外部イベントリストを返却する """
		
		c = vobject.readOne(requests.get(i.URL).text)
		todays_external_events = [ e for e in c.vevent_list if self.__external(e) and self.__today(e, today) ]
		for e in todays_external_events:
			print e.prettyPrint()
		
		return [ self.__convert_message(e)  for e in todays_external_events ]
	
	def __internal(self, event):
		return True if event.x_confluence_subcalendar_type.value == 'custom' else False
	
	def __external(self, event):
		return True if event.x_confluence_subcalendar_type.value == 'other' else False
	
	def __today(self, event, today):
		return self.__today_check(event.dtstart.value, today)
	
	def __today_check(self, start, today):
		""" 今日開催されるイベントかどうか """
		if isinstance(start, datetime):
			start_date = self.__to_jst(start).date()
			return start_date == today
		
		if isinstance(start, date):
			return start == today
		return False
	
	
	def __convert_message(self, event):
		""" イベントを投稿用メッセージに変換する """
		if event.description.value == "" :
			return i.EVENT_FORMAT.format(
				self.__convert_schedule_message(event.dtstart.value, event.dtend.value), 
				event.summary.value
			)
		
		return i.EVENT_FORMAT_WITH_DESCRIPTION.format(
			self.__convert_schedule_message(event.dtstart.value, event.dtend.value), 
			event.summary.value,
			event.description.value
		)
		
	def __convert_schedule_message(self, start, end):
		""" 投稿用メッセージの日付部分を作成する """		
		if isinstance(start, datetime) and isinstance(end, datetime):
			start_jst = self.__to_jst(start)
			end_jst = self.__to_jst(end)
			
			schedule_format = "{:%m/%d %H:%M}-{:%H:%M}" if self.__same_day( start_jst, end_jst ) else "{:%m/%d %H:%M} - {:%m/%d %H:%M}"
			return schedule_format.format( start_jst, end_jst )
		
		if isinstance(start, date) and isinstance(end, date):
			return "{:%m/%d}-{:%m/%d}".format(start, end)
		
		return ""
		
	def __same_day(self, start, end):
		""" startとendが同じ日かどうかを判定する """		
		return True if start.date() == end.date() else False

	def __to_jst(self, dt):
		""" dtのタイムゾーンをJSTに変換する """		
		return dt.astimezone(timezone('Asia/Tokyo'))
