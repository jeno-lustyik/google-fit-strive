from model_fitting import model_fitting
from data_splitting import data_splitting
from data_cleaning import data_cleaning

path = 'dataset_halfSecondWindow.csv'
data = data_cleaning(path)
x_train, x_test, x_val, y_train, y_test, y_val = data_splitting(data)
results, params = model_fitting(x_train, x_test, x_val, y_train, y_test, y_val)


print(results)
