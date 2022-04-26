from environs import Env

env = Env()
env.read_env()


POLY_API = env.str('POLY_API')