import pandas as pd
from sklearn.preprocessing import StandardScaler
import time
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV


def model_fitting(x_train, x_test, x_val, y_train, y_test, y_val):
    scaler = StandardScaler()
    X_train = scaler.fit_transform(x_train)
    X_test = scaler.transform(x_test)
    X_val = scaler.transform(x_val)

    classifiers = {
        "Decision Tree": DecisionTreeClassifier(),
        "SVM": SVC(),
        "Random Forest": RandomForestClassifier()}

    results = pd.DataFrame({'Model': [], 'MSE': [], 'MAE': [], " % error": [], 'Time': []})

    for model_name, model in classifiers.items():
        start_time = time.time()
        model.fit(X_train, y_train)
        total_time = time.time() - start_time

        pred = model.predict(X_test)

        results = results.append({"Model": model_name,
                                  "MSE": metrics.mean_squared_error(y_test, pred),
                                  "MAE": metrics.mean_absolute_error(y_test, pred),
                                  "Accuracy Score": model.score(x_test, y_test),
                                  "Time": total_time},
                                 ignore_index=True)

    results_ord = results.sort_values(by=['MSE'], ascending=True, ignore_index=True)

    params_svm = {'C': [1,10,20], 'kernel': ['rbf', 'linear']}
    grid_svm = RandomizedSearchCV(SVC(gamma='auto'), params_svm, cv=5, return_train_score=False, n_iter=4)
    grid_svm.fit(X_train, y_train)
    grid_svm.best_params_
    return grid_svm.best_params_
