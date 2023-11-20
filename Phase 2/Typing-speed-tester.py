import time

def calculate_typing_speed(start_time, end_time, typed_words):
    elapsed_time = end_time - start_time
    minutes = elapsed_time / 60.0
    words_per_minute = typed_words / minutes
    return words_per_minute

def typing_speed_test():
    input("Type the following text and press Enter when you're done:\n\n"
          "The quick brown fox jumps over the lazy dog.\n\n")

    start_time = time.time()

    typed_text = input("Type the text here: ")

    end_time = time.time()

    typed_words = len(typed_text.split())
    speed = calculate_typing_speed(start_time, end_time, typed_words)

    print(f"\nYour typing speed is: {speed:.2f} words per minute")

if __name__ == "__main__":
    typing_speed_test()
