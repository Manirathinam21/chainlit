import chainlit as cl

@cl.on_message
async def main(message: cl.Message):
    
    # Send a response back to the user
    await cl.Message(
        content= f"Received: {message.content}",
            ).send()
    
    
import chainlit as cl


