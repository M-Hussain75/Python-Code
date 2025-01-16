a= input("Enter a character :")
match a :
    case "a":
        print("It is a vowel")
    case "A":
        print("It is a vowel")
    case "e": 
        print("It is a vowel")
    case "E":
        print("It is a vowel")
    case "i":
        print("It is a vowel")
    case "I":
        print("It is a vowel")
    case "o":
        print("It is a vowel")
    case "O":
        print("It is a vowel")
    case "u":
        print("It is a vowel")
    case "U":
        print("It is a vowel")
    case _:
        print("It is not vowel")
#Another way 
a = input("Enter a character: ")
match a:
    case "a" | "A":
        print("It is a vowel")
    case "e" | "E":
        print("It is a vowel")
    case "i" | "I":
        print("It is a vowel")
    case "o" | "O":
        print("It is a vowel")
    case "u" | "U":
        print("It is a vowel")
    case _:
        print("It is not a vowel")
