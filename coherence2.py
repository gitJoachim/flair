from collections import defaultdict

# Example: Documents and their assigned topics
documents = ["Text of doc 1", "Text of doc 2", "Text of doc 3", "Text of doc 4"]
topics = [0, 0, 1, -1]  # Topic assignments from BERTopic (-1 is noise)

# Group documents by topic
topic_documents = defaultdict(list)
for doc, topic in zip(documents, topics):
    if topic != -1:  # Ignore noise
        topic_documents[topic].append(doc)
        

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load SBERT model
sbert_model = SentenceTransformer("all-MiniLM-L6-v2")

# Compute embeddings for each topic's documents
topic_embeddings = {
    topic: sbert_model.encode(docs)
    for topic, docs in topic_documents.items()
}

 # Calculate coherence for each topic
def calculate_topic_coherence(embeddings):
    # Compute pairwise cosine similarity
    similarity_matrix = cosine_similarity(embeddings)
    # Take the average of the upper triangle (excluding diagonal)
    return np.mean(similarity_matrix[np.triu_indices_from(similarity_matrix, k=1)])

# Topic coherence scores
topic_coherence_scores = {
    topic: calculate_topic_coherence(embeds)
    for topic, embeds in topic_embeddings.items()
}

# Overall coherence score (average across all topics)
overall_coherence_score = np.mean(list(topic_coherence_scores.values()))
print("Overall Topic Coherence Score:", overall_coherence_score)