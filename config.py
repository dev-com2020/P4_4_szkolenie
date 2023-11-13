class BaseConfig():
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False


class StagingConfig(BaseConfig):
    SECRET_KEY = '423vfddsx'