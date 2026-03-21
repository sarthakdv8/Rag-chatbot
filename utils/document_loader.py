# To get the path
from pathlib import Path
# to import text loader so that it can got to the file and load the text in document objects
from langchain_community.document_loaders import TextLoader
# This is document class to create document objects
from langchain_core.documents import Document
# To import pdf reader to read pdf files
from pypdf import PdfReader
# to make the function that can load the document and return a list of document objects




def load_document(dir_path:Path)->list:
    docs=[]
    dir_path=Path(dir_path)
    if not dir_path.exists():
        return docs
    for p in dir_path.rglob("*"):
        if p.is_dir():
            continue
        suffix=p.suffix.lower()
        try:
            if suffix==".txt":
                docs.extend(TextLoader(str(p),encoding="utf-8").load())
            elif suffix==".md":
                docs.extend(TextLoader(str(p),encoding="utf-8").load())
            elif suffix==".pdf":
                reader=PdfReader(str(p))
                for i,page in enumerate(reader.pages):
                    text=page.extract_text() or ""
                    if not text.strip():
                        continue
                    docs.append(Document(page_content=text,metadata={"source":str(p),"page":i+1}))
        except Exception:
            continue
    return docs
    