---
title: "MetaTrader/MQL: OrderSend で決済注文を出す（ポジションのクローズ）(MT5)"
linkTitle: "OrderSend で決済注文を出す（ポジションのクローズ）(MT5)"
url: "/p/wb8rxic"
date: "2021-02-02"
tags: ["MetaTrader/MQL"]
weight: 201
---

ポジションのクローズは反対売買
----

MT5 においてポジションのクローズ（決済）を行うには、`OrderSend` で逆方向のポジションを追加する注文を行います。
つまり、現在のポジションと相殺するように買い注文 or 売り注文を出します。

現在の口座が、両建て可能な「ヘッジアカウント」の場合、反対注文を出すときは、対象のポジションを特定するためのチケット番号 (`MqlTradeRequest.position`) を指定しなければいけないことに注意してください。
「ネットアカウント」を使用している場合は、シンボル（銘柄）だけを指定すれば OK です（ポジションのチケット番号を指定しても無視されます）。

- 参考: [ヘッジアカウントとネットアカウントの違いを理解する](/p/xmseugr)


ネットアカウントにおけるポジションクローズ
----

ネットアカウントにおいて既存のポジションをクローズするには、シンボル名を指定して `OrderSend` で成行注文 (`action == TRADE_ACTION_DEAL`) あるいは、指値注文 (`action == TRADE_ACTION_PENDING`) を入れます。
成行注文でも指値注文でも決済タイミングが異なるだけで同様です。

あるシンボルのポジションをすべて閉じるには、反対方向に同じボリュームだけ売買注文を入れる必要があります。
そのため、まずは現在のポジションの量を調べます。

{{< code lang="cpp" >}}
/**
 * ネットアカウントにおいて、指定したシンボルのポジション情報を取得します。
 * ヘッジアカウントで使用すると、最初に見つかったポジションの情報を返します。
 *
 * @param volume[out] 保有ポジションのロット数
 * @param posType[out] 保有ポジションの売買方向
 *                     (POSITION_TYPE_SELL or POSITION_TYPE_BUY)
 * @param symbol[in] 取得対象のシンボル（省略時はカレントシンボル）
 * @return ポジションが見つかった場合: true、ノーポジの場合: false
 */
bool getOpenPosition_InNetAccount(
    double &volume,
    ENUM_POSITION_TYPE &posType,
    string symbol = NULL
) {
    if (symbol == NULL) symbol = Symbol();

    if (!PositionSelect(symbol)) {
        // 指定したシンボルのポジションが存在しないときは、PositionSelect() は失敗して、
        // GetLastError() == 4753 (Position not found) になる。
        return false;
    }

    // 見つかったポジション情報を格納
    volume = PositionGetDouble(POSITION_VOLUME);
    posType = (ENUM_POSITION_TYPE) PositionGetInteger(POSITION_TYPE);
    return true;
}

void OnStart() {
    double volume;
    ENUM_POSITION_TYPE posType;
    if (getOpenPosition_InNetAccount(volume, posType)) {
        printf("ポジション情報: volume=%f, posType=%s", volume, EnumToString(posType));
    } else {
        Print("ポジション情報が見つかりません");
    }
}
{{< /code >}}

見つかったポジションのタイプが `POSITION_TYPE_BUY` であれば、ロングポジション（買いポジ）を持っているので、同じボリュームの売り注文を出せば、すべてのポジションをクローズできることになります。

{{< code lang="cpp" title="Scripts/ClosePosition_InNetAccount.mq5" >}}
/**
 * 買い or 売りの成行注文を出します。
 *
 * @param symbol 対象シンボル
 * @param volume ロット数（ボリューム）
 * @param orderType 買い(ORDER_TYPE_BUY) or 売り(ORDER_TYPE_SELL)
 */
