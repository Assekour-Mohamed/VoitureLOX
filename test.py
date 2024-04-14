import datetime
from datetime import datetime
end = datetime.strptime("2022-11-15","%Y-%m-%d").date() 
start = datetime.strptime("2022-11-11","%Y-%m-%d").date()
print((end - start).days)