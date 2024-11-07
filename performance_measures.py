import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score, jaccard_score, cohen_kappa_score
import sklearn

def performance_measures(name, model, X_test, y_test, dataFrame):

    y_pred = model.predict(X = X_test)
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average = "weighted")
    recall = recall_score(y_test, y_pred, average = "weighted")
    precision = precision_score(y_test, y_pred, average = 'weighted')
    jaccard = jaccard_score(y_test, y_pred, average = 'weighted')
    kappa = cohen_kappa_score(y_test, y_pred)
    print("Accuracy :", accuracy)
    print("F1 :", f1)
    print("Recall :", recall)
    print("Precision :", precision)
    print("Jaccard :", jaccard)
    print("Kappa :", kappa)
    measures = {"Classifier Model":name, "Accuracy":accuracy, "F1-Score":f1,"Recall":recall, "Precision":precision, "Jaccard-Score":jaccard, "Kappa-Score":kappa}
    return measures