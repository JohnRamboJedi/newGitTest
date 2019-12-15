def trade_action (current_stock, purchase_price, investment):
	import math
	current_shares = int(current_stock)
	purchase_price = float(purchase_price)
	market_price = float(current_prcie)
	available_funds = float(investment)
	transaction_fee = 10
	actual_availale_funds = available_funds - transaction_fee
	amount_of_shares_to_buy = actual_availale_funds / market_price
	shares_to_buy_rounde - math.floor(amount_of_shares_to_buy)
	profitable_buy