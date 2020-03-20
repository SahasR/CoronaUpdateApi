
import requests
from datetime import datetime

def get_corona():
    print("Fetching Corona Stats...")
    now = datetime.now()
    current_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    URL = 'http://hpb.health.gov.lk/api/get-current-statistical'
    page = requests.get(URL)
    json_object = page.json()
    new_cases = json_object["data"]["local_new_cases"]
    Tot = json_object["data"]["local_total_cases"]
    Rec = json_object["data"]["local_recovered"]
    global_new = json_object["data"]["global_new_cases"]
    ReplyString = 'Sri Lanka\nTotal No. Of Covid-19 Patients:' + str(Tot) + '\nNew Cases:' + str(new_cases) + '\nNo. Of Patients Recovered:' + str(Rec) + '\nNew Global Cases:' + str(global_new) +'\n' + current_time + '\n#LKA #SriLanka #Coronavirus #COVID2019 #COVID19\nFrom hpb.health.gov.lk'
    print(ReplyString)
    print(len(ReplyString))
    corona_prompt = input("Is the User pleased with the Reply String?(Y/N): ").lower()
    if corona_prompt == "y":
        print("Posting on @sahasbot...")
        api.update_status(ReplyString)

get_corona()
