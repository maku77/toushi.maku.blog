---
title: "MetaTrader/MQL: シンボルのスプレッド情報を取得する (SymbolInfoInteger)"
linkTitle: "シンボルのスプレッド情報を取得する (SymbolInfoInteger)"
url: "p/zyvwxx9/"
date: "2015-10-08"
tags: ["MetaTrader/MQL"]
---

指定した通貨ペアのスプレッドを取得するには、__`SymbolInfoInteger`__ 関数の引数に __`SYMBOL_SPREAD`__ を指定します。
現在のチャートの通貨ペアは、`Symbol` 関数を使えば取得できます。

{{< code lang="cpp" title="Scripts/ShowSymbolSpread.mq5" >}}
void OnStart() {
    long spread = SymbolInfoInteger(Symbol(), SYMBOL_SPREAD);
    Alert(StringFormat("Spread of %s: %d", Symbol(), spread));
}
{{< /code >}}

{{< code title="実行結果" >}}
Spread of USDJPY: 4
{{< /code >}}

