from random import randint


def generate_share_key():
    code_list = [str(randint(0, 9)) for _ in range(6)]
    return "".join(code_list)

