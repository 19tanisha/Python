import zlib,base64

data = open('demo.txt', 'r').read()
data_byte = bytes(data, 'utf-8')
data_compress = base64.b64encode(zlib.compress(data_byte))
decode_file = data_compress.decode('utf-8')
open('tanya.txt', 'w').write(decode_file)

decompress_data = zlib.decompress(base64.b64decode(decode_file))
print(decompress_data)
