---
title: "MetaTrader/MQL: 音声を再生する"
linkTitle: "音声を再生する"
url: "p/xof3ydu/"
date: "2014-12-07"
tags: ["MetaTrader/MQL"]
---

MQL5 の [PlaySound 関数](https://www.mql5.com/ja/docs/common/playsound) を使うと音声ファイル (WAV) を再生することができます。

{{< code lang="cpp" title="使用例" >}}
PlaySound("alert.wav");
{{< /code >}}

`PlaySound` の引数には、MetaTrader の __`Sounds`__ ディレクトリ内の WAV ファイルを指定します。
例えば次のようなファイルがあります。

- `alert.wav`
- `alert2.wav`
- `connect.wav`
- `disconnect.wav`
- `email.wav`
- `expert.wav`
- `news.wav`
- `ok.wav`
- `stops.wav`
- `tick.wav`
- `timeout.wav`
- `wait.wav`

音声の再生は非同期に実行されるため、`PlaySound` 関数の呼び出しがプログラムを停止させることはありません。
音声の再生中にもう一度 `PlaySound` 関数を呼び出すと、現在再生中の音声は停止し、新しく指定した音声の再生が開始されます。
例えば、下記のように連続して実行すると、最後に指定した音だけが聞こえます。

```cpp
PlaySound("alert.wav");  // この音は聞こえず、
PlaySound("ok.wav");     // この音だけが聞こえる
```

引数にファイル名ではなく __`NULL`__ を指定すると、現在再生中の音声を停止することができます。

{{< code lang="cpp" title="音声を停止する" >}}
PlaySound(NULL);
{{< /code >}}

次のスクリプトは、1 秒おきに異なる音声を再生していきます。

{{< code lang="cpp" title="Scripts/sample.mq5" >}}
void OnStart() {
    string sounds[] = {
        "alert.wav", "alert2.wav", "connect.wav",
        "disconnect.wav", "email.wav", "expert.wav",
        "news.wav", "ok.wav", "stops.wav",
        "tick.wav", "timeout.wav", "wait.wav"
    };

    for(int i = 0; i < ArraySize(sounds); ++i) {
        Print("Sound file: " + sounds[i]);  // Experts タブにファイル名を表示
        PlaySound(sounds[i]);               // 音声を再生
        Sleep(1000);                        // 1 秒待つ
    }
}
{{< /code >}}

