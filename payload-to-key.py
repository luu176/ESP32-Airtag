import base64


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
