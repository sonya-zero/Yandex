def reverse():
    file_read = open("input.dat", "rb")
    file_write = open("output.dat", "wb")
    r = file_read.read()
    rr = r[::-1]
    file_write.write(rr)
    file_read.close()
    file_write.close()