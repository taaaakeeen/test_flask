import time
import sys
import argparse
from pathlib import Path
import os

FILE = Path(__file__).resolve()
# print(FILE)
ROOT = FILE.parents[0]
# print(ROOT)
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  
ROOT = Path(os.path.relpath(ROOT, Path.cwd())) 
# print(ROOT)

def main(opt):
    # print(opt)
    length = opt.length
    sleep = opt.sleep
    print("start")
    # print(1+"hoge")
    for i in range(length):
        print(i+1)
        time.sleep(sleep)
    print("end")

def parse_opt(known=False):
    # print(known)
    parser = argparse.ArgumentParser()
    parser.add_argument('--length', type=int, default=10)
    parser.add_argument('--sleep', type=int, default=1)

    opt = parser.parse_known_args()[0] if known else parser.parse_args()
    # print(opt)
    return opt

if __name__ == "__main__":
    opt = parse_opt()
    main(opt)