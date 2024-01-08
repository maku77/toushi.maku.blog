---
title: "（ドラフト）MQL 未整理・雑多メモ"
url: "/p/bs5bejb"
date: "2021-06-14"
tags: ["MetaTrader/MQL"]
draft: true
weight: 1
---

コーディングスタイルを考える
----

- エンコーディング形式: UTF-8
- インデント: スペース 4 文字
- 命名規則（大文字・小文字）
  - メンバー変数: `m_camelCase`
  - グローバル変数: `g_camelCase`
  - 定数: `UPPER_CASE`
  - クラス名: `CamelCase`
  - public/protected メソッド: `CamelCase`
  - private メソッド: `camelCase`
  - 長いパラメーターの改行位置（Kotlin のスタイルを参考に）
  - インプット変数: `i_camelCase`（行末コメントで表示するテキストを定義する）


iHogeHoge 形式の指標関数を使う
----

```cpp
int handle = iATR(NULL, PERIOD_CURRENT, 20);
```

- 関連関数
  - iCustom
  - IndicatorCreate() // テクニカル指標の作成
    - 銘柄名
    - 時間軸
    - 種類
    - 入力パラメーターの数
    - 入力パラメーターの `MqlParam` 配列
  - IndicatorRelease()
- `iHogeHoge` 形式の関数はグローバルキャッシュにテクニカル指標の計算結果を格納し、その指標ハンドルを返す？
- 指標値の計算には時間がかかるので、`OnInit()` などでハンドルを取得するのが望ましい。
- 全ての指標関数は少なくともシンボル名（`NULL` なら現在のシンボル）と、時間軸（`0` なら現在の時間軸）の 2 つのパラメーターを持っている。


CExpert クラス
----

```cpp
#include <Expert\Expert.mqh>
```

- Expert Advisor が認識するポジションは、シンボル (`m_symbol`) とマジック (`m_magic`) のペア情報により識別される。
- マジックナンバーをセットしておかないと、手動で入れた取引と区別できなくなってしまうので注意が必要。


クラスライブラリ
----

- `CObject` (`Object.mqh`) ... MQL5 クラスライブラリのベースクラス
  - `CWnd` (`Controls/Wnd.mqh`) ... 全コントールの共通クラス。サイズの制御やイベントハンドリングなどが含まれます。
  - `CWndContainer` (`Controls/WndContainer.mqh`) ... `CWnd` のコンテナ
    - `CDialog` (`Controls/Dialog.mqh`) ... キャプション付きのダイアログ
      - `CAppDialog` (`Controls/Dialog.mqh`)
  - `CWndObj` (`Controls/WndObj.mqh`)
    - `CPanel` (`Controls/Panel.mqh`)


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

