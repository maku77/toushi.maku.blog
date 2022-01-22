---
title: "MetaTrader/MQL: 組み込み関数の実行に失敗したときにエラー情報を表示する (GetLastError, ErrorDescription)"
linkTitle: "組み込み関数の実行に失敗したときにエラー情報を表示する (GetLastError, ErrorDescription)"
url: "/p/av9kv7g"
date: "2016-03-20"
tags: ["MetaTrader/MQL"]
---

MQL の組み込み関数の実行に失敗した時には、`GetLastError` 関数によってそのエラーコードを取得できます。
このエラーコードは int 型の数値のため、その内容をテキストで取得したい場合は次のように変換する必要があります。


MT4 の場合
----

`GetLastError` 関数で取得したエラーコードを `ErrorDescription` に渡すことで、テキスト形式でエラー内容を取得することができます。
これらの関数を使用するには、`stdlib.mqh` をインクルードしておく必要があります。

下記は、`ObjectCreate` の実行に失敗した時のエラー表示の例です。

{{< code lang="cpp" title="MQL4" >}}
// #include <stdlib.mqh>

if (!ObjectCreate(0 , name, OBJ_LABEL, subWindow, 0, 0)) {
    Alert("Failed to create a label: ", ErrorDescription(GetLastError()));
    return;
}
{{< /code >}}

{{< code title="表示例" >}}
Failed to create a label: object already exists
{{< /code >}}


MT5 の場合
----

MT5 の場合は、なんと `ErrorDescription` 関数が提供されてません（なんでやねん）。
正確には、MT4 で用意されていた `stdlib.mqh` が提供されていません。
代わりに、下記のサイトで、MetaQuotes 社からライブラリとして `ErrorDescription.mqh` ファイルが提供されています。
自分でダウンロードして使えということですね（なんでやねん）。

- [ErrorDescription - library for MetaTrader 5](https://www.mql5.com/en/code/79)

これをダウンロードして `MQL5/Inlude` ディレクトリにコピーすれば、

{{< code lang="cpp" title="MQL5" >}}
#include <ErrorDescription.mqh>
{{< /code >}}

とインクルードして、MT4 と同様に `ErrorDescription` 関数が使えるようになります。
自力で `int` → `string` 変換する関数を定義しているだけなのであたり前ですけど。

こういうユーティリティ系の関数は、自分用のユーティリティ関数をまとめたファイル（例えば `Util.mqh` など）で定義しておくと、細かいファイルをたくさんインクルードしなくて済むのでスッキリします。
下記の例では、ユーティリティ系のクラスを `Util` ネームスペース内にまとめて定義しています。

- 参考: [MQL5/Include/maku77/Util.mqh](https://github.com/maku77/metatrader/blob/main/MQL5/Include/maku77/Util.mqh)

{{< code lang="cpp" title="使用例" >}}
// #include <maku77/Util.mqh>

if (!ObjectCreate(0 , name, OBJ_LABEL, subWindow, 0, 0)) {
    Alert(Util::ErrorDescWithCode());
    return;
}
{{< /code >}}

