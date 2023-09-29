import great_expectations as gx
context = gx.get_context()

from ruamel import yaml

import great_expectations as gx
from great_expectations.core.batch import BatchRequest, RuntimeBatchRequest

context = gx.get_context()

datasource_config = {
    "name": "my_postgres_datasource",
    "class_name": "Datasource",
    "execution_engine": {
        "class_name": "SqlAlchemyExecutionEngine",
        "connection_string": "postgresql+psycopg2://postgres:password@10.82.0.37:5432/postgres",
    },
    "data_connectors": {
        "default_runtime_data_connector_name": {
            "class_name": "RuntimeDataConnector",
            "batch_identifiers": ["default_identifier_name"],
        },
        "default_inferred_data_connector_name": {
            "class_name": "InferredAssetSqlDataConnector",
            "include_schema_name": True,
        },
    },
}

context.test_yaml_config(yaml.dump(datasource_config))

context.add_datasource(**datasource_config)
batch_request = RuntimeBatchRequest(
    datasource_name="my_postgres_datasource",
    data_connector_name="default_runtime_data_connector_name",
    data_asset_name="fct_current_weather",  # this can be anything that identifies this data
    runtime_parameters={"query": "SELECT * from rusina_test.fct_current_weather"},
    batch_identifiers={"default_identifier_name": "default_identifier"},
)
context.add_or_update_expectation_suite(expectation_suite_name="rusina_test_suite")
validator = context.get_validator(
    batch_request=batch_request, expectation_suite_name="rusina_test_suite"
)
validator.expect_column_values_to_not_be_null(column="hash_id")

validator.save_expectation_suite(discard_failed_expectations=False)


checkpoint = context.add_or_update_checkpoint(
    name="rusina_checkpoint",
    validations=[
        {
            "batch_request": batch_request,
            "expectation_suite_name": "rusina_test_suite",
        },
    ],
)