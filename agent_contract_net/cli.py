"""Command line interface for agent-contract-net."""
from .protocol import ContractNetManager

def main():
    cnp = ContractNetManager()
    cnp.submit_bid("worker_fast", cost=2.0, estimated_ms=200)
    cnp.submit_bid("worker_cheap", cost=0.5, estimated_ms=1200)
    print("Awarded agent:", cnp.award_best_bid())

if __name__ == "__main__":
    main()
