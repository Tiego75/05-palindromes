"""
this module check if the words in the list are palindromes
"""


def ispalindrome(p):
    """
    Return true if the word is a palindrome

    Args:
        p(str): the string to test
    Return: 
        bool: True if the word is a palindrome, False if not
    """


    table = str.maketrans("éèêëàâùûçôîïâ","eeeeaauucoiia")
    p = p.lower().translate(table)
    for punctuation in ' \'!,.?;:"-':
        p = p.replace(punctuation, "")

    for j in range(len(p)//2):
        if p[j]!=p[-j-1]:
            return False
    return True



#### Fonction principale
def main():
    """
    Check if the words in the list are palindromes
    """
    # vos appels à la fonction secondaire ici
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))
if __name__ == "__main__":
    main()
