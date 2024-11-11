import spacy
from sklearn.cluster import KMeans
from bertopic import BERTopic
from sklearn.feature_extraction.text import CountVectorizer

# Load spaCy's German model
nlp = spacy.load("de_core_news_md")

# Example list of texts
texts = [
    "Das ist ein Beispieltext.",
    "Ich mag den Service von diesem Geschäft nicht.",
    "Die Lieferung war zu spät.",
    "Das Produkt ist beschädigt angekommen.",
    "Ich bin zufrieden mit dem Einkauf.",
    "Der Kundenservice war hervorragend."
]

# Step 1: Generate embeddings using spaCy
def generate_spacy_embeddings(texts):
    embeddings = []
    for doc in nlp.pipe(texts, disable=["tagger", "parser", "ner"]):  # Use only word vectors
        embeddings.append(doc.vector)  # spaCy's vector representation of the document
    return embeddings

embeddings = generate_spacy_embeddings(texts)

# Step 2: Define KMeans clustering model
n_clusters = 3  # Adjust this based on your dataset
kmeans_model = KMeans(n_clusters=n_clusters, random_state=42)

# Step 3: Initialize BERTopic with custom KMeans clustering
topic_model = BERTopic(
    embedding_model=None,  # We use spaCy embeddings directly
    vectorizer_model=CountVectorizer(ngram_range=(1, 2), stop_words="german"),
    verbose=True
)

# Step 4: Fit BERTopic with KMeans clustering
topics, probs = topic_model.fit_transform(texts, embeddings)

# Assign custom clusters from KMeans
kmeans_model.fit(embeddings)
cluster_labels = kmeans_model.labels_

# Step 5: Visualize or print results
print("Topics assigned by BERTopic:")
print(topic_model.get_topic_info())

# Cluster-based evaluation (if needed)
for i, cluster in enumerate(cluster_labels):
    print(f"Text: {texts[i]} | Cluster: {cluster}")

# Step 6: Visualize topics
topic_model.visualize_topics()



###

from sklearn.metrics import silhouette_score

silhouette = silhouette_score(embeddings, cluster_labels)
print("Silhouette Score:", silhouette)

###
from sklearn.feature_extraction.text import CountVectorizer
from bertopic import BERTopic

# Initialize BERTopic with CountVectorizer that uses stopwords
vectorizer_model = CountVectorizer(ngram_range=(1, 2), stop_words="german")

# Initialize BERTopic
topic_model = BERTopic(
    embedding_model=None,  # Use custom embeddings (spaCy in this case)
    vectorizer_model=vectorizer_model,  # Stopwords applied here
    verbose=True
)

# Fit BERTopic with embeddings and texts
topics, probs = topic_model.fit_transform(texts, embeddings)

# Print clean topic information
print(topic_model.get_topic_info())


