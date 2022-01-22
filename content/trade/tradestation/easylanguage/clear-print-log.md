---
title: "EasyLanguage: 印刷ログの内容をクリアする (ClearPrintLog)"
linkTitle: "印刷ログの内容をクリアする (ClearPrintLog)"
url: "/p/znydp2d"
date: "2020-04-13"
tags: ["EasyLanguage"]
---

`Print` 関数を使って「印刷ログ」ウィンドウにログを出力してデバッグしていると、どんどんログ出力が溜まっていくので、最後に適用したインジケーターの出力がどの行から始まっているかが分かりにくくなります。

そのような場合は、EasyLanguage のコード内から __`ClearPrintLog`__ を呼び出すことで、「印刷ログ」の内容を自動でクリアすることができます（他の分析テクニックが出力した内容もクリアされてしまうことに注意してください）。

{{< code >}}
// インジケーター適用時にログをクリア
once ClearPrintLog;

// バー番号と終値をログ出力
Print(CurrentBar:4:0, ": Close = ", Close:0:0);
{{< /code >}}

`ClearPrintLog` をそのまま実行してしまうと、各足の処理で毎回ログをクリアすることになってしまうので、__`once`__ を使って、インジケーターを適用したときに一度だけ実行するようにします。

