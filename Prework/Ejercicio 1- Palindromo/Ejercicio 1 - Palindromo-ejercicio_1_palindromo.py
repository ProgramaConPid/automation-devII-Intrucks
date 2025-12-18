# Escribe tu solución aquí
def is_palindrome(text: str) -> bool:
    text = text.lower()
    clean_text = "".join(
      char for char in text 
      if char.isalnum()
    )
    return clean_text == clean_text[::-1]

if __name__ == "__main__":
    print(is_palindrome("A man, a plan, a canal: Panama")) # True
    print(is_palindrome("Automation developer")) # False
