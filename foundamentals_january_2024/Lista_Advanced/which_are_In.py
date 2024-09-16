first_words = input().split(", ")
second_words = input().split(", ")
final_list = []

for word in first_words:
    for second_word in second_words:
        if word in second_word:
            if word not in final_list:
                final_list.append(word)

print(final_list)