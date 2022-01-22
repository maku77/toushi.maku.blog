---
title: "資産配分シミュレーター（高橋ダン氏のライオン戦略用）"
url: "/p/jxanz7d"
date: "2020-12-07"
tags: ["ツール"]
---

投資資金を振り分けるための計算機
----

高橋ダン氏の書籍 {{<amazon-inline id="4761275073" title="お金の増やし方" >}}、{{< amazon-inline id="4046049448" title="勝利の投資術" >}} で紹介されている「ライオン戦略」は、長期投資の戦略として非常に参考になります。
簡単に言うと、投資用の資金を「長期投資用、短期投資用」の 2 つに分け、さらに長期投資用の資金を一定の比率でいろいろな資産に分散投資する戦略です。

下記のツールは、投資資金を一定の比率で各資産に分配するための計算機です。
投資資金のところに金額を入力すると、それぞれいくら配分すればよいか表示されます（割合は固定してます）。

<style>
  .local-total {
    font-size: 1.1em;
    width: 4em;
    margin-right: 0.2em;
    vertical-align: middle;
  }
  .local-table input {
    width: 3em;
    text-align: right;
    border: none;
    font-size: larger;
    font-weight: bolder;
    color: blue;
  }
  .local-table th, .local-table td {
    border: none;
  }
  .local-long {
    text-align: left;
    background: green;
    color: white;
  }
  .local-short {
    text-align: left;
    background: #933;
    color: white;
  }
  .local-long-sub {
    text-align: left;
    background: #cfc;
    color: green;
  }
  .local-result {
    background: #eee;
  }
</style>

<center style="font-size: larger">
  <b>投資資金</b>:
  <input class="local-total" id="total" type="text" value="100"></input>万円
</center>

<table class="local-table">
  <tbody>
    <tr>
      <th colspan="2" class="local-long">長期投資（8割）</th>
      <td class="local-result"><input id="longTerm" disabled type="text" />万円</td>
    </tr>
    <tr>
      <td class="local-long">&nbsp;</td>
      <th class="local-long-sub">株式・社債・不動産（5割）</th>
      <td class="local-result"><input id="stock" disabled type="text" />万円</td>
    </tr>
    <tr>
      <td class="local-long">&nbsp;</td>
      <th class="local-long-sub">コモディティ（3割）</th>
      <td class="local-result"><input id="commodity" disabled type="text" />万円</td>
    </tr>
    <tr>
      <td class="local-long">&nbsp;</td>
      <th class="local-long-sub">国債・現金（2割）</th>
      <td class="local-result"><input id="bond" disabled type="text" />万円</td>
    </tr>
    <tr>
      <th colspan="2" class="local-short">短期投資（2割）</th>
      <td class="local-result"><input id="shortTerm" disabled type="text" value="0"></input>万円</td>
    </tr>
  </tbody>
</table>

<script>
window.addEventListener('DOMContentLoaded', () => {
  const total = document.getElementById('total');
  const longTerm = document.getElementById('longTerm');
  const shortTerm = document.getElementById('shortTerm');
  const stock = document.getElementById('stock');
  const commodity = document.getElementById('commodity');
  const bond = document.getElementById('bond');

  total.addEventListener('input', (e) => {
    updateValues();
  });

  updateValues();

  function updateValues() {
    const t = total.value;
    longTerm.value = (t * 0.8).toFixed();
    stock.value = (t * 0.8 * 0.5).toFixed();
    commodity.value = (t * 0.8 * 0.3).toFixed();
    bond.value = (t * 0.8 * 0.2).toFixed();
    shortTerm.value = (t * 0.2).toFixed();
  }
});
</script>

各資産について
----

まず、__「長期投資」と「短期投資」に使う資金は口座（証券口座）を分けて管理__ することで、比率を守って投資できるようにします。
長期投資部分は、毎月いろいろな領域の ETF を少しずつ買っていくことで、分散投資します（シャープレシオを上げるのが重要）。
特定の領域の資産割合が大きくなってしまった場合は、別の領域の ETF の購入割合を大きくするなどして毎月リバランスします。

### 長期投資（8割）

長期投資用の資産は長く持ち続けることによる複利効果を狙います。
短期的な大きなリターンは期待せず、多くの商品に分散投資することで安定したリターンを確保します。
出来高が大きく、信託報酬（経費率）の低い ETF を活用します。

<table>
  <thead>
    <tr>
      <th>長期投資資産のカテゴリ</th>
      <th>どう分散するか？</th>
      <th>具体的な ETF 例</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>株式・社債・不動産</b>（5割）<br><small>（経済成長時に上昇する部分）</small></td>
      <td>「先進国／途上国」、<br>「ドル建て／円建て／ユーロ建て」</td>
      <td>VEA, VWO, SPY,<br>1615, 1306, 2800,<br>FXI, SX5S, FEZ,<br>EIDO, HYG</td>
    </tr>
    <tr>
      <td><b>コモディティ</b>（3割）<br><small>（経済危機に備える部分）</small></td>
      <td>貴金属（金／銀／プラチナ）、<br>ベースメタル（亜鉛／鉛／アルミニウム）、<br>原油、天然ガス、農業商品、ビットコイン</td>
      <td>GLD, IAU, GDX,<br>GDXJ, SLV, PPLT,<br>1541, PALL, DBB,<br>USO, UNG, DBA</td>
    </tr>
    <tr>
      <td><b>国債・現金</b>（2割）<br><small>（守りの部分）</small></td>
      <td>「米国債／日本国債／欧州国債」、<br>「短期／中期／長期」</td>
      <td>VGSH, SPTS, TIP,<br>BND, VGIT, SPTI,<br>EDV, SPTL, TLT</td>
    </tr>
  </tbody>
</table>

### 短期投資（2割）

一部の投資資金は短期戦略でハイリターンを狙います。
様々なトレードアイデアで相場の波に乗り、細かい売買を繰り返して利益を出します。
経済危機時には、すべての長期投資資産が下がってしまうことがあるので、この短期投資でカバーします。
次のようなことを意識します。

- トレンドを探してそれに乗ることで小さな利益を積み重ねる
    - 100円を1回で取るのは難しいが、10円を10回取るのは簡単
    - 10バガーを狙うのではなく、数十％上がりそうな波に乗って数％抜くというのを繰り返す
- トレンドが変わったと判断したら利確。損切りも同じ
- ひとつの商品には 5〜10％ の資金まで（大きく負けないことがとっても大切）
- 流動性の高い ETF や FX などを使う

少なくとも、長期投資用と短期投資用の口座をちゃんと分けておけば、短期投資で熱くなって資産の大部分を溶かしてしまうという心配はなくなります。

