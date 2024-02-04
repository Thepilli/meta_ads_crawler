import re

text = "Budapesti bemutatótermünkben reggel 8-tól este 8-ig várjunk szeretettel kedves vásárlóinkat! 💚 Raktári készletünk széles választéka sok lehetőséget biztosít a kényelmes vásárlásra 😉\n\n📅 Hétvégén is nyitva vagyunk\n💨 Több ezer azonnal megvásárolható termék\n🔧 Technikai tanácsadás és szervizszolgáltatások\n🅿 Ingyenes parkolás\n🎮☕Gaming zóna és Alzacafé"

# Define a regex pattern to match emojis
emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # Emoticons
                           u"\U0001F300-\U0001F5FF"  # Miscellaneous Symbols and Pictographs
                           u"\U0001F680-\U0001F6FF"  # Transport and Map Symbols
                           u"\U0001F700-\U0001F77F"  # Alchemical Symbols
                           u"\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
                           u"\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
                           u"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
                           u"\U0001FA00-\U0001FA6F"  # Chess Symbols
                           u"\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
                           u"\U0001F004-\U0001F0CF"  # CJK Compatibility Ideographs Supplement
                           u"\U0001F170-\U0001F251"  # Enclosed Ideographic Supplement
                           "]+", flags=re.UNICODE)

# Use the sub() function to remove emojis from the text
cleaned_text = emoji_pattern.sub(r'', text)

print(cleaned_text)
