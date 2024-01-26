import requests, time
from tqdm import tqdm
import hashlib
from config import TOKEN, FINAL_URL
from IO import append_to_csv, update_download_list


HEADERS = {
    "Authorization": TOKEN
}


MESSAGE_END = ""  # If you want to end at a particular message
HEADERS = {
    "Authorization": TOKEN
}
def get_data(offset=0):
    r = requests.get(url=FINAL_URL+"&offset="+str(offset), headers=HEADERS)
    if r.status_code == 429:
        # print("Rate Limited")
        time.sleep(5)
        return get_data()
    elif r.status_code == 10004:
        print("10004 - Check your GUILD_ID")
        r.close()
        return None
    elif r.status_code == 50001:
        print("50001 - Check your CHANNEL/AUTHOR ID")
        r.close()
        return None
    elif r.status_code == 401:
        print("401 : Unauthorized Access - Check your TOKEN")
        r.close()
        return None
    else:
        data = r.json()
        # print("Data fetched")
        r.close()
        return data
    
def parse_data(data):
    if data is None:
        print("Error in fetching data")
        exit(1)
    entries = []
    for i in data['messages']:
        message_id = i[0]['id']
        author_id = i[0]['author']['id']
        author_username = i[0]['author']['username'].replace(',', '')
        author_global_name = i[0]['author']['global_name'].replace(',', '')

        if len(i[0]['attachments']) > 0:
            for attachment in i[0]['attachments']:
                attachment_id = attachment['id']
                attachment_url = attachment['url']
                attachment_filename = attachment['filename'].replace(',', '')
                attachment_size = attachment['size']
                attachment_proxy_url = attachment['proxy_url']
                attachment_height = attachment['height']
                attachment_width = attachment['width']
                attachment_content_type = attachment['content_type'].replace(',', '')
                entries.append([ hashlib.sha256((message_id + attachment_id + attachment_url).encode()).hexdigest(), message_id, author_id, author_username, author_global_name, attachment_id, attachment_url, attachment_filename, attachment_size, attachment_proxy_url, attachment_height, attachment_width, attachment_content_type])
        else:
            attachment_id = "NaN"
            attachment_url = "NaN"
            attachment_filename = "NaN"
            attachment_size = "NaN"
            attachment_proxy_url = "NaN"
            attachment_height = "NaN"
            attachment_width = "NaN"
            attachment_content_type = "NaN"
            entries.append([ hashlib.sha256((message_id + attachment_id + attachment_url).encode()).hexdigest(), message_id, author_id, author_username, author_global_name, attachment_id, attachment_url, attachment_filename, attachment_size, attachment_proxy_url, attachment_height, attachment_width, attachment_content_type])
    return entries 
        
    

def get_num_messages():
    data = get_data()
    return data['total_results']
    
num_messages = get_num_messages()
print("Total messages with the filters :", num_messages)
print("Fetching messages...")

for i in tqdm(range(int(num_messages/25)+1)):
    data = get_data(offset=i*25)
    rows = parse_data(data)
    append_to_csv(rows)
