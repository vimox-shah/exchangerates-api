# main.py
from tasks import huey  # import our "huey" object
from tasks import update_rates  # import our task


if __name__ == '__main__':
    update_rates(True)
    print('Running job')