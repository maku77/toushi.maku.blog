---
title: "MetaTrader/MQL: #property strict で安全な EA を作る"
linkTitle: "#property strict で安全な EA を作る"
url: "p/6riotap/"
date: "2015-06-09"
tags: ["MetaTrader/MQL"]
---

MetaTrader Build 765 以降では、EA やインジケーターの実装内で __`#property strict`__ を指定しておくと、`OnInit` による初期化時に `INIT_SUCCEEDED (0)` 以外が返されたときに、チャートから自動的に EA やインジケーターを取り除いてくれます。

- `#property strict` ありで `OnInit` 処理が失敗 → EA がチャートから取り除かれる
- `#property strict` なしで `OnInit` 処理が失敗 → EA はチャートに関連付けられたまま

特に理由がない限り、コードの先頭で `#property strict` を指定しておくことをおすすめします。

