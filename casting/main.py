# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

leek_price = int(2)
print(f'Leek is {leek_price} euro per kilo.')

order_0 = "leek 4"
order_0_amount = int(order_0[-1])

sum_total = order_0_amount * leek_price
print(sum_total)

broccoliPrice = round(2.34, 2)
broccoliOrder = "broccoli 1.6"
broccoliAmount = round(float(broccoliOrder[-3:]), 2)
print(f'{broccoliAmount}kg broccoli costs {round((broccoliAmount * broccoliPrice), 2)}e')
