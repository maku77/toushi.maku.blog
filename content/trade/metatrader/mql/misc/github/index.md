---
title: "MetaTrader/MQL: GitHub で MetaTrader 用のプログラムを管理する"
linkTitle: "GitHub で MetaTrader 用のプログラムを管理する"
url: "/p/od4bq8j"
date: "2021-01-07"
tags: ["MetaTrader/MQL"]
---

MetaTrader (MT4/MT5) 用に作成した EA やカスタムインジケーターは大切な資産です。
ここでは、MetaTrader 用のプログラムを GitHub で管理する方法を説明します。


MetaTrader のデータディレクトリ
----

MetaTrader では、自作した EA やカスタムインジケーター（`.mq5` ファイルなど）は、あらかじめ用意されたデータディレクトリに格納することになっています。
このディレクトリのパスは、MetaTrader のデスクトップアプリや MetaEditor のメニューから次のように開いて確認することができます。

- `ファイル` → `データフォルダを開く` （あるいは __`Ctrl + Shift + D`__）

データフォルダのパスは環境ごとに異なり、例えば次のような感じになっています。

{{< code >}}
C:\Users\maku\AppData\Roaming\MetaQuotes\Terminal\84E63C3B90BC3EC3DADC66BC66DD0A1E
{{< /code >}}

自作した `.mq5` ファイルを保存するディレクトリは、このデータディレクトリ以下の `MQL5/Experts` や `MQL5/Indicators` ディレクトリになります。

しかし、データディレクトリには MetaTrader のインストーラーによって作成されたファイルなども含まれているため、`MQL5` ディレクトリを丸ごと GitHub で管理しようとすると、余計なファイルがコミットされてしまいます。

そこで、自作したプログラムは別のディレクトリで管理して、データディレクトリからそのディレクトリに __シンボリックリンク__ を張ることにします。


シンボリックリンクを作成する
----

まずは、GitHub で作成したコード格納用のリポジトリを `git clone` しておきます。
ここでは、GitHub 上に `metatrader` という名前のリポジトリを作成済みで、作業用ディレクトリとして `D:\y\gitwork` を使うことを想定しています（パスは環境に合わせて調整してください）。

{{< code >}}
cd /d D:\y\gitwork
git clone https://github.com/ユーザー名/metatrader
{{< /code >}}

ローカルに `metatrader` というディレクトリが作成されるので、この中に `MQL5` ディレクトリを作成して、そこに自作の EA やインジケーターを格納することにします。
シンボリックリンクはディレクトリ単位で作成したいので、実際には次のようにもう一段階ディレクトリ作成します。
ここでは `maku77` というディレクトリ名にしてますが、GitHub のユーザー名などにしておけばよいでしょう。

{{< code >}}
cd metatrader
mkdir MQL5\Experts\maku77
mkdir MQL5\Images\maku77
mkdir MQL5\Include\maku77
mkdir MQL5\Indicators\maku77
mkdir MQL5\Libraries\maku77
mkdir MQL5\Scripts\maku77
{{< /code >}}

Windows でディレクトリのシンボリックリンクを作成するには、コマンドプロンプトを __管理者として実行__ し、__`mklink /d`__ コマンドを使用します。
コマンドプロンプトを起動したら、次のように MetaTrader のデータディレクトリに移動して、各ディレクトリのシンボリックリンクを作成します。

{{< code >}}
cd /d C:\Users\maku\AppData\Roaming\MetaQuotes\Terminal\84E63C3B90BC3EC3DADC66BC66DD0A1E
mklink /d MQL5\Experts\maku77 D:\y\gitwork\metatrader\MQL5\Experts\maku77
mklink /d MQL5\Images\maku77 D:\y\gitwork\metatrader\MQL5\Images\maku77
mklink /d MQL5\Include\maku77 D:\y\gitwork\metatrader\MQL5\Include\maku77
mklink /d MQL5\Indicators\maku77 D:\y\gitwork\metatrader\MQL5\Indicators\maku77
mklink /d MQL5\Libraries\maku77 D:\y\gitwork\metatrader\MQL5\Libraries\maku77
mklink /d MQL5\Scripts\maku77 D:\y\gitwork\metatrader\MQL5\Scripts\maku77
{{< /code >}}

MetaEditor のナビゲータに、次のような感じで `maku77` ディレクトリが見えていれば成功です。

{{< image src="img-001.png" title="データディレクトリにシンボリックリンクが作成された" >}}

あとは、いつも通り MetaEditor から `maku77` ディレクトリに `.mq5` ファイルを新規作成すれば、Git ディレクトリの方にファイルが保存されるようになります。


gitignore を設定する
----

コンパイル後の `.ex4`、`.ex5` ファイルは Git では管理したくないので、__`.gitignore`__ ファイルで Git 管理しないように除外しておきましょう。

{{< code title="metatrader/.gitignore" >}}
*.ex4
*.ex5
{{< /code >}}


シンボリックリンク作成用のバッチファイルを作成する
----

上記の説明では、手動でデータディレクトリから Git ディレクトリへのシンボリックリンクを作成しましたが、この処理はバッチファイルなどで自動化しておくと便利です。

{{< code lang="batch" title="metatrader/create-symlinks.bat" >}}
@echo off
setlocal

set user=maku77
set current_dir=%~dp0
set data_dir=%~1

REM Exit if not admin
net session >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo ERROR: Need to run as Administrator
    exit /b
)

REM Check if the data dir is specified
if "%data_dir%"=="" (
    echo Usage: %~n0 MT_DATA_DIR
    echo You can check the path by pressing CTRL+SHIFT+D in MetaTrader platform
    exit /b
)

REM Create symbolic links
cd /d %data_dir%
mklink /d MQL5\Experts\%user% %current_dir%MQL5\Experts\%user%
mklink /d MQL5\Images\%user% %current_dir%MQL5\Images\%user%
mklink /d MQL5\Include\%user% %current_dir%MQL5\Include\%user%
mklink /d MQL5\Indicators\%user% %current_dir%MQL5\Indicators\%user%
mklink /d MQL5\Libraries\%user% %current_dir%MQL5\Libraries\%user%
mklink /d MQL5\Scripts\%user% %current_dir%MQL5\Scripts\%user%
{{< /code >}}

これで、別の PC 環境に移行したときでも、次のように実行するだけで一発で環境構築が完了します。

{{< code >}}
git clone https://github.com/ユーザー名/metatrader
cd metatrader
create-symlinks C:\Users\maku\AppData\Roaming\MetaQuotes\Terminal\84E63...30A1E
{{< /code >}}

