"""
1. split the sentence and make a list
2. reverse the list
3. swapcase of each letter word by word
4. join the word list
"""

def reverse_words_order_and_swap_cases(sentence: str):
    words = sentence.split(" ")
    words = words[::-1]
    result= [word.swapcase() for word in words]
    return " ".join(result)

def main():
    s = "rUns dOg"
    result = reverse_words_order_and_swap_cases(s)
    print(result)

if __name__ == "__main__":
    main()