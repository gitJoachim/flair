import re
import kfp
from kfp import dsl
from typing import List

# List of greetings in lowercase
greetings = [
    "mit freundlichen grüßen", "mit besten grüßen", "mit herzlichen grüßen",
    "freundliche grüße", "beste grüße", "hochachtungsvoll", "herzliche grüße",
    "mit vorzüglicher hochachtung", "viele grüße", "liebe grüße", "sonnige grüße",
    "warme grüße", "schöne grüße", "beste wünsche", "herzlichst", "alles liebe",
    "mfg", "vg", "lg", "bg", "sg", "hg", "servus", "grüße aus", "ciao", "grüß dich",
    "grüß gott", "bis bald", "tschüss", "mach's gut", "ade", "pfiat di", "baba",
    "peace und liebe", "bis die tage", "bleib stark", "mit feinstem gruß"
]

# Create regex pattern to match any greeting followed by up to three words
pattern = r'(' + '|'.join(re.escape(g) for g in greetings) + r')\s+([a-z]+(?:\s+[a-z]+){0,2})'

# Function to find up to three words after greetings in text
def find_up_to_three_words_in_text(text: str) -> List[str]:
    matches = re.findall(pattern, text)
    results = [f"Greeting: {match[0]}, Words: {match[1]}" for match in matches]
    return results

# Kubeflow component for text processing
@dsl.component
def process_text_up_to_three_words_component(texts: List[str]) -> List[str]:
    results = []
    for text in texts:
        results.extend(find_up_to_three_words_in_text(text))
    return results
