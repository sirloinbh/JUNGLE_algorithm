max_customer = 0
customer = 0
for _ in range(10) :
    out, come = map(int, input().split())
    customer += come-out
    max_customer = max(max_customer, customer)
print(max_customer)