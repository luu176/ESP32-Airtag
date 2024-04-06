import base64
import random
import string
import subprocess
import os

def gen(addr_hex, payload_hex):
    addr = bytearray.fromhex(addr_hex)
    key = bytearray(28)
    key[0:6] = addr[0:6]
    key[0] &= 0b00111111

    payload = bytearray.fromhex(payload_hex)
    key[6:28] = payload[7:29]
    key[0] |= (payload[29] << 6)

    return key

payload = input("enter payload: ").replace(" ", "")
addr = input("enter mac address: ").replace(" ", "").replace(":", "")
adv_key = bytes.fromhex(gen(addr.lower(), payload.lower()).hex())

print('advertisement key:', base64.b64encode(adv_key).decode("ascii"))

def randomness(length):
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

filename = f"{randomness(6)}.key"

with open(filename, "wb") as f:
    f.write(adv_key)

subprocess.run(["pip", "install", "esptool"])

command = f"esptool --baud 921600 write_flash 0x1000 bootloader.bin 0x8000 partitions.bin 0x10000 firmware.bin 0xe000 {filename}"

try:
    subprocess.run(command, shell=True)
    print("enjoy your airtag :)")
except Exception as e:
    print(e)

os.remove(f"{filename}")
