from collections import defaultdict
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Example Inputs: Replace these with your actual data
documents = ["Text of document 1", "Text of document 2", "Text of document 3"]
topics = [0, 0, 1]  # Topic assignments from BERTopic (use model.fit_transform to get this)
document_embeddings = np.random.rand(len(documents), 384)  # Replace with actual SBERT embeddings

# Step 1: Group document embeddings by topic
topic_embeddings = defaultdict(list)
for doc, topic, embedding in zip(documents, topics, document_embeddings):
    if topic != -1:  # Ignore noise
        topic_embeddings[topic].append(embedding)

# Step 2: Calculate the centroid (mean) for each topic
topic_centroids = {
    topic: np.mean(embeddings, axis=0)
    for topic, embeddings in topic_embeddings.items()
}

# Step 3: Compute distances of each embedding to the topic centroid
topic_distances = {
    topic: [np.linalg.norm(embedding - centroid) for embedding in embeddings]
    for topic, (centroid, embeddings) in zip(topic_centroids.keys(), topic_embeddings.items())
}

# Step 4: Measure density using average distance
topic_density = {
    topic: 1 / np.mean(distances)  # Higher value = denser topic
    for topic, distances in topic_distances.items()
}

# Or measure density using variance
topic_variance = {
    topic: np.var(distances)  # Lower variance = denser topic
    for topic, distances in topic_distances.items()
}

# Step 5: Optionally calculate pairwise similarity within each topic
topic_pairwise_similarity = {
    topic: np.mean(cosine_similarity(embeddings))
    for topic, embeddings in topic_embeddings.items()
}

# Step 6: Sort topics by density
sorted_density = sorted(topic_density.items(), key=lambda x: x[1], reverse=True)
print("Topics Ranked by Density:", sorted_density)

# Output Example: Densities and Variances for topics
print("Topic Density Scores:", topic_density)
print("Topic Variance Scores:", topic_variance)
print("Pairwise Similarity Scores:", topic_pairwise_similarity)
