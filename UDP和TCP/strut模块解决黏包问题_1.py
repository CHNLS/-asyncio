import struct

# pack("i", a) i表示a为int类型
# 将一个数字转换成固定长度的bytes类型
result = struct.pack("i", 2048)
print(result)

# 将转换后的bytes类型，返回值为一个元组，元组第一个值是转换前的a
source_data = struct.unpack("i", result)
print(source_data)

# 取到数字a
print(source_data[0])
