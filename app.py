import streamlit as st
from collections import Counter
import re
import matplotlib.pyplot as plt
from pypdf import PdfReader
from wordcloud import WordCloud, STOPWORDS

st.set_page_config(page_title="PDF Text Mining | Muhammad Kamil Shah", page_icon="📄", layout="wide")
st.title("PDF Text Mining & WordCloud Explorer")
st.caption("Upload a text-based PDF to extract text, inspect frequent terms and generate a WordCloud.")

file=st.file_uploader("Upload PDF",type=["pdf"])
if file is None:
    st.info("Upload a text-based PDF to begin. Scanned image-only PDFs require OCR, which this project does not include.")
    st.stop()

reader=PdfReader(file)
text="\n".join((p.extract_text() or "") for p in reader.pages)
clean=re.sub(r"[^A-Za-z\s]"," ",text).lower()
words=[w for w in clean.split() if len(w)>2 and w not in STOPWORDS]
counts=Counter(words)

a,b,c=st.columns(3); a.metric("Pages",len(reader.pages)); b.metric("Extracted characters",f"{len(text):,}"); c.metric("Unique terms",f"{len(counts):,}")
top_n=st.slider("Top terms",10,50,20)
st.dataframe([{"term":w,"frequency":n} for w,n in counts.most_common(top_n)],use_container_width=True)

if words:
    wc=WordCloud(width=1200,height=600,background_color="white",stopwords=STOPWORDS).generate(" ".join(words))
    fig,ax=plt.subplots(figsize=(12,6)); ax.imshow(wc,interpolation="bilinear"); ax.axis("off"); st.pyplot(fig); plt.close(fig)
else:
    st.warning("No usable terms were extracted.")

st.info("WordCloud size represents frequency, not sentiment or contextual importance.")
st.caption("Muhammad Kamil Shah · PDF extraction · text cleaning · frequency analysis · visualization")
