from aws_cdk import core as cdk
from bootcamp_data_platform.data_lake.stack import DataLakeStack
from bootcamp_data_platform.common_stack import CommonStack

app = cdk.App()
data_lake = DataLakeStack(app)
common_stack = CommonStack(app)

app.synth()
