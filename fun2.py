# 寫一個function來算出清單中數字的總數
# function應該要有一個參數讓使用者投入（傳遞進去）一個清單，
# function應該回傳(return)清單中數字的總數。
# 請把function命名為sum_of_list，這樣才可以執行測試。
# print(sum_of_list([1, 2, 3]))#應該要印出6

def sum_of_list(numbers):
	return sum(numbers)

print(sum_of_list([1, 2, 3]))	
