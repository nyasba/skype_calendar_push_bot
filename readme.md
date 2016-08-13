GoogleCalendarから予定を取得し、毎日Skypeへ通知するbot

## 機能

1. ~~CloudWatchEventで以下の機能を持つLambdaFunctionを起動する~~
2. ~~GoogleCalendarから本日の予定を取得する~~
3. 取得した情報を、SkypeへMicrosoftBotFrameworkのRESTAPIで投稿する

## 環境設定

### 取得元のGoogleCalendar設定

未対応


### 通知先のSkype設定

設定ファイルをコピーして、skypeの認証情報などを更新する

```
cp src/skype_config_original.py src/skype_config.py
```



## 実行方法

```
pip install -r requirements.txt -t <this directory>
python src/calendar_push_bot.py 
```

