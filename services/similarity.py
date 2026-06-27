from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(resume_text, job_description):
    """
    Calculate similarity score between resume and job description.
    Parameters
    ----------
    resume_text : str
        Extracted resume text.
    job_description : str
        Job description entered by user.
    Returns
    -------
    float
        Similarity percentage (0 - 100).
    """

    # Handle empty inputs
    if not resume_text.strip() or not job_description.strip():
        return 0.0

    # Create TF-IDF vectors
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform([resume_text,job_description])

    # Calculate Cosine Similarity
    similarity = cosine_similarity(vectors[0:1],vectors[1:2])[0][0]

    similarity_percentage = round(similarity * 100,2)
    return similarity_percentage