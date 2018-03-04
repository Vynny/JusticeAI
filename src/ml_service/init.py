import os
import time
import nltk
import requests
from sys import stdout
from threading import Thread
from util.constant import Path
from util.log import Log
import threading

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('perluniprops')

ADDRESS_INDEX = 0
FILE_SIZE_INDEX = 1

sem = threading.Semaphore()

binary_names_dict = {
    'classifier_labels': ['https://capstone.cyberjustice.ca/data/bin/classifier_labels.bin', 638],
    'additional_indemnity_money_regressor': ['https://capstone.cyberjustice.ca/data/bin/additional_indemnity_money_regressor.bin', 54384],
    'additional_indemnity_money_scaler': ['https://capstone.cyberjustice.ca/data/bin/additional_indemnity_money_scaler.bin', 1250],
    'multi_class_svm_model': ['https://capstone.cyberjustice.ca/data/bin/multi_class_svm_model.bin', 20180973],
    'tenant_pays_landlord_regressor': ['https://capstone.cyberjustice.ca/data/bin/tenant_pays_landlord_regressor.bin', 478584],
    'tenant_pays_landlord_scaler': ['https://capstone.cyberjustice.ca/data/bin/tenant_pays_landlord_scaler.bin', 1250],
    'similarity_case_numbers': ['https://capstone.cyberjustice.ca/data/bin/similarity_case_numbers.bin', 999347],
    'similarity_model': ['https://capstone.cyberjustice.ca/data/bin/similarity_model.bin', 31334058],
    'similarity_scaler': ['https://capstone.cyberjustice.ca/data/bin/similarity_scaler.bin', 1586]
}


def monitor_download(filename, filesize):
    sem.acquire()
    time.sleep(2)
    current_size = 0
    limit = filesize * 0.99
    while limit > current_size:
        current_size = os.stat(filename).st_size
        percentage = (current_size / filesize * 1.00) * 100
        percentage = float("{0:.2f}".format(percentage, 2))
        stdout.write("\r%s - Download percentage: %.2f%%" %
                     (filename, percentage))
        stdout.flush()
        time.sleep(3)
    Log.write("\n[END] Downloaded {} Binary".format(filename))
    sem.release()


for binary_name in binary_names_dict:
    # Checks if file exists before downloading
    rel_path = binary_name + '.bin'
    abs_file_path = os.path.join(Path.binary_directory, rel_path)

    if not os.path.exists(abs_file_path):
        Log.write("[START] Downloading {} binary".format(binary_name))
        thr = Thread(target=monitor_download, args=(abs_file_path, binary_names_dict[binary_name][FILE_SIZE_INDEX]))
        thr.start()

        response = requests.get(
            binary_names_dict[binary_name][ADDRESS_INDEX],
            auth=(
                os.environ['CJL_USER'],
                os.environ['CJL_PASS']),
            stream=True,
            verify=False)
        with open(abs_file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
    else:
        Log.write("{} binary file requirement already satisfied.".format(binary_name))
