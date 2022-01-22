---
title: "MetaTrader/MQL: ポジション情報を取得する (PositionXxx) (MT5)"
linkTitle: "ポジション情報を取得する (PositionXxx) (MT5)"
url: "/p/qcp2cnx"
date: "2021-01-24"
tags: ["MetaTrader/MQL"]
weight: 102
---

ポジション情報の取得方法
----

MT5 で現在の口座のポジション情報を取得するには、下記のような関数に取得したい情報の enum 値を渡します。

- [long PositionGetInteger(ENUM_POSITION_PROPERTY_INTEGER)](https://www.mql5.com/en/docs/trading/positiongetinteger)<br>戻り値が整数（あるいは bool や enum 値）のポジション情報
- [double PositionGetDouble(ENUM_POSITION_PROPERTY_DOUBLE)](https://www.mql5.com/en/docs/trading/positiongetdouble)<br>戻り値が浮動小数点数のポジション情報
- [string PositionGetString(ENUM_POSITION_PROPERTY_STRING)](https://www.mql5.com/en/docs/trading/positiongetstring)<br>戻り値が文字列のポジション情報

これらの関数を呼び出す前に、どのポジションの情報を取得するかを、次のような関数を使って選択しておく必要があります。
これらの関数を呼び出した瞬間に、内部的にそのポジションの情報がコピーされ、上記の参照関数で取得できるようになるようです。

- [string PositionGetSymbol(int index)](https://www.mql5.com/en/docs/trading/positiongetsymbol)<br>ポジションのインデックス番号を指定してポジションを選択します。指定可能なインデックスの範囲は `0` 〜 `PositionsTotal() - 1` です。この関数は、ついでに選択したポジションのシンボル名を返します。ポジションを選択できなかった場合は、空文字列(`""`) を返します。
- [bool PositionSelect(string symbol)](https://www.mql5.com/en/docs/trading/positionselect)<br>シンボル名でポジションを選択します。主にシンボルごとにポジションが集約されるネットアカウントで使われますが、ヘッジアカウントで使用すると、そのシンボルのポジションのうち、最小インデックスのポジションが選択されます。
- [bool PositionSelectByTicket(ulong ticket)](https://www.mql5.com/en/docs/trading/positionselectbyticket)<br>ポジションのチケット番号を指定してポジションを選択します。通し番号ではなく、ポジションごとに割り当てられたユニークな ID であることに注意してください。

{{< note title="ポジションの選択という煩わしさ" >}}
ポジションに関する情報を取得する場合、「ポジションの選択 → そのポジションの情報取得」という手順を踏まないといけないため、コーディングが非常に煩わしくなってしまいます。
非同期処理があたり前の昨今では、このような API 体系は設計が悪いとしか言いようがないのですが、こうなっている以上、これを使ってがんばるしかないです。
多くの EA では独自のラッパー関数を作成して、ポジションの選択と情報取得をまとめて行うようにしているようです。
{{< /note >}}


戻り値が bool 型のバージョン
----

`PositionGetInteger`、`PositionGetDouble`、`PositionGetString` 関数には、戻り値が bool 型になった次のようなオーバーロードが用意されています。
このバージョンを使うと、戻り値の真偽値によって、情報取得に成功したかどうかを判断できます。
取得した値は、2 つ目の引数で参照渡しした変数に格納されます。

{{< code lang="cpp" >}}
bool PositionGetInteger(ENUM_POSITION_PROPERTY_INTEGER property_id, long& long_var);
bool PositionGetDouble(ENUM_POSITION_PROPERTY_DOUBLE property_id, double& double_var);
bool PositionGetString(ENUM_POSITION_PROPERTY_STRING property_id, string& string_var);
{{< /code >}}

ポジション情報を取得できなかったときのエラーチェックを入れる場合は、こちらのバージョンを使うとコードの意味が伝わりやすくなるかもしれません。
とはいえ、戻り値が数値や文字列のバージョンでも、値の取得に失敗した場合は 0 や空文字列を返すようになっているので、エラーチェックを行えないということはありません。

{{< code lang="cpp" title="戻り値で情報を取得するバージョン" >}}
double volume = PositionGetDouble(POSITION_VOLUME);
if (volume == 0) {
    // 情報を取得できなかった場合のエラー処理
}
{{< /code >}}

{{< code lang="cpp" title="第 2 引数で情報を取得するバージョン" >}}
double volume;
if (!PositionGetDouble(POSITION_VOLUME, volume)) {
    // 情報を取得できなかった場合のエラー処理
}
{{< /code >}}

大して変わらないので、好きな方を使えばよさそうです。


ポジション情報取得のサンプルコード
----

次のサンプルスクリプトは、現在保有しているポジションの情報をメッセージボックスで表示します。
ポジションの数だけ表示されるので注意してください。
メッセージボックスのタイトルバーに、現在表示中のポジションのインデックス番号が表示されます。

{{< code lang="cpp" title="Scripts/ShowPositionInfo.mq5" >}}
#property strict

string getPositionInfoStr() {
    // ポジションのシンボル名（"USDJPY" など）
    string symbol = PositionGetString(POSITION_SYMBOL);
    // ポジションのコメント（オプショナル）
    string comment = PositionGetString(POSITION_COMMENT);
    // 外部の取引システム（取引所）におけるポジション ID
    string externalId = PositionGetString(POSITION_EXTERNAL_ID);

    string s;
    StringConcatenate(s,
        "POSITION_SYMBOL = ", symbol,
        "\nPOSITION_COMMENT = ", comment,
        "\nPOSITION_EXTERNAL_ID = ", externalId
    );
    return s;
}

string getPositionInfoInteger() {
    // ポジションのチケット番号（MqlTradeRequest.position で使う）
    long ticket = PositionGetInteger(POSITION_TICKET);
    // リオープンされても変化しないポジションの ID
    long identifier = PositionGetInteger(POSITION_IDENTIFIER);
    // ポジションをオープンした日時の datetime 値
    datetime time = (datetime) PositionGetInteger(POSITION_TIME);
    // ポジションをオープンした日時の　1970 年からの経過ミリ秒
    long timeMsc = PositionGetInteger(POSITION_TIME_MSC);
    // ポジションの最終更新日時の datetime 値
    datetime timeUpdate = (datetime) PositionGetInteger(POSITION_TIME_UPDATE);
    // ポジションの最終更新日時の 1970 年からの経過ミリ秒
    long timeUpdateMsc = PositionGetInteger(POSITION_TIME_UPDATE_MSC);
    // ポジションの種類
    ENUM_POSITION_TYPE type = (ENUM_POSITION_TYPE) PositionGetInteger(POSITION_TYPE);
    // ポジションの EA マジックナンバー
    long magic = PositionGetInteger(POSITION_MAGIC);
    // ポジションが何によって作られたか（モバイルアプリ、EAなど）
    ENUM_POSITION_REASON reason = (ENUM_POSITION_REASON) PositionGetInteger(POSITION_REASON);

    string s;
    StringConcatenate(s,
        "POSITION_TICKET = ", ticket,
        "\nPOSITION_IDENTIFIER = ", identifier,
        "\nPOSITION_TIME = ", time,
        "\nPOSITION_TIME_MSC = ", timeMsc,
        "\nPOSITION_TIME_UPDATE = ", timeUpdate,
        "\nPOSITION_TIME_UPDATE_MSC = ", timeUpdateMsc,
        "\nPOSITION_TYPE = ", type, " (", EnumToString(type), ")",
        "\nPOSITION_MAGIC = ", magic,
        "\nPOSITION_REASON = ", reason, " (", EnumToString(reason), ")"
    );
    return s;
}

string getPositionInfoDouble() {
    // ポジションのボリューム（ロット数）
    double volume = PositionGetDouble(POSITION_VOLUME);
    // ポジションオープン時の価格
    double priceOpen = PositionGetDouble(POSITION_PRICE_OPEN);
    // 対象シンボルの現在価格
    double priceCurrent = PositionGetDouble(POSITION_PRICE_CURRENT);
    // ポジションの損切価格 (Stop loss level)
    double sl = PositionGetDouble(POSITION_SL);
    // ポジションの利確価格 (Take profit level)
    double tp = PositionGetDouble(POSITION_TP);
    // このポジションでの損益
    double profit = PositionGetDouble(POSITION_PROFIT);
    // このポジションでの累積スワップ
    double swap = PositionGetDouble(POSITION_SWAP);

    // ポジションの価格を小数点数以下何桁まで表示すればいいか
    int symbolDigits = (int) SymbolInfoInteger(PositionGetString(POSITION_SYMBOL), SYMBOL_DIGITS);
    // 損益と累積スワップをどの通貨で表示すればいいか
    string accountCurrency = AccountInfoString(ACCOUNT_CURRENCY);
    int accountDigits = (int) AccountInfoInteger(ACCOUNT_CURRENCY_DIGITS);

    string s;
    StringConcatenate(s,
        "POSITION_VOLUME = ", volume,
        "\nPOSITION_PRICE_OPEN = ", DoubleToString(priceOpen, symbolDigits),
        "\nPOSITION_PRICE_CURRENT = ", DoubleToString(priceCurrent, symbolDigits),
        "\nPOSITION_SL = ", sl,
        "\nPOSITION_TP = ", tp,
        "\nPOSITION_PROFIT = ", DoubleToString(profit, accountDigits), " ", accountCurrency,
        "\nPOSITION_SWAP = ", DoubleToString(swap, accountDigits), " ", accountCurrency
    );
    return s;
}

void OnStart() {
    const int total = PositionsTotal();
    for (int i = 0; i < total; i++) {
        PositionGetSymbol(i);  // ポジションを選択状態にする
        string s = StringFormat("%s\n%s\n%s",
            getPositionInfoStr(),
            getPositionInfoInteger(),
            getPositionInfoDouble());
        MessageBox(s, StringFormat("Position[%d]", i));
    }
}
{{< /code >}}

{{< code title="表示例" >}}
POSITION_SYMBOL = EURUSD
POSITION_COMMENT =
POSITION_EXTERNAL_ID =
POSITION_TICKET = 1558806
POSITION_IDENTIFIER = 1558806
POSITION_TIME = 2021.01.07 21:42:30
POSITION_TIME_MSC = 1610055750757
POSITION_TIME_UPDATE = 2021.01.07 21:42:30
POSITION_TIME_UPDATE_MSC = 1610055750757
POSITION_TYPE = 0 (POSITION_TYPE_BUY)
POSITION_MAGIC = 5432100
POSITION_REASON = 3 (POSITION_REASON_EXPERT)
POSITION_VOLUME = 0.1
POSITION_PRICE_OPEN = 1.22690
POSITION_PRICE_CURRENT = 1.21694
POSITION_SL = 0.0
POSITION_TP = 0.0
POSITION_PROFIT = -10337 JPY
POSITION_SWAP = -682 JPY
{{< /code >}}

