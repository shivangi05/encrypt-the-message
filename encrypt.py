#ceaser cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
newalphabet =[]
def encode(textv, shiftv):
    textlen = len(textv)
    newtext = []
    for i in range(0,textlen):
        j = alphabet.index(textv[i])  + shiftv 
        newalphabet.append(alphabet[j])
    print(f"{''.join(newalphabet)}")

def decode(textv, shiftv):
    textlen = len(textv)
    newtext = []
    for i in range(0,textlen):
        j = alphabet.index(textv[i])  - shiftv
        newalphabet.append(alphabet[j])
    print(f"{''.join(newalphabet)}")
        
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction in "encode":
    encode(text,shift)
elif direction in "decode": 
    decode(text,shift)
