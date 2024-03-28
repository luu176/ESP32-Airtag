import base64
import struct
import random
import string
import subprocess
import os


def reverse_generate_mac_and_payload(addr_hex, payload_hex):
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
adv_key = reverse_generate_mac_and_payload(addr.lower(), payload.lower()).hex()
advertisement_key = base64.b64encode(bytes.fromhex(adv_key)).decode("ascii")

print('advertisement key:', advertisement_key)

def int_to_bytes(integer):
    return integer.to_bytes((integer.bit_length() + 7) // 8, byteorder='big')
def generate_random_string(length):
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

filename = generate_random_string(5)

keyfile = open(filename, 'wb')
keyfile.write(struct.pack("B", 1))


keyfile.write(base64.b64decode(advertisement_key))

subprocess.run(["pip", "install", "esptool"])

command = f"esptool write_flash 0x1000 bootloader.bin 0x8000 partitions.bin 0x10000 firmware.bin 0x110000 {filename}"

subprocess.run(command, shell=True)

print("enjoy your airtag :)")

os.remove(f"{filename}")
