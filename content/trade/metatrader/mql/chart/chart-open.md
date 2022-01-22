---
title: "MetaTrader/MQL: 新しいチャートを開く (ChartOpen)"
linkTitle: "新しいチャートを開く (ChartOpen)"
url: "/p/hx7enu3"
date: "2015-10-10"
lastmod: "2021-02-12"
tags: ["MetaTrader/MQL"]
---

[ChartOpen 関数](https://www.mql5.com/en/docs/chart_operations/chartopen) を使うと、指定した通貨ペア、時間足のチャートを開くことができます。
下記は、ドル円の週足チャートを開く例です。
`ChartOpen` 関数が返したチャート ID を使って、開いたチャートの設定を行うことができます。

{{< code lang="cpp" title="Scripts/Hello.mq5" >}}
void OnStart() {
    // 週足チャートを開く
    long chartId = ChartOpen("USDJPY", PERIOD_W1);
    if (chartId == 0) {
        // オープンに失敗した場合（シンボル名がおかしいとか、チャートを開きすぎとか）
        Alert("Could not open a new chart: ", GetLastError());
        return;
    }

    // 開いたチャートを設定する
    ChartSetInteger(chartId, CHART_MODE, CHART_LINE);  // ライン形式
    ChartSetInteger(chartId, CHART_SHOW_VOLUMES, CHART_VOLUME_TICK);  // 出来高
    ChartSetInteger(chartId, CHART_SHOW_GRID, false);  // グリッドを非表示
}
{{< /code >}}

カレントチャートと同じ通貨ペアのチャートを新しく開きたい場合は、第 1 引数で `"USDJPY"` と指定しているところを `NULL` に置き換えれば OK です。
第 2 引数で指定する足のタイムフレームには、[ENUM_TIMEFRAMES](https://www.mql5.com/en/docs/constants/chartconstants/enum_timeframes) 型のいずれかの値を指定します。
`PERIOD_CURRENT` を指定して、カレントチャートと同じタイムフレームを指定することもできます。

