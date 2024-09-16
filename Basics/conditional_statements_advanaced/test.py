import os

# Prompt the user for their name
names = input("")

# Sanitize the input name to remove invalid characters for a filename
sanitized_names = ''.join(char for char in names if char.isalnum() or char in (' ', '_', '-'))

# Get the user's desktop directory
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Create the file path on the desktop
file_path = os.path.join(desktop_path, f"{sanitized_names}.txt")

# Open and write to the file with UTF-8 encoding
with open(file_path, "w", encoding="utf-8") as f:
    f.write(f'''Уважаеми г-н/г-жо {names},
    С наше съжаление, искаме да ви уведомим, че след внимателен анализ на вашата кандидатура, не можем да ви одобрим за бърз заем с нашата компания.
    Ние разбираме, че сте изразили интерес и се надявахме да ви предоставим финансовата помощ, която търсите. Вашето кандидатура бе обект на задълбочена оценка, но според нашите текущи оценки и критерии, не можем да ви предоставим заем на този етап.

    Това решение не засяга вашата кредитна репутация или възможността ви за бъдещи заеми. Надяваме се, че в бъдеще ще имате възможност да отговорим на вашите финансови нужди.

    Благодарим ви, че избрахте да кандидатствате при нас и се надяваме да имаме възможност да ви обслужим в бъдеще.

С уважение,
Александра Иванова
Фаст Кеш Солюшън Българя
Клиентско Обслужване
''')

print(f"The file {sanitized_names}.txt has been created on your desktop.")
