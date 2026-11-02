"""Contract Net Protocol implementation."""
from typing import Dict, Any, List, Optional

class ContractNetManager:
    def __init__(self):
        self.bids: Dict[str, Dict[str, Any]] = {}

    def submit_bid(self, agent_id: str, cost: float, estimated_ms: float) -> None:
        self.bids[agent_id] = {"cost": cost, "estimated_ms": estimated_ms}

    def award_best_bid(self, cost_weight: float = 0.5, speed_weight: float = 0.5) -> Optional[str]:
        if not self.bids:
            return None

        # Lower score is better
        best_agent = None
        best_score = float("inf")

        for agent, stats in self.bids.items():
            score = (stats["cost"] * cost_weight) + (stats["estimated_ms"] / 1000.0 * speed_weight)
            if score < best_score:
                best_score = score
                best_agent = agent

        return best_agent
