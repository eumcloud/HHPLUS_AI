from langchain.chains.summarize import load_summarize_chain
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import Document
import os

def summarize_text(text: str, method: str = "map_reduce") -> str:
    llm = ChatOpenAI(temperature=0.2, model="gpt-4")
    docs = [Document(page_content=text)]

    chain = load_summarize_chain(llm, chain_type=method)
    summary = chain.run(docs)

    return summary
