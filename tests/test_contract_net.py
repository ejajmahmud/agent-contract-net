"""Unit tests for ContractNetManager."""
import unittest
from agent_contract_net.protocol import ContractNetManager

class TestContractNet(unittest.TestCase):
    def test_bidding_and_award(self):
        cnp = ContractNetManager()
        cnp.submit_bid("fast", cost=1.0, estimated_ms=100)
        cnp.submit_bid("slow", cost=1.0, estimated_ms=900)
        winner = cnp.award_best_bid()
        self.assertEqual(winner, "fast")

if __name__ == "__main__":
    unittest.main()
