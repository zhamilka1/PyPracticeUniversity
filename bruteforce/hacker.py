import zipfile
from tqdm import tqdm
wordlist = "E:\rockyou2021"
zip_file = "dilettantish-internal-portal-0.1.zip"
n_words = len(list(open(wordlist, "rb")))
zip_file = zipfile.ZipFile(zip_file)
with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=n_words, unit="word"):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            continue
        else:
            print("[+] Password found:", word.decode().strip())
            exit(0)
print("[!] Password not found, try other wordlist.")