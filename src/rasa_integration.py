import asyncio
from rasa.core.agent import Agent

async def _get_chatbot_response(agent, message):
    responses = await agent.handle_text(message)
    return responses

def get_chatbot_response(message):
    loop = asyncio.get_event_loop()
    model_directory = './models'
    
    agent = Agent.load(model_directory)
    
    responses = loop.run_until_complete(_get_chatbot_response(agent, message))
    return responses