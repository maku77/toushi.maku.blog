---
title: "MetaTrader/MQL: 表示しているチャートを列挙する (ChartFirst, ChartNext)"
linkTitle: "表示しているチャートを列挙する (ChartFirst, ChartNext)"
url: "/p/244ung6"
date: "2020-12-19"
tags: ["MetaTrader/MQL"]
---

MQL の下記の関数を使用すると、現在表示しているチャートの情報を列挙することができます。

- [ChartFirst 関数](https://www.mql5.com/ja/docs/chart_operations/chartfirst) ... 最初のチャート ID を取得します（見つからない場合は -1）。
- [ChartNext 関数](https://www.mql5.com/ja/docs/chart_operations/chartnext) ... 次のチャートのチャート ID を取得します（見つからない場合は -1）。

具体的には、`ChartFirst` 関数で最初のチャートの ID を取得し、`ChartNext` 関数でその次のチャートの ID を繰り返し取得していく、という感じで処理できます。
処理するチャートがなくなったときは、上記の関数は -1 を返すので、正の値を返す間だけ繰り返し処理すれば OK です。

次のサンプルスクリプトでは、現在表示しているすべてのチャートの情報（チャートID、シンボル名、時間足）を列挙しています。

{{< code lang="cpp" title="Scripts/Sample.mq5" >}}
void showChartInfo(long chartId) {
    string sym = ChartSymbol(chartId);
    ENUM_TIMEFRAMES period = ChartPeriod(chartId);
    PrintFormat("%I64d: %s (%s)", chartId, sym, EnumToString(period));
}

void OnStart() {
    for (long id = ChartFirst(); id >= 0; id = ChartNext(id)) {
        showChartInfo(id);
    }
}
{{< /code >}}

{{< code title="実行結果" >}}
128968169024912109: USDJPY (PERIOD_M5)
128968169024912110: EURJPY (PERIOD_H1)
128968169024912111: EURUSD (PERIOD_D1)
{{< /code >}}

MQL5 の標準ライブラリとして提供されている [CChart クラス](https://www.mql5.com/ja/docs/standardlibrary/cchart) を使っても同様のことを行えます。

{{< code lang="cpp" title="Scripts/Sample.mq5" >}}
#include <Charts/Chart.mqh>

void showChartInfo(const CChart& chart) {
    long id = chart.ChartId();
    string sym = chart.Symbol();
    ENUM_TIMEFRAMES period = chart.Period();
    PrintFormat("%I64d: %s (%s)", id, sym, EnumToString(period));
}

void OnStart() {
    CChart ch;
    for (ch.FirstChart(); ch.ChartId() != -1; ch.NextChart()) {
        showChartInfo(ch);
    }
}
{{< /code >}}

