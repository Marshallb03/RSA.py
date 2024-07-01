# The program in this file is the
# individual work of Mab21bb

import random
import math

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def generate_prime(digits):
    lower_bound = 10**(digits - 1)  
    upper_bound = 10**digits - 1    
    while True:
        num = random.randint(lower_bound, upper_bound) 
        if is_prime(num):  
            return num  
    

def generate_e(phi_n):
        e = random.randint(2, phi_n)
        while not gcd(e, phi_n) == 1:
            e = random.randint(2, phi_n)
        return e

def calculate_d(e, phi_n):
      d = pow(e, -1, phi_n)
      return d
       

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def encrypt(message, public_key):
    e, n = public_key
    return pow(message, e, n)

def decrypt(ciphertext, private_key):
    d, n = private_key
    return pow(ciphertext, d, n)

def key_exchange(pubkey1, privkey1, pubkey2, privkey2):
    alice_k = int(input("Enter Alice’s k value: "))
    bob_k = int(input("Enter Bob’s k value: "))
    
    alice_sends = encrypt(alice_k, pubkey2)
    bob_sends = encrypt(bob_k, pubkey1)
    
    decrypted_alice = decrypt(bob_sends, privkey1)
    decrypted_bob = decrypt(alice_sends, privkey2)
    
    alice_secret_key = (alice_k * decrypted_alice) % 2**128
    bob_secret_key = (bob_k * decrypted_bob) % 2**128
    
    print("Alice Sends", alice_sends)
    print("Bob sends", bob_sends)
    print("Alice’s secret key:", alice_secret_key)
    print("Bob’s secret key:", bob_secret_key)


if __name__ == "__main__":
    digits = int(input("Enter the number of digits: "))

    # Generate prime numbers p and q
    p = generate_prime(digits)
    q = generate_prime(digits)

    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = generate_e(phi_n)
    d = calculate_d(e, phi_n)

    print("n:", n)
    print("phi(n):", phi_n)


    # Print the public and private keys
    public_key =  (e, n)
    private_key =   (d, n)
    print("The public key is", public_key)
    print("The private key is", private_key)

    # Encryption
    print("Encryption:")
    message = int(input("Enter the message: "))
    encrypted_message = encrypt(message, public_key)
    print("The encrypted message is", encrypted_message)

    # Decryption
    decrypted_message = decrypt(encrypted_message, private_key)
    print("The decrypted message is", decrypted_message)
    print("Message Reicieved")

    # Signature
    print("Signature:")
    message_to_sign = int(input("Enter the message to be signed: "))
    signature = decrypt(message_to_sign, private_key)
    print("The signed value is", signature)


    # Verification
    verification_result = encrypt(signature, public_key)
    print("The verification result is", verification_result)

    # Key Exchange
    print("Key Exchange:")
    key_exchange(public_key, private_key, public_key, private_key)
 





