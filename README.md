## Welcome to our AML project repository for speed-dating match prediction!

This project applies supervised machine learning to predict whether a speed-dating interaction results in a mutual match. Using participant ratings and preferences, several classification models are trained, tuned, and evaluated under class imbalance.

Models implemented include Logistic Regression, Decision Tree, Random Forest, K-Nearest Neighbors, and a baseline DummyClassifier. Model selection is based primarily on F1-score, supported by precision, recall, ROC-AUC, and error analysis.

The project also includes a fairness sensitivity analysis that evaluates model performance under different feature inclusion scenarios for sensitive attributes such as gender, race, and religion.

This project was developed as part of the Applied Machine Learning course at can.merc.IT at CBS.