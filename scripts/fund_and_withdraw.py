from scripts.helpful_scripts import get_account
from brownie import FundMe


def fund():
    account = get_account()
    fund_me = FundMe[-1]
    entranceFee = fund_me.getEntranceFee()
    print(entranceFee)
    print("Funding")
    fund_me.fund({"from": account, "value": entranceFee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
