import hashlib

code = 'chanchanhwan'

datas = code+'1'
ob_sha256 = hashlib.sha256(datas.encode())
hex_sha256 = ob_sha256.hexdigest()
print(hex_sha256)
buf = 1
while True:
    datas = code + str(buf)
    ob_sha256 = hashlib.sha256(datas.encode())
    hex_sha256 = ob_sha256.hexdigest()
    if hex_sha256[:5] == '01234':
        break
    buf += 1
print(hex_sha256)
print(buf)

