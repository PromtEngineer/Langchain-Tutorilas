import time
from dotenv import load_dotenv
import langchain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback
from langchain.cache import InMemoryCache

# Initialize OpenAI API
load_dotenv()

# add cache to langchain
langchain.llm_cache = InMemoryCache()


# To make the caching really obvious, lets use a slower model.
llm = OpenAI(model_name="gpt-3.5-turbo-16k",)

# The first time, it is not yet in cache, so it should take longer
prompt="What is the Capital of France?"

with get_openai_callback() as cb:
    print("------------------------------------------")
    start_time = time.time()
    response = llm.predict(prompt)
    end_time = time.time()

    print(f"LLM Response: {response}")
    print(f"Time taken: {end_time-start_time:0.2f} sec")
    print(f"{cb}")

    print("------------------------------------------")


with get_openai_callback() as cb_cache:
    print("------------------------------------------")
    start_time = time.time()
    response = llm.predict(prompt)
    end_time = time.time()

    print(f"LLM Response: {response}")
    print(f"Time taken: {end_time-start_time:0.2f} sec")
    print(f"{cb_cache}")

    print("------------------------------------------")




