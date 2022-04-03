---
title: "MetaTrader/MQL: OrderSend で注文を出す (MT4)"
linkTitle: "OrderSend で注文を出す (MT4)"
url: "/p/oanyb2a"
date: "2021-01-12"
tags: ["MetaTrader/MQL"]
weight: 500
---

MT4 で指定したシンボル（USDJPY などの通貨ペア）に対して、成行注文や指値注文を出すには [OrderSend 関数](https://docs.mql4.com/trading/ordersend) を使用します。
MT4 バージョンと、MT5 バージョンでは関数のパラメータや戻り値が異なるので注意してください。
多くの環境では、まだ MT4 が使われているので、ここでは MT4 バージョンの `OrderSend` 関数の使い方を説明します。


OrderSend 関数 (MT4) の使い方
----

{{< code lang="cpp" title="OrderSend 関数 (MQL4)" >}}
int OrderSend(
   string   symbol,              // symbol
   int      cmd,                 // operation
   double   volume,              // volume
   double   price,               // price
   int      slippage,            // slippage
   double   stoploss,            // stop loss
   double   takeprofit,          // take profit
   string   comment=NULL,        // comment
   int      magic=0,             // magic number
   datetime expiration=0,        // pending order expiration
   color    arrow_color=clrNONE  // color
)
{{< /code >}}

### OrderSend のパラメーター

- `symbol` ... 注文する通貨ペアのシンボル名。例えば、`"USDJPY"` などを指定します。選択中のチャートのシンボルを使いたい場合は、`Symbol()` を指定すれば OK です。
- `cmd` ... [注文の種類 (Order Properties)](https://docs.mql4.com/constants/tradingconstants/orderproperties) を指定します。
    - `OP_BUY` ... 成行買い
    - `OP_SELL` ... 成行売り
    - `OP_BUYLIMIT` ... 指値買い（今より安くなったら買う）
    - `OP_SELLLIMIT` ... 指値売り（今より高くなったら売る）
    - `OP_BUYSTOP` ... 逆指値買い（今より高くなったら買う）
    - `OP_SELLSTOP` ... 逆指値売り（今より安くなったら売る）
- `volume` ... ロット数。多くの場合 `0.1` で 1 万通貨です。
- `price` ... 価格。例えば、1 ドル 110.5 円で売買するなら `110.5` と指定します。スリッページを考慮するため、成行注文の場合でも指定する必要があります。
- `slippage` ... 最大許容スリッページ（ポイント）。`price` で指定した価格から、どれだけずれて約定してもいいかをポイントで指定します。例えば、USDJPY が小数点以下 3 桁の価格まで表示される FX 会社の場合、1ポイント＝0.001円 になります。プログラムで [1 ポイントがいくらかを調べる](/p/gkcxsb2) こともできます。
- `stoploss` ... 損切り価格（決済逆指値）。設定しない場合は 0。
- `takeprofit` ... 利食い価格（決済指値）。設定しない場合は 0。
- `comment=NULL` ... 注文のコメント。
- `magic=0` ... 注文のマジックナンバー。
- `expiration=0` ... 注文の有効期限。待機注文（指値／逆指値）のときのみ有効です。
- `arrow_color=clrNONE` ... 矢印の色。指定すると、ポジションをオープンしたときにチャート上に矢印が表示されます。

### OrderSend 戻り値

`OrderSend` 関数は、注文に成功するとチケット番号を返します。注文に失敗すると、`-1` を返します。
`-1` が返された場合は、`GetLastError()` を使ってエラーの原因を調べることができます。


OrderSend による注文の例
----

下記のサンプルスクリプトを実行すると、カレントチャートの通貨ペアを 0.01 ロット（USDJPY であれば通常 1000 通貨）成行注文で購入します。

{{< code lang="cpp" title="Scripts/Buy.mq4（スクリプトの例）" >}}
#property strict
#property show_confirm  // 実行前に確認ダイアログを表示

#include <stdlib.mqh>  // ErrorDescription 関数のため
#define MShowLastError() \
    MessageBox(StringFormat("ERROR in %s: %s", \
    __FUNCTION__, ErrorDescription(GetLastError())));

// スクリプトのエントリーポイント
void OnStart() {
    int ticket = OrderSend(
        Symbol(),  // 現在の通貨
        OP_BUY,    // 成行買い
        0.01,      // ロット数は 0.01 ロット
        Ask,       // 現在の提示価格で買う
        1,         // 最大許容スリッページは 1 ポイント
        0,         // 損切りレベルは設定しない (stoploss=0)
        0          // 利食いレベルは設定しない (takeprofit=0)
    );
    if (ticket == -1) {
        MShowLastError();
    } else {
        PrintFormat("Ticket = %d", ticket);
    }
}
{{< /code >}}

