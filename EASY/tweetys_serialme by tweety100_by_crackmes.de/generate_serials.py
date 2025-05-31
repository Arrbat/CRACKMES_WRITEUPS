def generate_serials(name):
    sum_ascii = sum(ord(c) for c in name)

    firstSerial = (sum_ascii * 0x1f) // 0x275 + 0x2a5f828
    while firstSerial > 999_999_999:
        firstSerial //= 10

    secondSerial = firstSerial * 0x52 - 3
    while secondSerial > 99_999:
        secondSerial //= 10

    return firstSerial, secondSerial

# example
name = "admin"
serial1, serial2 = generate_serials(name)

print(f"Name: {name}")
print(f"Serial 1: {serial1}")
print(f"Serial 2: {serial2}")