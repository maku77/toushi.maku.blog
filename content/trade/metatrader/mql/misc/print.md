---
title: "MetaTrader/MQL: テキストを出力する方法まとめ (Alert, Comment, Print, MessageBox)"
linkTitle: "テキストを出力する方法まとめ (Alert, Comment, Print, MessageBox)"
url: "p/q37kiwa/"
date: "2023-06-18"
tags: ["MetaTrader/MQL"]
---

Alert/Comment/Print 関数
----

プログラムのテストや、ユーザへの通知のために画面上にテキストを表示したい場合は、下記の関数を使用できます。

* [Alert 関数](http://www.mql5.com/en/docs/common/alert) ... アラートボックスでテキスト表示する（Strategy Tester での実行時は無視されます）
* [Comment 関数](https://www.mql5.com/en/docs/common/comment) -- チャートの左上にテキスト表示する
* [Print 関数](https://www.mql5.com/en/docs/common/print) -- Terminal ビュー (Ctrl+T) の Expert タブ内にテキスト表示する

メソッドごとに出力先は異なりますが、どのメソッドも渡されたパラメータの型によって適切な形式でテキスト表示してくれます。

```cpp
string s = "Hello";
bool b = true;
int i = 100;
float f = 0.123456789f;
double d = 0.123456789;
datetime dt = TimeLocal();
color cl = C'0xFF,0xC0,0x80';

Alert(s);  //=> Hello
Alert(b);  //=> true
Alert(i);  //=> 100
Alert(f);  //=> 0.12346
Alert(d);  //=> 0.123456789
Alert(dt); //=> 2014.12.19 23:59:59
Alert(cl); //=> 255,192,128
```

パラメータは複数渡すことができ、それぞれが連結されて表示されます。

```cpp
Print("value = ", value);  //=> "value = 100"
```

出力時に改行を入れたい場合は、文字列中に改行コード (`\n`) を含めれば OK です。

```cpp
Comment("AAA\nBBB\nCCC");
```


メッセージボックスを表示する
----

[MessageBox](https://www.mql5.com/en/docs/common/messagebox) 関数を使用すると、Yes/Cancel ボタンなどを表示し、ユーザの意思を確かめることができます。

{{< code lang="cpp" title="確認ダイアログ (OK or Cancel) を表示する" >}}
int ret = MessageBox("Are you sure?", "", MB_OKCANCEL | MB_ICONQUESTION);
if (ret == IDOK) {
    // OK button was pressed
}
{{< /code >}}


Comment 関数を使いやすくする
----

チャートの左上にテキスト表示する `Comment` 関数は、続けて呼び出すと、最後に指定したテキストで内容が上書きされてしまいます。
次のような関数を用意しておけば、過去に出力したメッセージを残しながら追加出力していくことができます。

```cpp
void Debug(string msg) {
    static string lines = "";
    lines = msg + "\n" + lines;
    Comment(lines);
}
```

{{< code lang="cpp" title="使用例" >}}
void OnStart() {
    Debug("AAA");
    Debug("BBB");
    Debug("CCC");
}
{{< /code >}}

上記の `Debug` 関数は、呼び出すごとにどんどんメッセージの行数が増えていってしまいますが、出力を最大 10 行に抑えたい場合などは、例えば以下のようにします。

```cpp
#include <Arrays\ArrayString.mqh>

void Debug(string msg) {
    static const int MAX_LINES = 10;
    static CArrayString lines;
    int len = lines.Total();
    if (len > MAX_LINES - 1) {
        lines.Delete(0);
        --len;
    }
    lines.Add(msg);
    string text = "";
    for (int i = len; i >= 0; --i) {
        text += lines.At(i) + "\n";
    }
    Comment(text);
}
```

