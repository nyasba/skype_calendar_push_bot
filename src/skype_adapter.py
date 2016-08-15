# -*- coding: utf-8 -*-

import requests
import json
import skype_config as s

class SkypeAdapter:
	""" Skypeに投稿するためのAdapterClass """
	
	def postConversation(self, message):
		""" Skypeへメッセージを投稿する """
		token = self.__auth()
		self.__post( token, message )

	def __auth(self):
		""" MicrosoftBotFrameworkのOAuthClient認証を行いaccess_tokenを取得する """
		
		headers = { 'Content-Type' : 'application/x-www-form-urlencoded' }
		data = {
			'grant_type' : 'client_credentials',
			'client_id' : s.CLIENT_ID,
			'client_secret' : s.CLIENT_SECRET,
			'scope' : s.SCOPE
		}
		 
		access_token_response = requests.post( s.AUTH_URL, headers=headers, data=data )

		if access_token_response.status_code != 200 :
			print access_token_response.headers
			print access_token_response.text
			raise StandardError('Skype OAuth Failed')
		 
		tokens = json.loads(access_token_response.text)
		return tokens['access_token']
	
	def __post(self, token, message):
		""" MicrosoftBotFrameworkのチャット投稿用RESTAPIを叩く """
		
		headers = { 
			'Authorization' : 'Bearer ' + token,
			'Content-Type' : 'application/json'
		}
		
		data = {
			'type' : 'message/text',
			'text' : message
		}
		
		response = requests.post( s.POST_URL, headers=headers, json=data)
		
		if response.status_code != 201 :
			print response.status_code
			print response.headers
			print response.text
			raise StandardError('Skype Post Failed')
		
		return
