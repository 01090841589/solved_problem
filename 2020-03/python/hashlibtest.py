import hashlib

code = 'chanchanhwan'
ob_sha256 = hashlib.sha256(code.encode())
hex_sha256 = ob_sha256.hexdigest()
print(hex_sha256)