bool marketOrder(const string& symbol, double volume, ENUM_ORDER_TYPE orderType) {
    // Ask/Bid 価格のどちらを使うか？
    ENUM_SYMBOL_INFO_DOUBLE bidOrAsk =
        orderType == ORDER_TYPE_BUY ? SYMBOL_ASK : SYMBOL_BID;

    // 注文の作成
    MqlTradeRequest request = {0};
    request.action = TRADE_ACTION_DEAL;  // 成行注文
    request.symbol = symbol;  // シンボル（銘柄）
    request.volume = volume;  // ロット数
    request.type = orderType;  // 買い or 売り
    request.price = SymbolInfoDouble(symbol, bidOrAsk);  // 価格
    request.type_filling = ORDER_FILLING_IOC;  // フィル・モード
    request.deviation = 10;  // 許容スリッページ（ポイント）

    // 注文を送信
    MqlTradeResult result = {0};
    if (OrderSend(request, result)) {
        switch (result.retcode) {
            case TRADE_RETCODE_PLACED: // 注文が出された
            case TRADE_RETCODE_DONE: // リクエスト完了
            case TRADE_RETCODE_DONE_PARTIAL: // リクエストが一部完了
            case TRADE_RETCODE_NO_CHANGES: // リクエストに変更なし
                printf("Position closed: %s, vol=%f, %s",
                    request.symbol, result.volume, EnumToString(orderType));
                return true;
        }
    }

    // OrderSend 関数自体が失敗した場合（パラメータの不正など）、
    // あるいは、取引サーバーがエラーコードを返した場合
    printf("Could not close position: retcode=%d, comment=%s",
        result.retcode, result.comment);
    return false;
}

/**
 * ネットアカウントにおいて、指定したシンボル（省略時はカレントシンボル）のポジションをすべて決済します。
 * ヘッジアカウントで使用すると、最初に見つかったポジションと同じボリュームの新規反対ポジションが作られます。
 *
 * @return ポジションクローズしたら true、ポジションがなかったり、クローズしっぱしたら false
 */
bool closePosition_InNetAccount(string symbol = NULL) {
    if (symbol == NULL) symbol = Symbol();

    // ポジション情報を取得する
    if (!PositionSelect(symbol)) {
        // 指定したシンボルのポジションが存在しないときは、PositionSelect() は失敗して、
        // GetLastError() == 4753 (Position not found) になる。
        return false;
    }
    double volume = PositionGetDouble(POSITION_VOLUME);
    ENUM_POSITION_TYPE posType =
        (ENUM_POSITION_TYPE) PositionGetInteger(POSITION_TYPE);

    // 反対方向の売買注文を出す
    ENUM_ORDER_TYPE orderType =
        posType == POSITION_TYPE_BUY ? ORDER_TYPE_SELL : ORDER_TYPE_BUY;
    return marketOrder(symbol, volume, orderType);
}

void OnStart() {
    closePosition_InNetAccount();
}
{{< /code >}}

ネットアカウント（両建てなし口座）において、上記のスクリプトを実行すると、カレントシンボルのポジションをすべて決済します。
ただし、ヘッジアカウント（両建てあり口座）で実行すると、最初に見つかったポジションと同量の反対ポジションが新規にオープンされることに注意してください。
なぜなら、ヘッジアカウントで各ポジションのロット数を増減させるときは、対象のポジションを示すチケット番号 (`MqlTradeRequest.position`) を指定しなければいけないからです。
ヘッジアカウントでポジションのチケット番号を指定せずに注文すると、新規にポジションが作られ、新しいチケット番号が割り当てられます。

ヘッジアカウントでも、次のように取得したポジションのチケット番号を `MqlTradeRequest.position` に指定してやれば、反対方向の売買注文がそのポジションのクローズ（ロット数削減）として扱われます。

{{< code lang="cpp" >}}
// PositionSelect(symbol);
uint positionTicket = (uint) PositionGetInteger(POSITION_TICKET);
{{< /code >}}

ただし、ヘッジアカウントにおいて `PositionSelect` 関数（シンボル指定）でポジションを選択すると、そのシンボル内で一番古いポジションが 1 つだけ選択されることになります。
つまり、上記のように取得したチケット番号でポジションをクローズしようとすると、一番古いポジションだけがクローズされることになります。

次に説明する、ポジションチケット単位でクローズする処理は、ネットアカウントとヘッジアカウントの両方で動作します。


ヘッジアカウントにおけるポジションクローズ（ネットアカウントでも利用可）
----

ヘッジアカウント（両建て可能口座）では、1 つのシンボルにつき複数のポジションを同時保有することができます。
そのため、ヘッジアカウントにおいて、あるシンボルのポジションをすべてクローズするには、複数のポジションをループ処理して順番にクローズしていく必要があります。

すべてのポジションをループ処理するには、`PositionGetTicket` あるいは `PositionGetSymbol` にインデックスを指定してポジション情報を 1 つずつ取得していきます。
ポイントは、ポジションクローズ時に残りのポジションのインデックスがずれてしまわないように、__後ろのインデックスのものからクローズしていく__ ところです。

