# ------------------------------------------------------------
# 1. Import libraries
# ------------------------------------------------------------
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np

# ------------------------------------------------------------
# 2. Load dataset
# ------------------------------------------------------------
df = pd.read_csv("train.csv")

# Fjern rækker med manglende værdier
df = df.dropna(subset=["is_match"])

# Hvis nogle kolonner er tekst (fx race, gender), omkod dem til numeriske dummy-variable
df = pd.get_dummies(df, drop_first=True)

# ------------------------------------------------------------
# 3. Split features og target
# ------------------------------------------------------------
X = df.drop("is_match", axis=1)
y = df["is_match"]

# Først: 80 % train + val, 20 % test
X_train_full, X_test, y_train_full, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# Dernæst: 20 % af train bruges til validation
X_train, X_val, y_train, y_val = train_test_split(
    X_train_full, y_train_full, test_size=0.2, stratify=y_train_full, random_state=42
)

print(f"Train: {len(X_train)}, Validation: {len(X_val)}, Test: {len(X_test)}")

# ------------------------------------------------------------
# 4. Skalering
# ------------------------------------------------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled   = scaler.transform(X_val)
X_test_scaled  = scaler.transform(X_test)

# ------------------------------------------------------------
# 5. Logistisk regression
# ------------------------------------------------------------
model = LogisticRegression(
    solver="liblinear",        # robust til små datasæt
    random_state=42,
    max_iter=500
)
model.fit(X_train_scaled, y_train)

# ------------------------------------------------------------
# 6. Validation performance
# ------------------------------------------------------------
y_val_pred = model.predict(X_val_scaled)
print("\n--- Validation Performance ---")
print(confusion_matrix(y_val, y_val_pred))
print(classification_report(y_val, y_val_pred, digits=3))

# ------------------------------------------------------------
# 7. Test performance
# ------------------------------------------------------------
y_test_pred = model.predict(X_test_scaled)
print("\n--- Test Performance ---")
print(confusion_matrix(y_test, y_test_pred))
print(classification_report(y_test, y_test_pred, digits=3))

# ------------------------------------------------------------
# 8. Feature importance (koefficienter)
#
