movies = {
    "action" : ["avengers","ironman","spiderman","baahubali","robot","KGF",
                "kaala","junglee","batman","superman","kee"],
    "comedy" : ["bala","housefull","dhamaal","golmaal","avengers","sanju"],
    "thriller" : ["ugly","kahani","kee","baahubali","kaala","saw","it"],
    "biopic" : ["sanju","ms dhoni","gandhi","bhagat singh"],
    "horror":  ["the nun","saw","insidious","it"]
    }

user_1 = {"avengers","kee","sanju","robot","KGF","bala","golmaal","KGF","batman"}
user_2 = {"ugly","robot","it","avengers","junglee"}

simMovies = user_1.intersection(user_2)

# Similarity Score => Jaccard Similarity
simScore = {}
for key in movies:
    simScore[key]=  0.0

for key in movies:
    intersection = set(movies[key]).intersection(simMovies)
    union = set(movies[key]).union(simMovies)
    sim = len(intersection) / len(union)
    simScore[key] = round(sim * 100,2)

def show(x):
    return x[1]

print(simScore)
cat = max(simScore.items(), key = show)
rec = user_2.intersection(movies[cat[0]]) - user_1.intersection(movies[cat[0]])
print("Recommended movie for user_1",rec)

rec = user_1.intersection(movies[cat[0]]) - user_2.intersection(movies[cat[0]])
print("Recommended movie for user_2",rec)
