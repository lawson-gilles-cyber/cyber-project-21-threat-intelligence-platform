# IOC Management

def load_iocs():

    iocs = []

    with open("data/ioc_feed.txt", "r") as file:
        for line in file:
            iocs.append(line.strip())

    return iocs
