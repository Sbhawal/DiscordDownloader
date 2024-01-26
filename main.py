from src.download import download
from src.IO import update_download_list
from src.dataFetching import scrape

if __name__ == "__main__":
    print("Starting...")
    choice = input("1. Download\n2. Scrape Messages\n3. Update Download List\n4. Exit\n")
    if choice == "1":
        download()
    elif choice == "2":
        scrape()
    elif choice == "3":
        update_download_list(return_data=False)
    elif choice == "4":
        exit()
    else:
        print("Invalid Choice")
        exit()