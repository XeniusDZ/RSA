import math
from random import randint

class RSA:
    def __init__(self,message):
        self.message = message

    def is_prime(self,n):
        for i in range(2, n):
            if (n % i) == 0:
                return False
        return True

    def gcd(self,a, b):
        q,r,y = 0,0,0
        y2, y1 = 0, 1
        while a != 1:
            q = a // b
            r = a % b
            y = y2 - q * y1
            a = b
            b = r
            y2 = y1
            y1 = y
        return y2
    def gen_e(self,phi):
        e = int(randint(1,phi))
        if self.is_prime(e) and e < phi and phi%e != 0:
            return e
        else:
            return self.gen_e(phi)

    def gen_key(self):
        p,q = int(input("input 1st prime number")),int(input("input 2nd prime number"))
        if not(self.is_prime(p) and self.is_prime(q)):
            print("incorrect value")
        else:
            n = p*q
            phi = (p-1)*(q-1)
            e = self.gen_e(phi)
            d = (self.gcd(phi,e))%phi
        public = (e,n)
        private = d
        return self.decrypt(private,public[1],self.encrypt(public[1],public[0],self.message))

    def convert_to_asii(self, message):
        string = ""
        for char in message:
            a = str(format(ord(char), 'b')).zfill(8)
            string += a
        return string
    def encrypt(self,n,e,message):
        cipher_text = ""
        cipher_block = ""
        binary_msg = self.convert_to_asii(message)
        blocks_size = math.floor(math.log(n,2))
        while len(binary_msg) % blocks_size != 0:
            binary_msg = "0" + binary_msg
        for i in range(0,len(binary_msg),blocks_size):
            block = binary_msg[i:i+blocks_size]
            c = (int(block,2)**e)%n
            c = str(format(c, 'b')).zfill(blocks_size+1)
            cipher_block += c
        while len(cipher_block) % 8 != 0:
            cipher_block = "0" + cipher_block
        for j in range(0,len(cipher_block),8):
            cipher_text += chr(int(cipher_block[j:j+8],2))
        print(cipher_text)
        return cipher_text
    def decrypt(self,d,n,cipher_text):
        open_text = ""
        bin_cipher = ""
        binary = ""
        blocks_size = math.floor(math.log(n,2))
        for char in cipher_text:
            bin_cipher += (str(format(ord(char), 'b'))).zfill(8)
        bin_cipher = bin_cipher[::-1]
        for i in range(0,len(bin_cipher),blocks_size+1):
            block = bin_cipher[i:i+blocks_size+1][::-1]
            if len(block) == blocks_size+1:
                c = int((int(block, 2) ** d) % n)
                c = bin(c).replace("0b", "")
                while len(c) < blocks_size:
                    c = "0"+c
                binary = c + binary
        while(len(binary)%8 != 0):
            binary = "0"+binary
        for j in range(0,len(binary),8):
            num = int(binary[j:j + 8], 2)
            if num != 0:
                open_text += chr(num)
        print(open_text)
        return open_text

lol = RSA("lmao")
lol.gen_key()