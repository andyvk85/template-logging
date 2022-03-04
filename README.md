# Python Logging Template with Dynaconf

This template shows how to use the Python built-in logging lib correctly and how to use Dynaconf to load the configuration for
the root logger.

Now, it is possible to switch from default env to prd env, which will change some parts of the logging config:
``` dotenv
export ENV_FOR_DYNACONF="prd"
```
