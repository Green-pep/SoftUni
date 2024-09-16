def grade_indicator(grade_rating):
    if 2.00 <= grade_rating <= 2.99:
        return "Fail"
    if grade_rating <= 3.49:
        return "Poor"
    if grade_rating <= 4.49:
        return "Good"
    if grade_rating <= 5.49:
        return "Very Good"
    if grade_rating <= 6.00:
        return "Excellent"


rating = float(input())
print(grade_indicator(rating))
