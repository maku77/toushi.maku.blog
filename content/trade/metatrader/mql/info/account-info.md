---
title: "MetaTrader/MQL: アカウント情報（口座情報）を取得する (AccountInfo*) (MT5)"
linkTitle: "アカウント情報（口座情報）を取得する (AccountInfo*) (MT5)"
url: "p/nb7h9vg/"
date: "2021-01-12"
lastmod: "2023-06-18"
changes:
  - 2023-06-18: それぞれの情報について詳しい説明を追加
tags: ["MetaTrader/MQL"]
weight: 101
---

MQL5 の下記の関数を使用すると、現在の口座の情報（証拠金残高や損益合計など）を取得することができます。
関数は、戻り値の型によって使い分けます。

- [long AccountInfoInteger(ENUM_ACCOUNT_INFO_INTEGER)](https://www.mql5.com/en/docs/account/accountinfointeger) ... 戻り値が整数（あるいは bool）の口座情報
- [double AccountInfoDouble(ENUM_ACCOUNT_INFO_DOUBLE)](https://www.mql5.com/en/docs/account/accountinfodouble) ... 戻り値が浮動小数点数の口座情報
- [string AccountInfoDouble(ENUM_ACCOUNT_INFO_STRING)](https://www.mql5.com/en/docs/account/accountinfostring) ... 戻り値が文字列の口座情報


デポジット通貨を取得する
----

口座の入出金に使用される通貨（デポジット通貨）は、下記のようにして取得することができます。

```cpp
// 口座の通貨（"JPY" など）
string currency = AccountInfoString(ACCOUNT_CURRENCY);
```


口座残高、純資産の情報を取得する
----

口座の証拠金情報は、__`AccountInfoDouble`__ を使用して取得することができます。
通貨が日本円 (JPY) の場合は小数点数以下の情報は必要ありませんが、いろいろな通貨を扱えるようにするために戻り値は `double` 型になっています。


```cpp
// 証拠金残高（ポジションを取っても変化せず、決済した時点で増減する）
double balance = AccountInfoDouble(ACCOUNT_BALANCE);

// 評価損益（ポジションを閉じると証拠金残高に反映される）
double profit = AccountInfoDouble(ACCOUNT_PROFIT);

// 純資産（証拠金残高＋評価損益）
double equity = AccountInfoDouble(ACCOUNT_EQUITY);

Alert(StringFormat("Balance: %.0f, Profit: %.0f, Equity: %.0f",
    balance, profit, equity));
```

純資産は評価損益を加味したものですので、`balance + profit = equity` が成り立っているはずです。


必要証拠金や有効証拠金の情報を取得する
----

現在のポジションのために使用している __必要証拠金__ や、さらにどれだけのエントリができるかを表す __有効証拠金__ の情報を取得するには、下記のようにします。

```cpp
// 純資産
double equity = AccountInfoDouble(ACCOUNT_EQUITY);

// 必要証拠金（ポジションや予約注文のために使用している証拠金）
double margin = AccountInfoDouble(ACCOUNT_MARGIN);

// 有効証拠金（使用可能な証拠金の残り金額）
double freeMargin = AccountInfoDouble(ACCOUNT_MARGIN_FREE);

Alert(StringFormat(
    "Equity: %.0f, Margin: %.0f, FreeMargin: %.0f",
    equity, margin, freeMargin));
```

有効証拠金は、純資産から必要証拠金を引いた残りの金額なので、上記の結果は `equity = margin + freeMargin` となっているはずです。


証拠金維持率を取得する
----

証拠金維持率 (%) に関する情報を取得するには下記のようにします。
マージンコールがかかる維持率の情報を取得することもできます。

```cpp
// 証拠金維持率 (%)（純資産／必要証拠金）
double marginLevel = AccountInfoDouble(ACCOUNT_MARGIN_LEVEL);

// マージンコールがかかる証拠金維持率 (Margin call level: %)
double marginSoCall = AccountInfoDouble(ACCOUNT_MARGIN_SO_CALL);

// 強制ロスカットがかかる証拠金維持率 (Stop out level: %)
double marginSoSo = AccountInfoDouble(ACCOUNT_MARGIN_SO_SO);

Alert(StringFormat(
    "MarginLevel: %.2f%%, MarginSoCall: %.2f%%, MarginSoSo: %.2f%%",
    marginLevel, marginSoCall, marginSoSo));
```

ちなみに、ちょくちょく出てくる So というのは Stop Out の略です。

証拠金維持率は、現在の必要証拠金 (margin) に対する純資産 (equity) の割合ですから、下記のように計算することもできます。

```cpp
double equity = AccountInfoDouble(ACCOUNT_EQUITY);
double margin = AccountInfoDouble(ACCOUNT_MARGIN);
double marginLevel = equity * 100 / margin;
Alert(StringFormat("MarginLevel: %.2f%%", marginLevel));
```


レバレッジ情報を取得する
----

現在の口座のレバレッジ設定を取得するには下記のようにします。
例えば、レバレッジ 25 倍の口座であれば、25 という値が取得できます。

```cpp
long leverage = AccountInfoInteger(ACCOUNT_LEVERAGE);
Alert(StringFormat("Leverage: %d", leverage));
```


すべてのアカウント情報を表示するスクリプト
----

最後に、簡単にすべてのアカウント情報を表示するスクリプトの実装例を紹介しておきます。
次のスクリプトを実行すると、すべてのアカウント情報をメッセージボックスで表示します。

{{< code lang="cpp" title="Scripts/maku/ShowAccountInfo.mq5" >}}
#property strict

/**
 * AccountInfoInteger API で取得できるアカウント情報を取得する。
 */
string getAccountInfoInteger() {
    // 口座番号
    long login = AccountInfoInteger(ACCOUNT_LOGIN);
    // 口座取引モード
    ENUM_ACCOUNT_TRADE_MODE tradeMode = (ENUM_ACCOUNT_TRADE_MODE) AccountInfoInteger(ACCOUNT_TRADE_MODE);
    // 口座レバレッジ
    long leverage = AccountInfoInteger(ACCOUNT_LEVERAGE);
    // アクティブな未決注文の最大許容数
    long limitOrders = AccountInfoInteger(ACCOUNT_LIMIT_ORDERS);
    // 許容された最小証拠金を設定するモード
    ENUM_ACCOUNT_STOPOUT_MODE marginSoMode = (ENUM_ACCOUNT_STOPOUT_MODE) AccountInfoInteger(ACCOUNT_MARGIN_SO_MODE);
    // 口座で取引が許可されているか
    bool tradeAllowed = AccountInfoInteger(ACCOUNT_TRADE_ALLOWED);
    // エキスパートアドバイザーで取引が許可されているか
    bool tradeExpert = AccountInfoInteger(ACCOUNT_TRADE_EXPERT);
    // 証拠金計算モード
    ENUM_ACCOUNT_MARGIN_MODE marginMode = (ENUM_ACCOUNT_MARGIN_MODE) AccountInfoInteger(ACCOUNT_MARGIN_MODE);
    // 取引結果を正確に表示するために必要な口座通貨の小数点以下の桁数
    int currencyDigits = (int) AccountInfoInteger(ACCOUNT_CURRENCY_DIGITS);
    // FIFOルールによってのみポジションを決済できることを示す
    bool fifoClose = AccountInfoInteger(ACCOUNT_FIFO_CLOSE);

    string s;
    StringConcatenate(s, "----- AccountInfoInteger -----"
        "\nACCOUNT_LOGIN = ", login,
        "\nACCOUNT_TRADE_MODE = ", tradeMode, " (", EnumToString(tradeMode), ")",
        "\nACCOUNT_LEVERAGE = ", leverage,
        "\nACCOUNT_LIMIT_ORDERS = ", limitOrders,
        "\nACCOUNT_MARGIN_SO_MODE = ", marginSoMode, " (", EnumToString(marginSoMode), ")",
        "\nACCOUNT_TRADE_ALLOWED = ", tradeAllowed,
        "\nACCOUNT_TRADE_EXPERT = ", tradeExpert,
        "\nACCOUNT_MARGIN_MODE = ", marginMode, " (", EnumToString(marginMode), ")",
        "\nACCOUNT_CURRENCY_DIGITS = ", currencyDigits,
        "\nACCOUNT_FIFO_CLOSE = ", fifoClose
    );
    return s;
}

/**
 * AccountInfoDouble API で取得できるアカウント情報を取得する。
 */
string getAccountInfoDouble() {
    // 証拠金残高（円）
    double balance = AccountInfoDouble(ACCOUNT_BALANCE);
    // 信用額（円）
    double credit = AccountInfoDouble(ACCOUNT_CREDIT);
    // 評価損益（円）
    double profit = AccountInfoDouble(ACCOUNT_PROFIT);
    // 純資産（証拠金残高 - 損益）（円）
    double equity = AccountInfoDouble(ACCOUNT_EQUITY);
    // 必要証拠金（円）
    double margin = AccountInfoDouble(ACCOUNT_MARGIN);
    // 有効証拠金（円）
    double marginFree = AccountInfoDouble(ACCOUNT_MARGIN_FREE);
    // 証拠金維持率（％）
    double marginLevel = AccountInfoDouble(ACCOUNT_MARGIN_LEVEL);
    // マージンコール値（ACCOUNT_MARGIN_SO_MODE によってパーセントまたは預金通貨）
    double marginSoCall = AccountInfoDouble(ACCOUNT_MARGIN_SO_CALL);
    // 強制ロスカット値（ACCOUNT_MARGIN_SO_MODE によってパーセントまたは預金通貨）
    double marginSoSo = AccountInfoDouble(ACCOUNT_MARGIN_SO_SO);
    // 当初証拠金（全ての未決注文の証拠金をカバーするために口座内でリザーブされた額）
    double marginInitial = AccountInfoDouble(ACCOUNT_MARGIN_INITIAL);
    // 維持証拠金（全ての未決済ポジションの最小額をカバーするために口座内でリザーブされた最低資本金）
    double marginMaintenance = AccountInfoDouble(ACCOUNT_MARGIN_MAINTENANCE);
    // 流動資産？
    double assets = AccountInfoDouble(ACCOUNT_ASSETS);
    // 流動負債？
    double liabilities = AccountInfoDouble(ACCOUNT_LIABILITIES);
    // 拘束された手数料の額
    double commissionBlocked = AccountInfoDouble(ACCOUNT_COMMISSION_BLOCKED);

    // 文字列に結合して返す
    int digits = (int) AccountInfoInteger(ACCOUNT_CURRENCY_DIGITS);
    int soDigits = AccountInfoInteger(ACCOUNT_MARGIN_SO_MODE) == ACCOUNT_STOPOUT_MODE_PERCENT ? 1 : digits;
    string s;
    StringConcatenate(s, "----- AccountInfoDouble -----",
        "\nACCOUNT_BALANCE = ", DoubleToString(balance, digits),
        "\nACCOUNT_CREDIT = ", DoubleToString(credit, digits),
        "\nACCOUNT_PROFIT = ", DoubleToString(profit, digits),
        "\nACCOUNT_EQUITY = ", DoubleToString(equity, digits),
        "\nACCOUNT_MARGIN = ", DoubleToString(margin, digits),
        "\nACCOUNT_MARGIN_FREE = ", DoubleToString(marginFree, digits),
        "\nACCOUNT_MARGIN_LEVEL = ", DoubleToString(marginLevel, 1),
        "\nACCOUNT_MARGIN_SO_CALL = ", DoubleToString(marginSoCall, soDigits),
        "\nACCOUNT_MARGIN_SO_SO = ", DoubleToString(marginSoSo, soDigits),
        "\nACCOUNT_MARGIN_INITIAL = ", DoubleToString(marginInitial, digits),
        "\nACCOUNT_MARGIN_MAINTENANCE = ", DoubleToString(marginMaintenance, digits),
        "\nACCOUNT_ASSETS = ", DoubleToString(assets, digits),
        "\nACCOUNT_LIABILITIES = ", DoubleToString(liabilities, digits),
        "\nACCOUNT_COMMISSION_BLOCKED = ", DoubleToString(commissionBlocked, digits)
    );
    return s;
}

/**
 * AccountInfoString API で取得できるアカウント情報を取得する。
 */
string getAccountInfoString() {
    // クライアント名
    string name = AccountInfoString(ACCOUNT_NAME);
    // 取引サーバー名
    string server = AccountInfoString(ACCOUNT_SERVER);
    // 口座の通貨名
    string currency = AccountInfoString(ACCOUNT_CURRENCY);
    // 口座を提供している会社名
    string company = AccountInfoString(ACCOUNT_COMPANY);

    return "---- AccountInfoString ----" +
        "\nACCOUNT_NAME = " + name +
        "\nACCOUNT_SERVER = " + server +
        "\nACCOUNT_CURRENCY = " + currency +
        "\nACCOUNT_COMPANY = " + company;
}

/**
 * スクリプトのエントリーポイント。
 */
void OnStart() {
    MessageBox(
        getAccountInfoInteger() + "\n\n" +
        getAccountInfoDouble() + "\n\n" +
        getAccountInfoString()
    );
}
{{< /code >}}

{{< code title="実行結果" >}}
----- AccountInfoInteger -----
ACCOUNT_LOGIN = 123456789
ACCOUNT_TRADE_MODE = 0 (ACCOUNT_TRADE_MODE_DEMO)
ACCOUNT_LEVERAGE = 25
ACCOUNT_LIMIT_ORDERS = 0
ACCOUNT_MARGIN_SO_MODE = 0 (ACCOUNT_STOPOUT_MODE_PERCENT)
ACCOUNT_TRADE_ALLOWED = true
ACCOUNT_TRADE_EXPERT = true
ACCOUNT_MARGIN_MODE = 2 (ACCOUNT_MARGIN_MODE_RETAIL_HEDGING)
ACCOUNT_CURRENCY_DIGITS = 0
ACCOUNT_FIFO_CLOSE = false

----- AccountInfoDouble -----
ACCOUNT_BALANCE = 2998975
ACCOUNT_CREDIT = 0
ACCOUNT_PROFIT = -46086
ACCOUNT_EQUITY = 2952889
ACCOUNT_MARGIN = 203632
ACCOUNT_MARGIN_FREE = 2749257
ACCOUNT_MARGIN_LEVEL = 1450.1
ACCOUNT_MARGIN_SO_CALL = 100.0
ACCOUNT_MARGIN_SO_SO = 100.0
ACCOUNT_MARGIN_INITIAL = 0
ACCOUNT_MARGIN_MAINTENANCE = 0
ACCOUNT_ASSETS = 0
ACCOUNT_LIABILITIES = 0
ACCOUNT_COMMISSION_BLOCKED = 0

---- AccountInfoString ----
ACCOUNT_NAME = maku
ACCOUNT_SERVER = OANDA-Japan MT5 Demo
ACCOUNT_CURRENCY = JPY
ACCOUNT_COMPANY = OANDA Corporation
{{< /code >}}

