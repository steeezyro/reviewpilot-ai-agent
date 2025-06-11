
SUMMARY_PROMPT = """
You are a product copywriter.

Summarize the following product page content in an enthusiastic, Gen Z-friendly tone that could appear on a product listing:

{content}
"""

CRITIQUE_PROMPT = """
You are an expert UX/product reviewer.

Read the following product page content and identify 3-5 things that are unclear, missing, or could confuse potential buyers:

{content}
"""

FAKE_REVIEWS_PROMPT = """
Generate 3 fake customer reviews for the following product based on its description and tone. Make one super enthusiastic, one neutral, and one skeptical:

{content}
"""
