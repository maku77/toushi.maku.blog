---
title: "MetaTrader/MQL: OrderSend で成行注文を出す (MT5)"
linkTitle: "OrderSend で成行注文を出す (MT5)"
url: "/p/iz8gpw6"
date: "2021-02-01"
tags: ["MetaTrader/MQL"]
weight: 200
---

成行注文時の OrderSend 関数の使い方
----

MT5 で売買注文を出すには、[OrderSend 関数](https://www.mql5.com/en/docs/trading/ordersend)（[日本語](https://www.mql5.com/en/docs/trading/ordersend)） を使用します。
`OrderSend` 関数は様々な注文で使用されるため、成行注文を行うには、それ用に設定した `MqlTradeRequest` オブジェクトを引数で渡してやる必要があります。

{{< code lang="cpp" >}}
bool OrderSend(MqlTradeRequest& request, MqlTradeResult& result)
{{< /code >}}

まず、ブローカーが設定している __注文執行方式__ によって指定すべき値が変わってくるので、対象銘柄がどの注文執行方式で取引されるかを把握しておいてください（→ [FX 会社の注文執行方式について](/p/2roz7fo)）。

簡単に言えば、次の注文執行方式であれば価格とスリッページ (deviation) の指定が必要で、

- Instant Execution（成行方式、ストリーミング方式）
- Request Execution（リクエスト方式）

次の注文執行方式であれば価格とスリッページの指定は必要ありません（取引価格は時価で決まる）。

- Market Execution（カウントダウン方式、マーケット方式）
- Exchange Execution（エクスチェンジ方式）

それぞれの注文執行方式において、`MqlTradeRequest` オブジェクトのどのフィールドが必須かは [MqlTradeRequest 構造体のドキュメント](https://www.mql5.com/en/docs/constants/structures/mqltraderequest)（[日本語](https://www.mql5.com/ja/docs/constants/structures/mqltraderequest)）に説明があります。
ただ、公式ドキュメントはとても分かりにくいので下記表でまとめておきます。

| 引数 | Instant / Request Execution | Market / Exchange Execution |
| ---- | :--: | :--: |
| action | `TRADE_ACTION_DEAL` | `TRADE_ACTION_DEAL` |
| magic | ほぼ必須 | ほぼ必須 |
| symbol | 必須 | 必須 |
| volume | 必須 | 必須 |
| type | 必須 | 必須 |
| type_filling | 必須 | 必須 |
| price | __必須__ | ─ |
| deviation | __必須__ | ─ |
| sl | オプショナル | オプショナル |
| tp | オプショナル | オプショナル |
| comment | オプショナル | オプショナル |

<center>表: 成行注文で必要な MqlTradeRequest のフィールド</center>

一見難しそうですが、要するに約定させる価格 (`price` / `deviation`) をユーザーが指定すべきかどうかだけの違いです。
どの注文執行方式でも動作するように `OrderSend` 関数を呼び出すには、常に `price` 引数と `deviation` 引数を指定するようにすればよいでしょう（Market Execution および Exchange Execution では無視されます）。

マジックナンバーはオプショナルですが、プログラムから売買するときは設定しておいた方がよいでしょう（[マジックナンバーに関しての説明はこちら](/p/p6fgxgf)）。


OrderSend 関数で成行注文を出す
----

下記の EA をチャートにアタッチすると、キーボードの 1 キーを押したときに成行の買い注文を出せるようになります。
ユーティリティ関数 (`Util::SelectFillPolicy`、`Util::ErrorDescWithCode`) を使用するために、[Util.mqh](https://github.com/maku77/metatrader/blob/main/MQL5/Include/maku77/Util.mqh) をインクルードしてます。

{{< code lang="cpp" title="Experts/BuyWith1Key.mq5" >}}
#include <maku77/Util.mqh>

input double Lot = 0.1;
input ulong SlippagePoint = 3;
input ulong Magic = 67068000;

// 0.1 ロットの成行買い注文を出す
uint buyMarketOrder() {
    MqlTradeRequest request = {0};
    request.action = TRADE_ACTION_DEAL;  // 成行注文
    request.magic = Magic;  // マジックナンバー
    request.symbol = Symbol();  // カレントシンボル
    request.volume = Lot;  // ロット数
    request.type = ORDER_TYPE_BUY;  // 買い注文
    request.price = SymbolInfoDouble(Symbol(), SYMBOL_ASK);  // 価格
    request.type_filling = Util::SelectFillPolicy(request.symbol);  // フィル・モード
    request.deviation = SlippagePoint;  // 許容スリッページ（ポイント）

    // 注文を送信
    MqlTradeResult result = {0};
    if (OrderSend(request, result)) {
        switch (result.retcode) {
            case TRADE_RETCODE_PLACED: // 注文が出された
            case TRADE_RETCODE_DONE: // リクエスト完了
            case TRADE_RETCODE_DONE_PARTIAL: // リクエストが一部完了
            case TRADE_RETCODE_NO_CHANGES: // リクエストに変更なし
                // 注文成功時のログ出力
                printf("BUY: symbol=%s, price=%f, volume=%f, retcode=%d, comment=%s",
                    request.symbol, result.price, result.volume,
                    result.retcode, result.comment);
                break;
            default:
                // 取引サーバーがエラーコードを返した場合（不正な価格指定や、証拠金不足など）
                printf("Trade ERROR: retcode=%d, comment=%s",
                    result.retcode, result.comment);
                break;
        }
    } else {
        // OrderSend 関数自体が失敗した場合（パラメータの不正など）
        Print(Util::ErrorDescWithCode("OrderSend"));
        printf("Trade ERROR: retcode=%d, comment=%s",
            result.retcode, result.comment);
    }

    return result.retcode;
}

int OnInit() {
    return INIT_SUCCEEDED;
}

void OnChartEvent(const int id, const long &lparam, const double &dparam, const string &sparam) {
    // チャート上で 1 キーを押したときに成行買い注文
    if (id == CHARTEVENT_KEYDOWN && lparam == '1') {
        if (MessageBox("Are you sure to buy?", NULL, MB_YESNO) == IDYES) {
            buyMarketOrder();
        }
    }
}
{{< /code >}}

`OrderSend` 関数が戻り値 `true` を返し、さらに `MqlTradeResult` 構造体の [retcode フィールドの値](https://www.mql5.com/en/docs/constants/errorswarnings/enum_trade_return_codes) が次のような値になっていれば、注文は正しく受け入れられたと判断できます。

- `MqlTradeResult.retcode` の値:
    - `TRADE_RETCODE_PLACED` ... 注文が出された
    - `TRADE_RETCODE_DONE` ... リクエスト完了
    - `TRADE_RETCODE_DONE_PARTIAL` ... リクエストが一部完了
    - `TRADE_RETCODE_NO_CHANGES` ... リクエストに変更なし

`OrderSend` 関数が `true` 返しただけだと、トレードサーバー側で注文を最後まで処理（リクエスト完了）できなかった場合の判断ができないので、必ず `MqlTradeResult.retcode` の値を確認する必要があります。

`MqlTradeResult.comment` には、`MqlTradeResult.retcode` に対応する説明テキスト（トレードサーバーからのメッセージ）が格納されているので、これらを合わせてログ出力しておけば、注文失敗時の原因が簡単にわかります。

成行の「買い」注文ではなく、「売り」注文にするには、`MqlTradeRequest` の次のフィールドを変更すれば OK です。

{{< code lang="cpp" >}}
// 買いの場合
request.type = ORDER_TYPE_BUY;
request.price = SymbolInfoDouble(Symbol(), SYMBOL_ASK);

// 売りの場合
request.type = ORDER_TYPE_SELL;
request.price = SymbolInfoDouble(Symbol(), SYMBOL_BID);
{{< /code >}}

