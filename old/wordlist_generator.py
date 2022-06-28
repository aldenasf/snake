import sys
import string
from itertools import product
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, "../")


def wordlist_generator():
    min_len = int(input("[>] Minimum length: "))
    max_len = int(input("[>] Maximum length: "))
    file_name = str(input("[>] Save wordlist as: "))
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    file = open(file_name, "a")
    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.submit(gen_word(min_len=min_len, max_len=max_len, chars=chars, file=file))


def gen_word(min_len, max_len, chars, file):
    counter = 0
    for i in range(min_len, max_len + 1):
        for x in product(chars, repeat=i):
            file.write("".join(x) + "\n")
            counter = + 1
            # Helper.progress_bar(Helper, counter, , "Generating passwords...", "", "[", "]", 2, 75)
            xlen = "".join(x)
            print(f"{i} | {xlen}")
