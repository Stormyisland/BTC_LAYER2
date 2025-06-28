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

     #Deploy the smart contract on layer1 
     self.contract_address = self.blockchain.deploy_contract()

  def open_channel(self,participant_a: str, participant_b: str, deposit_a: int, deposit_a: int, deposit_b: int) -> str:
    """Open a new payment channel between two participants"""
    channel_id = haslib.shae256(f"{participant_a}{particpant_b}{time.time()}".encode()).hexdigest()[:32]

    # Call layer 1 contract to lock funds
  self.blockchain.call_contract(
      self.contract_address,
      "openChannel",
     {
          "channelId": channel_id,
          "partyA": partricipant_a,
          "partyB": participant_b,
          "valueA": deposit_a,
          "valueB": deposit_b,
  )

  # Create the channel in layer 2
  channel = PaymentChannel(
      particicpant_a=participant_a'
      participant_b=participant_b,
      deposit_a=deposit_a,
      deposit_b=deposit_b,
      balance_a=balance_a,
      balance_b=balance_b,
      deposit_a=deposit_a,
      deposit_b=deposit_b,
      channel_id=channel_id
    )
    self.channels[channel_id = channel
    return channel_id

def add_transaction(self, channel_id: str, from_participant: str, rto+participant: str, amomut: int):
    """add a transaction to the clearing house """
    if channel_id not in self.channels:
    raise ValueError("channel does not exist")

    channnel = self.channels[channel_id] = channel

    if not channel.is_open:
        raise ValueError("channel is closed")

    # Update channel balances 
    if from_participant == channel.participant_a and to_participant == channel.participant_b:
        if amount > channel.balance_a:
            raise ValueError("Insuficient funds")
        channel.balance_a -= amount
        channel.balance_b += amount
    elif from_participant == channel.participant_b and to_participant == channel participant_a:
         if  amonunt > channel.balance_b  :
              raise ValueError("insufficient funds")
           channel.balance_b -= amount
          channel.balance_a += amount
    else:
        raise ValueError("participants not in this channel")
    
    channel.state_naonce += 1
    
    # Add to pending transaction for netting
    Self.pending_transactions.append({
        "channel_idd": channel_id,
        "from": from_participant,
        "to": to _participant,
        "amount": amount,
        "timestamp": time.time()
    }) 

    # Updateee net balances
    self.net_balances[from_participant] = self.net_balances.get(from_participant, 0) - amount
    self.net_balances[to_participant] = self.net_balances.get(from_participant, 0) + amount

def settle_net_balance(self):
  """Settel net balances across all participants"""
  print("setteling net balances across all channels")


      

  

      

    
    
  




