words = input().split(" ")
search_word = input()
palindromes = []
count_of_palindromes = 0
for word in words:
    if "".join(reversed(word)) == word:
        palindromes.append(word)
        if search_word == word:
            count_of_palindromes += 1

print(palindromes)
print(f"Found palindrome {count_of_palindromes} times")