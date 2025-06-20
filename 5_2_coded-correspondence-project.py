def caesar_decode(message, offset):
    decoded_message = ''
    for char in message:
        if char.isalpha():
            shifted = ord(char) - offset
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decoded_message += chr(shifted)
        else:
            decoded_message += char
    return decoded_message


# Task 1 message
message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
offset = 10
print(caesar_decode(message, offset))


def caesar_encode(message, offset):
    encoded_message = ''
    for char in message:
        if char.isalpha():
            shifted = ord(char) + offset
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encoded_message += chr(shifted)
        else:
            encoded_message += char
    return encoded_message


# Task 2 message
response = "Hello Vishal! Caesar Cipher is fun!"
encoded_response = caesar_encode(response, offset)
print(encoded_response)

# First message
first_message = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
print(caesar_decode(first_message, offset))

# Second message
second_message = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"
print(caesar_decode(second_message, 14))  # Offset inferred from the hint


def brute_force_caesar(message):
    for test_offset in range(1, 26):
        print(f"Offset {test_offset}: {caesar_decode(message, test_offset)}")


brute_force_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."
brute_force_caesar(brute_force_message)


def vigenere_decode(message, keyword):
    keyword_repeated = (keyword * (len(message) // len(keyword) + 1))[:len(message)]
    decoded_message = ''
    for m_char, k_char in zip(message, keyword_repeated):
        if m_char.isalpha():
            shift = ord(k_char.lower()) - ord('a')
            shifted = ord(m_char) - shift
            if m_char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif m_char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decoded_message += chr(shifted)
        else:
            decoded_message += m_char
    return decoded_message


vigenere_message = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztylktoikqq!"
keyword = "friends"
print(vigenere_decode(vigenere_message, keyword))


def vigenere_encode(message, keyword):
    keyword_repeated = (keyword * (len(message) // len(keyword) + 1))[:len(message)]
    encoded_message = ''
    for m_char, k_char in zip(message, keyword_repeated):
        if m_char.isalpha():
            shift = ord(k_char.lower()) - ord('a')
            shifted = ord(m_char) + shift
            if m_char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif m_char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encoded_message += chr(shifted)
        else:
            encoded_message += m_char
    return encoded_message


# Test encoding and decoding
message = "Thanks for the fun project Vishal!"
encoded_message = vigenere_encode(message, keyword)
decoded_message = vigenere_decode(encoded_message, keyword)

print("Encoded:", encoded_message)
print("Decoded:", decoded_message)
