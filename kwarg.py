#ORDER SUMMARY
def order_summary(item,*arguments,**keywords):
    print("--You ordered:",item)
    print("--Additional notes:")
    for arg in arguments:
        print(arg)
    print('-' * 40)
    for kw in keywords:
        print(kw,":",keywords[kw])

order_summary(
    "pizza",
    "Extra cheese",
    "Extra spicy.",
    customer="alice",
    location="Table 5",
    Time="7.30 PM"
)


#ENHANCED ORDER SUMMARY

def order_summary(item,*arguments,**keywords):
    print("--YOU ORDERED:",item.upper())
    print("--Additional notes:")
    for arg in arguments:
        print(arg)
    print('-' * 40)
    for kw in sorted(keywords):
        print(f"{kw.ljust(8)}: {keywords[kw]}")

order_summary(
    "pizza",
    "Extra cheese",
    "Extra spicy.",
    customer="alice",
    location="Table 5",
    Time="7.30 PM"
)