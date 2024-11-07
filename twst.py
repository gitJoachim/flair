import re

# List of greetings (as expanded in the CSV file)
greetings = [
    "mit freundlichen grüßen", "mit besten grüßen", "mit herzlichen grüßen",
    "freundliche grüße", "beste grüße", "hochachtungsvoll", "herzliche grüße",
    "mit vorzüglicher hochachtung", "viele grüße", "liebe grüße", "sonnige grüße",
    "warme grüße", "schöne grüße", "beste wünsche", "herzlichst", "alles liebe",
    "mfg", "vg", "lg", "bg", "sg", "hg", "servus", "grüße aus", "ciao", "grüß dich",
    "grüß gott", "bis bald", "tschüss", "mach's gut", "ade", "pfiat di", "baba", 
    "peace und liebe", "bis die tage", "bleib stark", "mit feinstem gruß"
    # Add all other variations as needed
]

# Create a regex pattern to match any greeting followed by words (e.g., names)
pattern = r'(' + '|'.join(re.escape(g) for g in greetings) + r')\s+([a-z]+(?:\s+[a-z]+)*)'

# Sample text (all lowercase)
texts = [
    "vielen dank für ihre hilfe. mit freundlichen grüßen joachim müller",
    "ich melde mich später. liebe grüße anna",
    "vielen dank, mfg max mustermann",
    "bis bald, servus marco reus"
]

# Function to find and print all names after the greeting
def find_names(texts):
    for text in texts:
        matches = re.findall(pattern, text)
        for match in matches:
            greeting, name = match
            print(f"Greeting: {greeting}, Name: {name}")

# Run the function on sample texts
find_names(texts)