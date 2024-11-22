from top2vec import Top2Vec

# Step 1: Load Data
documents = [
    "I love playing football with my friends on weekends.",
    "Artificial intelligence is transforming the world.",
    "Quantum computing will change the future of technology.",
    "The soccer match last night was incredible.",
    "Machine learning is a subset of artificial intelligence.",
    "The latest advancements in AI are amazing.",
    "Football is one of the most popular sports globally.",
    "Deep learning is a revolutionary technology."
]

# Step 2: Train Top2Vec Model
model = Top2Vec(documents, speed="learn", workers=4)  # Adjust speed and workers based on your resources

# Step 3: Explore Topics
# Get number of topics
print(f"Number of topics: {model.get_num_topics()}")

# View top words for each topic
topic_words, word_scores, topic_nums = model.get_topics()
for i, words in enumerate(topic_words):
    print(f"Topic {i}: {words}")

# Get topic sizes
topic_sizes, topic_nums = model.get_topic_sizes()
print("Topic Sizes:", topic_sizes)

# Step 4: Retrieve Representative Documents
# Example: Get 3 representative documents for Topic 0
docs, doc_scores = model.search_documents_by_topic(topic_num=0, num_docs=3)
for doc, score in zip(docs, doc_scores):
    print(f"Document (Score: {score}): {doc}")

# Step 5: Search for Documents by Keywords
# Example: Search for documents about "football"
docs, doc_scores = model.search_documents_by_keywords(keywords=["football"], num_docs=3)
for doc, score in zip(docs, doc_scores):
    print(f"Document (Score: {score}): {doc}")

# Step 6: Visualize Topics
# Generate word cloud for a specific topic
model.generate_topic_wordcloud(topic_num=0)

# Visualize topic distribution
model.visualize_topics()

# Visualize topic hierarchy (reduce topics to 5)
model.hierarchical_topic_reduction(num_topics=5)
model.visualize_hierarchy()

# Step 7: Save and Load the Model
# Save the model
model.save("top2vec_model")

# Load the model
model = Top2Vec.load("top2vec_model")
