import os


def get_env_variable(key):
    return os.getenv(key, "DefaultValue")  # Vulnerable to injection
