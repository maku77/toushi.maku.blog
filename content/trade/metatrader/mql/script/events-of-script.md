---
title: "MetaTrader/MQL: スクリプトで使用できるイベント"
linkTitle: "スクリプトで使用できるイベント"
url: "p/fvh3d6r/"
date: "2023-07-16"
tags: ["MetaTrader/MQL"]
---

MetaTrader のスクリプトでハンドル可能なイベントは、__Start__ イベントのみです。

OnStart 関数
----

```cpp
int OnStart(void);
```

スクリプトの [OnStart()](https://www.mql5.com/en/docs/event_handlers/onstart) 関数は、__Start__ イベントが発生したときに呼び出されます。
戻り値が `void` のバージョンもありますが、互換性のために残されているだけなので、`int` を返すバージョンを使ってください。

スクリプトは、チャートにアタッチした瞬間にロードされ、実行されます。
そして、その処理が完了され次第、自動的にアンロードされます。

{{% note title="インジケーターでは OnInit() や OnDeinit() は使えない" %}}
カスタムインジケーターや EA では、`OnInit()` や `OnDeinit()` が呼び出されるようになっていますが、スクリプトではこれらの関数は呼び出されません。
これらのイベントハンドラーは、チャートの内容（シンボルや時間足）が変更されたときのために用意されています。
それが必要なのは、カスタムインジケーターや EA のみです。
スクリプトには `OnStart()` だけあれば十分なのです。
{{% /note %}}

{{% reference %}}
- [アプリの種類ごとに扱えるイベントハンドラーの一覧](/p/um6bbep/)
- [カスタムインジケーターで使用できるイベント](/p/ugs5fq2/)
- [EA で使用できるイベント](/p/aamwkiu/)
{{% /reference %}}
