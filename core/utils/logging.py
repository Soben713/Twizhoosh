import settings


def log(text):
    print(text)


def debug(text):
    if settings.DEBUG:
        log(text)
