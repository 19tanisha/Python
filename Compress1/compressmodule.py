import zlib , base64

def compress(inputfile,outputfile):
    data = open(inputfile,'r').read()
    data_bytes = bytes(data, 'utf-8')
    data_compress = base64.b64encode(zlib.compress(data_bytes))
    data_decode = data_compress.decode('utf-8')
    compressed_file = open(outputfile,'w')
    compressed_file.write(data_decode)

compress('demo.txt', 'ot.txt')

def decompress(inputfile, outputfile):
    file_content = open(inputfile,'r').read()
    file_encode = file_content.encode('utf-8')
    file_decompress = zlib.decompress(base64.b64decode(file_encode))
    file_decode = file_decompress.decode('utf-8')
    file = open(outputfile,'w')
    file.write(file_decode)
    file.close()


