---
title: "MetaTrader/MQL: インジケーターの実装例 - アカウント（口座）情報を表示する"
linkTitle: "インジケーターの実装例 - アカウント（口座）情報を表示する"
url: "p/tsig7ew/"
date: "2016-03-26"
tags: ["MetaTrader/MQL"]
weight: 900
---

{{< image border="true" src="img-001.png" title="AccountInfo インジケーター" >}}

下記の AccountInfo インジケータを使用すると、チャート上に口座情報（証拠金情報）を表示することができます。

- [Indicators/maku/AccountInfo.mq5](https://github.com/maku77/metatrader/blob/main/MQL5/Indicators/maku77/AccountInfo.mq5)

それぞれの表示は下記のような意味を持っています。

- `Balance`: 証拠金残高
- `Profit`: 損益
- `Equity`: 純資産（証拠金残高 - 損益）
- `Margin level`: 証拠金維持率
- `Margin`: 必要証拠金
- `Free margin`: 有効証拠金

こういった口座情報は、`AccountInfo*` 系の API で取得することができます。
詳しくは下記を参照してください。

- [MetaTrader/MQL: アカウント情報（口座情報）を取得する (AccountInfo*) (MT5)](/p/nb7h9vg/)

