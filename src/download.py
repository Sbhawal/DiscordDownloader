import os, threading
import requests
from tqdm import tqdm
import time
from src.IO import download_history_id_set, download_history_url_set, save_history, update_download_list
from src.config import filterByAuthor, STREAM

download_folder = r'.\downloads'


def download_file(url, filename, author):
    try:
        if url in download_history_url_set:
            return
        response = requests.get(url, stream=STREAM)
        if filterByAuthor == "TRUE":
            if os.path.exists(os.path.join(download_folder, author)):
                pass
            else:
                os.mkdir(os.path.join(download_folder, author))
            filename = os.path.join(download_folder, author, filename)
        else:
            filename = os.path.join(download_folder, filename)
        if os.path.exists(filename):
            try:
                os.remove(filename)
            except:
                pass
        if STREAM == "TRUE":
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
        else:
            with open(filename, 'wb') as f:
                f.write(response.content)
        
        download_history_url_set.add(url)
    except Exception as e:
        pass


def multi_download(download_list):
    global COUNT
    COUNT = 0
    threads = []
    download_list = {key: value for key, value in download_list.items() if key not in download_history_id_set}

    for id in tqdm(download_list):
        if id in download_history_id_set:
            continue
        if COUNT % 50 == 0 and COUNT != 0:
            save_history()
            time.sleep(5)
        if COUNT % 200 == 0 and COUNT != 0:
            time.sleep(60)
        if COUNT > 2000:
            print("2000 downloads completed, sleeping for 5 min")
            time.sleep(300)
            exit()
        COUNT += 1
        thread = threading.Thread(target=download_file, args=(download_list[id]['attachment_url'], download_list[id]['attachment_filename'], download_list[id]['author_global_name']))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()





def download():
    download_list = update_download_list()
    download_list = download_list.set_index('hash_id')[['attachment_url', 'attachment_filename', 'author_global_name']].to_dict(orient='index')
    multi_download(download_list)
    save_history()