import pandas as pd
from datetime import datetime

from read_csv import read_csv
from WebDriverAceess import WebDriverAcess
from UHK import UHK
from CUHK import CUHK
from CityU import CityU
from PolyU import PolyU
from HKBU import HKBU
from LingnanU import LingnanU


if __name__ == '__main__':
    #haperparamater
    keyword = []
    final_dict = {'University': [], 'Job Details': [], 'URL': []}
    #read csv
    csv = read_csv()

    for index in range(len(csv)):
        un_name = csv['UN_Name'][index]
        job_link = csv['Job_Links'][index]
        print('{} starts!'.format(un_name))

        try:
            driver = WebDriverAcess(job_link)
        except:
            print("{}'s url is broken!".format(un_name))
            continue

        if un_name == 'University of Hong Kong':
            final_dict = UHK(driver, final_dict)
            #pass
        elif un_name == 'The Chinese University of Hong Kong':
            final_dict = CUHK(driver, final_dict)
            #pass
        elif un_name == 'City University of Hong Kong':
            final_dict = CityU(driver, final_dict)
            #pass
        elif un_name == 'The Hong Kong Polytechnic University':
            final_dict = PolyU(driver, final_dict)
            #pass
        elif un_name == 'Lingnan University':
            final_dict = LingnanU(driver, final_dict)

        elif un_name == 'Hong Kong Baptist University':
            #waiting down!!
            pass
        elif un_name == 'Hong Kong University of Science and Technology':
            #waiting down!!
            pass

    final_df = pd.DataFrame(final_dict)
    

    #final_df.to_csv('job detail time: {}.csv'.format(datetime.now()), encoding='utf-8-sig')
    final_df.to_csv('{} job detail time.csv'.format(datetime.today().strftime('%Y-%m-%d')), encoding='utf-8-sig')

