---
title: "所得税の計算: 10種類の所得を計算する"
url: "/p/hbwxvp5"
linkTitle: "10種類の所得"
date: "2016-01-02"
tags: ["税金"]
description: "所得税は 10 種類に分類されており、計算の仕方がそれぞれ異なっています。日本の納税制度の難しいところですが、ここはしっかり押さえておく必要があります。"
---

<style>
.local-taxTable {
  font-size: smaller;
  margin: auto;
  border-collapse: collapse;  /* セル間の隙間をなくす */
}
.local-taxTable td {
  padding: 5px;
  border: 1px solid gray;
  margin: 0px;
}
.local-taxTable .type {
  background: #ccc;
  text-align: center;
  padding: 4px;
}
.local-taxTable .type-indent {
  background: #ddd;
}
.local-check {
  text-align: center;
  background: #cfc;
}
</style>

10 種類の所得
----

所得は、その種類ごとに経費として扱えるものや、特別な控除の仕組みが異なっているため、10 種類に分類されており、それぞれ別々に所得金額を計算する必要があります。
ただし、**配当所得に関しては、課税方法を選択できる**ため、下記では 3 種類に分けています。
さらに、**譲渡所得に関しても、譲渡するものの種類（土地・建物、株式、それ以外）によって税金の扱いが異なる**ため、下記では 3 種類に分けています。

<table class="local-taxTable">
  <tr>
    <th colspan="2">所得の種類</th><th>総合<br>課税</th><th>分離<br>課税</th><th>損益<br>通算</th><th>補足</th>
  </tr>
  <tr>
    <td colspan="2" class="type">事業所得</td>
    <td class="local-check">&#10003;</td><td></td><td class="local-check">&#10003;</td><td></td>
  </tr>
  <tr>
    <td colspan="2" class="type">不動産所得</td>
    <td class="local-check">&#10003;</td><td></td><td class="local-check">△</td>
    <td>土地のための借金の利子は損益通算できない。建物ための借金の利子は損益通算できる。</td>
  </tr>
  <tr>
    <td colspan="2" class="type">給与所得</td>
    <td class="local-check">&#10003;</td><td></td><td></td><td>源泉徴収＋年末調整</td>
  </tr>
  <tr>
    <td colspan="2" class="type">一時所得</td>
    <td class="local-check">&#10003;</td><td></td><td></td><td></td>
  </tr>
  <tr>
    <td colspan="2" class="type">雑所得</td>
    <td class="local-check">&#10003;</td><td></td><td></td><td>他の 9 種類のいずれにも分類できない所得。FX などによる利益は雑所得になる。</td>
  </tr>

  <tr>
    <td class="type" rowspan="3">配<br>当<br>所<br>得</td>
    <td class="type-indent">総合課税</td>
    <td class="local-check">&#10003;</td><td></td><td></td>
    <td><strong>配当控除（税額控除）</strong>が使えるが、総合課税となる所得が多い場合は分離課税にしておいた方がよい。</td>
  </tr>
  <tr>
    <td class="type-indent">申告分離課税</td>
    <td></td><td class="local-check">&#10003;</td><td class="local-check">&#10003;</td>
    <td><strong>株式の譲渡損失と損益通算</strong>できる。ただし、非上場株式の配当所得は損益通算不可。</td>
  </tr>
  <tr>
    <td class="type-indent">源泉分離課税</td>
    <td></td><td class="local-check">&#10003;</td><td></td>
    <td>多くの人が申告不要制度による「源泉分離課税」を選択していて、配当が出た時に約20％の税金を自動的に徴収されている。</td>
  </tr>

  <tr>
    <td class="type" rowspan="3">譲<br>渡<br>所<br>得</td>
    <td class="type-indent">土地・建物・株式以外</td>
    <td class="local-check">&#10003;</td><td></td><td class="local-check">△</td>
    <td>生活に必要のない資産（クルーザー、別荘、貴金属（30万円超）、ゴルフ会員権）の譲渡は損益通算できない。</td>
  </tr>
  <tr>
    <td class="type-indent">土地・建物</td>
    <td></td><td class="local-check">&#10003;</td><td></td>
    <td>土地や建物の譲渡損失は損益通算できない。ただし、<strong>自宅</strong>譲渡時の損失については、給与所得等と損益通算できる特例あり（居住用財産の譲渡損失の損益通算および繰越控除の特例）。</td>
  </tr>
  <tr>
    <td class="type-indent">株式</td>
    <td></td><td class="local-check">&#10003;</td><td class="local-check">&#10003;</td>
    <td>株式の譲渡損失は損益通算できる。</td>
  </tr>

  <tr>
    <td colspan="2" class="type">退職所得</td>
    <td></td><td class="local-check">&#10003;</td><td></td><td></td>
  </tr>
  <tr>
    <td colspan="2" class="type">山林所得</td>
    <td></td><td class="local-check">&#10003;</td><td class="local-check">&#10003;</td><td></td>
  </tr>
　<tr>
    <td colspan="2" class="type">利子所得</td>
    <td></td><td class="local-check">&#10003;</td><td></td>
    <td><strong源泉分離課税</strong>（利子の支払い時に源泉徴収）</td>
  </tr>
</table>


### 総合課税はいろいろ足し合わせ

**総合課税の対象**となっている所得に関しては、最終的に**総所得金額として合算**されます。
所得税額は、課税所得金額に対して税率（累進課税）を掛けることで計算するのですが、総合課税の対象となっている所得に対しては、総所得金額に対して税率が掛けられるということです。

### 配当金の税金は払い方を選択できる

配当所得に関しては、3 種類の課税方法を選ぶことができるので、どの方法が自分にとって有利になるかを判断して確定申告するべきです。
特に、株式の譲渡などで損失が出ている場合は、配当所得の申告分離課税を選択することによって損益通算を行うことができるようになり、余計な税金を払わなくて済むようになります。

<!--
損益通算というのは、必要経費による損失があった場合に、所得から

### 事業所得
-->

