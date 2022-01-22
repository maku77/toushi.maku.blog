---
title: "貸借対照表の読み方"
url: "/p/fwtpsqp"
tags: ["財務分析"]
description: "三大財務諸表のひとつである貸借対照表の基本的な読み方を説明します。"
---

<style>
.local-center {
  margin-left: auto;
  margin-right: auto;
}
/* 資産 */
.local-asset {
  background: #ddf;
  color: #00a;
}
/* 負債 */
.local-liability {
  background: #fdd;
  color: #c00;
}
/* 純資産/資本 */
.local-equity {
  background: #ffc;
  color: #c60;
}
/* 利益剰余金 */
.local-surplus {
  color: #090;
  background: #dfd;
  border: 1px solid #090;
  padding: 3px;
  margin: 8px;
}

.local-balancedWidth {
  width: 200px;
  text-align: center;
}
.local-balancedHeight {
  height: 40px;
}
</style>


貸借対照表の構成
----

<table class="local-center">
  <tr class="local-balancedHeight">
    <td rowspan="2" class="local-asset local-balancedWidth">資産の部<br>(Assets)</td>
    <td class="local-liability local-balancedWidth">負債の部<br>(Liabilities)</td>
  </tr>
  <tr class="local-balancedHeight">
    <td class="local-equity local-balancedWidth">純資産の部<br>(Equity)</td>
  </tr>
</table>

貸借対照表はこのような構成で表現されます。
右側（貸方という）が資金の調達元、左側（借方という）がその資金をどのような資産として運用しているかを表しています。
資産の欄には、資金を使用して購入した固定資産も含まれますし、現金として残っているのならば、そのまま現金（及び預金）として記述されます。
つまり、資金全体の運用状態（資産構成）が示されているので、右側の合計金額と、左側の合計金額は常に一致します。

- 左側（借方）
    - <b class="local-asset">資産の部</b>: 現金や固定資産など、どのような資産として運用しているか。
- 右側（貸方）
    - <b class="local-liability">負債の部</b>: 借入金など他人から借りていて返済義務のあるお金（他人資本）
    - <b class="local-equity">純資産の部</b>: 資本金や自己株式など返済義務のないお金（自己資本）

右側の負債や純資産は、いわゆる「お金」の調達元を表しています。
負債の欄に記述されているものは、返済義務のあるお金なので、いつかはそのお金を返さなければいけません。
そのためには、営業活動などで利益をあげて返済するか、資産を切り崩して支払う必要があります。
こういった現金の流れは、財務諸表のひとつであるキャッシュフロー計算書を見るとわかるようになっています。


利益剰余金
----

<table class="local-center">
  <tr class="local-balancedHeight">
    <td rowspan="2" class="local-asset local-balancedWidth">
        資産の部<br>(Assets)
        <div class="local-surplus">新しい資産</div>
    </td>
    <td class="local-liability local-balancedWidth">負債の部<br>(Liabilities)</td>
  </tr>
  <tr class="local-balancedHeight">
    <td class="local-equity local-balancedWidth">
        純資産の部<br>(Equity)
    </td>
  </tr>
</table>

経営がうまくいっていると、売り上げによる利益が出て資産が増えていきます（現金や売掛金という資産が増える）。
単純に金額ベースで見ると、貸借対照表のサイズは大きくなることになります。

貸借対照表の左右の金額は一致させなければいけません。
利益が出て左側の資産が増えたのであれば、右側の金額も増やしてバランスをとる必要があります。
利益が出た場合は、内部的にお金が入ってきて純資産の部分も同時に増えたとみなし、**利益剰余金**という科目で純資産の増加を表現します。

<table class="local-center">
  <tr class="local-balancedHeight">
    <td rowspan="2" class="local-asset local-balancedWidth">
      資産の部<br>(Assets)
      <div class="local-surplus">新しい資産</div>
    </td>
    <td class="local-liability local-balancedWidth">負債の部<br>(Liabilities)</td>
  </tr>
  <tr class="local-balancedHeight">
    <td class="local-equity local-balancedWidth">
        純資産の部<br>(Equity)
        <div class="local-surplus">利益剰余金<br>(Surplus)</div>
    </td>
  </tr>
</table>

逆に、経営がうまくいかず、損失が出ている場合は資産が減っていきます。
この場合は、利益剰余金をマイナスで記入（表示上は △ で表現）することで純資産の減少を表現します。
いわゆる欠損金です。利益剰余金のマイナスが大きくなり、純資産の合計がマイナスになってしまうと、**債務超過**になり、資産を売り払っても負債を返しきれない状態になってしまいます。
資産は借金すればいくらでも増やせますが、利益剰余金がプラスでなければ、いつかは債務超過に陥ります。
財務の健全性を調べる場合は、利益剰余金がプラスであることは最初に見ておきたいポイントです。

利益剰余金の金額は、つまりは経営で儲かったお金なわけですから、損益計算書の方にも数値となって現れているはずです。
損益計算書の方では、**当期純利益**（あるいは**当期純損失**）という勘定項目が、儲かったお金、あるいは失ったお金として表現されます。
貸借対照表の方では利益剰余金という科目で表現されていますが、本質的には同じものを指しているというわけです。

