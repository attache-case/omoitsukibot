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
	# もしかして、botがスレッドに参加すれば上手くIssueにコメントできるかもしれない

@listen_to(r'^【おもいつき】.*')
@listen_to(r'^おもいつき.*')
@listen_to(r'^【思いつき】.*')
@listen_to(r'^思いつき.*')
@listen_to(r'^【思い付き】.*')
@listen_to(r'^思い付き.*')
def listen_func(message):
	text = message.body["text"]
	text = text.replace('【おもいつき】', '【おもいつき】 ')
	text = text.replace('【思いつき】', '【思いつき】 ')
	text = text.replace('【思い付き】', '【思い付き】 ')
	text = text.replace('。', '。 ')
	text = text.replace('．', '． ')
	string_list = text.split(None, 2)
	string_list_len = len(string_list)
	if string_list_len == 0:
		message.reply("Couldn't parse correctly(len(string_list)=0).\nSomething is wrong with my program.")
	elif string_list_len == 1:
		message.reply("Please write the title and content of your OMOITSUKI.")
	else:
		if string_list_len == 2:
			string_list.append(string_list[1]) # タイトルしか無かったらIssueの本文をタイトルと同一にする。
		else: # string_list_len == 3
			string_list[1] = string_list[1].replace('。', '')
			string_list[1] = string_list[1].replace('．', '')
		print("title: {0}".format(string_list[1]))
		print("content: {0}".format(string_list[2]))
		GHF.make_github_issue(string_list[1], string_list[2], os.environ.get('GITHUB_USERNAME'), None, [])
		message.react('octocat') # notice that the OMOITSUKI has been successfully posted to Github.