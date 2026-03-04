import pandas as pd
from scipy.stats import norm

def two_proportion_z_test(p1, n1, p2, n2):
    # pooled proportion
    p_pool = (p1*n1 + p2*n2) / (n1 + n2)
    se = (p_pool * (1 - p_pool) * (1/n1 + 1/n2)) ** 0.5
    z = (p2 - p1) / se if se > 0 else 0
    p_value = 2 * (1 - norm.cdf(abs(z)))
    return z, p_value

def simulate_ab():
    # Simulated experiment: checkout redesign
    data = pd.DataFrame({
        "group": ["A", "B"],
        "users": [10000, 10000],
        "purchases": [1200, 1450]
    })
    data["conversion_rate"] = data["purchases"] / data["users"]

    p1 = data.loc[data.group=="A", "conversion_rate"].iloc[0]
    n1 = data.loc[data.group=="A", "users"].iloc[0]
    p2 = data.loc[data.group=="B", "conversion_rate"].iloc[0]
    n2 = data.loc[data.group=="B", "users"].iloc[0]

    lift = (p2 - p1) / p1
    z, p_value = two_proportion_z_test(p1, n1, p2, n2)

    summary = pd.DataFrame([{
        "metric": "purchase_conversion",
        "group_A_rate": p1,
        "group_B_rate": p2,
        "lift": lift,
        "z_score": z,
        "p_value": p_value,
        "decision": "SHIP B" if p_value < 0.05 and lift > 0 else "DO NOT SHIP"
    }])

    data.to_csv("experiments/ab_groups.csv", index=False)
    summary.to_csv("experiments/ab_results.csv", index=False)

    with open("reports/ab_test_summary.txt", "w") as f:
        f.write(summary.to_string(index=False))

    print("Saved experiments/ab_results.csv and reports/ab_test_summary.txt")

if __name__ == "__main__":
    simulate_ab()