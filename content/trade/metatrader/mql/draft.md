---
title: "（ドラフト）MQL 未整理・雑多メモ"
url: "/p/bs5bejb"
date: "2021-06-14"
tags: ["MetaTrader/MQL"]
draft: true
---

現在の背景色に隠れない色を作る (XOR な色)
----

{{< code >}}
color colorLabel = (color) (ChartGetInteger(0, CHART_COLOR_BACKGROUND) ^ 0xFFFFFF);

// さらにこれも使える？
color colorInfo = (color) (colorLabel & 0x202020);
{{< /code >}}


疑問
----

- `OnTick` の中で `Sleep()` したら、その間は `OnTick` が呼ばれなくなる？


static な Engine クラスを作って全体のライフサイクルを制御したらどうか？
----

{{< code lang="cpp" >}}
OnInit() {
    Engine.OnInit();
}

OnCalculate(...) {
    Engine.OnCalculate(...);
}
{{< /code >}}

みたな共通アプリクラス作っておいて、他のクラスのインスタンスは、この `Engine` に `addCallback` して、自律的に動作するようにする。

