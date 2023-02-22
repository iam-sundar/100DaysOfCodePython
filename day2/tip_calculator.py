#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print('Welcome to the tip calculator!')
bill_amount = float(input('What was the total bill? $'))
tip = int(input('How much tip would you like to give? 10, 12, or 15? '))
split = int(input('How many people to split the bill? '))
tip_amount = bill_amount*(tip/100)
per_share_tip = tip_amount/split
per_share_principal = bill_amount/split

per_share = per_share_principal + per_share_tip
r_per_share = format(per_share,".2f")
final_amount = "{:.2f}".format(per_share)
print(f'Each person should pay: ${final_amount}')