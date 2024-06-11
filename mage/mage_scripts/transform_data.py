import pandas as pd
import requests
import io

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@transformer
def transform(data, *args, **kwargs):
    # Ensure DATE_ENG and DATE_LIQ are datetime formats
    data['DATE_ENG'] = pd.to_datetime(data['DATE_ENG'], errors='coerce')
    data['DATE_LIQ'] = pd.to_datetime(data['DATE_LIQ'], errors='coerce')

    # Columns to drop
    columns_to_drop = [
        'ID_BCE_ORG', 'NAME_ORG1_FR', 'NAME_ORG1_NL', 'NAME_ORG2_FR',
        'NAME_ORG2_NL', 'ID_ORG3', 'NAME_ORG3_FR', 'ID_AB', 'DEVCOD',
        'CC_RECIPIENT', 'DESC_AB_FR', 'ACC_ID_FUNCTION', 'ACC_DESC_FUNCTION_FR',
        'ACC_DESC_FUNCTION_NL', 'ACC_DESC_ECONOMIC_FR', 'ID_ENG', 'CURRENCY_ENG',
        'NAME_ENG', 'NAME_LIQ', 'ID_LIQ', 'ID_BCE_RECIPIENT', 'ID_RECIPIENT', 'NAME_ORG3_NL'
    ]

    # Drop specified columns
    data.drop(columns=columns_to_drop, inplace=True)

    return data

@test
def test_output(output, *args) -> None:
    assert output is not None, 'The output is undefined'

    # Ensure DATE_ENG and DATE_LIQ are datetime formats
    assert pd.api.types.is_datetime64_any_dtype(output['DATE_ENG']), 'DATE_ENG is not datetime format'
    assert pd.api.types.is_datetime64_any_dtype(output['DATE_LIQ']), 'DATE_LIQ is not datetime format'

    # Check that the specified columns have been dropped
    columns_to_drop = [
        'ID_BCE_ORG', 'NAME_ORG1_FR', 'NAME_ORG1_NL', 'NAME_ORG2_FR',
        'NAME_ORG2_NL', 'ID_ORG3', 'NAME_ORG3_FR', 'ID_AB', 'DEVCOD',
        'CC_RECIPIENT', 'DESC_AB_FR', 'ACC_ID_FUNCTION', 'ACC_DESC_FUNCTION_FR',
        'ACC_DESC_FUNCTION_NL', 'ACC_DESC_ECONOMIC_FR', 'ID_ENG', 'CURRENCY_ENG',
        'NAME_ENG', 'NAME_LIQ', 'ID_LIQ', 'ID_BCE_RECIPIENT', 'ID_RECIPIENT', 'NAME_ORG3_NL'
    ]
    for column in columns_to_drop:
        assert column not in output.columns, f"{column} was not dropped"

