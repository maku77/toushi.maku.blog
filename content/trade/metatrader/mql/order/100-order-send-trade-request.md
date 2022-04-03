---
title: "MetaTrader/MQL: OrderSend の引数を理解する - MqlTradeRequest/MqlTradeResult 構造体 (MT5)"
linkTitle: "OrderSend の引数を理解する - MqlTradeRequest/MqlTradeResult 構造体 (MT5)"
url: "/p/j6iu7hs"
date: "2020-11-08"
lastmod: "2022-04-03"
tags: ["MetaTrader/MQL"]
weight: 100
---

MT5 の OrderSend 関数
----

MT5 で注文を出すには [OrderSend 関数](https://www.mql5.com/en/docs/trading/ordersend)（[日本語](https://www.mql5.com/ja/docs/trading/ordersend)）を使用します。

{{< code lang="cpp" title="MT5 の OrderSend 関数" >}}
bool OrderSend(
  MqlTradeRequest& request,  // 注文内容を指定する
  MqlTradeResult&  result    // 注文結果が格納される
)
{{< /code >}}

ここでは、注文結果が格納される [MqlTradeResult 構造体](https://www.mql5.com/en/docs/constants/structures/mqltraderesult)（[日本語](https://www.mql5.com/ja/docs/constants/structures/mqltraderesult)）と、注文結果が格納される [MqlTradeResult 構造体](https://www.mql5.com/en/docs/constants/structures/mqltraderesult)（[日本語](https://www.mql5.com/ja/docs/constants/structures/mqltraderesult)）について説明します。


MqlTradeRequest 構造体（注文内容を指定する）
----

`MqlTraderRequest` 構造体には次のようなフィールドが定義されています。
各フィールドにどのような値を設定すべきかを順に説明していきます。

{{< code lang="cpp" title="MqlTradeRequest 構造体" >}}
struct MqlTradeRequest {
  ENUM_TRADE_REQUEST_ACTIONS action;  // アクション（取引タイプ）
  ulong   magic;      // EA のマジックナンバー
  ulong   order;      // オーダーのチケット番号（待機注文を操作する場合）
  string  symbol;     // シンボル名
  double  volume;     // ロット数
  double  price;      // 価格
  double  stoplimit;  // ストップ・リミット注文発火時に使われる指値価格
  double  sl;         // 利確の価格
  double  tp;         // 損切の価格
  ulong   deviation;  // 最大許容スリッページ（ポイント）
  ENUM_ORDER_TYPE          type;          // 売買のタイプ
  ENUM_ORDER_TYPE_FILLING  type_filling;  // フィル・タイプ
  ENUM_ORDER_TYPE_TIME     type_time;     // 有効期限タイプ
  datetime  expiration;   // 有効期限
  string    comment;      // 注文コメント
  ulong     position;     // ポジションのチケット番号（ポジションを操作する場合）
  ulong     position_by;  // 反対ポジションのチケット番号（ポジション相殺用）
};
{{< /code >}}

### ENUM_TRADE_REQUEST_ACTIONS action（必須）

[ENUM_TRADE_REQUEST_ACTIONS 列挙値](https://www.mql5.com/en/docs/constants/tradingconstants/enum_trade_request_actions) でアクション（取引タイプ）を指定します。
つまり、この `OrderSend` 関数を何のために使用するかを示します。
この値によって、残りのパラメータに何を設定すべきかがガラリと変わってきます。

`TRADE_ACTION_DEAL`
: <i>Place a <b>market order</b></i><br/>
  __成行注文__ を出します。

`TRADE_ACTION_PENDING`
: <i>Place a <b>pending order</b></i><br/>
  __待機注文（指値／逆指値）__ を出します。

`TRADE_ACTION_SLTP`
: <i>Modify the stop loss (sl) and/or take profit (tp) of the <b>current position</b></i><br/>
  __オープンポジションの損切／利確価格を、設定／修正__ します。

`TRADE_ACTION_MODIFY`
: <i>Modify the previously placed <b>pending order</b></i><br/>
  __待機注文の内容を修正__ します。

`TRADE_ACTION_REMOVE`
: <i>Cancel a previously placed <b>pending order</b></i><br/>
  __待機注文を削除__ します。

`TRADE_ACTION_CLOSE_BY`
: <i>Close a position by an opposite one</i><br/>
  2 つの反対方向の __オープンポジションを相殺__ することでクローズします。MT5 の新機能で、ヘッジアカウントを使っている場合のみ利用可能です。通常 2 回の取引が必要ですが、このアクションを指定することで、__1 回分のスプレッドで 2 つのポジションをクローズできます__。どちらかのポジションの方が多い場合は、差し引き分がオープンポジションとして残ります。ネットアカウントを使用している場合は、そもそも反対方向のポジションを持つことはできないので、このアクションは使用できません。

MT5 で追加されたアクション `TRADE_ACTION_CLOSE_BY` は要注目です。
両建てを活用する EA では、このアクションを活用することでスプレッドの支払額を減らして成績を上げることができます。

### ulong magic（EA ならおそらく必須）

EA ごとに一意なマジックナンバーを設定します。
マジックナンバーは [こちらの自動生成ツール](/p/p6fgxgf) で生成したものを指定すれば OK です。
EA でも `magic` 引数を省略 (=`0`) することはできますが、その場合はマニュアル注文と区別できなかったりと色々問題があるので、EA の場合は通常はこの引数は必須です。

### ulong order（オプショナル）

発注済みの待機注文 (pending order) を削除／修正するときに、待機注文を特定するためのオーダーチケット番号（注文番号）です。
`action` 引数で `TRADE_ACTION_REMOVE`（待機注文の削除）や `TRADE_ACTION_MODIFY`（待機注文の修正）を指定した時に必須になります。

### string symbol（新規売買時に必須）

トレード対象のシンボル名（`"USDJPY"` など）を指定します。
カレントチャートのシンボルであれば、`Symbol()` や `_Symbol` を指定すれば OK です。

待機注文の削除／修正（`action` 引数が `TRADE_ACTION_REMOVE` あるいは `TRADE_ACTION_MODIFY`）の場合）は `symbol` 引数は省略することができます（`order` 引数のオーダーチケット番号で対象となる注文を特定できるため）。

### double volume（必須）

トレードの量をロット数で指定します。
`USDJPY` のトレードであれば、通常 0.1 ロットが 1 万通過を表します（1 万ドルの売買）。
実際にどれだけ約定するかは、Filling policy（`type_filling` 引数）によって変わってくることに注意してください。

### double price（オプショナル）

売買の価格を指定します。

`price` 引数が必須になるのは、`action` 引数が `TRADE_ACTION_DEAL` かつ [ブローカーの注文執行方式](/p/2roz7fo) が Instant execution か Request execution に設定されている場合、あるいは、`action` 引数が `TRADE_ACTION_PENDING`、`TRADE_ACTION_MODIFY` のいずれかである場合です。
それ以外の注文では、`price` 引数の値は無視されます。

成行の買い注文であれば現在の Ask 価格 (`SymbolInfoDouble(Symbol(), SYMBOL_ASK)`)、売り注文であれば現在の Bid 価格 (`SymbolInfoDouble(Symbol(), SYMBOL_BID)`) を指定すれば OK です。
待機注文 (`action == TRADE_ACTION_PENDING`) の場合は、`type` 引数によって指値価格（現在より有利な価格）と逆指値価格（現在より不利な価格）のどちらの価格を指定するかが変わってきます。

{{< note >}}
成行注文の注文執行方式が、ブローカーによって Market execution か Exchange execution に設定されている場合は、`price` 引数の値は使用されないということになっています。
なぜなら、それらの注文執行方式の場合は、常に最終的な市場価格で約定されるからです。
一方、Instant execution か Request execution の場合は、ユーザー側から注文価格 (`price`) と許容スリッページポイント (`deviation`) の両方を指定する必要があります。
なぜなら、ブローカー側は「売買価格」と「スリッページ」の両方の情報をもって初めてスリッページを考慮したリクオート（約定拒否）判断を行えるからです。
{{< /note >}}

### double stoplimit（オプショナル）

ストップ・リミット注文時のトリガー価格（逆指値）を指定します。
ストップ・リミット注文を出すには、`action` 引数で `TRADE_ACTION_PENDING` を指定し、`type` 引数で `ORDER_TYPE_BUY_STOP_LIMIT` あるいは `ORDER_TYPE_SELL_STOP_LIMIT` を指定する必要があります。

例えば、「買い」のストップ・リミット注文 (`type=ORDER_TYPE_BUY_STOP_LIMIT`) の場合、`price` の価格まで上昇したときに、`stoplimit` の価格で買いの指値注文が入ります。
このとき、`stoplimit` で指定した価格より高い価格で買ってしまうことはありません（トリガー後に買い指値注文になるので）。
価格が上抜けしたときに、このくらいの価格なら買ってもよいよというブレークアウト戦略で利用できます。

逆に、「売り」のストップ・リミット注文 (`type=ORDER_TYPE_SELL_STOP_LIMIT`) の場合、`price` の価格まで下落したときに、`stoplimit` の価格で売りの指値注文が入ります。
このとき、`stoplimit` で指定した価格より低い価格で売ってしまうことはありません（トリガー後に売り指値注文になるので）。
価格が下抜けしたときに、このくらいの価格なら売ってもよいよというブレークアウト戦略で利用できます。

### double sl（オプショナル）

損切りのための逆指値価格 (Stop loss) を指定します。
指定した価格に到達すると、このポジションはすべて決済されます。
損切り設定しない場合は、`sl` 引数に 0 を指定します。

{{< note >}}
古いバージョンでは、ブローカーの注文執行方式が Market execution のときに、`sl` 引数は指定できませんでしたが、現在は指定可能です。
{{< /note >}}

### double tp（オプショナル）

利食いのための指値価格 (Take profit) を指定します。
指定した価格に到達すると、このポジションはすべて決済されます。
利食い設定しない場合は、`tp` 引数に 0 を指定します。

{{< note >}}
古いバージョンでは、ブローカーの注文執行方式が Market execution のときに、`tp` 引数は指定できませんでしたが、現在は指定可能です。
{{< /note >}}

### ulong deviation（注文執行方式により必須）

`price` 引数で指定した価格からの許容スリッページ（ポイント数）を指定します。
ブローカーの注文執行方式が、Instant execution あるいは Request execution のときのみ有効です。
注文後に許容スリッページ以上の価格変化があった場合、ブローカーからリクオート（約定拒否）されます。

- 参考: [MT5 のポイントとは何か](/p/gkcxsb2)

### ENUM_ORDER_TYPE type（必須）

注文タイプ（買い／売りのどちらなのか、成行／待機注文のどちらなのか）を指定します。
指定可能な注文タイプには以下のようなものがあります。

- `ORDER_TYPE_BUY` ... 買いの成行注文
- `ORDER_TYPE_SELL` ... 売り成行注文
- `ORDER_TYPE_BUY_STOP` ... 買いの逆指値注文（つまり、上抜けブレーク時に成行買い）
- `ORDER_TYPE_SELL_STOP` ... 売りの逆指値注文（つまり、下抜けのブレーク時に成行売り）
- `ORDER_TYPE_BUY_LIMIT` ... 買いの指値注文（つまり、安くなったら成行買い）
- `ORDER_TYPE_SELL_LIMIT` ... 売りの指値注文（つまり、高くなったら成行売り）
- `ORDER_TYPE_BUY_STOP_LIMIT` ... 買いのストップ・リミット注文（つまり、上抜けブレーク時に指値買い注文）
- `ORDER_TYPE_SELL_STOP_LIMIT` ... 売りのストップ・リミット注文（つまり、下抜けブレーク時に指値売り注文）
- `ORDER_TYPE_CLOSE_BY` ... 反対方向のポジションを相殺する注文

### ENUM_ORDER_TYPE_FILLING type_filling（オプショナル）

注文の [フィル・ポリシー (fill policy)、約定形式](https://www.mql5.com/en/docs/constants/tradingconstants/orderproperties#enum_order_type_filling)（[日本語](https://www.mql5.com/ja/docs/constants/tradingconstants/orderproperties#enum_order_type_filling)） を指定します。
注文時に指定したロット数（`volume` 引数）が一度に約定させられない場合にどう処理するかを指定します。

- `ORDER_FILLING_FOK (0)` ... Fill or Kill. 全約定できなければ全ロットをキャンセル。
- `ORDER_FILLING_IOC (1)` ... Immediate or Cancel. できるだけ約定させ、残りをキャンセル。
- `ORDER_FILLING_RETURN (2)` ... Return. 取引サーバー側で全約定するまで市場に注文を出し続ける。

フィル・ポリシーに関しては複雑な事情があるので、下記ページで別途説明しています。

- 参考: [注文時のフィル・ポリシーの指定について](/p/9jjrrp5)

### ENUM_ORDER_TYPE_TIME type_time（オプショナル）

待機注文を出す時に、その注文の [有効期限タイプ](https://www.mql5.com/ja/docs/constants/tradingconstants/orderproperties#enum_order_type_time)（[日本語](https://www.mql5.com/ja/docs/constants/tradingconstants/orderproperties#enum_order_type_time)）を指定します。

- `ORDER_TIME_GTC (0)` ... Good till canceled. 待機注文の有効期限を設定しません（明示的にキャンセルされるまで有効です）
- `ORDER_TIME_DAY (1)` ... 待機注文はその日の間だけ有効です。
- `ORDER_TIME_SPECIFIED (2)` ... 待機注文は `datetime` 引数で指定した日時まで有効です。
- `ORDER_TIME_SPECIFIED_DAY (3)` ... 待機注文は `datetime` 引数で指定した日が終わるまで有効です（23:59:59 あるいはその日の最終取引時刻までです）。

### datetime expiration（オプショナル）

待機注文の有効期限を指定します。
有効期限タイプ（`type_time` 引数）の値に、`ORDER_TIME_SPECIFIED` あるいは `ORDER_TIME_SPECIFIED_DAY` が指定されている場合のみ有効です。

### string comment（オプショナル）

注文にコメントテキストを設定します。

### ulong position（オプショナル）

ヘッジアカウントにおいて、ポジションの内容を修正（`TRADE_ACTION_SLTP`）したり、決済 (`TRADE_ACTION_CLOSE` / `TRADE_ACTION_CLOSE_BY`) したりするときにポジションのチケット番号を指定します。
ネットアカウントの場合は、すべてのポジションはシンボル（銘柄）ごとに集約されるため、このパラメーターは必要ありません（`symbol` の指定だけで OK）。

### ulong position_by（オプショナル）

`action` 引数で `TRADE_ACTION_CLOSE_BY` を指定して 2 つの反対ポジションを相殺させるときに、2 つ目のポジションのチケット番号を指定します。1 つ目のポジションは `position` 引数で指定します。
両建てが可能なヘッジアカウントのみで有効です。


MqlTradeResult 構造体（注文結果が格納される）
----

（追記予定）

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

