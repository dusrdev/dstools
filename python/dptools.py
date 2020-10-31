import urllib.request
import re
import time
from collections import OrderedDict
import concurrent.futures
import multiprocessing
import hashlib
import base64
from Cryptodome import Random
from Cryptodome.Cipher import AES
from Cryptodome.Util import Padding
import ssl
import math
from colorama import init, Fore, Back, Style
import os
import urllib3
import http.client as httplib
import itertools as it

urllib3.disable_warnings()
http = urllib3.PoolManager()

class Native:
    def __init__(self):
        init()

    @staticmethod #* return the number of cpu cores/threads of current pc
    def cpuCores(): return multiprocessing.cpu_count()

    @staticmethod #* replace spaces in a string with custom space characters
    def search_query(text: str, space_characters: str):
        return text.replace(" ", space_characters, -1)

    @staticmethod  #* green text
    def green(obj):
        return Fore.GREEN + str(obj) + Fore.RESET

    @staticmethod #* black text with green background
    def reverse_green(obj):
        return Back.GREEN + Fore.BLACK + str(obj) + Fore.RESET + Back.RESET

    @staticmethod  #* cyan text
    def cyan(obj):
        return Fore.CYAN + str(obj) + Fore.RESET

    @staticmethod  #* Kills current application
    def closeProgram():
        os._exit(0)

    @staticmethod #* Checks if internet connection is available (To avoid database corruption)
    def checkForInternetConnection(url="www.google.com", timeout=5):
        conn = httplib.HTTPConnection(url, timeout=timeout)
        try:
            conn.request("HEAD", "/")
            conn.close()
            return True
        except:
            return False

    @staticmethod #* gets html using urllib3 (very fast)
    def get_html(url: str):
        r = http.request("GET", url)
        return r.data
    
    @staticmethod #* password longer than 7 characters including lower, upper, digits, and special characters.
    def validate_password(psw: str):
        if (len(psw) > 7 and
            re.search(r"[a-z]", psw)and
            re.search(r"[A-Z]", psw)and
            re.search(r"\d", psw)and
                re.search(r"[!@$&]", psw)):
            return True
        return False

    @staticmethod #* returns the string size in bytes
    def byte_to_size(size_in_bytes):
        size_in_bytes = float(size_in_bytes)
        if size_in_bytes >= math.pow(1024, 4):
            size_in_bytes /= math.pow(1024, 4)
            return f'{size_in_bytes:.3f} TB'
        elif size_in_bytes >= math.pow(1024, 3):
            size_in_bytes /= math.pow(1024, 3)
            return f'{size_in_bytes:.3f} GB'
        elif size_in_bytes >= math.pow(1024, 2):
            size_in_bytes /= math.pow(1024, 2)
            return f'{size_in_bytes:.3f} MB'
        elif size_in_bytes >= 1024:
            size_in_bytes /= 1024
            return f'{size_in_bytes:.3f} KB'
        return f'{size_in_bytes:.3f} BT'

    @staticmethod  #* encrypts text
    def encrypt(text: str):
        return AESCipher().encrypt(text)

    @staticmethod #* decrypts text
    def decrypt(text: str):
        return AESCipher().decrypt(text)

class Mathematics:
    @staticmethod #* Returns factorial of n
    def factorial(n: int):
        if n <= 0:
            return 0
        elif n == 1 or n == 2:
            return n
        return n * Mathematics.factorial(n - 1)
    
    @staticmethod #* Returns the n-th fib number
    def fibonacci(n: int): return n if n < 2 else Mathematics.fibonacci(n - 1) + Mathematics.fibonacci(n - 2)
    
    @staticmethod #* Checks if n is even
    def isEven(n): return n % 2 == 0

    @staticmethod #* Checks if n is prime
    def isPrime(n):
        n = float(n)
        if n == 1:
            return False
        elif n == 2:
            return True
        for i in range(2, math.ceil(math.sqrt(n))):
            if n % i == 0:
                return False
        return True

    @staticmethod #* Returns the GCD of a and b
    def gcd(a: int, b: int): return a if b == 0 else Mathematics.gcd(b, a % b)
    
    @staticmethod #* Calculates projectile drop over distance using distance and velocity
    def calculateProjectileDrop(distance: float, velocity: float): return 4.9 * math.pow(distance / velocity, 2)

    @staticmethod  #* Returns x1, x2 answers of a quadratic equation
    def quadratic(a, b, c):
        des = math.sqrt(math.pow(b, 2) - 4 * a * c)
        x1 = (-b + des) / (2 * a)
        x2 = (-b - des) / (2 * a)
        return x1, x2

