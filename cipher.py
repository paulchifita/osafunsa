#Cipher.py
#This program encodes and decodes the Caesar cipher
#by: Paul Chifita

def main():
    while True:
        print("This program encodes and decodes the Caesar cipher.")
        print()
        alphabet = "abcdefghijklmnopqrstuvwxyz.! '?,"

        print("This is the alphabet and punctuation characters your message is restricted to:  ", alphabet)
        print()


    #Input the message to be encoded
        
        message = input("Enter the message to be encoded: ")
        print()
        
    #Input the key for which to shift the plaintext
        
        key = eval(input("Enter the key value. To decode the message enter negative of the key value: "))
        print()
        
        Cmessage = ""

    #Loop through the message
        
        for ch in message:
            value = ((alphabet.find(ch)) + key)%len(alphabet)
            
            Cmessage = Cmessage + (alphabet[value])
            
        print("Your encoded message is: ",message)
        print()
        print("Your decoded message is: ",Cmessage)
        print()
main()

