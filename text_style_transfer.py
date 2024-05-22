from asyncflows import AsyncFlows


writing_sample = """
Hullo mai neyms Kruubi Duubi, aI'm hear to rite yu a fanfic abowt enyting yu want. 
"""


async def main():
    # Load the chatbot flow
    flow = AsyncFlows.from_file("text_style_transfer.yaml").set_vars(
        writing_sample=writing_sample,
    )

    # Run the flow
    while True:
        # Get the user's query via CLI interface (swap out with whatever input method you use)
        try:
            message = input("Write about: ")
        except EOFError:
            break

        # Set the query and conversation history
        topic_flow = flow.set_vars(
            topic=message,
        )

        # Run the flow and get the result
        result = await topic_flow.run()
        print(result)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
