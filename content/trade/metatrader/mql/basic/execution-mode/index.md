---
title: "MetaTrader/MQL: 成行注文の 4 つの注文執行方式 (Request Execution Type) を理解する"
linkTitle: "成行注文の 4 つの注文執行方式 (Request Execution Type) を理解する"
url: "/p/2roz7fo"
date: "2021-01-18"
tags: ["MetaTrader/MQL"]
weight: 202
---

4 つの注文執行方式
----

{{% private %}}
- [Android 版 MT5 - 注文執行の種類](https://www.metatrader5.com/ja/mobile-trading/android/help/trade/general_concept/execution_types)
{{% /private %}}

MT5 から成行注文 (Market Orders) を出すときには、4 種類の注文執行方式（Request Execution Type/Mode とも）が用意されており、ブローカー（FX 会社）によって設定されることとされています。
これが意外とややこしいのでまとめておきます。

| | 執行モード | 説明 |
| ---- | ---- | ---- |
| 1 | <b>Market Execution</b>（カウントダウン方式、マーケット方式） | 最終的なマーケット価格で約定 |
| 2 | <b>Instant Execution</b>（成行方式、ストリーミング方式） | ユーザー指定の価格で約定（許容スリッページ指定あり） |
| 3 | <b>Exchange Execution</b>（エクスチェンジ方式） | ECN ブローカーを通じて FX 市場に直接注文を出す方式 (NDD)。扱い方は Market Execution と同じ。 |
| 4 | <b>Request Execution</b>（リクエスト方式） | ブローカーから先に提示された価格で取引する。主に為替以外で使われる。 |

「成行方式」と「成行注文」という用語の違いに注意してください。
注文執行方式として成行方式を採用しているブローカーに対しては、「成行方式で成行注文を出す」ということになります。
注文執行方式によって、MQL5 プログラム内の `OrderSend` 関数で指定すべきパラメーターが変わってくるので、EA を作成する場合はこれらの違いを把握しておく必要があります（このあたりを理解せずに作られた EA がたくさん出回っています）。

日本の多くの FX 会社は、Market Execution（カウントダウン方式）か Instant Execution（成行方式）を採用しているので、この 2 つの違いを理解しておけば OK です。
簡単に言えば、許容スリッページの指定があるかないかの違いです。
海外の FX 会社はよく Exchange Execution（エクスチェンジ方式）を採用していますが、MQL プログラムなどでの扱い方は Market Execution と同じです。

### 1. Market Execution（カウントダウン方式、マーケット方式）

カウントダウン方式は __注文を約定させることを重視__ する方式で、スリッページが発生したとしても、最終的な市場価格 (Ask/Bid) で約定させます。
必ず市場価格で約定させるので、Market Execution と呼ばれます。
FX 会社からの約定拒否（リクオート）が発生しない代わりに、価格のボラティリティが大きいときには、不利な価格で約定してしまう可能性があります。

最大許容スリッページの概念が存在しないため、MetaTrader のオーダーダイアログにもスリッページの設定項目は表示されません。
MQL5 プログラムの `OrderSend` 関数で成行注文 (`TRADE_ACTION_DEAL`) を出すときも、`MqlTradeRequest.price` フィールドの値が無視されます（設定してもエラーにはならないので、後述の成行方式の場合にも動作するように、プログラム上は常に設定しておくことができます）。

{{< note >}}
古いバージョンの MT5 では、カウントダウン方式による注文時には、利確 (tp: take profit)、損切 (sl: stop loss) の価格を設定できないようになっていました。
現在はカウントダウン方式でも、注文と同時に利確／損切価格の設定を行えるようになっています。
古い MQL5 入門書では、成行注文が約定したあとに、再度 `OrderSend` 関数を呼び出して利確／損切設定 (`TRADE_ACTION_SLTP`) しているものがありますが、そのような実装はしないよう注意してください。
{{< /note >}}

### 2. Instant Execution（成行方式、ストリーミング方式）

成行方式は、__ユーザーが指定した価格を重視__ する方式で、最大許容スリッページを指定することができます。
トレードサーバーに注文を送った後に、市場価格が許容スリッページを超えて変動してしまった場合はリクオート（FX 会社からの約定拒否）されます。
重要な指標発表の前後などは、価格の変動が激しくなるので、許容スリッページの設定が小さすぎると約定しない可能性が高くなります。

### 3. Exchange Execution（エクスチェンジ方式）

ECN (Electronic Communications Network) ブローカーが採用している注文執行方式で、FX 会社のディーリング・デスクを介さずに、直接 FX 市場に注文を出す方式です。
それ以外の特徴は、Market Execution（カウントダウン方式）と同様で、常に市場価格で約定します。
つまり、スリッページの指定はなく、FX 会社都合での約定拒否（リクオート）は発生しません。

このような方式を採用している FX 会社のことを NDD（Non Dealing Desk) と呼び、主に海外の FX 会社が採用しています。
ブローカーが完全に取引を仲介するだけの場合、注文ごとに手数料をとることでブローカーは利益を確保しています。

### 4. Request Execution（リクエスト方式）

事前にブローカーが価格をユーザーに提示し、その価格にユーザーが了承することで約定させるという方式です。
提示された価格は数秒間のみ有効で、その間にユーザーは売買の判断をする必要があります。
主に為替以外の取引のために用意されており、あまり使われることはないようです。
MT5 で初めて追加された注文執行方式です。


現在のブローカーがどの注文執行方式を採用しているか調べる
----

### オーダーダイアログで確認する方法

MT5 上で新規オーダーのダイアログ (New Order) を開いて、タイプ (Type) のプルダウンメニューを見ると、そのブローカーが採用している注文執行方式を把握できることが多いです。

{{< image border="true" w="650" src="img-001.png" >}}

この例では、タイプが __`カウントダウン注文`__ となっているので、Market Execution（カウントダウン方式）であることが分かります。
注意が必要なのは、ここが __`成行注文`__ となっている場合です。
その場合は、それが注文執行方式のひとつである Instant Execution（成行方式）を示しているのか、単純に注文の種類（成行注文 or 待機注文）を示しているのかが区別できません。
以下に示す方法で確認するのが確実です。

### シンボル情報で確認する方法

気配値表示ウィンドウのシンボル名を右クリックして __`仕様`__ を選択すると、その銘柄の注文執行方式を確認できます。

{{< image border="true" w="500" src="img-002.png" >}}

この例では、執行 (Execution) が __`マーケット (Market)`__ となっているので、Market Execution（カウントダウン方式）であることが分かります。

### MQL5 プログラムで確認する方法

MQL プログラムの中で注文執行方式を調べるには、`SymbolInfoInteger` 関数を使用します。

{{< code lang="cpp" >}}
ENUM_SYMBOL_TRADE_EXECUTION mode = (ENUM_SYMBOL_TRADE_EXECUTION)
    SymbolInfoInteger(Symbol(), SYMBOL_TRADE_EXEMODE);
{{< /code >}}

__`ENUM_SYMBOL_TRADE_EXECUTION`__ 列挙型には次のような値が定義されています。

- `SYMBOL_TRADE_EXECUTION_MARKET` ... Market Execution（カウントダウン方式、マーケット方式）
- `SYMBOL_TRADE_EXECUTION_INSTANT` ... Instant Execution（成行方式、ストリーミング方式）
- `SYMBOL_TRADE_EXECUTION_EXCHANGE` ... Exchange Execution（エクスチェンジ方式）
- `SYMBOL_TRADE_EXECUTION_REQUEST` ... Request Execution（リクエスト方式）

この結果を見て、Instant Execution だったらスリッページを設定する、といった分岐処理が可能です。

