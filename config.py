from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix='DYNACONF',
    settings_files=[
        'configs/logging.toml',
    ],
    environments=['dev', 'tst', 'prd'],
)
