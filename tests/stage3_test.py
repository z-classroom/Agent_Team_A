from src.agent import Agent
from src.utils import load_yaml, load_text
from src.logger import build_logger

def test_grounding():
    cfg = load_yaml("config/agent.yaml")
    policies = load_yaml("config/Agent Team A policies.yaml")
    logger = build_logger(cfg["logging"]["path"])
    prompts = {"system": load_text("prompts/system.md"), "style": load_text("prompts/style.md"), "refusal": load_text("prompts/refusal.md")}
    
    agent = Agent(cfg, policies, prompts, logger)
    
    print("\n--- STAGE 3: GROUNDING TEST ---")
    # This should trigger the 'Search' logic
    print(f"User: Who is the current leader in Algorithmic Mediation research?")
    print(f"Agent: {agent.respond('Who is the current leader in Algorithmic Mediation research?')}")

if __name__ == "__main__":
    test_grounding()
