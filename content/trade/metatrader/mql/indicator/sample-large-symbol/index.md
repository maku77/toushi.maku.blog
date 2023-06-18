---
title: "MetaTrader/MQL: インジケーターの実装例 - 大きなシンボル名を表示する"
linkTitle: "インジケーターの実装例 - 大きなシンボル名を表示する"
url: "p/mbewc25/"
date: "2023-06-18"
tags: ["MetaTrader/MQL"]
weight: 900
---

{{< image w="500" src="img-001.png" title="LargeSymbol インジケーター" >}}

下記の LargeSymbol インジケーターをチャートに適用すると、チャートの左上に大きな文字で通貨ペアと、タイムフレーム（時間足）を表示します（コードリポジトリは[こちら](https://github.com/maku77/metatrader/)）。

{{< code lang="cpp" title="Indicators/maku/LargeSymbol.mq4" >}}
/*
 * LargeSymbol indicator.
 *
 * This indicator displays large symbol name and timeframe
 * on the top-left corner of the current chart.
 */
#property copyright "maku77"
#property link "https://toushi.maku.blog/"
#property version "1.00"
#property strict
#property indicator_chart_window
#property indicator_plots 0 // Surpress "no indicator plot" warning

#include <maku77/ErrorUtil.mqh>
#include <ChartObjects/ChartObjectsTxtControls.mqh>

input color gForegroundColor = clrBlack; // Foreground color
input color gBackgroundColor = clrWhite; // Background color

CChartObjectLabel gLabel;
CChartObjectRectLabel gRect;

// Hide Open/High/Low/Close price indicator
void HideOhlc() {
    ::ChartSetInteger(0, CHART_SHOW_OHLC, false);
}

string RandomObjectName() {
    return "Object-" + IntegerToString(MathRand());
}

string GetPeriodText() {
    switch (Period()) {
        case PERIOD_D1: return "D1";
        case PERIOD_H1: return "H1";
        case PERIOD_H4: return "H4";
        case PERIOD_M1: return "M1";
        case PERIOD_M5: return "M5";
        case PERIOD_M15: return "M15";
        case PERIOD_M30: return "M30";
        case PERIOD_MN1: return "MN1";
        case PERIOD_W1: return "W1";
    }
    return "???";
}

string GetLabelText() {
    return Symbol() + ", " + GetPeriodText();
}

bool AddRect() {
    // Create a new rectangle
    if (!gRect.Create(0, RandomObjectName(), 0, 0, 0, 200, 50)) {
        ErrorUtil::AlertLastError();
        return false;
    }

    // Position
    gRect.Corner(CORNER_LEFT_UPPER);

    // Background
    gRect.BackColor(gBackgroundColor);
    gRect.Background(false);

    gRect.Width(0);
    return true;
}

bool AddLabel() {
    // Create a new label
    if (!gLabel.Create(0, RandomObjectName(), 0, 0, 0)) {
        ErrorUtil::AlertLastError();
        return false;
    }

    // Text
    gLabel.SetString(OBJPROP_TEXT, GetLabelText());
    gLabel.Font("Arial");
    gLabel.FontSize(16);
    gLabel.Color(gForegroundColor);

    // Position
    gLabel.Corner(CORNER_LEFT_UPPER);
    gLabel.Anchor(ANCHOR_LEFT_UPPER);
    gLabel.X_Distance(10);
    gLabel.Y_Distance(0);

    return true;
}

int OnInit() {
    HideOhlc();
    if (!AddRect()) return INIT_FAILED;
    if (!AddLabel()) return INIT_FAILED;
    return INIT_SUCCEEDED;
}

int OnCalculate(const int rates_total,
                const int prev_calculated,
                const datetime &time[],
                const double &open[],
                const double &high[],
                const double &low[],
                const double &close[],
                const long &tick_volume[],
                const long &volume[],
                const int &spread[]) {
    return rates_total;
}
{{< /code >}}

