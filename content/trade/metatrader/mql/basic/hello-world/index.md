---
title: "MQL で Hello World"
url: "/p/ay9a762"
date: "2020-10-27"
tags: ["MetaTrader/MQL"]
weight: 2
---

ここでは、MetaTrader の MetaEditor を使って、次のように `Hello World` と表示するだけの Script を作成してみます。

{{< image src="img-002.png" border="true" >}}

MetaEditor の起動
----

MQL でコーディングを行うためには、MetaTrader に付属している MetaEditor を使用します。MetaTrader の画面で下記のいずれかの方法で MetaEditor を起動します。

- __`F4`__ キーを押す
- ツールバー上の `Editor アイコン` をクリックする
- メニューから `ツール` → `MetaQuotes Language Editor` を選択する


Script ファイルの新規作成
----

MetaEditor が起動したら、下記のようにして新規コードを作成します。
最初に作成するファイルの種類を選ぶのですが、ここでは一番単純な「Script」を選択します。

1. __`Ctrl + N`__ で新規作成ウィザード (MQL Wizard) を開く
2. `Script` を選択
3. プロパティとして次のような感じで入力
    - 名前: `Scripts\Hello`
    - 著作者: （空欄）
    - リンク: （空欄）

すると、`Hello.mq4` というファイル（MQL5 の場合は `Hello.mq5`）というファイルが生成され、エディタが開きます。

{{< note >}}
ここではファイルの種類として Script を選択しましたが、新規作成ウィザードから選択できるもののうち、下記のものが __実行可能__ になるプログラムです。

* `エキスパートアドバイザー (Expert Advisor)` ... 自動売買用のプログラム（EAと呼ばれる）
* `カスタム指標 (Custom Indicator)` ... 独自のインジケータを表示するためのプログラム
* `スクリプト (Script)` ... 一度だけ実行するプログラム

それ以外の Library などのファイルは、他のプログラムから共有して使用する関数群などを定義するためのファイルを作成したい時に使用します。
{{< /note >}}


ソースコードの入力
----

MetaEditor 上で開いた `Hello.mq4` ファイルに、次のように入力します。

{{< code lang="cpp" title="Hello.mq4 (Hello.mq5)" >}}
void OnStart() {
    MessageBox("Hello World", "Sample");
}
{{< /code >}}

Script のエントリポイントは、Start イベントをハンドルする、`OnStart()` という関数です。
この中に、メッセージボックスで `Hello World` と表示するコードを記述しています。


ソースコードのコンパイルと実行
----

MQL4/MQL5 のソースコードの拡張子は、それぞれ `mq4` と `mq5` ですが、このソースコードのままでは実行はできません。
C/C++ と同様に、実行する前にはコンパイルする必要があり、__`ex4`__、__`ex5`__ という拡張子の実行ファイルを作成する必要があります。

MetaEditor 上で作成しているコードをコンパイルするには、__`F7`__ キーを押します。

コンパイルに成功すると、MetaTrader のメイン画面の方の「ナビゲーター」ウィンドウに `Hello` スクリプトのアイコンが表示されます。
MetaTrader のメイン画面には、`F4` キーで切り替えられます。

{{< image src="img-001.png" border="true" >}}

`Hello` スクリプトのアイコンをダブルクリックするとスクリプトを実行できます。
次のようなメッセージボックスが表示されれば成功です。

{{< image src="img-002.png" border="true" >}}

スクリプトは特定のチャートに関連付けて実行することができるため、スクリプトアイコンを、チャート上にドラッグ＆ドロップすることでもスクリプトを起動できます。

