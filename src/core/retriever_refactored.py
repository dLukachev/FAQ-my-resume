from typing import List, Dict, Tuple, Optional
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.retrievers import BM25Retriever
from langchain_core.documents import Document
from src.core.utils_refactored import detect_intent, preprocess_text


class E5Embeddings(SentenceTransformerEmbeddings):
    def embed_documents(self, texts):
        texts = [f"passage: {t}" for t in texts]
        return self.client.encode(texts, normalize_embeddings=True).tolist()

    def embed_query(self, text):
        return self.client.encode(f"query: {text}", normalize_embeddings=True).tolist()

def build_e5_embeddings(model_name: str = "./e5smallv2"):
    return E5Embeddings(model_name=model_name, encode_kwargs={"normalize_embeddings": True})

emb_model = build_e5_embeddings()
vectordb = Chroma(persist_directory="data/chroma_db", embedding_function=emb_model)

def _load_docs() -> List[Document]:
    raw = vectordb._collection.get(include=["documents", "metadatas"])
    return [Document(page_content=c, metadata=m) for c, m in zip(raw["documents"], raw["metadatas"])] # type: ignore

_BM25 = BM25Retriever.from_documents(_load_docs())

def retrieve(query: str, chat_id: str = "default", k: int = 6) -> Tuple[List[Document], Dict]:
    intent = detect_intent(query)
    dense_hits = vectordb.similarity_search(query, k=k)
    sparse_hits = _BM25.get_relevant_documents(query)[:k]
    merged = {d.page_content: d for d in dense_hits + sparse_hits}.values()
    return list(merged)[:k], {"intent": intent.__dict__}