import pandas as pd

def generate_recommendations(funnel_csv="reports/funnel_daily.csv"):
    df = pd.read_csv(funnel_csv)

    # Simple heuristic insights (PM-realistic)
    avg_rate = df["view_to_purchase_rate"].dropna().mean()

    # Find worst 7 days
    worst = df.dropna(subset=["view_to_purchase_rate"]).nsmallest(7, "view_to_purchase_rate")

    recs = []
    recs.append(f"Average View→Purchase conversion rate: {avg_rate:.2%}")

    for _, r in worst.iterrows():
        recs.append(
            f"[{r['event_date']}] Low conversion ({r['view_to_purchase_rate']:.2%}). "
            f"Investigate checkout friction, pricing, or product detail page clarity."
        )

    # If carters are high but purchases low → checkout issue
    df["cart_to_purchase_proxy"] = df["purchasers"] / (df["carters"].replace(0, pd.NA))
    cart_issue_days = df.dropna(subset=["cart_to_purchase_proxy"]).nsmallest(5, "cart_to_purchase_proxy")
    for _, r in cart_issue_days.iterrows():
        recs.append(
            f"[{r['event_date']}] Cart→Purchase weak. Recommend: "
            f"reduce checkout steps, add trust badges, clarify shipping/returns."
        )

    return recs

def run():
    recs = generate_recommendations()
    with open("reports/ai_recommendations.txt", "w") as f:
        f.write("\n".join(recs))
    print("Saved: reports/ai_recommendations.txt")

if __name__ == "__main__":
    run()