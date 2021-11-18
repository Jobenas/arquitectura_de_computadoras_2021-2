import psutil

if __name__ == "__main__":
    res = psutil.disk_partitions()
    for item in res:
        print(item.device)

    usage = psutil.disk_usage("/")
    print(usage.percent)