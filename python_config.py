import os


def get_variables_from_env():
    env_vars = {}
    with open(".env") as env:
        for variables in env:
            env_vars[variables.split('=')[0]] = variables.split('=')[1]
    return env_vars


def set_environment_variables():
    for key, value in get_variables_from_env().items():
        os.putenv(key, value)


if __name__ == "__main__":
    print(get_variables_from_env())
