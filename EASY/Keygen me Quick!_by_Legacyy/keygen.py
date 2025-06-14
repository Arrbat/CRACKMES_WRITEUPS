import random

def generate_valid_key():
    first_block = ''.join([str(random.randint(0, 9)) for _ in range(4)])
    
    even_digits = ['0', '2', '4', '6', '8']
    second_block = ''.join([random.choice(even_digits) for _ in range(4)])
    
    third_block = "R3KT"
    
    return f"{first_block}-{second_block}-{third_block}"

if __name__ == "__main__":
    key = generate_valid_key()
    print(f"Generated valid key: {key}")