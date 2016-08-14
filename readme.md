GoogleCalendarから予定を取得し、毎日Skypeへ通知するbot

## 機能

1. ~~CloudWatchEventで以下の機能を持つLambdaFunctionを起動する~~
2. ~~GoogleCalendarから本日の予定を取得する~~
3. 取得した情報を、SkypeへMicrosoftBotFrameworkのRESTAPIで投稿する

## 環境設定

### 取得元のiCal設定

未対応


### MicrosoftBotFrameworkでMyBotの登録を行う

SkypeBotFrameworkはMicrosoftBotFrameworkに統合されるので、以下から登録する
https://dev.botframework.com/

1. 「Register a bot」メニュー
2. IconとNameがほかの人から見えるものになるのでBotのキャラにあったものにする
3. MicrosoftAppIdとPasswordを生成する（これは後で使うので重要）
4. Publisher profileは公開しない前提で適当に
5. その他もエラーが出ないように適当に記入して登録
6. MyBotの登録が完了したら、ChannelsのSkypeのEditで「Group messaging」をONにしておく
7. ChannelsのSkypeの「Add to Skype」でBotとつながる
8. 通知したいチャットルームにBotを招待する
9. 通知したいチャットルームで「/get name」というコマンドをたたき、conversationIDを取得する

### 通知先のSkype設定

設定ファイルをコピーして、skypeの認証情報や投稿先のチャットルーム(conversationID)を更新する

```
cp src/skype_config_original.py src/skype_config.py
```



## 実行方法

```
pip install -r requirements.txt -t ./src
python src/calendar_push_bot.py 
```

