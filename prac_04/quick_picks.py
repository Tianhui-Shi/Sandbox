import random

def main():
    number = int(input("How many quick picks? ")) # ask the user input
    quick_picks(number)


def quick_picks(picks):
    # generate a row with 6 none repeat numbers
    for i in range(picks):
        create_row()
        #print("\n")

# create each row
def create_row():
    row = []
    r = random.randint(1, 45)
    row.append(r)
    while len(row) < 6:
        r = random.randint(1, 45)
        if r not in row:
            row.append(r)

    # output the result without [] and ','
    print(*row, sep=' ')

main()