# whale-graph

[whale-api](https://github.com/haru-sushiring/whale-api)で取得したビットコインのトランザクションから、「不明アドレスから取引所へのBTC移動量」「取引所から不明アドレスへのBTC移動量」を取り出し、グラフ化したWebアプリケーションです。

apiの無料枠は50万ドル以上の移動量に絞られているため、大口投資家の動きが丸わかりです。今は取引所にお金が流れているのか、個人のウォレットに流れているのかがひと目で分かります。ぜひ利用して儲けちゃってください笑

## 動かし方
1. Pythonの仮想環境をつくる（venv）
2. pip install -r requirements.txt
3. 「.env」ファイルを作成する
4. config＞settings.pyの修正（SECRET_KEY、ALLOWED_HOSTS、DATABASES）
5. settings.pyの情報、PostgreSQLの情報（USER、PASSWORD、HOST、PORT、DATABASE）、最新のタイムスタンプTIMESTAMPを「.env」に書いておきます。
6. python manage.py runserver　で動くと思います。。。

## URL
[https://whale-analytics.com/](https://whale-analytics.com/)

## グラフ化するメリット
* 分析しやすくなる
* ビットコインを売買するタイミングが分かる
* みんな儲かる

## 使用した技術
* Python 3.10.8
* Django 4.1.2
* AWS EC2（Amazon Linux2）
* AWS RDS PostgreSQL 13.7
* AWS ElasticIP
* Nginx
* uWSGI 2.0.21
* Certbot（SSL認証書を発行）

ドメインはお名前.comで取得したため、「Route 53」は使用しませんでした。

## 参考にしたサイト
[Django+Nginx+uWSGI+EC2+PostgreSQLのWebアプリ作成まとめ](https://sushiringblog.com/django-nginx-uwsgi)の記事にまとめました。
皆さまありがとうございました！
