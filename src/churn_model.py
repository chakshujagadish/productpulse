import pandas as pd
from pathlib import Path
from joblib import dump
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

MODEL_DIR = Path("models")
MODEL_DIR.mkdir(exist_ok=True)

FEATURES = [
    "total_events", "active_days", "sessions", "views", "carts", "purchases",
    "avg_price", "revenue", "lifecycle_days", "recency_days",
    "view_to_purchase_rate", "view_to_cart_rate", "cart_to_purchase_rate"
]

def load_data(path="reports/user_features.csv"):
    df = pd.read_csv(path)
    # Fill missing numeric values
    df[FEATURES] = df[FEATURES].fillna(0)
    df = df.dropna(subset=["churn"])
    return df

def train():
    df = load_data()
    X = df[FEATURES]
    y = df["churn"].astype(int)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Model 1: Logistic Regression 
    lr = Pipeline([
        ("scaler", StandardScaler(with_mean=False)),
        ("clf", LogisticRegression(max_iter=2000))
    ])
    lr.fit(X_train, y_train)
    lr_pred = lr.predict_proba(X_test)[:, 1]
    lr_auc = roc_auc_score(y_test, lr_pred)

    # Model 2: Random Forest 
    rf = RandomForestClassifier(
        n_estimators=200, random_state=42, class_weight="balanced", n_jobs=-1
    )
    rf.fit(X_train, y_train)
    rf_pred = rf.predict_proba(X_test)[:, 1]
    rf_auc = roc_auc_score(y_test, rf_pred)

    # Choose best
    best_model, best_name, best_auc = (rf, "random_forest", rf_auc) if rf_auc >= lr_auc else (lr, "log_reg", lr_auc)

    # Save model
    dump(best_model, MODEL_DIR / f"churn_model_{best_name}.joblib")

    # Save evaluation report
    best_labels = (rf_pred >= 0.5).astype(int) if best_name == "random_forest" else (lr_pred >= 0.5).astype(int)
    report = classification_report(y_test, best_labels)
    with open("reports/churn_model_report.txt", "w") as f:
        f.write(f"Chosen model: {best_name}\n")
        f.write(f"AUC: {best_auc:.4f}\n\n")
        f.write(report)

    # Feature importance (RF) or coefficients (LR)
    if best_name == "random_forest":
        importances = pd.Series(best_model.feature_importances_, index=FEATURES).sort_values(ascending=False)
        importances.to_csv("reports/churn_feature_importance.csv", header=["importance"])
    else:
        coefs = pd.Series(best_model.named_steps["clf"].coef_[0], index=FEATURES).sort_values(key=lambda s: s.abs(), ascending=False)
        coefs.to_csv("reports/churn_feature_coefficients.csv", header=["coef"])

    print(f"Saved model + reports. Best={best_name}, AUC={best_auc:.4f}")

if __name__ == "__main__":
    train()