import os
import secrets


def create_env_file():
    prompt = "> "
    if os.path.exists(".env"):
        print(".env Datei exisiter bereits.")
    else:
        
        print("POSTGRES_USER= ?")
        POSTGRES_USER = input(prompt)

        print("POSTGRES_PW= ?")
        POSTGRES_PW = input(prompt)

        print("DATABASE= ?")
        DATABASE = input(prompt)

        print("REDIS_PW= ?")
        REDIS_PW = input(prompt)


        SECRET_KEY = secrets.token_hex(32)
        JWT_SECRET = secrets.token_hex(32)

        env_list = [
            "POSTGRES_USER={}\n".format(POSTGRES_USER),
            "POSTGRES_PW={}\n".format(POSTGRES_PW),
            "DATABASE={}\n".format(DATABASE),
            "REDIS_PW={}\n".format(REDIS_PW),
            "SECRET_KEY={}\n".format(SECRET_KEY),
            "JWT_SECRET={}\n".format(JWT_SECRET)

        ]

        with open(os.path.join('.env'), 'a') as f:
            [ f.write(env_var) for env_var in env_list ]
            f.close()


def main():
    create_env_file()


if __name__ == '__main__':
    main()
