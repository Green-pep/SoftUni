def split_text(input_text):
    text = input_text.split("@")
    neighborhood_numbers = [int(numbers) for numbers in text]
    return neighborhood_numbers

input_text = input()
print(split_text(input_text))