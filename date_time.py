import sys
from pytz import timezone
from datetime import datetime

if len(sys.argv)!=2:
    sys.exit('Chosoe one command from 1, 2 or 3')
elif int(sys.argv[1])==1:
    # date=date.today().strftime('%Y.%m.%d')
    date=datetime.now().strftime('%Y.%m.%d')
    print(date)
elif int(sys.argv[1])==2:
    date=datetime.now().strftime('%Y.%m.%d %H:%M:%S')
    print(date)
elif int(sys.argv[1])==3:
    tzone=timezone('Asia/Yerevan')
    date=datetime.now(tz=tzone).strftime('%a %b %d %Y %H:%M:%S %z')
    print(date)