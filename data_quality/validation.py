import pandas as pd


def validate_airline(airline):
    if isinstance(airline, str) and airline.strip() != "":
        return (True, "")
    return (False, "Invalid airline")


def validate_source_destination(source, destination):
    if (
        isinstance(source, str)
        and source.strip() != ""
        and isinstance(destination, str)
        and destination.strip() != ""
        and source != destination
    ):
        return (True, "")
    return (False, "Invalid source or destination")


def validate_total_stops(total_stops):
    if isinstance(total_stops, int) and total_stops >= 0:
        return (True, "")
    return (False, "Invalid total stops")


def validate_price(price):
    if isinstance(price, int) and price > 0:
        return (True, "")
    return (False, "Invalid price")


def validate_date(date, month, year):
    try:
        pd.Timestamp(year, month, date)
        return (True, "")
    except ValueError:
        return (False, "Invalid date")


def validate_time(hour, minute):
    if (
        isinstance(hour, int)
        and 0 <= hour < 24
        and isinstance(minute, int)
        and 0 <= minute < 60
    ):
        return (True, "")
    return (False, "Invalid time")


def validate_duration(hours, minutes):
    if (
        isinstance(hours, int)
        and hours >= 0
        and isinstance(minutes, int)
        and 0 <= minutes < 60
    ):
        return (True, "")
    return (False, "Invalid duration")


def get_validation_errors(row):
    errors = []
    validations = [
        validate_airline(row["Airline"]),
        validate_source_destination(row["Source"], row["Destination"]),
        validate_total_stops(row["Total_Stops"]),
        validate_price(row["Price"]),
        validate_date(row["Date"], row["Month"], row["Year"]),
        validate_time(row["Dep_hours"], row["Dep_min"]),
        validate_time(row["Arrival_hours"], row["Arrival_min"]),
        validate_duration(row["Duration_hours"], row["Duration_min"]),
    ]
    for valid, error in validations:
        if not valid:
            errors.append(error)
    return errors


def validate_row(row):
    errors = get_validation_errors(row)
    return len(errors) == 0


def get_error_rows(df):
    error_rows = []
    for index, row in df.iterrows():
        errors = get_validation_errors(row)
        if errors:
            error_rows.append((index, row, errors))
    return error_rows


def validate_table(df):
    if df.shape[1] != 14:
        return False
    return df.apply(validate_row, axis=1).all()


def detect_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] < lower_bound) | (df[column] > upper_bound)]


def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]


def check_missing_values(df):
    return df.isnull().sum().sum() == 0


def check_duplicates(df):
    return df.duplicated().any()


def check_data_consistency(df):
    return (df["Dep_hours"] != df["Arrival_hours"]) | (
        df["Dep_min"] != df["Arrival_min"]
    )


def validate_data_quality(df):
    return (
        validate_table(df)
        and check_missing_values(df)
        and not check_duplicates(df)
        and check_data_consistency(df)
    )
