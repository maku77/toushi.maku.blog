---
title: "MetaTrader/MQL: インジケーターの実装例 - SMA（単純移動平均）"
linkTitle: "インジケーターの実装例 - SMA（単純移動平均）"
url: "/p/h3fr3do"
date: "2015-02-01"
tags: ["MetaTrader/MQL"]
weight: 900
---

移動平均線のカスタムインジケータを作成する
----

単純移動平均線 (SMA: Simple Moving Average) を表示するためのインジケータはデフォルトで用意されていますが、ここでは勉強のためにインジケータを自作してみます。

{{< image src="img-001.png" >}}

{{< code lang="cpp" title="MySma.mt4" >}}
#property description "My Moving Average"
#property strict
#property indicator_chart_window
#property indicator_buffers 1
#property indicator_plots   1

// Indicator settings
#property indicator_label1  "MA"
#property indicator_type1   DRAW_LINE
#property indicator_color1  clrRed
#property indicator_style1  STYLE_SOLID
#property indicator_width1  1

// Input parameters
input int gPeriod = 7; // MA Period

// Indicator buffers
double gMaBuffer[];

int OnInit() {
    if (gPeriod <= 0) {
        Alert("Period must be larger than 0");
        return INIT_PARAMETERS_INCORRECT;
    }
    SetIndexBuffer(0, gMaBuffer); 
    IndicatorShortName("MA(" + gPeriod + ")");
    return INIT_SUCCEEDED;
}

/**
 * [Utility]
 * How many candles should be re-calculated.
 */
int changedBars(int rates_total, int prev_calculated) {
    if (prev_calculated == 0) {
        return rates_total;
    }
    // The latest bar should be updated, so add 1.
    return rates_total - prev_calculated + 1;
}

/**
 * Calculate average of vals[index .. index+count)
 */
double average(const double &vals[], int index, int count) {
    double sum = 0.0;
    for (int i = 0; i < count; ++i) {
        sum += vals[index + i];
    }
    return sum / count;
}

/**
 * Updates a moving average buffer.
 *
 * Parameters:
 *   buf -- the buffer where calculated MA is stored
 *   price -- the price used for calculating the MA
 *   price_count -- the number of prices
 *   changed -- price[0..changed-1] has been updated
 *   period -- MA's period
 */
void calcMovingAverage(double &buf[], const double &price[], int price_count,
        int changed, int period) {
    // Needs adequate price data for calculating MA.
    if (price_count < period) {
        ArrayFill(buf, 0, price_count, EMPTY_VALUE);
        return;
    }

    // Update each MA
    int count = MathMin(changed, price_count - period + 1);
    for (int i = 0; i < count; ++i) {
        buf[i] = average(price, i, period);
    }
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
    if (rates_total < gPeriod) {
        return 0;
    }

    int changed = changedBars(rates_total, prev_calculated);
    calcMovingAverage(gMaBuffer, close, rates_total, changed, gPeriod);

    return rates_total;
}
{{< /code >}}

### コードの説明

{{< code lang="cpp" >}}
// Input parameters
input int gPeriod = 7; // MA Period
{{< /code >}}

何本のローソク足を使って平均値を求めるかを示す変数です。
__`input`__ キーワードを使うことで、インジケータをチャートにセットするときに、ユーザが自由に値を変更できるようになります。
そのときにデフォルトでは変数名が表示されるのですが、上記のように、変数宣言の後ろにコメントを記載しておくと、そのテキストが代わりに表示されるようになります。

{{< code lang="cpp" >}}
// Indicator buffers
double gMaBuffer[];

int OnInit() {
    if (gPeriod <= 0) {
        Alert("Period must be larger than 0");
        return INIT_PARAMETERS_INCORRECT;
    }
    SetIndexBuffer(0, gMaBuffer); 
    IndicatorShortName("MA(" + gPeriod + ")");
    return INIT_SUCCEEDED;
}
{{< /code >}}

今回は、移動平均線を一本だけ表示するので、指標バッファをひとつだけ (`gMaBuffer`) 用意しています。

{{< code lang="cpp" >}}
void calcMovingAverage(double &buf[], const double &price[], int price_count,
        int changed, int period) {
    // Needs adequate price data for calculating MA.
    if (price_count < period) {
        ArrayFill(buf, 0, price_count, EMPTY_VALUE);
        return;
    }

    // Update each MA
    int count = MathMin(changed, price_count - period);
    for (int i = 0; i < count; ++i) {
        buf[i] = average(price, i, period);
    }
}

int OnCalculate(...) {
    int changed = changedBars(rates_total, prev_calculated);
    calcMovingAverage(gMaBuffer, close, rates_total, changed, gPeriod);
    return rates_total;
}
{{< /code >}}

`OnCalculate` 関数では、実際に移動平均を求めていきます。
ローソク足の数（`rates_total`）が移動平均区間に満たない場合は、移動平均を求めることはできないので、そのまま return しています。
その後、各ローソク足から見て、指定区間分の合計を求めて平均を出しています。
よく考えると、各計算で重複した期間を合計しているので、もう少し計算を効率化できることが分かります。


移動平均計算の最適化
----

