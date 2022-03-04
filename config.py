from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix='DYNACONF',
    settings_files=[  # order matters!
        'configs/logging.toml',
    ],
    environments=[  # use layered environments
        'dev',
        'tst',
        'prd',
    ],
)
