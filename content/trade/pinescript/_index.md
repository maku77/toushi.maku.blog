---
title: "Pine Script (TradingView)"
url: "p/offioix/"
date: "2024-01-20"
draft: true
---

ローソク足に重ねてプロットする
----

```cpp
//@version=5
indicator("My Indicator", overlay=true)
plot(close)
```


RSI のプロット（例）
----

```cpp
//@version=5
indicator(title="Plotting RSI", overlay=false)
myRsi = ta.rsi(close, 7)
plot(myRsi)
```

PineScript 5 のテクニカル分析 (technical analysis) 用のインジケーター関数は、__`ta`__ 名前空間の下に格納されています。


色 (color) の定義方法まとめ
----

1. 定数（名前）
   - `color.aqua`
   - `color.fuchsia`
   - `color.gray`
   - `color.lime`
   - `color.maroon`
   - `color.navy`
   - `color.olive`
   - `color.orange`
   - `color.purple`
   - `color.silver`
   - `color.teal`
1. 16 進数リテラル
   - `#33ffcc`
1. `color.rgb(r, g, b, transp)`
   - `r` ... 0 〜 255
   - `g` ... 0 〜 255
   - `b` ... 0 〜 255
   - `trans` ... 0:不透過 〜 100:透過
1. その他
   - `color.new(#ff3366, 50)`
   - `color.new(color.blue, 75)`


プロット (plot) 関数の引数
----

- `linewidth` ... 1 (default) 〜 4 の範囲の整数
- `color` ... 線の色
- `style` ... 線のスタイル
  - `plot.style_line`
  - `plot.style_stepline`
  - `plot.style_histogram`
  - `plot.style_cross`
  - `plot.style_area`
  - `plot.style_columns`
  - `plot.style_circles`
- `offset`
  - -1 ... 左へ 1 バー分シフト
  - 1 ... 右へ 1 バー分シフト


fill 関数で 2 つの線で囲まれた部分に色を付ける
----

```cpp
//@version=5
indicator("Example of fill", overlay=true)
sma7 = ta.sma(close, 7)
sma14 = ta.sma(close, 14)
plot1 = plot(sma7)   // plot() 関数の戻り値を保存しておくのがポイント
plot2 = plot(sma14)
fill(plot1, plot2, color=color.new(color.blue, 50))
```


バーの上下にアイコンを表示する
----

```cpp
plotshape(true/false, color, style, location(above/below))
```

{{< code lang="cpp" title="使用例" >}}
plotshape(isCrossed, color=color.blue, style=shape.circle, location=location.abovebar)
{{< /code >}}
🏴
`style` にはどのようなアイコンを表示するかを指定します。

- `shape.cross`
- `shape.circle`
- `shape.triangleup` / `shape.triangledown`
- `shape.flag`
- `shape.arrowup` / `shape.arrowdown`
- `shape.square`
- `shape.diamond`
- `shape.labelup` / `shape.labeldown`

文字を表示したいときは、`plotshape()` の代わりに __`plotchar()`__ 関数を使います。


構文（ループ）
----

```cpp
sum = 0.0
for i = 0 to 6 (step 1)
  sum := sum + close[i]
sma7 = sum / 7
```