下記は、移動平均線の計算処理において、重複した計算をしないように効率化したものです。

{{< code lang="cpp" >}}
/**
 * Sum the elements of the array.
 */
double sumArray(const double& values[], int count) {
    double sum = 0.0;
    for (int i = 0; i < count; ++i) {
        sum += values[i];
    }
    return sum;
}

/**
 * Updates a moving average buffer.
 *
 * Parameters:
 *   buf -- the buffer where calculated MA is stored
 *   price -- the price used for calculating the MA
 *   price_count -- the number of prices
 *   changed -- price[0..changed-1] has been updated
 *   period -- MA's period
 */
void calcMovingAverage(double &buf[], const double &price[], int price_count,
        int changed, int period) {
    // Needs adequate price data for calculating MA.
    if (price_count < period) {
        ArrayFill(buf, 0, price_count, EMPTY_VALUE);
        return;
    }

    // Update the MA for the latest candle
    double sum = sumArray(price, period);
    buf[0] = sum / period;

    // Update each MA
    int count = MathMin(changed, price_count - period);
    for (int i = 0; i < count - 1; ++i) {
        sum = sum - price[i] + price[i + period];
        buf[i + 1] = sum / period;
    }
}
{{< /code >}}


3 本の移動平均線を表示する
----

下記は、ひとつのカスタムインジケータで、複数の移動平均線を表示するサンプルです。
ここでは、3 本の移動平均線を表示しています。
1 本のときと異なるのは、3 本分の指標バッファを用意しているところだけです。

{{< code lang="cpp" title="MySma.mt4" >}}
// Global settings
#property description "My Moving Average"
#property strict
#property indicator_chart_window
#property indicator_buffers 3
#property indicator_plots   3

// Indicator settings
#property indicator_type1   DRAW_LINE
#property indicator_type2   DRAW_LINE
#property indicator_type3   DRAW_LINE
#property indicator_color1  clrPink
#property indicator_color2  clrYellow
#property indicator_color3  clrCyan
#property indicator_style1  STYLE_SOLID
#property indicator_style2  STYLE_SOLID
#property indicator_style3  STYLE_DOT
#property indicator_width1  1
#property indicator_width2  1
#property indicator_width3  1

// Input parameters
input int gPeriod1 = 5;  // MA Period 1
input int gPeriod2 = 25; // MA Period 2
input int gPeriod3 = 75; // MA Period 3

// Indicator buffers
double gMaBuffer1[];
double gMaBuffer2[];
double gMaBuffer3[];

int OnInit() {
    if (gPeriod1 <= 0 || gPeriod2 <= 0 || gPeriod3 <= 0) {
        Alert("Period must be larger than 0");
        return INIT_PARAMETERS_INCORRECT;
    }

    SetIndexBuffer(0, gMaBuffer1);
    SetIndexBuffer(1, gMaBuffer2);
    SetIndexBuffer(2, gMaBuffer3);
    SetIndexLabel(0, StringFormat("MA(%i)", gPeriod1));  // データウィンドウに出る名前
    SetIndexLabel(1, StringFormat("MA(%i)", gPeriod2));
    SetIndexLabel(2, StringFormat("MA(%i)", gPeriod3));
    IndicatorShortName(StringFormat("MA(%i, %i, %i)",
            gPeriod1, gPeriod2, gPeriod3));

    return INIT_SUCCEEDED;
}

/**
 * [Utility]
 * How many candles should be re-calculated.
 */
int changedBars(int rates_total, int prev_calculated) {
    if (prev_calculated == 0) {
        return rates_total;
    }
    // The latest bar should be updated, so add 1.
    return rates_total - prev_calculated + 1;
}

/**
 * Sum the elements of the array.
 */
double sumArray(const double& values[], int count) {
    double sum = 0.0;
    for (int i = 0; i < count; ++i) {
        sum += values[i];
    }
    return sum;
}

/**
 * Updates a moving average buffer.
 *
 * Parameters:
 *   buf -- the buffer where calculated MA is stored
 *   price -- the price used for calculating the MA
 *   price_count -- the number of prices
 *   changed -- price[0..changed-1] has been updated
 *   period -- MA's period
 */
void calcMovingAverage(double &buf[], const double &price[], int price_count,
        int changed, int period) {
    // Needs adequate price data for calculating MA.
    if (price_count < period) {
        ArrayFill(buf, 0, price_count, EMPTY_VALUE);
        return;
    }

    // Update the MA for the latest candle
    double sum = sumArray(price, period);
    buf[0] = sum / period;

    // Update each MA
    int count = MathMin(changed, price_count - period);
    for (int i = 0; i < count - 1; ++i) {
        sum = sum - price[i] + price[i + period];
        buf[i + 1] = sum / period;
    }
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
    int changed = changedBars(rates_total, prev_calculated);
    calcMovingAverage(gMaBuffer1, close, rates_total, changed, gPeriod1);
    calcMovingAverage(gMaBuffer2, close, rates_total, changed, gPeriod2);
    calcMovingAverage(gMaBuffer3, close, rates_total, changed, gPeriod3);
    return rates_total;
}
{{< /code >}}

