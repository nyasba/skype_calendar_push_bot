GoogleCalendar����\����擾���A����Skype�֒ʒm����bot

## �@�\

1. ~~CloudWatchEvent�ňȉ��̋@�\������LambdaFunction���N������~~
2. ~~GoogleCalendar����{���̗\����擾����~~
3. �擾���������ASkype��MicrosoftBotFramework��RESTAPI�œ��e����

## ���ݒ�

### �擾����iCal�ݒ�

���Ή�


### MicrosoftBotFramework��MyBot�̓o�^���s��

SkypeBotFramework��MicrosoftBotFramework�ɓ��������̂ŁA�ȉ�����o�^����
https://dev.botframework.com/

1. �uRegister a bot�v���j���[
2. Icon��Name���ق��̐l���猩������̂ɂȂ�̂�Bot�̃L�����ɂ��������̂ɂ���
3. MicrosoftAppId��Password�𐶐�����i����͌�Ŏg���̂ŏd�v�j
4. Publisher profile�͌��J���Ȃ��O��œK����
5. ���̑����G���[���o�Ȃ��悤�ɓK���ɋL�����ēo�^
6. MyBot�̓o�^������������AChannels��Skype��Edit�ŁuGroup messaging�v��ON�ɂ��Ă���
7. Channels��Skype�́uAdd to Skype�v��Bot�ƂȂ���
8. �ʒm�������`���b�g���[����Bot�����҂���
9. �ʒm�������`���b�g���[���Łu/get name�v�Ƃ����R�}���h���������AconversationID���擾����

### �ʒm���Skype�ݒ�

�ݒ�t�@�C�����R�s�[���āAskype�̔F�؏��Ⓤ�e��̃`���b�g���[��(conversationID)���X�V����

```
cp src/skype_config_original.py src/skype_config.py
```



## ���s���@

```
pip install -r requirements.txt -t ./src
python src/calendar_push_bot.py 
```

