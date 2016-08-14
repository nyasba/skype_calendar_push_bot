# -*- coding: utf-8 -*-

from oauth2client.service_account import ServiceAccountCredentials
from httplib2 import Http
from apiclient.discovery import build
import gcal_config as g

#-----------------------------------------------------------------
# GoogleCalendarからイベント情報を取得する
#-----------------------------------------------------------------
class GoogleCalendarAdapter:
	
	def getTodaysEventList(self):
		# GoogleのOAuth認証(for Server to Server Applications)を行う。
		
		credentials = ServiceAccountCredentials.from_json_keyfile_name(g.JSON_PATH, g.SCOPE)#.create_delegated(g.DELEGATED_ACCOUNT)
		service = build('calendar', 'v3', credentials=credentials)
		print vars(credentials)
		
		events = service.events().list(calendarId=g.CALENDER_ID, maxResults=3).execute()
		print events
		
		return
	
