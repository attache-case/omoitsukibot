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

# 「おもいつき」の書き方を質問されたと思ったら、「おもいつき」の書き方を答える
@respond_to('フォーマット')
@respond_to('おもいつき')
@respond_to('思いつき')
@respond_to('思い付き')
@respond_to('書き方')
def mention_omoitsuki_format(message):
	message.reply('\nおもいつき投稿のフォーマットは\n> おもいつき タイトル\n> 本文\nだよ。本文の前に改行(Shift+Enter)を忘れないでね。')
	# もしかして、botがスレッドに参加すれば上手くIssueにコメントできるかもしれない

@respond_to('詳しく')
@respond_to('くわしく')
def mention_omoitsuki_format_detail(message):
	message.reply('\nおもいつき投稿フォーマットの細かい仕様について。\n文頭にある、「おもいつき/思いつき/思い付き」に反応するよ。\nその後に何でもいいから区切り文字を挟んでからタイトルを書いてほしいな。\nタイトルの後には必ず改行(Shift+Enter)をしてから本文を書いてね。\nちなみに、文頭が「【おもいつき/思いつき/思い付き】」の時は、タイトルの前に区切り文字は要らないよ。')

@listen_to(r'^【おもいつき】.*')
@listen_to(r'^おもいつき\s+\S.*')
@listen_to(r'^【思いつき】.*')
@listen_to(r'^思いつき\s+\S.*')
@listen_to(r'^【思い付き】.*')
@listen_to(r'^思い付き\s+\S.*')
def listen_func(message):
	print("MESSAGE->")
	print(message.body)
	print("<-MESSAGE")
	text = message.body["text"]
	text = text.replace('【おもいつき】', '【おもいつき】 ')
	text = text.replace('【思いつき】', '【思いつき】 ')
	text = text.replace('【思い付き】', '【思い付き】 ')
	string_list = text.split(None, 1)
	string_list_len = len(string_list)
	if string_list_len == 0:
		message.reply("おもいつきに反応したつもりが、my_mention.pyにてstring_list_len==0となっている。何かがおかしい。")
	elif string_list_len == 1:
		message.reply("おもいつきの投稿かな？\n文頭に単語「おもいつき」「思いつき」「思い付き」が含まれていたけれど、タイトルと本文が見当たらなかったよ。\nおもいつき投稿のフォーマットは\n> おもいつき タイトル\n> 本文\nだよ。本文の前に改行(Shift+Enter)を忘れないでね。")
	else: # string_list_len == 2 -> at least there is a title of the OMOITSUKI
		title_body = string_list[1].split('\n', 1)
		if len(title_body) == 1:
			title_body.append(title_body[0]) # タイトルしか無かったらIssueの本文をタイトルと同一にする。
		print("title: {0}".format(title_body[0]))
		print("content: {0}".format(title_body[1]))
		GHF.make_github_issue(title_body[0], title_body[1], os.environ.get('GITHUB_USERNAME'), None, [])
		message.react('octocat') # notice that the OMOITSUKI has been successfully posted to Github.