class Collections:
    @staticmethod #* Merge sort implementation
    def mergeSort(lst):
        if len(lst)>1:
            mid = len(lst)//2
            lefthalf = lst[:mid]
            righthalf = lst[mid:]
        Collections.mergeSort(lefthalf)
        Collections.mergeSort(righthalf)
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                lst[k]=lefthalf[i]
                i=i+1
            else:
                lst[k]=righthalf[j]
                j=j+1
            k=k+1
        while i < len(lefthalf):
            lst[k]=lefthalf[i]
            i=i+1
            k=k+1
        while j < len(righthalf):
            lst[k]=righthalf[j]
            j=j+1
            k=k+1

    @staticmethod #* Returns the last object of many different types
    def getLast(data):
        if type(data) == 'list' or type(data) == 'str':
            return data[-1]
        elif type(data) == 'int':
            return data
        elif type(data) == 'dict':
            return {list(data.keys())[-1]: list(data.values())[-1]}
        return 'Unsupported'

    @staticmethod #* Removes objects from dict
    def removeFromDict(d: dict, value):
	    return {x: y for x, y in d.items() if y != value}

    @staticmethod #* Returns the added values between two dicts
    def dictAdded(new_dict: dict, old_dict: dict):
	    new_values = set(new_dict.values()) if new_dict.values() else []
	    old_values = set(old_dict.values()) if old_dict.values() else []
	    return new_values - old_values

    @staticmethod #* Returns a nested dict containing updates between two nested dicts
    def nestedDictUpdates(old_dict: dict, new_dict: dict):
        updates = {}
        for out_key, out_value in new_dict.items():
            part = {}
            if out_key in list(old_dict.keys()):
                newkeys = set(out_value.keys())
                oldkeys = set(old_dict.get(out_key).keys())
                dif = newkeys - oldkeys
                if dif:
                    part = {k: out_value.get(k) for k in list(dif)[::-1]}
                else:
                    part = {'No': 'Updates'}
            else:
                part = {k: v for k, v in zip(list(out_value.keys())[::-1], list(out_value.values())[::-1])}
            updates[out_key] = part
        return updates

    @staticmethod  #* Adds new search results to old results
    def nestedDictCollective(old: dict, new: dict):
        collective = {}
        for k, v in new.items():
            collective[k] = dict(old.get(k)) if k in old.keys() else {}
            if (v != {"No": "Updates"} and v != {"Not": "Found"}):
                collective[k].update(v)
        return Collections.sortedNestedDict(collective)

    @staticmethod #* Sorts a dict using the int value of the key instead of the string
    def sortedDict(d):
        if type(d) == dict or type(d) == OrderedDict:
            keys = sorted(d.keys(), reverse=True)
            n = OrderedDict()
            for k in keys:
                n[k] = d.get(k)
            return n
        else:
            return d

    @staticmethod  #* Sorts a nested dict
    def sortedNestedDict(d):
        if type(d) == dict or type(d) == OrderedDict:
            for k in d.keys():
                d[k] = Collections.sortedDict(d.get(k))
            return OrderedDict(d)
        else:
            return d

    @staticmethod #* merges dictionaries
    def merge_dicts(dictionary_array):
        result = {}
        for dictionary in dictionary_array:
            result.update(dict(dictionary))
        return OrderedDict(result)

    @staticmethod  #* Regular dict last n
    def dictLastN(d: dict, n: int):
        return dict(zip(list(d.keys())[:n], list(d.values())[:n])) if len(d) > n else d

    @staticmethod #* Returns a nested dict with every dict containing the last n values
    def nestedDictLastN(d: dict, n: int):
        return dict(OrderedDict({k: Collections.dictLastN(v, n) for k, v in d.items()}))

    @staticmethod #* Returns the combined length of every dict in the nested dict
    def nestedDictLen(d: dict):
	    return sum([len(v) for v in d.values() if v != {"No":"Updates"}])

    @staticmethod #* util to present dicts (Including nested dicts)
    def printNestedDict(data: dict):
        NestedDictionary(data).print()

    @staticmethod  #* prints regular dictionaries
    def printDict(data: dict):
        n = Native()
        for k, v in data.items():
            print(f"{n.green(k)}: {v}")

    @staticmethod  #* alphabetically prints list using n sized groups per line
    def printList(ls: list, n: int = 5):
        nt = Native()
        tbl = {k: list(g) for k, g in it.groupby(ls, lambda x: x[0][0])}
        for key in tbl.keys():
            print(nt.reverse_green(f"{key}:"))
            groups = [tbl[key][i * n : (i + 1) * n] for i in range((len(tbl[key]) + n - 1) // n)]
            for group in groups:
                print(*group, sep=nt.green(" | "))

    @staticmethod #* Returns a dictionary where all convertable keys were converted to int
    def intifyDictKeys(d: dict):
        return {int(k) if str(k).isdigit() else k: v for k, v in d.items()}

    @staticmethod #* Returns a nested dictionary where all convertable keys were converted to int
    def intifyNestedDictKeys(d: dict):
        d = {k: Collections.intifyDictKeys(v) for k, v in d.items()}
        return Collections.intifyDictKeys(d)

    @staticmethod  #* Encrypts a list
    def encryptList(ls):
        encrypter = AESCipher()
        return [encrypter.encrypt(l) for l in ls] 

    @staticmethod #* Encrypts a dict
    def encryptInner(data):
        encrypter = AESCipher()
        e = lambda e: encrypter.encrypt(e)
        if type(data) == dict:
            return {e(str(k)): e(v) for k, v in data.items()}
        else:
            return data

    @staticmethod #* Encrypts a nested dict
    def encryptNestedDict(obj: dict):
        encrypter = AESCipher()
        e = lambda e: encrypter.encrypt(e)
        encrypted = {}
        with concurrent.futures.ThreadPoolExecutor() as executor:
            for outer_key in obj.keys():
                type_of_data = type(obj.get(outer_key))
                if (type_of_data == 'dict'):
                    encrypted[e(outer_key)] = executor.submit(
                        Collections.encryptInner, obj.get(outer_key))
                elif type_of_data == 'list':
                    encrypted[e(outer_key)] = executor.submit(Collections.encryptList, obj.get(outer_key))
                else:
                    encrypted[e(outer_key)] = executor.submit(lambda l: l, obj.get(outer_key))
            concurrent.futures.as_completed(encrypted.values())
            encrypted = {k: v.result() for k, v in encrypted.items()}
        return encrypted

    @staticmethod  #* Decrypts a list
    def decryptList(ls):
        decrypter = AESCipher()
        return [decrypter.decrypt(l) for l in ls]

    @staticmethod #* Decrypts a dict
    def decryptInner(data):
        decrypter = AESCipher()
        d = lambda d: decrypter.decrypt(d)
        if type(data) == dict:
            return {int(d(k)) if str(d(k)).isdigit() else d(k): d(v) for k, v in data.items()}
        else:
            return data

    @staticmethod #* Decrypts a nested dict
    def decryptNestedDict(data: dict):
         decrypter = AESCipher()
         d = lambda d: decrypter.decrypt(d)
         decrypted = {}
         with concurrent.futures.ThreadPoolExecutor() as executor:
             for outer_key in data.keys():
                 type_of_data = type(data.get(outer_key))
                 if (type_of_data == 'dict'):
                    decrypted[d(outer_key)] = executor.submit(
                        Collections.decryptInner, data.get(outer_key))
                 elif (type_of_data == 'list'):
                     decrypted[d(outer_key)] = executor.submit(
                        Collections.decryptList, data.get(outer_key))
                 else:
                    decrypted[d(outer_key)] = executor.submit(lambda l: l, data.get(outer_key))
             concurrent.futures.as_completed(decrypted.values())
             decrypted = {k: v.result() for k, v in decrypted.items()}
         return decrypted

#* proprietary aes cipher class
class AESCipher():
    def __init__(self):
        self.bs = 16
        self.key = hashlib.sha256("12NKYmWL1dIRCb3g".encode('utf-8')).digest()

    def encrypt(self, raw):
        raw = self.pad(raw)
        iv = b"ODqoi2r3VkcS2jo1"
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw)).decode('utf8')

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self.unpad(cipher.decrypt(enc[16:])).decode('utf8')

    def pad(self, s):
        return Padding.pad(s.encode('utf8'), self.bs)

    def unpad(self, s):
        return Padding.unpad(s, self.bs)

