from brownie import Oracle, interface
from scripts.helpful_scripts import get_account



def deploy_oracle():
    owner = get_account()
    link_address = "0x326C977E6efc84E512bB9C30f76E30c160eD06FB"

    if len(Oracle) == 0:
        oracle_contract = Oracle.deploy({"from": owner})
        
    else:
        oracle_contract = Oracle[-1]
        

    # fund the oracle smart contract with some link tokens
    link_contract = interface.IERC20(link_address)
    print(f"Elisha's Link balance {link_contract.balanceOf(owner)}")

    link_contract.transfer(oracle_contract, 5 * 10**18 , {"from": owner})

    # making the api call
    oracle_contract.requestVolumeData({"from": owner})

    data = oracle_contract.volume()
    print(f"Hey I am the fetched data {data}")

def main():
    deploy_oracle()