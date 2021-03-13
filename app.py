from aws_cdk import core as cdk
from bootcamp_data_platform.data_lake.stack import DataLakeStack

app = cdk.App()
data_lake = DataLakeStack(app)

app.synth()
