---
title: "MetaTrader/MQL5: シンボル名を取得する (Symbol, ChartSymbol, SymbolsTotal, SymbolName)"
linkTitle: "シンボル名を取得する (Symbol, ChartSymbol, SymbolsTotal, SymbolName)"
url: "/p/8xwyrnf"
date: "2020-12-19"
tags: ["MetaTrader/MQL"]
---

カレントチャートのシンボル名を取得する (Symbol)
----

スクリプトや、EA から、現在のチャートのシンボル名を取得するには、[_Symbol 変数](https://www.mql5.com/ja/docs/predefined/_symbol) あるいは [Symbol 関数](https://www.mql5.com/ja/docs/check/symbol) を使用します。

{{< code lang="cpp" title="Scripts/Sample.mq5" >}}
void OnStart() {
    string sym = _Symbol;  // Symbol() でも同様
    Print(sym);  //=> "USDJPY"
}
{{< /code >}}


指定したチャートのシンボル名を取得する (ChartSymbol)
----

[ChartSymbol 関数](https://www.mql5.com/ja/docs/chart_operations/chartsymbol) を使用すると、チャート ID で指定したチャートのシンボル名を取得することができます。

{{< code lang="cpp" >}}
void OnStart() {
    // long chartId = ...;
    string sym = ChartSymbol(chartId);
    Print(sym);  //=> "USDJPY"
}
{{< /code >}}

- 参考: [表示しているチャートを列挙する (ChartFirst, ChartNext)](/p/244ung6)


すべてのシンボル名を取得する (SymbolTotal, SymbolName)
----

下記の関数を使用すると、現在のシステムで扱えるすべてのシンボル名を取得することができます。

- [SymbolTotal()](https://www.mql5.com/ja/docs/marketinformation/symbolstotal) ... シンボルの数を取得します。
- [SymbolName()](https://www.mql5.com/ja/docs/marketinformation/symbolname) ... 指定したインデックスのシンボル名を取得します。

次のサンプルスクリプトでは、すべてのシンボル名称と、それぞれの Bid/Ask 価格を表示しています。

{{< code lang="cpp" title="Scripts/Sample.mq5" >}}
/**
 * すべてのシンボル名を取得します。
 *
 * Params:
 *   symbols - シンボル名が格納されます
 *   onlyInMarketWatch - 「気配値表示」内のシンボルに限定するのであれば true
 * Returns:
 *   見つかったシンボルの数
 */
int getAllSymbolNames(string &symbols[], bool onlyInMarketWatch=true) {
    int n = SymbolsTotal(onlyInMarketWatch);
    ArrayResize(symbols, n);
    for (int i = 0; i < n; ++i) {
        symbols[i] = SymbolName(i, onlyInMarketWatch);
    }
    return n;
}

// スクリプトのエントリポイント
void OnStart() {
    string symbols[];
    int n = getAllSymbolNames(symbols);
    for (int i = 0; i < n; ++i) {
        double bid = SymbolInfoDouble(symbols[i], SYMBOL_BID);
        double ask = SymbolInfoDouble(symbols[i], SYMBOL_ASK);
        PrintFormat("%2d: %s %f/%f", i + 1, symbols[i], bid, ask);
    }
}
{{< /code >}}

{{< code title="実行結果" >}}
 1: USDJPY 103.301000/103.326000
 2: EURJPY 126.584000/126.639000
 3: GBPJPY 139.443000/139.493000
 4: AUDJPY 78.727000/78.759000
 5: EURUSD 1.225320/1.225550
 6: ...
{{< /code >}}
