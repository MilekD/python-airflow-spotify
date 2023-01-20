import datetime
from pandas import DataFrame, Series


def check_if_valid_data(df:DataFrame) ->bool:
    if df.empty:
        print("No songs")
        return False
    #Primary Key Check
    if Series(df['played_at']).is_unique:
        pass
    else:
        raise Exception("primary key check is violated")

    if df.isnull().values.any():
        raise Exception('nulls in table')
    yesterday = datetime.datetime.now() - datetime.timedelta(1)
    yesterday=yesterday.replace(hour=0,minute=0,second=0,microsecond=0)

    # timestamps=df['timestamps'].tolist()
    # for timestamp in timestamps:
    #     if datetime.datetime.strptime(timestamp,"%Y-%m-%d") < yesterday:
    #         raise Exception("At least one song doesn't come from within the last 24 hours")
    return True

