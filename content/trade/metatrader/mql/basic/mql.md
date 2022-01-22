---
title: "MetaTrader 用のプログラミング言語 MQL とは"
url: "/p/rk2hvbq"
date: "2014-11-09"
tags: ["MetaTrader/MQL"]
weight: 1
---

MQL は MetaQuotes Language の略であり、MetaQuotes Software 社の作成した言語です。MetaQuotes Software 社は FX トレードのためのソフトウェアである MetaTrader（Windows 用）を開発しており、MQL はこの中で動作するプログラムを作成するための言語です。MQL を使ってプログラムを作成すると、

* 自動売買を行うトレーディング・ロボット (**Expert Advisor**、通称 EA)
* カスタムインジケータ (**Custom Indicator**)
* 任意の処理を行うスクリプト (**Script**)

などを作成することができます。MQL は C/C++ 言語をベースとした構文になっているため、C/C++ の経験者であれば簡単に使用することができます。
MetaTrader には、MQL でコーディングを行うための MetaEditor が付属しています。まずは MetaTrader をダウンロードしてインストールしましょう。現在公開されている MetaTrader にはバージョン 4 と 5 があり、それぞれの環境で使用可能な MQL のバージョンも異なります (MQL4 と MQL5)。日本の FX 会社が対応しているのは、主に MetaTrader 4 です。

* [MetaTrader 4 のダウンロード](http://www.metatrader4.com/)
* [MetaTrader 5 のダウンロード](http://www.metaquotes.net/)

練習や、開発用途で使用するのであれば、MetaQuotes のサイトからダウンロードできる MetaTrader を使い、インストール時にデモアカウントを作成すれば十分です。
実際に FX 会社の口座を使って取引するための MetaTrader は、ほとんどの場合、その FX 会社がカスタマイズ版の MetaTrader として配布していますので、そちらを使うのがよいでしょう。

次のステップ → [MQL で Hello World](/p/ay9a762)

