#coding=utf-8

shopping = {"Mac":9000,"kindle":800,"tesla":900000,"python_book":105,"bike":2000}

amount =  input("请输入您的金额：")
product = input("请选择您的商品：")
amount = int(amount)

product_prace = int(shopping[product])
balance =amount-product_prace

if amount <product_prace:
    print("商品价格为%d元，您的余额不足！"%product_prace)

else :
    print("商品价格为%d,你的余额为%d元"%(product_prace,balance))



