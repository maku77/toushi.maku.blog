---
title: "MetaTrader/MQL: 注文を出す - MqlTradeResult構造体の詳細 (MT5)"
linkTitle: "注文を出す - MqlTradeResult構造体の詳細 (MT5)"
url: "/p/i5iu7ht"
date: "2021-01-24"
tags: ["MetaTrader/MQL"]
weight: 2
draft: true
---

MT5 の OrderSend 関数
----

MT5 で注文を出すには [OrderSend 関数](https://www.mql5.com/en/docs/trading/ordersend)（[日本語](https://www.mql5.com/ja/docs/trading/ordersend)）を使用します。

{{< code lang="cpp" title="MT5 の OrderSend 関数" >}}
bool OrderSend(
  MqlTradeRequest& request,  // 注文内容
  MqlTradeResult&  result    // 注文結果
)
{{< /code >}}

ここでは、注文結果が格納される [MqlTradeResult 構造体](https://www.mql5.com/en/docs/constants/structures/mqltraderesult)（[日本語](https://www.mql5.com/ja/docs/constants/structures/mqltraderesult)）について説明します。


MqlTradeResult 構造体
----

`MqlTraderResult` 構造体には次のようなフィールドが定義されています。
各フィールドにどのような値を設定すべきかを順に説明していきます。

{{< code lang="cpp" title="MqlTradeResult 構造体" >}}
struct MqlTradeResult {
  uint    retcode;  // 操作のリターンコード
  ulong   deal;     // 実行された場合の 約定チケット
  ulong   order;    // 注文された場合のチケット
  double  volume;   // ブローカーによって確認された約定ボリューム
  double  price;    // ブローカーによって確認された約定価格
  double  bid;      // 現在の売値
  double  ask;      // 現在の買値
  string  comment;  // 操作に対するブローカーコメント（デフォルトは取引サーバの返したコードの記述）
  uint    request_id;  // ディスパッチの際に、端末によって設定されたリクエストID
  uint    retcode_external;  // 外部取引システムのリターンコード
};
{{< /code >}}

### uint retcode

### ulong deal

### ulong order

### double volume

### double price

### double bid

### double ask

### string comment

### uint request_id

### uint retcode_external

