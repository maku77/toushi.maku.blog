---
title: "MetaTrader/MQL: 注文時のフィル・ポリシー（充填ポリシー）の指定について"
linkTitle: "注文時のフィル・ポリシー（充填ポリシー）の指定について"
url: "/p/9jjrrp5"
date: "2021-01-26"
tags: ["MetaTrader/MQL"]
---

フィル・ポリシーとは
----

`OrderSend` 関数 (MT5) で売買注文を出すとき、[MqlTradeRequest 構造体](https://www.mql5.com/en/docs/constants/structures/mqltraderequest)（[日本語](https://www.mql5.com/ja/docs/constants/structures/mqltraderequest)）の __`type_filling`__ フィールドにフィル・ポリシー（充填ポリシー？）を設定してやる必要があります。
フィル・ポリシーは、__注文時に指定したボリューム（ロット数）が一度に約定できない場合に、その注文をどのように扱うのか__ （部分的にでも約定させるのかなど）を表します。

この `type_filling` フィールドを適当に設定していると、`OrderSend` 関数が次のようなエラーコード返して失敗することがあります。

{{< code >}}
result.retcode: 10030
result.comment: Unsupported filling mode
{{< /code >}}

ようするに、ブローカー（FX 会社）側のトレードサーバーが、「そのフィル・ポリシーは受け付けないよ」と言っているんですね（理由はきっと大人の事情、あるいはブローカーの手抜き）。
フィル・ポリシーには、[ENUM_ORDER_TYPE_FILLING 列挙型](https://www.mql5.com/en/docs/constants/tradingconstants/orderproperties#enum_order_type_filling) で定義されている次のいずれかの値を指定することができます。

`ORDER_FILLING_FOK (0)`
: Fill or Kill. 注文時に指定したボリューム（ロット数）で全て約定できないときは、その注文をキャンセルします。

`ORDER_FILLING_IOC (1)`
: Immediate or Cancel. 指定したボリュームのうちすぐに約定できる部分だけ約定させ、残りをキャンセルします。システムによっては Fill or Cancel と呼ばれていたりします。

`ORDER_FILLING_RETURN (2)`
: Return. 指定したボリュームのうちすぐに約定できる部分だけを約定させ、残りも市場価格でさらに約定させるようにトレードサーバー側ががんばります。MT 用語としては、ひとつの「注文 (order)」で、複数の「約定 (deal)」が発生し、最終的にひとつの「ポジション (position)」になる、と表現されます。最新の市場価格で次々と約定させていく必要があるため、このポリシーはブローカーの注文執行方式が Market execution あるいは Exchange execution であるときのみ有効です。このポリシーは以下の注文タイプ（`type` 引数）で注文を出すときに有効です。
    - `ORDER_TYPE_BUY` / `ORDER_TYPE_SELL` ... 成行注文
    - `ORDER_TYPE_BUY_LIMIT` / `ORDER_TYPE_SELL_LIMIT` ... 指値注文
    - `ORDER_TYPE_BUY_STOP_LIMIT` / `ORDER_TYPE_SELL_STOP_LIMIT` ... ストップ・リミット注文（トリガー後に指値注文に置き換えられるので、そのときに `ORDER_FILLING_RETURN` のポリシーがセットされます）


フィル・ポリシーは自由には指定できない
----

MQL5 のドキュメントサイトには、以下のような [記載](https://www.mql5.com/en/docs/constants/environment_state/marketinfoconstants#symbol_filling_mode)（[日本語](https://www.mql5.com/ja/docs/constants/environment_state/marketinfoconstants#symbol_filling_mode)）があります。

> （英語）
> In the Request and Instant execution modes the Fill or Kill policy is always used for market orders, and the Return policy is always used for limit orders. In this case, when sending orders using OrderSend or OrderSendAsync, there is no need to specify a fill policy for them.
> In the Market and Exchange execution modes the Return policy is always allowed for all the order types. To find out whether the other policies are allowed, use the SYMBOL_FILLING_FOK and SYMBOL_FILLING_IOC properties.
>
> （日本語）
> Request 及び Instant 実行モードでは成行注文では常に「フィル・オア・キル」が常に使用され、リミット注文では常に「リターン」ポリシーが使用されます。この場合、OrderSend または OrderSendAsync を使用して注文を送信する時、充填ポリシーを指定する必要はありません。
> 「マーケット」と「エクスチェンジ」実行モードでは、「リターン」ポリシーは常に全種類の注文に許可されています。他のポリシーが許可されているかどうかを調べるには、SYMBOL_FILLING_FOK とSYMBOL_FILLING_IOC プロパティを使用します。

これを読む限り、次のような仕様であるかのように見えます。

<table>
  <thead>
    <tr>
      <th></th>
      <th>Instant/Request Execution<br>（price 指定可）</th>
      <th>Market/Exchange Execution<br>（price 指定不可）</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>成行注文</th>
      <td>常に <b>FOK</b> ポリシーとして扱われる</td>
      <td rowspan="2"><b>FOK</b> / <b>IOC</b> ポリシーを選択できるかは<br>
      ブローカーと取引対象のシンボルによるが、<br>
      <b>RETURN</b> ポリシーは常に選択可能</td>
    </tr>
    <tr>
      <th>待機注文</th>
      <td>常に <b>RETURN</b> ポリシーとして扱われる</td>
    </tr>
  </tbody>
</table>

例えば、注文執行方式として Market Execution を採用している OANDA Japan の MT5 では、成行注文時には必ず __`ORDER_FILLING_RETURN`__ ポリシーが指定可能ということですね。
EA の実装では、シグナルが発生したタイミングで、指定したロット数を全部約定させてしまいたいので、RETURN ポリシーが必ず指定できるというのは都合がよさそうです。

ところがどっこい（古い）、実際に RETURN ポリシーを指定して成行の買い注文を出そうとしたら、思いっきり 10030: Unsupported filling mode のエラーが返ってきました。
どうも、OANDA Japan での成行注文時には IOC ポリシーしか指定できないようです（2021年1月）。
OANDA Japan が仕様を無視しているのか、ドキュメントの記載が間違っているのか、わたしの理解が間違っているのか。。。

いずれにしても、作成したプログラムをうまいこと動作させるためには、ブローカーが受け入れてくれるフィル・ポリシーを調べて、それに応じて処理を変えるしかなさそうです。


結局、フィル・ポリシーはどう指定すればいいか？
----

上記で説明した通り、`MqlTradeRequest` オブジェクトの `type_filling` フィールドには、ブローカーが受け入れてくれるフィル・ポリシーの範囲内で値を指定する必要があります。
注文対象のシンボルが、どのフィル・ポリシーに対応しているかは、次のように __`SymbolInfoInteger(SYMBOL_FILLING_MODE)`__ を使って調べることができます。

{{< code lang="cpp" >}}
long modes = SymbolInfoInteger(Symbol(), SYMBOL_FILLING_MODE);
if ((modes & SYMBOL_FILLING_FOK) != 0) {
    Print("FOK ポリシーに対応しています");
}
if ((modes & SYMBOL_FILLING_IOC) != 0) {
    Print("IOC ポリシーに対応しています");
}

// 成行注文時には RETURN ポリシーは無条件で指定可能とされているため、
// RETURN ポリシーに対応しているかを調べるビットフラグは用意されていないようです。
Print("RETURN ポリシーに対応しています（嘘かも）");
{{< /code >}}

しかし、何ということでしょう。
上記のようにしても、ブローカーが RETURN ポリシーを受け入れてくれるかどうかは判断できません（FOK、IOC の対応状況は判断できる）。
仕様上、成行注文では RETURN ポリシーは常に選択可能とされているため、RETURN ポリシーの有効性を調べられる API になっていないようです。
なので、現実的な選択肢としては、

* IOC → FOK → RETURN の優先度で使えそうなポリシーを選択する
* FOK → IOC → RETURN の優先度で使えそうなポリシーを選択する

という二択しかなさそうです。
もちろん、スクリプトや EA の入力変数でフィル・ポリシーを選択させるという手はありますが、そこをマニュアル指定にするのは煩わしいので、できるだけフィル・ポリシーの選択は自動化したいところです。

下記のユーティリティ関数 `SelectFillPolicy` は、指定したシンボル（銘柄）で選択可能なフィル・ポリシーをひとつ返します。

{{< code lang="cpp" title="Scripts/maku77/Util.mqh" >}}
namespace Util {
    /**
     * 指定したシンボルで選択可能なフィル・ポリシーをひとつ返します。
     * 優先度は IOC、FOK、RETURN の順です。
     */
    ENUM_ORDER_TYPE_FILLING SelectFillPolicy(string symbol) {
        long modes = SymbolInfoInteger(symbol, SYMBOL_FILLING_MODE);
        if ((modes & SYMBOL_FILLING_IOC) != 0) return ORDER_FILLING_IOC;
        if ((modes & SYMBOL_FILLING_FOK) != 0) return ORDER_FILLING_FOK;
        return ORDER_FILLING_RETURN;
    }
}
{{< /code >}}

あとは、`MqlTradeRequest` オブジェクトの `type_filling` フィールドの値を次のように設定してやります。

{{< code lang="cpp" >}}
MqlTradeRequest request = {0};
request.type_filling = Util::SelectFillPolicy(Symbol());
{{< /code >}}

これで少なくとも、`OrderSend` 関数を呼び出したときのエラーコード 10030 (Unsupported filling mode) は発生しなくなるはずです。

