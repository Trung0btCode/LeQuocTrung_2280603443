def left_rotate(value, shift):
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

def md5(message):
    # Khởi tạo các biến ban đầu
    a = 0x67452301
    b = 0xEFCDAB89
    c = 0x98BADCFE
    d = 0x10325476

    # Tiền xử lý chuỗi văn bản
    original_length = len(message)
    message = b'\x80'
    while len(message) % 64 != 56:
        message += b'\x00'
    message += original_length.to_bytes(8, 'little')

    # Chia chuỗi thành các block 512-bit
    words = [int.from_bytes(message[i:i+4], 'little') for i in range(0, len(message), 4)]

    a0, b0, c0, d0 = a, b, c, d

    # Vòng lặp chính của thuật toán MD5
    for i in range(64):
        if i < 16:
            f = (b & c) | ((~b) & d)
        elif i < 32:
            f = (d & b) | ((~d) & c)
        elif i < 48:
            f = b ^ c ^ d
        else:
            f = c ^ (b | (~d))
        
        temp = d
        d = c
        c = b
        b = b + left_rotate((a + f + 0x5A827999 + words[i % 16]) & 0xFFFFFFFF, 3)
        a = temp
    
    a0 = (a0 + a) & 0xFFFFFFFF
    b0 = (b0 + b) & 0xFFFFFFFF
    c0 = (c0 + c) & 0xFFFFFFFF
    d0 = (d0 + d) & 0xFFFFFFFF

    return '{:08x}{:08x}{:08x}{:08x}'.format(a0, b0, c0, d0)

input_string = input("Nhập chuỗi cần băm: ")
md5_hash = md5(input_string.encode('utf-8'))
print("Mã băm MD5 của chuỗi '{}': {}".format(input_string, md5_hash))
