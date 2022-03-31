def data_splitting(df):
    df_train = df[(df["user"].isin([3, 0]))]
    df_test = df[(df["user"].isin([4, 1, 2, 10]))]
    df_val = df[(df["user"].isin([5, 6, 8, 9, 11, 12]))]

    x_train = df_train.drop(['user', 'target'], axis=1)
    y_train = df_train.target
    x_test = df_test.drop(['user', 'target'], axis=1)
    y_test = df_test.target
    x_val = df_val.drop(['user', 'target'], axis=1)
    y_val = df_val.target

    return x_train, x_test, x_val, y_train, y_test, y_val
