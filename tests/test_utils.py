from data_pipeline.utils import add_stg_prefix

def test_add_stg_prefix():
    input_data = {
        "customers": "SELECT * FROM customers"
    }

    expected = {
        "stg_customers": "SELECT * FROM customers"
    }

    result = add_stg_prefix(input_data)

    assert result == expected