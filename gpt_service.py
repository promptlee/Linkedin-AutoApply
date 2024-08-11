import os
import openai
from dotenv import load_dotenv

load_dotenv()
# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = os.getenv('OPENAI_PASSWORD')

###start here
# import os
# import asyncio
# from openai import AsyncOpenAI

# client = AsyncOpenAI(
#     # This is the default and can be omitted
#     api_key=os.environ.get("OPENAI_API_KEY"),
# )


# async def main() -> None:
#     chat_completion = await client.chat.completions.create(
#         messages=[
#             {
#                 "role": "user",
#                 "content": "Say this is a test",
#             }
#         ],
#         model="gpt-3.5-turbo",
#     )


# asyncio.run(main())
