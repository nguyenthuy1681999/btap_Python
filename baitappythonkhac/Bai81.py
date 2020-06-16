#Viết chương trình để nén và giải nén string ""hello world!hello world!hello world!hello world!".

#Gợi ý:

#Sử dụng zlib.compress() và zlib.decompress() để nén và giải nén string.
import zlib

s = "hello world!hello world!hello world!hello world!"
t = zlib.compress(s.encode("utf-8"))
print(t)
print(zlib.decompress(t))