from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression, RANSACRegressor
from sklearn.model_selection import GridSearchCV

linreg = LinearRegression()
ranfor = RandomForestRegressor()
ransac = RANSACRegressor()


def train_model(data_x, data_y, model=linreg):
    """
    Function to use to fit a model with a training dataset
    -------------
    Inputs
    -------------
    @params data_x pandas.DataFrame: dataset for training, in pandas dataframe format
    @params data_y pandas.Series: target data of the regressor, in pandas Series format
    @params model sklearn object: model to train, in sklearn model object format.
        Value can ONLY be one of the nexts variables : ransac, ranfor, linreg. Default = linreg

    -------------
    Return
    -------------
    model sklearn object : the fitted model
    """

    model = model
    if type(model) not in [type(LinearRegression()), type(RANSACRegressor()), type(RandomForestRegressor())]:
        raise TypeError("Model can only be instance of RANSACRegressor, RandomForestRegressor or LinearRegression")
    if isinstance(type(model), type(RandomForestRegressor())):
        param_grid = {"criterion": ["squared_error", "absolute_error", "friedman_mse"],
                      "max_depth": [None, 20, 100, 500]}
        gs_cv = GridSearchCV(estimator=model, param_grid=param_grid, scoring="r2", refit=True, verbose=1,
                             return_train_score=False)
        gs_cv.fit(data_x, data_y)
        model = gs_cv.best_estimator_
    else:
        model.fit(data_x, data_y)

    return model
