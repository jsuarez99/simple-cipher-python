#simple_cipher
#by Josh Suarez
#2019-05-16

import re #used for regex matching in __isValid

class Cipher:
    # -------------- encode ------------------------
    #Encode the string. By default each letter is shifted by one
    def encode(self, inpStr, shiftBy = 1):
        if self.__isValid(inpStr) == False:
            return ""

        #If the shift amount is more than 26, keep subtracting 26 until it is <= 26
        #This keeps the value within the unicode lowercase alphabet boundaries 
        while shiftBy > 26:
            shiftBy = shiftBy - 26

        lwrStr = inpStr.lower()
        #lambda function adds the shiftBy amount to each letter in the character array.
        resChrArr = map(lambda ltr : self.__shift(ltr, shiftBy), list(lwrStr))
        
        #join the results
        resStr = "".join(resChrArr)
        return resStr

    #--------------- decode --------------------------

    #Encode the string. By default each letter is shifted back by one
    #To avoid duplicating call, this only needs to be a call to encode with 
    #a negative number
    def decode(self, inpStr, shiftBy = 1):
        #Same as above in encode. After adjusting, this number will be turned negative
        while shiftBy > 26:
            shiftBy = shiftBy - 26

        #call the encode function, but mutiply the shiftBy amount by -1 to turn it into
        #a negative number
        resStr = self.encode(inpStr,shiftBy * -1)
        return resStr

    #====================================================
    # ------------ Private functions --------------------

    # ------------ isValid ----------------------

    #Check if we have an empty string or for non-alphabet characters
    def __isValid(self, inpStr):
        #if the string is empty, also invalid
        if inpStr == "":
            raise Exception("Input string is empty.")
            return False

        #regex match any non-letter character
        res = re.search("[^a-zA-Z]",inpStr)
        if res != None:
            raise Exception("Input string contains invalid characters.")
            return False
    
        return True


    #---------------- shift ---------------------------

    #This will shift each character while also wrapping around if it goes after 'z' or
    #before 'a'
    def __shift(self, inpLetter, shiftBy):
        #Add the the shift amount to the converted character. ord() convers the char to an int
        newChrVal = ord(inpLetter) + shiftBy
        
        #Check if the shifted character is out of bounds for lowercase letters
        #and adjust appropriately
        if newChrVal > 122:
            newChrVal = newChrVal - 26
        elif newChrVal < 97:
            newChrVal = newChrVal + 26

        return chr(newChrVal)
