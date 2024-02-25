###############################################################################
#
# PURPOSE:   This script runs the gambling method in American or European
#            Roulette. This script just allows for keeping a constant bet on
#            BLACK.
# AUTHOR:    Harsh Saxena
# DATE:      June 12, 2021
###############################################################################
import random


class Roulette:

    def __init__(self, table_slots):

        self.table_slots = table_slots
        self.loss_times, self.loss_total, self.accum_loss, self.greatest_loss, self.win_times, \
        self.payout_total, self.accum_gain, self.greatest_payout, self.current_total_loss = [0 for _ in range(9)]

    def play_roulette(self, min_bet, balance, spins):

        table_max = balance

        # Loop for each Roulette spin
        for each in range(spins):

            if self.current_total_loss == 0:
                bet = min_bet

            pocket = self.spin_roulette(self.table_slots)

            # Roulette strategy for payout
            if self.win_loss(pocket):

                self.win_times += 1
                self.payout_total += bet
                self.accum_gain += bet
                balance += bet
                if balance > self.greatest_payout:
                    self.greatest_payout = balance
                bet = min_bet
                self.current_total_loss = 0
            else:
                self.loss_times += 1
                self.loss_total += bet
                self.accum_loss += bet
                self.current_total_loss += bet
                balance -= bet
                if self.greatest_loss == 0:
                    self.greatest_loss = balance
                self.greatest_loss = min(balance, self.greatest_loss)
                bet = self.current_total_loss

            if self.current_total_loss >= table_max:
                break

    def spin_roulette(self, roulette_pockets):
        roll_pocket = random.choice(roulette_pockets)
        return roll_pocket

    def win_loss(self, pocket):
        if pocket == 'Black':
            win = True
        else:
            win = False
        return win


def input_display():
    print(f'\n{"*":>10} WELCOME TO PLAY ROULETTE *\n')

    table_slots = None

    while True:
        print("Which roulette table (E)uropean or (A)merican, you want to play? ")
        roulette_table = input()
        if not (roulette_table.upper() == 'E' or roulette_table.upper() == 'A'):
            print(f'Sorry, wrong selection..try again...')
            continue
        else:
            if roulette_table.upper() == 'A':
                table_slots = ["Black"] * 18 + ["Red"] * 18 + ["Green"] * 2
                roulette_table = 'American'
            else:
                table_slots = ["Red"] * 18 + ["Black"] * 18 + ["Green"]
                roulette_table = 'European'
            break

    while True:
        print("What is your minimum bet (in $)?")
        minimum_money = int(input())
        if minimum_money <= 0:
            print(f'Sorry, wrong input..try again...')
            continue
        else:
            break

    while True:
        print("What is your maximum bet (in $)?")
        maximum_money = int(input())
        if maximum_money <= 0 or maximum_money < minimum_money:
            print(f"Sorry, wrong input..try again...")
            continue
        else:
            break

    while True:
        print("Maximum rounds will you play?")
        maximum_rounds = int(input())
        if maximum_rounds <= 0:
            print(f"Sorry, wrong input..try again...")
            continue
        else:
            break

    return maximum_rounds, roulette_table, minimum_money, maximum_money, table_slots


def print_result(roulette, roulette_table, maximum_rounds, maximum_money, minimum_money):
    star = "*" * 121
    average_payout = 0
    average_loss = 0

    if roulette.loss_times > 0:
        average_loss = int(round(roulette.loss_total / roulette.loss_times, 0))
    if roulette.win_times > 0:
        average_payout = int(round(roulette.payout_total / roulette.win_times, 0))

    star_new = ("*" * 47)
    print(f'\n{star_new} Roulette table : {roulette_table} {star_new}')
    print(f'CONFIGURATION : Number of Rounds     : {maximum_rounds:>7}'
          f'\t\tMinimum bet($)        : {minimum_money:>7}'
          f'\t\tMaximum bet($)           : {maximum_money:>6}')

    print(f'\nRESULT        : Accumulated gains($) : {roulette.accum_gain:>7}'
          f'\t\tAccumulated losses($) : {roulette.accum_loss:>7}')

    print(f'WINNINGS      : Greatest payout($)   : {roulette.greatest_payout:>7}'
          f'\t\tAverage payout($)     : {average_payout:>7}'
          f'\t\tNumber of winning rounds : {roulette.win_times:>6}')

    print(f'LOSSES        : Greatest loss($)     : {roulette.greatest_loss:>7}'
          f'\t\tAverage loss($)       : {average_loss:>7}'
          f'\t\tNumber of losing rounds  : {roulette.loss_times:>6}')

    print(f'{star}')


def main():
    (maximum_rounds, roulette_table, minimum_money, maximum_money, table_slots) = input_display()

    roulette = Roulette(table_slots)

    roulette.play_roulette(minimum_money, maximum_money, maximum_rounds)

    print_result(roulette, roulette_table, maximum_rounds, maximum_money, minimum_money)


if __name__ == "__main__":
    main()
    print("Complete")
