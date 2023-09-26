import great_expectations as gx
context = gx.get_context()

#postgres_conn = ("postgresql+psycopg2://postgres:password@10.82.0.37:5432/postgres")
datasource_name = "rusina_datasource"
postgres_conn = ("postgresql+psycopg2://postgres:password@10.82.0.37:5432/postgres")

datasource = context.sources.add_postgres(name=datasource_name, connection_string=postgres_conn)

asset_name = "rusina_asset"
asset_table_name = "fct_current_weather"
table_asset = datasource.add_table_asset(name=asset_name, table_name=asset_table_name)

asset_query = "SELECT * from fct_current_weather"

query_asset = datasource.add_query_asset(name=asset_name, query=asset_query)