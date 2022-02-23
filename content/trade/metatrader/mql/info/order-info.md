---
title: "MetaTrader/MQL: 注文情報を取得する (OrderXxx) (MT5)"
linkTitle: "注文情報を取得する (OrderXxx) (MT5)"
url: "/p/4p3fq3d"
date: "2021-01-24"
tags: ["MetaTrader/MQL"]
weight: 103
---

待機注文 (Pending Order) とは
----

待機注文というのは、指値価格や逆指値価格を指定して売買を待機している注文のことです。
日本では、「指値注文」や「逆指値注文」というと、この待機注文のことを示していることが多いです。

MQL の関数で `Order` で始まる次の関数群は、待機注文 (Pending Order) を扱う関数であることを示しています。

- `OrdersTotal` ... 待機注文の数を取得
- `OrderGetTicket` / `OrderSelect` ... 待機注文を選択
- `OrderGetDouble` / `OrderGetInteger` / `OrderGetString` ... 待機注文の情報を取得

これらの関数は、取引関数 (Trade Functions) に分類されており、下記に関数の一覧があります。

- [Trade Functions - MQL5 Reference](https://www.mql5.com/en/docs/trading)（[日本語](https://www.mql5.com/ja/docs/trading)）


現在入っている注文の数を調べる (OrdersTotal)
----

[OrdersTotal 関数](https://www.mql5.com/en/docs/trading/orderstotal)（[日本語](https://www.mql5.com/ja/docs/trading/orderstotal)）を使用すると、現在の口座における待機注文の数を取得することができます。

{{< code lang="cpp" >}}
int total = OrdersTotal();
printf("OrdersTotal: %d", total);
{{< /code >}}

これを利用すると、まだ注文が入っていないときのみ注文処理を行うプログラムを作成することができます。

{{< code lang="cpp" title="Scripts/SampleScript.mq5" >}}
void OnStart() {
    if (OrdersTotal() == 0) {
        // 注文がひとつもないときの処理
    } else {
        // すでに何らかの注文が入っているときの処理
    }
}
{{< /code >}}

EA のプログラム内で現在の注文数合計を取得する場合は、次のように、その EA のマジックナンバーで入れられた注文だけを対象にカウントすべきかもしれません。

{{< code lang="cpp" >}}
input ulong Magic = 63043000;

/** 指定したマジックナンバーで入っている注文の数を調べます。 */
int GetOrdersTotalByMagic(ulong magic) {
    const int total = OrdersTotal();
    int totalByMagic = 0;
    for (int i = 0; i < total; i++) {
        OrderGetTicket(i);  // 注文を選択状態にする
        if (OrderGetInteger(ORDER_MAGIC) == magic) {
            totalByMagic += 1;
        }
    }
    return totalByMagic;
}

void OnStart() {
    if (GetOrdersTotalByMagic(Magic) == 0) {
        // 注文がひとつもないときの処理
    } else {
        // すでに何らかの注文が入っているときの処理
    }
}
{{< /code >}}


待機注文の情報を取得する方法
----

MT5 で各待機注文の情報を取得するには、下記のような関数に取得したい情報の enum 値を渡します。

- [long  OrderGetInteger(ENUM_ORDER_PROPERTY_INTEGER)](https://www.mql5.com/en/docs/trading/ordergetinteger)（[日本語](https://www.mql5.com/jp/docs/trading/ordergetinteger)）<br>戻り値が整数（あるいは bool や enum 値）の待機注文情報
- [double OrderGetDouble(ENUM_ORDER_PROPERTY_DOUBLE)](https://www.mql5.com/en/docs/trading/ordergetdouble)（[日本語](https://www.mql5.com/jp/docs/trading/ordergetdouble)）<br>戻り値が浮動小数点数の待機注文情報
- [string OrderGetString(ENUM_ORDER_PROPERTY_STRING)](https://www.mql5.com/en/docs/trading/ordergetstring)（[日本語](https://www.mql5.com/jp/docs/trading/ordergetstring)）<br>戻り値が文字列の待機注文情報

これらの関数を呼び出す前に、どの待機注文の情報を取得するかを、次のような選択関数を使って選択しておく必要があります。
選択関数を呼び出した瞬間に、その待機注文の情報が内部バッファにコピーされ、上記の参照関数で取得できるようになるようです。

- [ulong OrderGetTicket(int index)](https://www.mql5.com/en/docs/trading/ordergetticket)（[日本語](https://www.mql5.com/ja/docs/trading/ordergetticket)）<br>待機注文のインデックス番号を指定して待機注文を選択します。指定可能なインデックスの範囲は `0` 〜 `OrdersTotal() - 1` です。この関数は、ついでに選択した待機注文のチケット番号を返します。待機注文を選択できなかった場合は、0 を返します。
- [bool OrderSelect(ulong ticket)](https://www.mql5.com/en/docs/trading/orderselect)（[日本語](https://www.mql5.com/ja/docs/trading/orderselect)）<br>待機注文のチケット番号を指定して待機注文を選択します。チケット番号は、`OrderGetInteger(ORDER_TICKET)` で取得できる値と同じものです。待機注文を選択できなかった場合は、`false` を返します。


サンプルコード（待機注文の情報を表示する）
----

下記のスクリプトを実行すると、現在入っている待機注文の詳細情報を 1 つずつメッセージボックスで表示します。

{{< code lang="cpp" title="Scripts/ShowOrderInfo.mq5" >}}
#property strict

// 文字列系の待機注文情報を文字列にして返します。
string getOrderInfoStr() {
    // 注文対処のシンボル（銘柄）
    string symbol = OrderGetString(ORDER_SYMBOL);
    // 注文につけられたコメント
    string comment = OrderGetString(ORDER_COMMENT);

    string s;
    StringConcatenate(s,
        "ORDER_SYMBOL = ", symbol,
        "\nORDER_COMMENT = ", comment
    );
    return s;
}

// 整数系の待機注文情報を文字列にして返します。
string getOrderInfoInteger() {
    // 注文のチケット番号
    long ticket = OrderGetInteger(ORDER_TICKET);
    // 注文の種類（ORDER_TYPE_BUY_LIMIT など）
    ENUM_ORDER_TYPE type = (ENUM_ORDER_TYPE) OrderGetInteger(ORDER_TYPE);
    // 注文状態（ORDER_STATE_PLACED など）
    ENUM_ORDER_STATE state = (ENUM_ORDER_STATE) OrderGetInteger(ORDER_STATE);
    // 注文のフィル・ポリシー（ORDER_FILLING_RETURN など）
    ENUM_ORDER_TYPE_FILLING typeFilling = (ENUM_ORDER_TYPE_FILLING) OrderGetInteger(ORDER_TYPE_FILLING);
    // 注文の設定日時（datetime 値）
    datetime timeSetup = (datetime) OrderGetInteger(ORDER_TIME_SETUP);
    // 注文の設定日時（1970年からの経過ミリ秒）
    long timeSetupMsc = OrderGetInteger(ORDER_TIME_SETUP_MSC);
    // 注文の実行及びキャンセル日時（datetime 値）
    datetime timeDone = (datetime) OrderGetInteger(ORDER_TIME_DONE);
    // 注文の実行及びキャンセル日時（1970年からの経過ミリ秒）
    long timeDoneMsc = OrderGetInteger(ORDER_TIME_DONE_MSC);
    // 注文期限の種類（ORDER_TIME_GTC など）
    ENUM_ORDER_TYPE_TIME typeTime = (ENUM_ORDER_TYPE_TIME) OrderGetInteger(ORDER_TYPE_TIME);
    // 注文期限の日時
    datetime timeExpiration = (datetime) OrderGetInteger(ORDER_TIME_EXPIRATION);
    // 注文時に指定した EA マジックナンバー
    long magic = OrderGetInteger(ORDER_MAGIC);
    // 注文の理由またはソース（ORDER_REASON_CLIENT など）
    ENUM_ORDER_REASON reason = (ENUM_ORDER_REASON) OrderGetInteger(ORDER_REASON);
    // 実行後すぐに注文に設定される不変のポジション識別子
    long positionId = OrderGetInteger(ORDER_POSITION_ID);
    // 反対注文 (ORDER_TYPE_CLOSE_BY) 時の反対ポジションの識別子
    long positionById = OrderGetInteger(ORDER_POSITION_BY_ID);

    string s;
    StringConcatenate(s,
        "ORDER_TICKET = ", ticket,
        "\nORDER_TYPE = ", type, " (", EnumToString(type), ")",
        "\nORDER_STATE = ", state, " (", EnumToString(state), ")",
        "\nORDER_TYPE_FILLING = ", typeFilling, " (", EnumToString(typeFilling), ")",
        "\nORDER_TIME_SETUP = ", timeSetup,
        "\nORDER_TIME_SETUP_MSC = ", timeSetupMsc,
        "\nORDER_TIME_DONE = ", timeDone,
        "\nORDER_TIME_DONE_MSC = ", timeDoneMsc,
        "\nORDER_TYPE_TIME = ", typeTime, " (", EnumToString(typeTime), ")",
        "\nORDER_TIME_EXPIRATION = ", timeExpiration,
        "\nORDER_MAGIC = ", magic,
        "\nORDER_REASON = ", reason, " (", EnumToString(reason), ")",
        "\nORDER_POSITION_ID = ", positionId,
        "\nORDER_POSITION_BY_ID = ", positionById
    );
    return s;
}

// 浮動小数点数系の待機注文情報を文字列にして返します。
string getOrderInfoDouble() {
    // 初期の注文ボリューム（ロット数）
    double volumeInitial = OrderGetDouble(ORDER_VOLUME_INITIAL);
    // 現在の注文ボリューム（ロット数）
    double volumeCurrent = OrderGetDouble(ORDER_VOLUME_CURRENT);
    // 注文時に指定された価格
    double priceOpen = OrderGetDouble(ORDER_PRICE_OPEN);
    // 注文シンボルの現在の価格
    double priceCurrent = OrderGetDouble(ORDER_PRICE_CURRENT);
    // ストップリミット注文の場合の指値注文価格
    double priceStoplimit = OrderGetDouble(ORDER_PRICE_STOPLIMIT);
    // 損切用の逆指値価格
    double sl = OrderGetDouble(ORDER_SL);
    // 利確用の指値価格
    double tp = OrderGetDouble(ORDER_TP);

    string s;
    StringConcatenate(s,
        "ORDER_VOLUME_INITIAL = ", volumeInitial,
        "\nORDER_VOLUME_CURRENT = ", volumeCurrent,
        "\nORDER_PRICE_OPEN = ", priceOpen,
        "\nORDER_PRICE_CURRENT = ", priceCurrent,
        "\nORDER_PRICE_STOPLIMIT = ", priceStoplimit,
        "\nORDER_SL = ", sl,
        "\nORDER_TP = ", tp
    );
    return s;
}

void showOrderInfo(int orderIndex) {
    // 待機注文を選択状態にする
    if (OrderGetTicket(orderIndex) == 0) {
        Alert("インデックス ", orderIndex, " の待機注文の選択に失敗しました");
        return;
    }

    // 選択した待機注文の情報を表示
    string msg = StringFormat("%s\n\n%s\n\n%s",
        getOrderInfoStr(),
        getOrderInfoInteger(),
        getOrderInfoDouble()
    );
    MessageBox(msg, StringFormat("Order[%d]", orderIndex));
}

void OnStart() {
    const int total = OrdersTotal();
    if (total == 0) {
        MessageBox("待機注文はありません");
        return;
    }
    for (int i = 0; i < total; i++) {
        showOrderInfo(i);
    }
}
{{< /code >}}

{{< code title="実行結果" >}}
ORDER_SYMBOL = USDJPY
ORDER_COMMENT =

ORDER_TICKET = 1699871
ORDER_TYPE = 2 (ORDER_TYPE_BUY_LIMIT)
ORDER_STATE = 1 (ORDER_STATE_PLACED)
ORDER_TYPE_FILLING = 2 (ORDER_FILLING_RETURN)
ORDER_TIME_SETUP = 2021.01.26 08:31:19
ORDER_TIME_SETUP_MSC = 1611649879303
ORDER_TIME_DONE = 1970.01.01 00:00:00
ORDER_TIME_DONE_MSC = 0
ORDER_TYPE_TIME = 0 (ORDER_TIME_GTC)
ORDER_TIME_EXPIRATION = 1970.01.01 00:00:00
ORDER_MAGIC = 0
ORDER_REASON = 0 (ORDER_REASON_CLIENT)
ORDER_POSITION_ID = 0
ORDER_POSITION_BY_ID = 0

ORDER_VOLUME_INITIAL = 0.1
ORDER_VOLUME_CURRENT = 0.1
ORDER_PRICE_OPEN = 103.686
ORDER_PRICE_CURRENT = 103.734
ORDER_PRICE_STOPLIMIT = 0.0
ORDER_SL = 0.0
ORDER_TP = 0.0
{{< /code >}}

