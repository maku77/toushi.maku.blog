---
title: "ドラフト: トレステメモ"
url: "/p/zjzevvf"
tags: ["トレステ"]
draft: true
---

- [トレステのトップページ](/p/wjwamw9/)

トレステ雑多メモ
----

- `Volume on Up Ticks` ... 直近の約定値を上回る（または等しい）値で約定した出来高。
- `Number of Up Ticks` ... 直近の約定値を上回る（または等しい）値で約定したティック数。
- 本日の仕掛けがまだないことを調べる
    - `if EntriesToday(Date[0]) < 0 then`
- イントラバーデータ更新有効時に最後のティックのみ何か処理する
    - `if BarStatus(1) = 2 then`（参考 p.148）
- 日足のみトレードを有効にする
    - `If BarType = 2 then`
- 文の順序（EasyLanguage ホームスタディコースより）
    - EasyLanguageプログラムの検証を成功させるための一般的なガイドラインとして、文は
下記の順序で書かれている必要があります（注釈: 意図的に他の順序で文を書く場合もあります）
        - インプット宣言文
        - 変数宣言文
        - 変数代入文
        - プロット文: インジケーター用
        - 売買文: ストラテジー用


統計解析に使える関数
----

- Average / AverageFC ... 平均
- Varianceps ... 分散
- StdDev ... 標準偏差（分散の正の平方根）
- Lowest ... 最小値
- Highest ... 最大値
- Percentile ... パーセンタイル（昇順ソートしたときの％で位置を指定してデータ取得）
- Median ... 中央値


その他
----

- 下記で **板情報** が取得できる？
    - InsideBid: 買い気配
    - InsideAsk: 売り気配
- p.165 ... `BigPointValue` 1ポイント当たりのドル価？
- 属性 `[IntraBarOrderGeneration = TRUE];`

{{< code >}}
If FastAvg Crosses over SlowAvg then Buy 500 shares next bar at market;
{{< /code >}}

同様に　短期の移動平均線が、長期の移動平均線を下に抜いたら　売り　のコードにも追加します

{{< code >}}
If FastAvg Crosses under SlowAvg then Sellshort 500 shares next bar at market;
{{< /code >}}

{{< code >}}
次の足の始値で 100 株の買い注文を生成
Buy 100 shares next bar at market

次の足の始値で 100 株の売り注文を生成
SellShort 100 shares next bar at market

次の足の始値でロングポジションのうち 100 株を決済する
Sell 100 shares total next bar at market
{{< /code >}}

