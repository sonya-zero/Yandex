import schedule


import datetime as dt


def Cu():
    time = dt.datetime.now()
    str(time) = time.split(":")
    k = int(time[0])
    print("Ку " * k)


schedule.every().minute.at(":00").do(Cu)
while True:
    schedule.run_pending()