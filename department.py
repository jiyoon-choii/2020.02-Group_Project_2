import pandas as pd 
from pandas import DataFrame

department = pd.DataFrame({
    'Name' : ['NC백화점 부산대점', '롯데백화점 동래점', '롯데백화점 부산본점', '신세계백화점 센텀시티점', '롯데백화점 광복점', 'NC백화점 서면', 'NC백화점 해운대점', '롯데백화점 센텀시티점', '현대백화점 부산점', '쥬디스태화백화점', '롯데백화점에비뉴엘 부산본점', '동화백화점12' ],
    'addr' : ['부산 금정구', '부산 동래구', '부산 부산진구', '부산 해운대구', '부산광역시 중구', '부산광역시 부산진구', '부산광역시 해운대구', '부산광역시 해운대구', '부산광역시 동구', '부산광역시 부산진구', '부산광역시 부산진구', '부산광역시 중구' ]})

print(department)

department.to_csv('./csv/department.csv', index=True )