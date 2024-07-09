from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression, RANSACRegressor
from sklearn.model_selection import GridSearchCV
import joblib

linreg = LinearRegression()
ranfor = RandomForestRegressor()
ransac = RANSACRegressor()


def train_model(data_x, data_y, model="linreg"):
    """
    Function to use to fit a model with a training dataset
    -------------
    Inputs
    -------------
    @params data_x pandas.DataFrame: dataset for training, in pandas dataframe format
    @params data_y pandas.Series: target data of the regressor, in pandas Series format
    @params model string: model to train, in string format. linreg is for LinearRegression,
        ransac is for RANSAC, and ranfor is for RandomForestRegressor. Value can ONLY be one of
        the nexts variables : ransac, ranfor, linreg. Default = linreg

    -------------
    Return
    -------------
    model sklearn object : the fitted model
    """

    match model:
        case "linreg":
            model = linreg
        case "ransac":
            model = ransac
        case "ranfor":
            model = linreg
        case _:
            raise ValueError("You can only type 'ransac', 'linreg', or 'ranfor'.")

    if isinstance(type(model), type(RandomForestRegressor())):
        param_grid = {"criterion": ["squared_error", "absolute_error", "friedman_mse"],
                      "max_depth": [None, 20, 100, 500]}
        gs_cv = GridSearchCV(estimator=model, param_grid=param_grid, scoring="r2", refit=True, verbose=1,
                             return_train_score=False)
        gs_cv.fit(data_x, data_y)
        model = gs_cv.best_estimator_
        filename = 'model.sav'
        joblib.dump(model, filename)

    else:
        model.fit(data_x, data_y)
        filename = 'model.sav'
        joblib.dump(model, filename)

    return model
