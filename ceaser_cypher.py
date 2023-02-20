

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
nums = ['0','1','2','3','4','5','6','7','8','9']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


c =str()




def encrypt(text,shift):
    global c
    if direction == "encode" :
        for letter in text :
            if letter == " "  :
                c+= letter
            elif letter in nums:
                c+= letter
            else:
                nshift = alphabet.index(letter) + shift
                if nshift > len(alphabet): 
                    nshift = nshift - len(alphabet)
                    c += alphabet[nshift]
                else:
                    c += alphabet[nshift]
                    

       
    elif direction == "decode":
        for letter in text :
            if letter == " "  :
                c+= letter
            elif letter in nums:
                c+= letter
            else:
                nshift = alphabet.index(letter) - shift
                if nshift > len(alphabet): 
                    nshift = nshift - len(alphabet)
                    c += alphabet[nshift]
                else:
                    c += alphabet[nshift]
                    



    print(c)
   

encrypt(text,shift)
