def local(infile, outfile):
    outfile.write(infile.read())
    infile.close()
    outfile.close()

def S3(client, infile, bucket, name):
    client.upload_fileobj(infile, bucket, name)