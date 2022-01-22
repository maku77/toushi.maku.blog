---
title: "Python で解析 - 日経平均のデータを取得する"
url: "/p/evsjk3x"
date: "2017-01-01"
tags: ["システムトレード"]
draft: true
---

{{< image w="500" src="python-fetch-n225.png" >}}

下記のサンプルで2005年から2016年の日経平均を FRED のデータベースから取得して、プロットしています。

{{< code lang="python" >}}
import pandas_datareader.data as web
import matplotlib.pyplot as plt

start="2005-01-01"
end="2016-12-31"
f = web.DataReader('NIKKEI225', 'fred', start, end)
f.plot(title='N225', grid=True)
plt.show()
{{< /code >}}

