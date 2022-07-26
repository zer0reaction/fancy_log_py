import datetime


def log(data):
    print('[' + str(datetime.datetime.now()) + ']: ' + data)


log('this is a test message for logging')
