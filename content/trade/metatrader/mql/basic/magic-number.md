---
title: "MetaTrader/MQL: EA のマジックナンバーについて理解する"
linkTitle: "EA のマジックナンバーについて理解する"
url: "/p/p6fgxgf"
date: "2020-12-27"
tags: ["MetaTrader/MQL"]
weight: 204
---

マジックナンバー・ジェネレーター
----

<form style="color:white; background:#c50; padding:1rem; text-align:center;">
  <div id="result" style="border-radius:1rem; letter-spacing:0.1em; text-align: left; background:#fff0e0; color:#c50; font-size: 1.5rem; font-weight: bolder; margin: 1rem 1rem 0 1rem; padding: 0.7em;"></div>
  <button onclick="generate(); return false;" style="margin-top:1rem; font-size:1.5em;">再生成</button>
</form>

<script>
function generate() {
  const RAND_START = 10000
  const RAND_END = 90000
  const SHIFT = 1000
  const rand = Math.floor(Math.random() * RAND_END) + RAND_START;
  const code = 'input ulong Magic = ' + (rand * SHIFT) + ';';
  document.getElementById('result').innerText = code;
}
window.onload = generate();
</script>

EA 用のマジックナンバーとして、ランダムな 8 桁の整数値を生成するツールです。
生成されたコードを `.mq5` コード内にコピペして使ってください。
変数 `Magic` の値は、`MqlTradeRequest` 構造体の `magic` フィールドなどにセットして使用します。


マジックナンバーとは
----

MT4/5 の EA（エキスパートアドバイザ）から何らかの注文を出す場合、マジックナンバーと呼ばれる整数値を設定する必要があります。
これは、[OrderSend 関数](https://www.mql5.com/ja/docs/trading/ordersend) で注文を出す場合も、[CTrade クラス](https://www.mql5.com/ja/docs/standardlibrary/tradeclasses/ctrade) で注文を出す場合も同様です。
具体的には次のようにマジックナンバーを指定します。

- MT5 の OrderSend 関数の場合 ... `MqlTradeRequest` オブジェクト の `magic` フィールド（uint 値）
- MT5 の CTrade クラスの場合 ... `SetExpertMagicNumber` メソッド（uint 値）
- MT4 の OrderSend 関数の場合 ... `magic` パラメータ（int 値）

このマジックナンバーは、__どの EA から出された注文かを識別するため__ のものであり、1 つの口座内で複数の EA を動かすときは、それぞれ異なる値を割り当てておく必要があります。
マジックナンバーが重複してしまうと、別の EA から注文を修正されてしまうといった誤動作の原因になります。
マジックナンバーを設定しなくても注文用の API は呼び出せてしまいますが、このときはデフォルト値として 0 が使われます。
__0 というマジックナンバーは手動でのエントリーを示す__ ものであり、EA のコードでは何らかの一意なマジックナンバーを指定しておく必要があります。

マジックナンバーは取引リストの画面では、「エキスパート ID」と表示されたりします。
正確には、マジックナンバーは EA ごとの ID というよりは、複数の取引をまとめて管理するための識別子です。
なので、1 つの EA の中で複数のマジックナンバーを扱うこともできます。
例えば、次のような EA で注文の種類ごとにマジックナンバーを割り当てたりします。

- 複数の時間足で同時に注文を出す EA
- 複数のアルゴリズムで同時に注文を出す EA

注文の種類ごとにマジックナンバーを割り当てることにより、アルゴリズム別に損益合計を求めたり、注文をまとめて決済したりできます。
とはいっても、シンプルな EA であれば、マジックナンバーは 1 つだけで十分です。


マジックナンバーの定義方法
----

マジックナンバーは、MT4 では int 型整数（最大値は `2147483647`）、MT5 では uint 型整数（最大値はすごく大きな値）で設定します。
互換性を考えると 9 桁以下にしておくのが無難ですが、口座内で一意な値であればよいので、それほど大きな値を設定する必要はありません（5 桁とかでも十分）。

EA のコード内にマジックナンバーをハードコードしてしまうと、別の EA のものと重複した場合に困るので、マジックナンバーは外部パラメータとして値を変更できるようにしておくことをオススメします。

次の例では、マジックナンバーのデフォルト値を `71952000` に設定しつつ、ユーザーが自由に設定する余地を残しています。

{{< code lang="cpp" title="Experts/SampleEA.mq5（EA の例）" >}}
#include <Trade/Trade.mqh>

input double Lot = 0.1;        // 取引するロット数（ボリューム）
input ulong Slippage = 3;      // 許容スリッページポイント
input ulong Magic = 71952000;  // EAマジックナンバー

CTrade trade;

int OnInit() {
    trade.SetDeviationInPoints(Slippage);
    trade.SetExpertMagicNumber(Magic);

    return INIT_SUCCEEDED;
}

void OnTick() {
    // ...
    // if (!trade.Buy(Lot)) { ... }
    // ...
}
{{< /code >}}

