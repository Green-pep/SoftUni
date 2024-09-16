yearly_price = int(input())

price_shoes = yearly_price - (yearly_price * 0.40)
price_outfit = price_shoes - (price_shoes * 0.20)
price_ball = price_outfit * 0.25
price_accessories = price_ball / 5

final_sum = price_shoes + price_outfit + price_ball + price_accessories + yearly_price

print(final_sum)