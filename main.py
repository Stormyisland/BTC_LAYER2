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

