movies = {
    "action" : ["avengers","ironman","spiderman","baahubali","robot","KGF",
                "kaala","junglee","batman","superman","kee"],
    "comedy" : ["bala","housefull","dhamaal","golmaal","avengers","sanju"],
    "thriller" : ["ugly","kahani","kee","baahubali","kaala","saw","it"],
    "biopic" : ["sanju","ms dhoni","gandhi","bhagat singh"],
    "horror":  ["the nun","saw","insidious","it"]
    }

user = {"avengers","kee","sanju","robot","KGF","bala","golmaal"}

# Similarity Score => Jaccard Similarity
simScore = {}
for key in movies:
    simScore[key]=  0.0

for key in movies:
    intersection = set(movies[key]).intersection(user)
    union = set(movies[key]).union(user)
    sim = len(intersection) / len(union)
    simScore[key] = round(sim * 100,2)

def show(x):
    return x[1]

print(simScore)
cat = max(simScore.items(), key = show)
recommended = set(movies[cat[0]]) - user
print("Recommended Movies are",recommended)
