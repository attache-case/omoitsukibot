# coding: utf-8

import os

# botアカウントのトークンを指定
API_TOKEN = os.environ.get('SLACK_API_TOKEN')

# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = "\nあんまり会話は得意じゃないんだ。\n【なにか思いついたら】\nチャンネルに直接\n> おもいつき タイトル\n> 本文\nと投稿すればGithubにIssueを作成するよ。本文の前に改行(Shift+Enter)を忘れないでね。"

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = [
	'plugins',
]