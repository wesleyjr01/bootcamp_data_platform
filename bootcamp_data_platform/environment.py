from enum import Enum
import os


class Environment(Enum):
    PRODUCTION = "production"
    STAGING = "staging"
    DEVELOP = "develop"


active_environment = Environment[os.environ["ENVIRONMENT"]]