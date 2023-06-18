---
title: "MetaTrader/MQL: カスタムインジケーターを作成する"
linkTitle: "カスタムインジケーターを作成する"
url: "/p/5q5gs5g"
date: "2015-02-01"
tags: ["MetaTrader/MQL"]
weight: 1
---

カスタムインジケータの作成
----

ここでは、最初のステップとして、ローソク足の終値をラインで結ぶだけのカスタムインジケータを作成してみます。
Meta Editor 上で `Control + N` を押して、Custom Indicator を選択すると、カスタムインジケータのファイルを新規作成することができます。

{{< code lang="cpp" title="MyIndicator.mt4" >}}
#property strict
#property indicator_chart_window
#property indicator_buffers 1
#property indicator_plots 1

// Default properties for Line 1
#property indicator_label1 "Line 1"
#property indicator_type1 DRAW_LINE
#property indicator_color1 clrRed
#property indicator_style1 STYLE_SOLID
#property indicator_width1 1

// Buffer for indicator line
double gBuffer[];

int OnInit() {
    SetIndexBuffer(0, gBuffer, INDICATOR_DATA);
    return INIT_SUCCEEDED;
}

int OnCalculate(
        const int rates_total,      // ローソク足の数
        const int prev_calculated,  // 前回の OnCalculate() の戻り値
        const datetime &time[],     // ローソク足ごとの時刻 [0..rates_total-1]
        const double &open[],       // ローソク足ごとの始値 [0..rates_total-1]
        const double &high[],       // ローソク足ごとの高値 [0..rates_total-1]
        const double &low[],        // ローソク足ごとの安値 [0..rates_total-1]
        const double &close[],      // ローソク足ごとの終値 [0..rates_total-1]
        const long &tick_volume[],
        const long &volume[],
        const int &spread[]) {
    // 終値をそのままインデックス・バッファに詰める
    for (int i = 0; i < rates_total; ++i) {
        gBuffer[i] = close[i];
    }

    // 最新の終値をチャートの左上に表示
    Comment(time[0] + " -- " + close[0]);

    // 次の OnCalculate() の prev_calculated にこの値が入る
    return rates_total;
}
{{< /code >}}

### 各パートの説明

{{< code lang="cpp" >}}
#property indicator_chart_window  // チャート上に表示する
#property indicator_buffers 1     // 使用する時系列バッファの数（表示用 ＋ 計算用）
#property indicator_plots 1       // 使用する時系列バッファの数（表示用）
{{< /code >}}

このプロパティでは、カスタムインジケータをローソクチャート上に重ねて表示すること、ラインを 1 本だけ使用することを宣言しています。
仮に、別ウィンドウでインジケータを表示したい場合は、`indicator_chart_window` の代わりに `indicator_separate_window` を指定します。

{{< code lang="cpp" >}}
#property indicator_label1 "Line 1"
#property indicator_type1 DRAW_LINE     // 表示方法: ライン
#property indicator_color1 clrRed       // 色: 赤
#property indicator_style1 STYLE_SOLID  // ラインの種類: 実線
#property indicator_width1 1            // 太さ: 1
{{< /code >}}

上記のプロパティでは、表示用の 1 本目のラインの設定を行っています。ここではラインが 1 本だけですが、複数のラインを表示するカスタムインジケータを作る場合は、各プロパティ名のサフィックスを 2、3、4 と増やしていきます。

{{< code lang="cpp" >}}
// Buffer for indicator line
double gBuffer[];

int OnInit() {
    SetIndexBuffer(0, gBuffer, INDICATOR_DATA);
    return INIT_SUCCEEDED;
}
{{< /code >}}

最初に一度だけ呼ばれる `OnInit()` 関数の中では、配列 `gBuffer` を、画面表示用のバッファ (`INDICATOR_DATA`) として割り当てています。このバッファに値を設定することで、画面上にインジケータが表示されることになります。仮に、計算用としてだけ使うバッファを追加で割り当てたい場合は、`INDICATOR_CALCULATIONS` というタイプを指定して割り当てます（この場合、`indicator_buffers` プロパティの値を 2 に増やします）。

{{< code lang="cpp" >}}
int OnCalculate(
        const int rates_total,
        const int prev_calculated,
        const datetime &time[],
        const double &open[],
        const double &high[],
        const double &low[],
        const double &close[],
        const long &tick_volume[],
        const long &volume[],
        const int &spread[]) {
    // 終値をそのままインデックス・バッファに詰める
    for (int i = 0; i < rates_total; ++i) {
        gBuffer[i] = close[i];
    }

    // 最新の終値をチャートの左上に表示
    Comment(time[0] + " -- " + close[0]);

    // 次の OnCalculate() の prev_calculated にこの値が入る
    return rates_total;
}
{{< /code >}}

計算のメイン部分となるのが `OnCalculate()` 関数です。`OnCalculate()` 関数は、tick（価格の更新）が発生するごとに呼び出されます。
チャート上のローソク足の数や、始値、終値などの情報がパラメータで渡されます。

### パラメータの説明

