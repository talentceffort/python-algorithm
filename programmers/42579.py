def solution(genres, plays):
    answer = []
    playDict = {}
    d = {}

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]

        playDict[genre] = playDict.get(genre, 0) + play
        d[genre] = d.get(genre, []) + [(play, i)]


    sorted_genre = sorted(playDict.items(), key=lambda x: x[1], reverse=True)

    for genre, totalPlay in sorted_genre:
        d[genre] = sorted(d[genre], key=lambda x: (-x[0], x[1]))

        answer += [idx for play, idx in d[genre][:2]]


    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
