from datetime import datetime

def time_delta(t1, t2):
    td1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    td2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    return int(abs((td1 - td2).total_seconds()))
    


if __name__ == '__main__':
    print(time_delta(
        "Fri 11 Feb 2078 00:05:21 +0400", 
        "Mon 29 Dec 2064 03:33:48 -1100"))