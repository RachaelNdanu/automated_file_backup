import os
import shutil
import datetime
import schedule
import time


source_dir = r"C:\Users\Dev-RBQ\Desktop\important"
destination_dir = r"C:\Users\Dev-RBQ\Desktop\backups"



def copy_folder_to_directory(source , destination):
    today = datetime.date.today()
    destination_dir= os.path.join(destination , str(today))

    try:
        shutil.copytree(source , destination_dir)
        print(f"folder copied to :{destination_dir}")

    except FileExistsError:
        print(f"folder already exist in: {destination}")



#copy_folder_to_directory(source_dir, destination_dir)
schedule.every().day.at("13:30").do( lambda:copy_folder_to_directory(source_dir, destination_dir))

while True:
    schedule.run_pending()
    time.sleep(60)