{{< code lang="cpp" title="Scripts/CloseAllPositions.mq5" >}}
/**
 * 買い or 売りの成行注文を出します（決済用）。
 *
 * @param symbol 対象シンボル
 * @param volume ロット数（ボリューム）
 * @param position 決済対象のポジションのチケット番号（ネットアカウント時は無視されます）
 * @param orderType 買い(ORDER_TYPE_BUY) or 売り(ORDER_TYPE_SELL)
 */
bool marketOrder(
    const string& symbol,
    double volume,
    ENUM_ORDER_TYPE orderType,
    uint position
) {
    // Ask/Bid 価格のどちらを使うか？
    ENUM_SYMBOL_INFO_DOUBLE bidOrAsk =
        orderType == ORDER_TYPE_BUY ? SYMBOL_ASK : SYMBOL_BID;

    // 注文の作成
    MqlTradeRequest request = {0};
    request.action = TRADE_ACTION_DEAL;  // 成行注文
    request.symbol = symbol;  // シンボル（銘柄）
    request.volume = volume;  // ロット数
    request.type = orderType;  // 買い or 売り
    request.position = position;
    request.price = SymbolInfoDouble(symbol, bidOrAsk);  // 価格
    request.type_filling = ORDER_FILLING_IOC;  // フィル・モード
    request.deviation = 10;  // 許容スリッページ（ポイント）

    // 注文を送信
    MqlTradeResult result = {0};
    if (OrderSend(request, result)) {
        switch (result.retcode) {
            case TRADE_RETCODE_PLACED: // 注文が出された
            case TRADE_RETCODE_DONE: // リクエスト完了
            case TRADE_RETCODE_DONE_PARTIAL: // リクエストが一部完了
            case TRADE_RETCODE_NO_CHANGES: // リクエストに変更なし
                printf("Position closed: %s, vol=%f, %s",
                    request.symbol, result.volume, EnumToString(orderType));
                return true;
        }
    }

    // OrderSend 関数自体が失敗した場合（パラメータの不正など）、
    // あるいは、取引サーバーがエラーコードを返した場合
    printf("Could not close position: retcode=%d, comment=%s",
        result.retcode, result.comment);
    return false;
}

/**
 * 指定したインデックス、シンボルのポジションをクローズします。
 */
bool closePositionByIndex(int posIndex, const string& symbol) {
    // ポジションをインデックスで選択すると同時にシンボルの確認
    string selectedSymbol = PositionGetSymbol(posIndex);
    if (selectedSymbol != symbol) {
        return false;  // 対象外のシンボル
    }

    // ポジション情報を取得する
    double volume = PositionGetDouble(POSITION_VOLUME);
    ENUM_POSITION_TYPE posType =
        (ENUM_POSITION_TYPE) PositionGetInteger(POSITION_TYPE);
    uint position = (uint) PositionGetInteger(POSITION_TICKET);

    // 反対方向の売買注文を出す
    ENUM_ORDER_TYPE orderType =
        posType == POSITION_TYPE_BUY ? ORDER_TYPE_SELL : ORDER_TYPE_BUY;
    return marketOrder(selectedSymbol, volume, orderType, position);
}

/**
 * 指定したシンボル（省略時はカレントシンボル）のすべてのポジションをクローズします。
 */
void closeAllPositions(string symbol = NULL) {
    if (symbol == NULL) symbol = Symbol();

    // インデックスがずれないように後ろのポジションから閉じていく
    for (int i = PositionsTotal(); i >= 0; i--) {
        closePositionByIndex(i, symbol);
    }
}

void OnStart() {
    closeAllPositions();
}
{{< /code >}}

ちなみに、ネットアカウントにおいても、ポジションのチケット番号の取得や、チケット番号ベースでの情報取得が可能です。
なので、上記の `closeAllPositions` 関数は、ネットアカウントでも動作します（`OrderSend` 関数はあくまでシンボル名に従って売買処理を行います）。


マジックナンバーの一致をチェックする
----

ヘッジアカウントで動作させる EA において、その EA がオープンしたポジションだけを決済対象にしたいときは、`PositionGetInteger` 関数でポジションのマジックナンバーを取得して、自分自身がオープンしたポジションかどうかをチェックします。

{{< code lang="cpp" title="Experts/MyEa.mq5（抜粋）" >}}
// input ulong Magic = 67639000;  // この EA のマジックナンバー

// ポジション情報を取得する
uint magic = (uint) PositionGetInteger(POSITION_MAGIC);
if (magic != Magic) {
    return false;  // 自分が開いたポジションではないので勝手にクローズしない
}
{{< /code >}}

