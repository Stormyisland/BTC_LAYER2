Import hashlib
import json
from typing import Dict, List, Tuple
from dataclass import dataclass
import time
class Blockchain:
  def __init__self:
      self.contracts = {}

  def deploy_contract(self, contract_code: str):
    contract_address = hashlib.sha256(contract_code.encode()).hexdigest()[:20]
    self.coontracts[contact_address] = contacr_code 
    return ccontract_address 

  def call_contract(self, address: str, function: str,args: dict):
      print(f"Blockchain: Calling {function} on address} with {args}")
      return True
  

  #payment channels between two partys
@dataclass 
class PaymentChannel
    participant_a: str
    participant_b: str
    derposit_a: int
    deposit_b: int
    balance_a: int
    balance_b: int
    channel_id: str
    state_nonce: int = 0 
    is_open: bool = True

class Clearing_House
  def__init__(self, blockchain, Blockchain):
     self.blockchain = blockchain
     self.channels: Dict[str, PaymentChannel] = {}
    self.pending_transactions: List[dict] = []
    self.net_balances: Dict[str, int] ={} # Participent -> net balance

#Deplot the smaoit comnte on layer1 
     self.contract_address = self.blockchain.deploy_contract()

def open_channel(self,participant_a: str, participant_b: str, deposit_a: int, deposit_a: int, deposit_b: int) -> str:
    """Open a new payment channel between two participants"""
    channel_id = haslib.shae256(f"{participant_a}{particpant_b}{time.time()}".encode()).hexdigest()[:32]

    # Call layer 1 contract to lock funds
self.blockchain.call_contract(
  self.contract_address,
  openChannel",
  {
      "channelId": channel_id,
      "partyA": partricipant_a
      "partyB": participant_b
      "valueA": deposit_a
      "valueB": deposit_b
  )

  # Create the channel in layer 2
channel = PaymentChannel(
  particicpant_a=participant_a'


  




