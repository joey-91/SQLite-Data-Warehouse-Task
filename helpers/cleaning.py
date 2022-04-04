import pandas as pd

def clean_price(value):
    value = str(value)
    value = value.replace(',','')
    value = int(value)
    return value

def clean_address(value):
    value = str(value)
    value = value.lower()
    return value

def clean_phone_number(value):
    value = str(value)
    value = value.replace(' ','')
    return value

def clean_postcode(value):
    value = str(value)
    value = value.replace(' ','')
    value = value.lower()
    return value

def clean_names(value):
    value = str(value)
    value = value.replace(' ','')
    value = value.lower()
    return value

def clean_df(df: pd.DataFrame):
    """
    utility function to clean the following fields
    """
    df['UnitPrice'] = df['UnitPrice'].apply(lambda x: clean_price(x))
    df['TotalPrice'] = df['TotalPrice'].apply(lambda x: clean_price(x))
    df['ClientName'] = df['ClientName'].apply(lambda x: clean_names(x))
    df['DeliveryAddress'] = df['DeliveryAddress'].apply(lambda x: clean_address(x))
    df['DeliveryCity'] = df['DeliveryCity'].apply(lambda x: clean_address(x))
    df['DeliveryCountry'] = df['DeliveryCountry'].apply(lambda x: clean_address(x))
    df['DeliveryContactNumber'] = df['DeliveryContactNumber'].apply(lambda x: clean_phone_number(x))
    df['DeliveryPostcode'] = df['DeliveryPostcode'].apply(lambda x: clean_postcode(x))
    return df