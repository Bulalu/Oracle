from brownie import Oracle, interface
from scripts.helpful_scripts import get_account



def deploy_oracle():
    owner = get_account()
    link_address = "0x326C977E6efc84E512bB9C30f76E30c160eD06FB" #goerli
    amount_to_transfer = 0.2 * 10**18

    if len(Oracle) == 0:
        oracle_contract = Oracle.deploy({"from": owner}, publish_source=False)
        
    else:
        oracle_contract = Oracle[-1]
        

    # fund the oracle smart contract with some link tokens
    link_contract = interface.IERC20(link_address)

    print(f"Elisha's Link balance {link_contract.balanceOf(owner)}")
    print(owner)

    if link_contract.balanceOf(owner) >= amount_to_transfer and link_contract.balanceOf(oracle_contract) < 1 * 10**18:
        link_contract.transfer(oracle_contract, amount_to_transfer , {"from": owner})
    else:
        print("You do not have enough link tokens 🥲, visit the chainlink faucet and get some more 🤑 ")
        print(f"Your link token balance {link_contract.balanceOf(owner)}, Oracle contract link balance {link_contract.balanceOf(oracle_contract)}")


    # assert link_contract.balanceOf(oracle_contract) >= amount_to_transfer


    # making the api call
    tx = oracle_contract.requestVolumeData({"from": owner})
    print(tx.events)

    data = oracle_contract.volume()
    print(f"Hey I am the fetched data {data}")



def main():
    deploy_oracle()