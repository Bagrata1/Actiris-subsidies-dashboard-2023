import pandas as pd
import requests
import io
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):

    # List of URLs to the Excel files
    urls = [
        "https://backend.datastore.brussels/rest/metadata/3a9a6fc0-375d-4bca-aa64-3e226520f557/resource/8f1d69c6-0393-4a65-982c-5660fd6c0f01/download/0239843188_S_2021.xlsx",
        "https://backend.datastore.brussels/rest/metadata/3a9a6fc0-375d-4bca-aa64-3e226520f557/resource/18673523-7c83-4933-a6bf-79c6001fbeb4/download/0239843188_S_2022.xlsx",
        "https://backend.datastore.brussels/rest/metadata/3a9a6fc0-375d-4bca-aa64-3e226520f557/resource/487fa7c2-9d61-42ad-95b3-3a89a3a1ad3c/download/0239843188_S_2023.xlsx"
    ]

    # Define the data types for the columns
    dtypes = {
        'ID_BCE_ORG': str,
        'NAME_ORG1_FR': str,
        'NAME_ORG1_NL': str,
        'NAME_ORG2_FR': str,
        'NAME_ORG2_NL': str,
        'ID_ORG3': str,
        'NAME_ORG3_FR': str,
        'NAME_ORG3_NL': str,
        'ID_AB': str,
        'DESC_AB_FR': str,
        'DESC_AB_NL': str,
        'ACC_ID_FUNCTION': str,
        'ACC_DESC_FUNCTION_FR': str,
        'ACC_DESC_FUNCTION_NL': str,
        'ACC_ID_ECONOMIC': str,
        'ACC_DESC_ECONOMIC_FR': str,
        'ACC_DESC_ECONOMIC_NL': str,
        'ID_ENG': str,
        'NAME_ENG': str,
        'AMOUNT_ENG': float,
        'CURRENCY_ENG': str,
        'ID_LIQ': str,
        'NAME_LIQ': str,
        'AMOUNT_LIQ': float,
        'DEVCOD': str,
        'ID_BCE_RECIPIENT': str,
        'ID_RECIPIENT': str,
        'NAME_RECIPIENT': str,
        'ADDRESS_RECIPIENT': str,
        'CP_RECIPIENT': str,
        'COMMUNE_RECIPIENT': str,
        'CC_RECIPIENT': str,
        'BUDEXE': str 
    }

    # Columns that should be parsed as dates
    parse_dates = ['DATE_ENG', 'DATE_LIQ']

    # Read each Excel file and concatenate them into a single DataFrame
    data_frames = []
    for url in urls:
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Failed to download file from {url}")
        excel_file = io.BytesIO(response.content)
        df = pd.read_excel(excel_file, dtype=dtypes, parse_dates=parse_dates)
        data_frames.append(df)

    data = pd.concat(data_frames, ignore_index=True)
    print(f'Shape of the data: {data.shape}')

    return data


@test
def test_output(output, *args) -> None:

    assert output is not None, 'The output is undefined'
    assert not output.empty, 'The output DataFrame is empty'
    # Add more tests as needed to verify the data
    # For example, check columns
    expected_columns = [
        'ID_BCE_ORG', 'NAME_ORG1_FR', 'NAME_ORG1_NL', 'NAME_ORG2_FR', 'NAME_ORG2_NL', 
        'ID_ORG3', 'NAME_ORG3_FR', 'NAME_ORG3_NL', 'ID_AB', 'DESC_AB_FR', 'DESC_AB_NL', 
        'ACC_ID_FUNCTION', 'ACC_DESC_FUNCTION_FR', 'ACC_DESC_FUNCTION_NL', 'ACC_ID_ECONOMIC', 
        'ACC_DESC_ECONOMIC_FR', 'ACC_DESC_ECONOMIC_NL', 'ID_ENG', 'NAME_ENG', 'DATE_ENG', 
        'AMOUNT_ENG', 'CURRENCY_ENG', 'ID_LIQ', 'NAME_LIQ', 'DATE_LIQ', 'AMOUNT_LIQ', 
        'DEVCOD', 'ID_BCE_RECIPIENT', 'ID_RECIPIENT', 'NAME_RECIPIENT', 'ADDRESS_RECIPIENT', 
        'CP_RECIPIENT', 'COMMUNE_RECIPIENT', 'CC_RECIPIENT', 'BUDEXE'
    ]
    assert all(column in output.columns for column in expected_columns), "Some expected columns are missing"
