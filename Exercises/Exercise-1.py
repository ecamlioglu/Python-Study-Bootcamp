"""
-------------------------------------------
This question is first week exercise in
Python Study Bootcamp in Kocaeli University
-------------------------------------------
QUESTION
John going to the market,
he buy egg(0.3$) napkin(3$) water(1$) bread(1.5$) milk(5$) pasta(2$) and chocolate(6$).
create a market receipt to these expenditures(tax %18).
-------------------------------------------
prepared by Erdem Çamlıoğlu
"""
def main():
    products=["egg", "napkin", "water", "bread", "milk", "pasta", "chocolate"]
    costs=[0.3,3,1,1.5,5,2,6]
    # print(products,costs)
    Receipt(products,costs)

def totalTax(costs):
    sum=0
    for number in costs:
        sum += number
    tax=sum*18/100
    includedTax=sum+tax
    return includedTax

def Receipt(a, b):
    for w in range(len(a)):
        print(a[w],b[w])
    print('Total', totalTax(b),"$")
main()