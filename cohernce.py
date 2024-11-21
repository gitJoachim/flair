from bertopic import BERTopic

# Example: Fit BERTopic
documents = ["This is the first document.", 
             "This is the second document.", 
             "And this is the third document."]
topic_model = BERTopic(embedding_model="all-MiniLM-L6-v2")  # Replace with your SBERT model
topics, probs = topic_model.fit_transform(documents)

# Get top words for each topic
topics_dict = topic_model.get_topics()
topic_words = [
    [word for word, _ in topic_model.get_topic(topic)] 
    for topic in topics_dict.keys() if topic != -1
]

from sentence_transformers import SentenceTransformer

# Load SBERT model
sbert_model = SentenceTransformer("all-MiniLM-L6-v2")  # Replace with the same model as in BERTopic


from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def compute_topic_coherence(topic_words, model):
    coherences = []
    for words in topic_words:
        # Get embeddings for each word
        embeddings = model.encode(words)
        # Compute pairwise cosine similarity
        similarity_matrix = cosine_similarity(embeddings)
        # Take the average of upper triangular matrix (excluding the diagonal)
        avg_coherence = np.mean(similarity_matrix[np.triu_indices_from(similarity_matrix, k=1)])
        coherences.append(avg_coherence)
    return coherences
    
    
    


# Calculate topic coherence scores
topic_coherences = compute_topic_coherence(topic_words, sbert_model)

# Overall coherence score (average across topics)
overall_coherence = np.mean(topic_coherences)
print("Topic Coherence Score:", overall_coherence)

  