* `int rates_total` ... ローソク足の数
* `const datetime &time[]` ... ローソク足が確定した時刻（time[0] が最新のローソク足）
* `const double &open[]` ... ローソク足ごとの始値（open[0] が最新のローソク足）
* `const double &high[]` ... ローソク足ごとの高値（high[0] が最新のローソク足）
* `const double &low[]` ... ローソク足ごとの安値（low[0] が最新のローソク足）
* `const double &close[]` ... ローソク足ごとの終値（close[0] が最新のローソク足）

価格などを示すデータは、配列の形で渡されます。配列のインデックス 0 が最新のローソク足の価格を表しています。ローソク足の本数は `rates_total` で渡されるので、配列のインデックスとしては、`0`（最新の値）〜 `rates_total-1`（一番古い値）の範囲で指定することができます。
例えば以下のような感じです。

* `close[rates_total - 1]` ... チャート上の左端のローソク足の終値
* `close[0]` ... チャート上の右端のローソク足の終値

以下のようにすべてのローソク足の終値を、インジケータ用のバッファにそのまま設定してやることで、終値を結ぶインジケータを表示しています。

{{< code lang="cpp" >}}
for (int i = 0; i < rates_total; ++i) {
    gBuffer[i] = close[i];
}
{{< /code >}}

実は、`OnCalculate()` が呼び出されるたびに `gBuffer[]` のすべての値を再設定する必要はありません。
前回の呼び出しでセットした値は、`gBuffer[]` に保持されているためです。
以降、これを利用した最適化の説明を行います。


カスタムインジケータの OnCalculate 関数を最適化する
-----

カスタムインジケータの計算部分を担う `OnCalculate` は、価格の変化（NewTick イベント）ごとに呼び出されますが、`prev_calculated` パラメータの値をうまく使うことで、すでに計算済みの値を再計算しないでも済むように処理を最適化ことができます。
下記の `OnCalculate()` は、インジケータバッファ (`gBuffer`) に、各ローソク足の終値をセットしています。


{{< code lang="cpp" >}}
// double gBuffer[];  // Buffer for indicator line

/**
 * How many candles should be re-calculated.
 */
int changedBars(int rates_total, int prev_calculated) {
    if (prev_calculated == 0) {
        return rates_total;
    }
    // The latest bar should be updated, so add 1.
    return rates_total - prev_calculated + 1;
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
    // 直近から見て何本のローソク足に対して計算が必要か？
    int changed = changedBars(rates_total, prev_calculated);

    // インジケータの計算（新しく計算した部分だけ更新すれば OK）
    for (int i = 0; i < changed; ++i) {
        gBuffer[i] = close[i];
    }

    // 計算済みローソク足の数を返す
    return rates_total;
}
{{< /code >}}

パラメータで渡される `prev_calculated` の値には、前回の `OnCalculate` 関数の戻り値として返した値が入ってきます。
つまり、`OnCalculate` 関数の戻り値として、いくつのローソク足の計算を終えたか (= `rates_total`) を返しておくことで、次回の `OnCalculate` 関数のパラメータ `prev_calculated` でその値を受け取ることができるということです。

`OnCalculate` 関数が呼び出された時、`gBuffer` 配列には、すでに `prev_calculated` の数だけ計算結果が格納されています。
例えば、現在のローソク足の数が 5 本 (`rates_total=5`) で、前回の計算数が 4 本 (`prev_calculated=4`) である場合、`gBuffer` の構成は下記のようになります。

{{< code >}}
gBuffer[0] ... 計算が必要（最新の価格）
gBuffer[1] ... 計算済み
gBuffer[2] ... 計算済み
gBuffer[3] ... 計算済み
gBuffer[4] ... 計算済み
{{< /code >}}

`gBuffer` の要素が 1 つシフトしていることに注意してください。前回の `OnCalculate()` で計算した `gBuffer[0]`〜`gBuffer[3]` の値は、今回の呼び出し時点では `gBuffer[1]`〜`gBuffer[4]` の位置に保持されています。常にインデックス 0 が最新の要素になるということです。
通常の配列は勝手に値がシフトしていくことはありませんが、`gBuffer` は、`OnInit` 関数の中で `SetIndexBuffer` を使ってデータバッファとして設定したため、このような動作をすることになります。

`rates_total` にはローソク足の総数、`prev_calculated` には計算済みの数が入っているので、新たに計算すべきローソク足の本数は下記のように計算することができます。

{{< code lang="cpp" >}}
// 直近から見て何本のローソク足に対して計算が必要か？
int changed = (prev_calculated == 0) ?
    rates_total : rates_total - prev_calculated + 1;
{{< /code >}}

例えば、新しく計算しなければならない足の本数が 10 本ならば、`changed` が 10 になります。
最初はひとつも計算していない状態 (`prev_calculated == 0`) なので、ローソク足の総数 (`rates_total`) の分すべて計算する必要があります。
2 回目以降の計算では、すでに前回の計算結果が保持されている (`prev_calculated != 0`) なので、その分だけ計算すべきローソク足の数は減ります。
ここで、1 を足しているのは、最新のローソク足の分を常に再計算するためです。
なぜなら、`OnCalculate` 関数はティック（価格変化）ごとに呼び出されるので、多くの場合最新のローソク足の終値が更新されているからです。

