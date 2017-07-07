# How to contribute
1. Fork it ( https://github.com/attache-case/omoitsukibot/fork )
2. Create your feature branch (git checkout -b my-new-feature)
3. Commit your changes (git commit -am 'Add some feature')
4. Push to the branch (git push origin my-new-feature)
5. Create new Pull Request

# ファイル構成

<pre>
omoitsukibot <small># ルートディレクトリ。名前は任意。</small>
├─ run.py               <small># bot本体。これを実行する。</small>
├─ slackbot_settings.py <small># botに関する設定(デフォルトリプライはここ)</small>
├─ plugins <small><strong># botの機能はこのディレクトリに追加する</strong></small>
|├─ __init__.py    <small># モジュールを示すもの。空で良い。</small>
|├─ my_mention.py  <small># Slackの発言に対する反応を規定するもの。</small>
|└─ Github_func.py <small># GitHubに投稿する機能をまとめたもの。</small>
|<small>(以下はherokuでappを動かすためのファイル)</small>
├─ Procfile         <small># heroku上のプロセスを定義</small>
├─ requirements.txt <small># Pythonの依存ライブラリの定義</small>
└─ runtime.txt      <small># 実行するPythonのバージョンの定義</small>
</pre>

以下、随時更新
