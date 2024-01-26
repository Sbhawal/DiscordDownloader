import os, pickle
import pandas as pd
import numpy as np

main_data_file = r'./data/data.csv'
download_list = r'./data/download_list.csv'
archivedDatabase = r'./history/archivedDatabase.csv'
download_history_url = r'./history/download_urls.pkl'
download_history_id = r'./history/download_ids.pkl'

download_history_url_set = set()
download_history_id_set = set()

def read_pickle(pickle_file):
    with open(pickle_file, 'rb') as f:
        return pickle.load(f)
def write_pickle(pickle_file, data):
    with open(pickle_file, 'wb') as f:
        pickle.dump(data, f)

if not os.path.exists(download_history_url):
    download_history_url_set = write_pickle(download_history_url, download_history_url_set)
else:
    download_history_url_set = read_pickle(download_history_url)


if not os.path.exists(download_history_id):
    download_history_id_set = write_pickle(download_history_id, download_history_id_set)
else:
    download_history_id_set = read_pickle(download_history_id)



def check_file_exists():
    if not os.path.exists(main_data_file):
        with open(main_data_file, 'w', encoding='utf8') as f:
            f.write('hash_id,message_id,author_id,author_username,author_global_name,attachment_id,attachment_url,attachment_filename,attachment_size,attachment_proxy_url,attachment_height,attachment_width,attachment_content_type\n')
        
    if not os.path.exists(download_list):
        with open(download_list, 'w', encoding='utf8') as f:
            f.write('hash_id,attachment_url,attachment_filename\n')


def append_to_csv(rows=[], main_data_file=main_data_file):
    check_file_exists()
    for row in rows:
        line = ','.join([str(i) for i in row]) + '\n'
        with open(main_data_file, 'a', encoding='utf8') as f:
            f.write(line)

def clean_data(return_data=False):
    data = pd.read_csv(main_data_file)
    data = data.drop_duplicates(subset=['hash_id'])
    data = data.dropna(subset=['attachment_url'])
    if return_data:
        return data
    data.to_csv(main_data_file, index=False)

def update_download_list():
    data = clean_data(return_data=True)
    if os.path.exists(archivedDatabase):
        archivedDatabase_data = pd.read_csv(archivedDatabase)
        archivedDatabase_data = pd.concat([archivedDatabase_data, data])
        archivedDatabase_data = archivedDatabase_data.drop_duplicates(subset=['hash_id'])
        archivedDatabase_data.to_csv(archivedDatabase, index=False)
    else:
        os.rename(main_data_file, archivedDatabase)
    data = data[['hash_id', 'attachment_url', 'attachment_filename']]
    download_list_data = pd.read_csv(download_list)
    download_list_data = pd.concat([download_list_data, data])
    download_list_data = download_list_data.drop_duplicates(subset=['hash_id'])
    download_list_data.to_csv(download_list, index=False)
    os.remove(main_data_file)


