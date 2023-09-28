import great_expectations as gx
import psycopg2 
context = gx.get_context()

datasource=context.get_datasource("rusina_datasource")

#asset_name = "fct_current_weather"
#asset_table_name = "rusina_test.fct_current_weather"
#table_asset = datasource.add_table_asset(name=asset_name, table_name=asset_table_name)

#asset_query = "SELECT * from rusina_test.fct_current_weather"

#query_asset = datasource.add_query_asset(name=asset_name, query=asset_query)