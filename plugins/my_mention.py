# coding: utf-8

import os
import plugins.Github_func as GHF

from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ

# @respond_to('string')     bot宛のメッセージ
#                           stringは正規表現が可能 「r'string'」
# @listen_to('string')      チャンネル内のbot宛以外の投稿
#                           @botname: では反応しないことに注意
#                           他の人へのメンションでは反応する
#                           正規表現可能
# @default_reply()          DEFAULT_REPLY と同じ働き
#                           正規表現を指定すると、他のデコーダにヒットせず、
#                           正規表現にマッチするときに反応
#                           ・・・なのだが、正規表現を指定するとエラーになる？

# message.reply('string')   @発言者名: string でメッセージを送信
# message.send('string')    string を送信
# message.react('icon_emoji')  発言者のメッセージにリアクション(スタンプ)する
#                               文字列中に':'はいらない
@respond_to('メンション')
def mention_func(message):
	message.reply('私にメンションと言ってどうするのだ') # メンション
	# もしかして、botがスレッドに参加すれば上手くいくかもしれない

@listen_to(r'^【おもいつき】\s+\S.*')
@listen_to(r'^おもいつき\s+\S.*')
def listen_func(message):
	text = message.body["text"]
	string_list = text.split(None, 2)
	string_list_len = len(string_list)
	if string_list_len == 0:
		message.send("Couldn't parse correctly(len(string_list)=0).\nSomething is wrong with my program.")
	elif string_list_len == 1:
		message.send("Please write the content of your OMOITSUKI.")
	elif string_list_len == 2:
		string_list.append(string_list[1]) # Issueの本文と内容を同一にする。
	# print(text)
	# message.send('誰かがおもいつきを投稿したようだ') # ただの投稿
	# message.reply('君だね？')              # メンション
	# message.send('内容は：' + text)
	print("title: {0}".format(string_list[1]))
	print("content: {0}".format(string_list[2]))
	GHF.make_github_issue(string_list[1], string_list[2], os.environ.get('GITHUB_USERNAME'), None, [])
	message.react('octocat')