---
title: "MetaTrader/MQL: 描画オブジェクトの基本 (ObjectCreate)"
linkTitle: "描画オブジェクトの基本 (ObjectCreate)"
url: "/p/du6env6"
date: "2021-02-13"
tags: ["MetaTrader/MQL"]
---

描画オブジェクトの作成 (ObjectCreate)
----

MetaTrader のチャート上に何らかの図形を描画するには、[ObjectCreate 関数](https://www.mql5.com/en/docs/objects/objectcreate)（[日本語](https://www.mql5.com/ja/docs/objects/objectcreate)）を使って、描画オブジェクトを生成します。

{{< code lang="cpp" title="ObjectCreate 関数" >}}
bool ObjectCreate(
    long chart_id,     // チャート ID（0 ならカレントチャート）
    string name,       // オブジェクト名
    ENUM_OBJECT type,  // オブジェクトの種類
    int sub_window,    // サブウィンドウ番号（0 ならメインウィンドウ）
    datetime time1,    // 1 番目のアンカーポイントの時刻
    double price1,     // 1 番目のアンカーポイントの価格
    ...                // :
    datetime time30=0, // 30番目のアンカーポイントの時刻
    double price30=0   // 30番目のアンカーポイントの価格
);
{{< /code >}}

### chart_id / sub_window

`chart_id` 引数と `sub_window` 引数には、どのチャートの、どのウィンドウに描画オブジェクトを表示するかを指定します。
カレントチャートのメインウィンドウに表示するのであれば、両方とも 0 を指定しておけば OK です。

### name

`name` 引数では、作成する描画オブジェクトに名前を付けます。
描画オブジェクトの各種プロパティを設定するときは、この名前で描画オブジェクトを指定することになります。
名前はチャート内（サブウィンドウを含む）で一意でなければいけません。
ただし、使用上 63 文字までしか使えないので、その範囲で他のインジケーターとできるだけ被らない名前を付ける必要があります。

簡単なテクニックとして、次のようなプレフィックスマクロを定義しておけば、

{{< code lang="cpp" >}}
#define OBJ_PREFIX "MY_INDI_"
{{< /code >}}

オブジェクト名が必要なところで次のように使えます。
文字列リテラルを並べると自動的に結合されるので、`+` 演算子を使った文字列結合は必要ないことに注意してください。

{{< code lang="cpp" >}}
string name1 = OBJ_PREFIX "LABEL_1";  //=> "MY_INDI_LABEL_1" になる
string name2 = OBJ_PREFIX "LABEL_2";  //=> "MY_INDI_LABEL_2" になる
{{< /code >}}

### type

`type` 引数では、どのような種類の描画オブジェクトを作成するかを指定します。
例えば、ラベルであれば `OBJ_LABEL` を指定し、水平線であれば `OBJ_HLINE` を指定します。

### time1 / price1

`time1` 引数や `price1` 引数では、描画オブジェクトのアンカーポイントを指定します。
アンカーポイントとは、描画オブジェクトの表示位置を示す座標情報です。
描画オブジェクトの種類によって、アンカーポイントをいくつ指定しなければいけないかが決まっています（0 個以上）。
例えば、長方形オブジェクト (`OBJ_RECTANGLE`) やトレンドラインオブジェクト (`OBJ_TREND`) の場合は、2 つのアンカーポイント（`time1`、`price1`、`time2`、`price2`）を指定する必要があります。

ラベルオブジェクト (`OBJ_LABEL`) のように、アンカーポイントをまったく使用しない描画オブジェクトもあります（ラベルの表示位置は `OBJPROP_XDISTANCE` などのプロパティで指定します）。
その場合でも、`ObjectCreate` 関数の使用上、1 つはアンカーポイントを指定しなければいけません。
ラベルオブジェクトを作成する場合は、`time1` 引数と `price1` 引数には、適当に 0 を指定しておけば OK です。

次のインジケーターでは、`CreateObject` 関数を使って、1 つの水平線オブジェクト (`OBJ_HLINE`) を作成しています。
水平線は 1 つのアンカーポイント（`price1` のみ）を使用します。

{{< code lang="cpp" title="Scripts/Test.mq5" >}}
#property strict
#property indicator_chart_window
#property indicator_plots 0

input double Price = 100;  // 水平線を引く価格

int OnInit() {
    ObjectCreate(0, "HLINE_1", OBJ_HLINE, 0, 0, Price);
    return INIT_SUCCEEDED;
}

int OnCalculate(const int rates_total, const int prev_calculated,
                const int begin, const double &price[]) {
    return rates_total;
}
{{< /code >}}


描画オブジェクトの削除 (ObjectDelete, ObjectDeleteAll)
----

### 描画オブジェクトを 1 つずつ削除（ObjectDelete）

`CreateObject` で作成した描画オブジェクトは、[ObjectDelete 関数](https://www.mql5.com/en/docs/objects/objectdelete)（[日本語](https://www.mql5.com/ja/docs/objects/objectdelete)）を使って削除することができます。

{{< code lang="cpp" title="ObjectDelete 関数" >}}
bool ObjectDelete(long chart_id, string name);
{{< /code >}}

インジケーターの `OnDeinit` 関数内で呼び出すようにしておけば、インジケーターをチャートからデタッチしたときに、自動的に描画オブジェクトを削除できます。

{{< code lang="cpp" title="Indicators/Test.mq5（抜粋）" >}}
input double Price = 105;  // 水平線をひく価格
#define OBJ_PREFIX "MY_INDI_"

int OnInit() {
    ObjectCreate(0, OBJ_PREFIX "HLINE_1", OBJ_HLINE, 0, 0, Price);
    return INIT_SUCCEEDED;
}

void OnDeinit(const int reason) {
    ObjectDelete(0, OBJ_PREFIX "HLINE_1");
    ObjectFind(0, OBJ_PREFIX "HLINE_1");  // 確実に反映させる
}
{{< /code >}}

注意点としては、`ObjectDelete` 関数は非同期で実行されるため、`OnDeinit` 関数で単独で呼び出しても処理が即座に反映されないことがあるということです（市場がクローズしているときなど）。
この問題を解決するには、`ObjectDelete` 関数の後ろで、`ObjectFind` 関数など同期実行される関数を呼び出しておきます。

### 描画オブジェクトをまとめて削除 (ObjectsDeleteAll)

[ObjectDeleteAll 関数](https://www.mql5.com/en/docs/objects/objectdeleteall)（[日本語](https://www.mql5.com/ja/docs/objects/objectdeleteall)）を使うと、指定したチャート内の描画オブジェクトをまとめて削除することができます。

{{< code lang="cpp" title="ObjectDeleteAll 関数" >}}
int ObjectsDeleteAll(
    long chart_id,      // チャート識別子
    int sub_window=-1,  // ウィンドウ番号
    int type=-1         // オブジェクトの型
);

int ObjectsDeleteAll(
    long chart_id,        // チャート識別子
    const string prefix,  // オブジェクト名のプレフィックス
    int sub_window=-1,    // ウィンドウ番号
    int object_type=-1    // オブジェクトの型
);
{{< /code >}}

2 つ目のバージョンでは、指定したプレフィックスを名前に持つ描画オブジェクトだけをまとめて削除することができます。
これを使えば、インジケーターが自分で追加したオブジェクトだけをまとめて削除することができます。

次のインジケーターは、チャートへのアタッチ時に 3 つの水平線を生成し、デタッチ時に自分が作成した水平線をすべて削除します。

{{< code lang="cpp" title="Indicators/Test.mq5" >}}
#property strict
#property indicator_chart_window
#property indicator_plots 0

input double Price = 105;  // 水平線をひく価格

// 描画オブジェクトのプレフィックス
#define OBJ_PREFIX "MY_INDI_"

int OnInit() {
    // 同じプレフィックスで描画オブジェクトを生成する
    ObjectCreate(0, OBJ_PREFIX "HLINE_UPPER", OBJ_HLINE, 0, 0, Price - 0.5);
    ObjectCreate(0, OBJ_PREFIX "HLINE_MIDDLE", OBJ_HLINE, 0, 0, Price);
    ObjectCreate(0, OBJ_PREFIX "HLINE_LOWER", OBJ_HLINE, 0, 0, Price + 0.5);

    return INIT_SUCCEEDED;
}

void OnDeinit(const int reason) {
    // 同じプレフィックスを持つ描画オブジェクトをすべて削除する
    ObjectsDeleteAll(0, OBJ_PREFIX);
}

int OnCalculate(const int rates_total, const int prev_calculated,
                const int begin, const double &price[]) {
    return rates_total;
}
{{< /code >}}


描画オブジェクトの設定 (ObjectSetXxx)
----

`ObjectCreate` 関数によって描画オブジェクトを作成したら、あとは次のような関数を使って各種プロパティを設定していきます。

- [ObjectSetInteger 関数](https://www.mql5.com/en/docs/objects/objectsetinteger)（[日本語](https://www.mql5.com/ja/docs/objects/objectsetinteger)）... 整数型のプロパティを設定
- [ObjectSetDouble 関数](https://www.mql5.com/en/docs/objects/objectsetdouble)（[日本語](https://www.mql5.com/ja/docs/objects/objectsetdouble)）... 浮動小数点数型のプロパティを設定
- [ObjectSetString 関数](https://www.mql5.com/en/docs/objects/objectsetstring)（[日本語](https://www.mql5.com/ja/docs/objects/objectsetstring)）... 文字列型のプロパティを設定

次のサンプルスクリプトでは、ラベルオブジェクト作成し、上記の関数を使ってフォントサイズや表示位置の設定を行っています。

{{< code lang="cpp" title="Indicators/Test.mq5（ラベルを右下に表示）" >}}
#property strict
#property indicator_chart_window
#property indicator_plots 0

// 描画オブジェクトのプレフィックス
#define OBJ_PREFIX "MY_INDI_"

int OnInit() {
    // ラベルを作成する
    string name = OBJ_PREFIX "LABEL_1";
    ObjectCreate(0, name, OBJ_LABEL, 0, 0, 0);

    // 表示するテキスト、色、フォントサイズを設定
    ObjectSetString(0, name, OBJPROP_TEXT, "Hello");
    ObjectSetInteger(0, name, OBJPROP_COLOR, clrYellow);
    ObjectSetInteger(0, name, OBJPROP_FONTSIZE, 20);

    // ラベルはチャートの右下に表示する
    ObjectSetInteger(0, name, OBJPROP_CORNER, CORNER_RIGHT_LOWER);
    ObjectSetInteger(0, name, OBJPROP_ANCHOR, ANCHOR_RIGHT_LOWER);
    ObjectSetInteger(0, name, OBJPROP_XDISTANCE, 10);
    ObjectSetInteger(0, name, OBJPROP_YDISTANCE, 10);

    // 直ちに画面に反映させる
    ChartRedraw();
    return INIT_SUCCEEDED;
}

void OnDeinit(const int reason) {
    ObjectsDeleteAll(0, OBJ_PREFIX);
}

int OnCalculate(const int rates_total, const int prev_calculated,
                const int begin, const double &price[]) {
    return rates_total;
}
{{< /code >}}

