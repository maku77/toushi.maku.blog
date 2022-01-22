---
title: "MetaTrader/MQL: チャートのサイズ（幅・高さ）を取得する"
linkTitle: "チャートのサイズ（幅・高さ）を取得する"
url: "/p/xhxumiu"
date: "2020-10-27"
lastmod: "2021-01-29"
tags: ["MetaTrader/MQL"]
---

[ChartGetInteger 関数](https://www.mql5.com/ja/docs/chart_operations/chartgetinteger) の第 2 パラメーター (prop_id) に __`CHART_WIDTH_IN_PIXELS`__ および __`CHART_HEIGHT_IN_PIXELS`__ を指定することで、指定したチャートの幅・高さを取得することができます。
取得されるサイズは、チャートの描画領域のみのサイズです（軸の価格表示部分などは含まれません）。

`ChartGetInteger()` には次のような 2 つのバージョンがあります。
2 つ目のバージョンを使うと、戻り値で関数の実行に成功したかどうかを調べることができます。

{{< code lang="cpp" >}}
long ChartGetInteger(
    long chart_id,    // 対象のチャート（0 はカレントチャート）
    int prop_id,      // 取得したいプロパティの ID
    int sub_window=0  // サブウィンドウ番号（0 はメインチャート）
)

bool ChartGetInteger(
    long chart_id,   // 対象のチャート（0 はカレントチャート）
    int prop_id,     // 取得したいプロパティの ID
    int sub_window,  // サブウィンドウ番号（0 はメインチャート）
    long& long_var   // 取得結果の格納先
)
{{< /code >}}

インジケーター用のサブウィンドウのサイズを調べたい場合は、第 3 パラメーター `sub_window` に 1, 2, 3 のような数値を指定します（1 がひとつめのサブチャートです）。

{{< code lang="cpp" title="Scripts/MyScript.mq5" >}}
void OnStart() {
    long width = ChartGetInteger(0, CHART_WIDTH_IN_PIXELS);
    long height = ChartGetInteger(0, CHART_HEIGHT_IN_PIXELS);
    MessageBox(StringFormat("width=%d, height=%d", width, height));
}
{{< /code >}}

下記はエラー処理なども行う例です（MT4用）。

{{< code lang="cpp" title="Scripts/ShowChartWidthAndHeight.mq4" >}}
#property strict
#include <stdlib.mqh>  // ErrorDescription

/**
 * 指定したチャートのメインチャートウィンドウの幅（ピクセル）を取得します。
 * 取得に失敗した場合は -1 を返します。
 */
int GetChartWidthInPixels(const long chartId = 0) {
    long result = -1;
    if (!ChartGetInteger(chartId, CHART_WIDTH_IN_PIXELS, 0, result)) {
        string err = ErrorDescription(GetLastError());
        PrintFormat("ERROR in %s: %s", __FUNCTION__, err);
    }
    return (int) result;
}

/**
 * 指定したチャートのメインチャートウィンドウの高さ（ピクセル）を取得します。
 * 取得に失敗した場合は -1 を返します。
 */
int GetChartHeightInPixels(const long chartId = 0) {
    long result = -1;
    if (!ChartGetInteger(chartId, CHART_HEIGHT_IN_PIXELS, 0, result)) {
        string err = ErrorDescription(GetLastError());
        PrintFormat("ERROR in %s: %s", __FUNCTION__, err);
    }
    return (int) result;
}

void OnStart() {
    int width = GetChartWidthInPixels();
    int height = GetChartHeightInPixels();
    MessageBox(StringFormat("width=%d, height=%d", width, height));
}
{{< /code >}}