class Timer:
    def Start(self):
        self.start = time.time()

    #* combines end timer with a string that displays the timer result
    def End(self, message: str, drop_before=False, drop_after=False):
        self.end = time.time()
        n = Native()
        timestring = f"{self.end - self.start:.2f}"
        self.time_message = f'{message}: {n.green(timestring)}s'
        if drop_before:
            self.time_message = "\n" + self.time_message
        if drop_after:
            self.time_message += "\n"
        return self.time_message

class NestedDictionary(object):
    def __init__(self,value):
        self.value = value

    #* prints the nested dictionary in a formatted way
    def print(self, depth = 0):
        inDepth = 5
        spacer="                    "
        if type(self.value)==type(dict()) or type(self.value)==type(OrderedDict()):
            for kk, vv in self.value.items():
                if (type(vv)==type(dict()) or type(vv)==type(OrderedDict())):
                    print(f'{Fore.LIGHTGREEN_EX}{spacer[:depth]} {kk}{Style.RESET_ALL}:')
                    vvv=(NestedDictionary(vv))
                    depth += inDepth
                    vvv.print(depth)
                    depth -= inDepth
                else:
                    if (type(vv)==type(list())):
                        for i in vv:
                            vvv=(NestedDictionary(i))
                            depth += inDepth
                            vvv.print(depth)
                            depth -= inDepth
                    else:
                        print(f'{spacer[:depth]} {kk}: {vv}')
