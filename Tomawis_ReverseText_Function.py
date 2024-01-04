def reverse_text():
    while True:
        text = input("Reverse a text: ")
        
        # Prompt the user to enter text containing alphabets only
        if text.isalpha():
            reversed_text = text[::-1]
            print("Output:", reversed_text)
            break
        else:
                print("Error Reported! Enter text only.")

reverse_text()