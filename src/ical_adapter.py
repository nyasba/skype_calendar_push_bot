# -*- coding: utf-8 -*-

import vobject
from datetime import datetime
from datetime import date
from pytz import timezone
import requests
import ical_config as i

#-----------------------------------------------------------------
# iCalから今日のイベント一覧を取得する
#-----------------------------------------------------------------
class ICalAdapter:
	
	def getTodaysInternalEventList(self, today):
		
		c = vobject.readOne(requests.get(i.URL).text)
		todays_internal_events = [ e for e in c.vevent_list if self.__internal(e) and self.__today(e, today) ]
		for e in todays_internal_events:
			print e.prettyPrint()
		
		return [ self.__convert_message(e)  for e in todays_internal_events ]
	
	
	def __internal(self, event):
		return True if event.x_confluence_subcalendar_type.value == 'custom' else False
	
	def __external(self, event):
		return True if event.x_confluence_subcalendar_type.value == 'other' else False
	
	def __today(self, event, today):
		return self.__today_check(event.dtstart.value, event.dtend.value, today)
	
	def __today_check(self, start, end, today):
		if isinstance(start, datetime) and isinstance(end, datetime):
			start_date = self.__to_jst(start).date()
			end_date = self.__to_jst(end).date()
			return start_date <= today and today <= end_date
		
		if isinstance(start, date) and isinstance(end, date):
			return start <= today and today <= end
			
		return False
	
	
	def __convert_message(self, event):
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
		
		if isinstance(start, datetime) and isinstance(end, datetime):
			start_jst = self.__to_jst(start)
			end_jst = self.__to_jst(end)
			
			schedule_format = "{:%m/%d %H:%M}-{:%H:%M}" if self.__same_day( start_jst, end_jst ) else "{:%m/%d %H:%M} - {:%m/%d %H:%M}"
			return schedule_format.format( start_jst, end_jst )
		
		if isinstance(start, date) and isinstance(end, date):
			return "{:%m/%d}-{:%m/%d}".format(start, end)
		
		return ""
		
	def __same_day(self, start, end):
		return True if start.date() == end.date() else False

	def __to_jst(self, dt):
		return dt.astimezone(timezone('Asia/Tokyo'))
