def trade_action (current_stock, purchase_price, investment):
	import math
	current_shares = int(current_stock)
	purchase_price = float(purchase_price)
	market_price = float(current_prcie)
	available_funds = float(investment)
	transaction_fee = 10
	actual_availale_funds = available_funds - transaction_fee
	amount_of_shares_to_buy = actual_availale_funds / market_price
	shares_to_buy_rounded - math.floor(amount_of_shares_to_buy)
	profitable_buy = (purchase_price - market_price) * shares_to_buy_rounded
	proftiable_sell = (market_price - purchase_price) * current_shares

	if proftiable_sell == transaction_fee:
		return "Hold shares"
	elif market_price > purchase_price:
		return "Sell" + str(current_shares) + " shares"
	if actual_availale_funds < market_price:
		return "Hold shares"
	if transaction_fee >= profitable_buy:
		return "Hold shares"
	elif actual_availale_funds >= market_price:
		return "Buy " + str(shares_to_buy_rounded) + " shares"