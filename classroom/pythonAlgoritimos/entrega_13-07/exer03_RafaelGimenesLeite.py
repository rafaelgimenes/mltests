# author Rafael Gimenes Leite
def chkPalindrome(palavra):
    if palavra.upper() == palavra.upper()[::-1]:
        return "Temos um palindrome"
    else:
        return "Nao foi dessa vez"
        
print(chkPalindrome("asrarA"))
