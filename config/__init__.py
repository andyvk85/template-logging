from dynaconf import Dynaconf

settings = Dynaconf(
    settings_files=['logging.toml'],
)
