count_pages = int(input())
pages_in_hour = int(input())
days_to_read = int(input())

#The sum for all pages in hours per day
sum_hours_book = count_pages / pages_in_hour
final_sum = sum_hours_book / days_to_read
print(int(final_sum))