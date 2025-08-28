from langchain.schema import Document
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma

file_path = "/Users/ddrxg/Code/LLM-app-public/src/data/data.txt"

# Функция для определения типа чанка по первой строке
def parse_chunk(chunk_text):
    first_line = chunk_text.split('\n', 1)[0].strip()
    if first_line == "[ПРОЕКТ]":
        chunk_type = "project"
    elif first_line == "[НАВЫКИ]":
        chunk_type = "skills"
    elif first_line == "[УСЛОВИЯ РАБОТЫ]":
        chunk_type = "wishes"
    elif first_line == "[КОНТАКТЫ]":
        chunk_type = "contacts"
    elif first_line == "[ОПЫТ РАБОТЫ]":
        chunk_type = "experience"
    elif first_line == "[НИЧЕГО НЕ НАЙДЕНО]":
        chunk_type = "none"
    else:
        chunk_type = "other"
    return Document(page_content=chunk_text, metadata={"type": chunk_type})

def build_index(data_file=file_path, db_dir='data/chroma_db', model_name='./e5smallv2'):
    with open(data_file, encoding="utf-8") as f:
        text = f.read()
    raw_chunks = [chunk.strip() for chunk in text.split("=== ЧАНК ===") if chunk.strip()]
    chunks = [parse_chunk(chunk) for chunk in raw_chunks]

    emb_model = SentenceTransformerEmbeddings(model_name=model_name)
    vectordb = Chroma.from_documents(chunks, embedding=emb_model, persist_directory=db_dir)
    vectordb.persist()
    print("Индекс создан!")

if __name__ == "__main__":
    build_index()