from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression, RANSACRegressor

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
    @params model sklearn object: model to train, in sklearn model object format

    -------------
    Return
    -------------
    model sklearn object : the fitted model
    """

    model = model
    if type(model) not in [type(LinearRegression()), type(RANSACRegressor()), type(RandomForestRegressor())]:
        raise TypeError("Model can only be instance of RANSACRegressor, RandomForestRegressor or LinearRegression")
    model.fit(data_x, data_y)

    return model
