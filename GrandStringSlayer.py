def char_to_hex(chars):
    hex_chars = ""
    for char in chars:
        hex_value = hex(ord(char))[2:]
        hex_chars += hex_value.zfill(2)
    return hex_chars

def decrypt_ope(value_enc, key):
    result = ""
    masking = True

    key_index = 0

    for i in range(0, len(value_enc), 2):
        if masking:
            masking = False
        else:
            hex_value_enc = value_enc[i:i+2]
            hex_key = char_to_hex(key[key_index % len(key)])
            key_index += 1
            xor_ope = hex(int(hex_value_enc, 16) ^ int(hex_key, 16))

            if int(xor_ope, 16) < int(value_enc[i-2:i], 16):
                xor_ope = hex(int(xor_ope, 16) + 0xFF)
            
            sub_ope = hex(int(xor_ope, 16) - int(value_enc[i-2:i], 16))
            result += sub_ope[2:]

    return result



def Get_Values_From_File(filename, key):
    with open(filename, 'r') as file:
        lines = file.readlines()

    for line in lines:
        value_enc = line.strip()
        result = decrypt_ope(value_enc, key)
        result = result.replace("0x", "")
        result = result.replace("x", "")
        result_chars = ''.join([chr(int(result[i:i+2], 16)) for i in range(0, len(result), 2)])
        print("{} ---> {}".format(result_chars,value_enc))
    
    
# Modify Here
filename = "file.txt"
key = "KEY_HERE"
Get_Values_From_File(filename, key)