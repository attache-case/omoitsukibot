# coding: utf-8

# botアカウントのトークンを指定
API_TOKEN = SLACK_API_TOKEN

# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = "\nリプライには対応していません。\nチャンネルに直接\n> おもいつき タイトル 本文\nと投稿すればGithubにIssueを作成します。"

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = [
	'plugins',
]