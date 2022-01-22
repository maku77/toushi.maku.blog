---
title: "EasyLanguage で入力変数の表示名を設定する (DisplayName)"
linkTitle: "入力変数の表示名を設定する (DisplayName)"
url: "/p/req3doz"
date: "2020-04-12"
tags: ["EasyLanguage"]
---

EasyLanguage で作成するインジケーターでは、使用者が値を変更可能な入力変数を定義することができます。
インジケーターの設定ダイアログでは、デフォルトでは入力変数の名前がそのまま表示されるのですが、次のように __`DisplayName`__ を指定することで、任意の表示名に変更することができます。

{{< code >}}
inputs:
    Price(Close) [DisplayName = "プロットする価格"];
{{< /code >}}

インジケーターの設定ダイアログで、次のように表示名が変わっていることを確認できます。

{{< image border="true" src="img-001.png" >}}

