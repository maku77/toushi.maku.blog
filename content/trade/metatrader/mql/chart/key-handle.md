---
title: "MetaTrader/MQL: チャート上でのキーハンドリング (OnChartEvent)"
linkTitle: "チャート上でのキーハンドリング (OnChartEvent)"
url: "/p/c5z4ka3"
date: "2021-01-30"
tags: ["MetaTrader/MQL"]
---

EA の `OnChartEvent` 関数でチャートイベントをハンドルすると、チャート上でのキーボード入力を取得することができます。
これを利用すると、自作の EA にキーボードショートカット（ホットキー）機能を付けることができます。
例えば、数字の `1` キーを押したときに、0.1 ロットの買い成行注文を出す、といったことができます。

キー入力時は、`OnChartEvent` 関数の `id` パラメータの値は `CHARTEVENT_KEYDOWN` になり、`lparam` パラメータにキーコードが格納されます。
下記のサンプル EA をチャートにアタッチすると、入力したキー情報がチャート上に表示されるようになります。

{{< code lang="cpp" title="Experts/MyEa.mq5" >}}
int OnInit() {
    return INIT_SUCCEEDED;
}

void OnChartEvent(const int id,
                  const long &lparam,
                  const double &dparam,
                  const string &sparam) {
    if (id == CHARTEVENT_KEYDOWN) {
        string key;
        if ('0' <= lparam && lparam <= 'z') {
            key = StringFormat("key=%c(%d)", lparam, lparam);
        } else {
            key = StringFormat("key=%d", lparam);
        }
        Comment("CHARTEVENT_KEYDOWN: ", key);
    }
}
{{< /code >}}

特定のキー（例えば数字の `1` キー）が押されたときに、ユーザーに確認を求めてから処理を行いたい場合は次のようにします。

{{< code lang="cpp" >}}
void OnChartEvent(const int id,
                  const long &lparam,
                  const double &dparam,
                  const string &sparam) {
    if (id == CHARTEVENT_KEYDOWN && lparam == '1') {
        if (MessageBox("Are you sure to buy?", NULL, MB_YESNO) == IDYES) {
            // ここで買う！
            // buyMarketOrder();
        }
    }
}
{{< /code >}}

{{< private >}}
[チャートイベントの種類](https://www.mql5.com/ja/docs/constants/chartconstants/enum_chartevents)
{{< /private >}}

