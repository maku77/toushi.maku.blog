---
title: "MetaTrader/MQL: MetaTrader 実行環境（ターミナル）の情報を取得する (TerminalInfo*)"
linkTitle: "MetaTrader 実行環境（ターミナル）の情報を取得する (TerminalInfo*)"
url: "p/85rz2xr/"
date: "2014-12-06"
lastmod: "2023-06-18"
changes:
  - 2023-06-18: 外部リンクを MQL5 の URL に更新
tags: ["MetaTrader/MQL"]
---

MetaTrader の実行環境（ターミナル）の情報を取得するには、__`TerminalInfo*`__ 系の関数を使用します。
戻り値の型によって使用する関数を呼び分ける必要があります。
取得したい項目は、各関数の引数で指定します。

- [TerminalInfoString 関数](https://www.mql5.com/en/docs/check/terminalinfostring)
  - __`string`__ 型の情報を取得するとき。
  - 取得する項目は [ENUM_TERMINAL_INFO_STRING enum 型](https://www.mql5.com/en/docs/constants/environment_state/terminalstatus#enum_terminal_info_string) から選択します。
- [TerminalInfoInteger 関数](https://www.mql5.com/en/docs/check/terminalinfointeger)
  - __`int`__ 型の情報を取得するとき。
  - 取得する項目は [ENUM_TERMINAL_INFO_INTEGER enum 型](https://www.mql5.com/en/docs/constants/environment_state/terminalstatus#enum_terminal_info_integer) から選択します。
- [TerminalInfoDouble 関数](https://www.mql5.com/en/docs/check/terminalinfodouble)
  - __`double`__ 型の情報を取得するとき。
  - 取得する項目は [ENUM_TERMINAL_INFO_DOUBLE enum 型](https://www.mql5.com/en/docs/constants/environment_state/terminalstatus#enum_terminal_info_double) から選択します。

次のスクリプトを実行すると、MetaTrader 実行環境（ターミナル）の情報をログ出力します。

{{< code lang="cpp" title="Scripts/PrintTerminalInfo.mq5" >}}
void OnStart() {
    Print("Language=" + TerminalInfoString(TERMINAL_LANGUAGE));
    Print("Company=" + TerminalInfoString(TERMINAL_COMPANY));
    Print("Name=" + TerminalInfoString(TERMINAL_NAME));
    Print("Path=" + TerminalInfoString(TERMINAL_PATH));
    Print("DataPath=" + TerminalInfoString(TERMINAL_DATA_PATH));
    Print("CommonDataPath=" + TerminalInfoString(TERMINAL_COMMONDATA_PATH));
}
{{< /code >}}

{{< code lang="ini" title="実行結果（OANDA の MT5 を使っている場合）" >}}
Language=Japanese
Company=OANDA Corporation
Name=OANDA MetaTrader 5
Path=C:\app\OANDA MetaTrader 5
DataPath=C:\Users\maku\AppData\Roaming\MetaQuotes\Terminal\84E63C3B90BC3EC3DADC66BC66DD0A1E
CommonDataPath=C:\Users\maku\AppData\Roaming\MetaQuotes\Terminal\Common
{{< /code >}}

