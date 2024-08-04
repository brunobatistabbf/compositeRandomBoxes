from subscription import Subscription

if __name__ == '__main__':
    levels = ["Bronze", "Prata", "Ouro", "Platina"]
    for level in levels:
     box = Subscription(level)
     print(f"{box}\n")