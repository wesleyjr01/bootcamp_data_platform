from aws_cdk import core as cdk
import databricks
from bootcamp_data_platform.data_lake.stack import DataLakeStack
from bootcamp_data_platform.common_stack import CommonStack
from bootcamp_data_platform.dms.stack import DmsStack
from bootcamp_data_platform.kinesis.stack import KinesisStack
from bootcamp_data_platform.glue_catalog.stack import GlueCatalogStack
from bootcamp_data_platform.athena.stack import AthenaStack
from bootcamp_data_platform.redshift.stack import RedshiftStack
from bootcamp_data_platform.databricks.stack import DatabricksStack

app = cdk.App()
data_lake = DataLakeStack(app)
common_stack = CommonStack(app)
# dms = DmsStack(
#     app, common_stack=common_stack, data_lake_raw_bucket=data_lake.data_lake_raw_bucket
# )
# kinesis = KinesisStack(app, data_lake_raw_bucket=data_lake.data_lake_raw_bucket)
glue_catalog = GlueCatalogStack(
    app,
    raw_data_lake_bucket=data_lake.data_lake_raw_bucket,
    processed_data_lake_bucket=data_lake.data_lake_processed_bucket,
)
athena = AthenaStack(app)
redshift = RedshiftStack(
    app,
    data_lake_raw=data_lake.data_lake_raw_bucket,
    data_lake_processed=data_lake.data_lake_processed_bucket,
    common_stack=common_stack,
)
databricks - DatabricksStack(app)
app.synth()
