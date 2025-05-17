import random
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from typing import Dict, Any

# 日本語フォント設定（環境に合わせて切り替える）
# plt.rcParams['font.family'] = 'IPAexGothic'       # Linuxなど
# plt.rcParams['font.family'] = 'MS Gothic'         # Windows
# plt.rcParams['font.family'] = 'Noto Sans CJK JP'  # macOS など
plt.rcParams['font.family'] = 'Yu Gothic'           # Windows 10以降

plt.rcParams['axes.unicode_minus'] = False  # マイナス記号の文字化け対策

class PCRSimulation:
    def __init__(self, population_size: int = 10000, sensitivity: float = 0.99, specificity: float = 0.99) -> None:
        self.population_size = population_size
        self.sensitivity = sensitivity
        self.specificity = specificity

    def run(self, infection_rate: float) -> Dict[str, Any]:
        true_positive = 0
        false_positive = 0
        true_negative = 0
        false_negative = 0
        infected = 0

        for _ in range(self.population_size):
            is_infected = random.random() < infection_rate
            if is_infected:
                infected += 1
                if random.random() < self.sensitivity:
                    true_positive += 1
                else:
                    false_negative += 1
            else:
                if random.random() < (1 - self.specificity):
                    false_positive += 1
                else:
                    true_negative += 1

        total_positive = true_positive + false_positive
        predictive_value = true_positive / total_positive if total_positive > 0 else 0.0

        return {
            "感染率": infection_rate,
            "感染者数": infected,
            "真陽性": true_positive,
            "偽陽性": false_positive,
            "偽陰性": false_negative,
            "真陰性": true_negative,
            "陽性的中率": predictive_value
        }

    def display_result(self, result: Dict[str, Any]) -> None:
        # テキスト出力
        print("▼ シミュレーション結果 ▼")
        print(f"感染率: {result['感染率']:.2%}")
        print(f"感染者数: {result['感染者数']}")
        print(f"真陽性: {result['真陽性']}")
        print(f"偽陽性: {result['偽陽性']}")
        print(f"偽陰性: {result['偽陰性']}")
        print(f"真陰性: {result['真陰性']}")
        print(f"陽性的中率（PPV）: {result['陽性的中率']:.2%}")

        # グラフ出力
        labels = ['真陽性', '偽陽性', '偽陰性', '真陰性']
        values = [result['真陽性'], result['偽陽性'], result['偽陰性'], result['真陰性']]

        plt.figure(figsize=(8, 6))
        bars = plt.bar(labels, values, color=['green', 'red', 'orange', 'blue'])
        plt.title(f"検査結果の分類（感染率: {result['感染率']:.2%}）", fontsize=14)
        plt.ylabel("人数", fontsize=12)
        plt.grid(axis='y')
        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2.0, yval + 5, f'{yval}', ha='center', va='bottom')
        plt.tight_layout()
        plt.show()


# 実行例
if __name__ == "__main__":
    sim = PCRSimulation(population_size=10000, sensitivity=0.99, specificity=0.99)
    result = sim.run(infection_rate=0.01)
    sim.display_result(result)
