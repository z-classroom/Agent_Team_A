from .tools import SearchTool

class Agent:
    def __init__(self, cfg, policies, prompts, logger):
        # ... (keep previous Stage 2 init code)
        self.search_tool = SearchTool()
        # ...

    def respond(self, user_text: str) -> str:
        # 1. Check Policy (Stage 1)
        # 2. Check Memory (Stage 2)
        
        # 3. Grounding Step (Stage 3)
        # We ask the LLM if it needs to search. 
        # For the prototype, we trigger search if certain 'uncertainty' keywords appear.
        needs_search = any(word in user_text.lower() for word in ["latest", "current", "who is", "what happened"])
        
        grounding_context = ""
        if needs_search:
            grounding_context = self.search_tool.search(user_text)
            self.logger.info(f"GROUNDING: Tool used for query '{user_text}'")

        # 4. Final Response Generation
        # We feed the search data into the LLM as 'Truth'
        reply = self.llm.complete(
            system=f"{self.prompts['system']}\nCONTEXT: {grounding_context}",
            messages=self.memory.messages(),
            user=user_text,
            refusal_prompt=self.prompts["refusal"]
        )
        
        self.memory.add(user_text, reply)
        return reply
