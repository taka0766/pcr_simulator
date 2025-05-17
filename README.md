# PCR Simulator / PCRシミュレーター

A Python simulation to demonstrate the counterintuitive nature of PCR test results due to false positives and false negatives.  
偽陽性・偽陰性の影響により、PCR検査の結果が直感に反することを示すPythonシミュレーションです。

---

## 📌 Overview / 概要

This tool simulates how sensitivity, specificity, and infection rate affect the accuracy of PCR tests.  
感度・特異度・感染率の違いが、PCR検査の信頼性にどのように影響するかをシミュレートします。

You can:
- Observe the number of true/false positives and negatives
- Understand why "positive" doesn't always mean "infected"
- Visualize the result in a simple bar chart

できること：
- 真陽性・偽陽性・偽陰性・真陰性の人数を確認できます  
- 「陽性 ＝ 感染」とは限らないことが理解できます  
- 結果をグラフで視覚的に確認できます  

---

## 🧪 Example Output / 実行例

```bash
▼ Simulation Result ▼
Infection rate: 1.00%
Infected individuals: 91
True positive: 89
False positive: 112
False negative: 2
True negative: 9797
Positive Predictive Value (PPV): 44.28%
````

![Graph Output](example_output.png)

---

## ⚙️ Parameters / パラメータ

| Parameter         | Default | Description (EN)                                | 説明（日本語）           |
| ----------------- | ------- | ----------------------------------------------- | ----------------- |
| `population_size` | 10000   | Number of people simulated                      | シミュレーション対象の人数     |
| `sensitivity`     | 0.99    | Probability that infected person tests positive | 感染者を正しく陽性と判定する確率  |
| `specificity`     | 0.99    | Probability that healthy person tests negative  | 非感染者を正しく陰性と判定する確率 |
| `infection_rate`  | 0.01    | Proportion of population that is infected       | 母集団における感染者の割合     |

---

## ▶️ How to Run / 実行方法

1. Install `matplotlib` if needed:
   必要に応じて `matplotlib` をインストールします：

   ```bash
   pip install matplotlib
   ```

2. Run the script:
   スクリプトを実行します：

   ```bash
   python pcr_simulator.py
   ```

---

## 📊 Applications / 活用例

* Understanding Bayes' theorem
  ベイズの定理の理解
* Public health education
  公衆衛生教育
* Statistical reasoning and data visualization
  統計的思考とデータ可視化の教材として

---

## 📁 Directory Structure / ディレクトリ構成

```
pcr_simulator/
├── pcr_simulator.py        # Main simulation script / メインスクリプト
├── example_output.png      # Sample graph output / サンプル出力グラフ
└── README.md               # This file / 本ドキュメント
```

---

## 📝 License / ライセンス

MIT License

---

## 🙋 Author / 作者

Created by \taka0766.
このプログラムは \taka0766 によって作成されました。

If you find it helpful, feel free to fork or contribute!
もし役立ったら、ぜひフォークやコントリビュートしてください！

```
