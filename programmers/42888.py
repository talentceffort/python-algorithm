# 2019 KAKAO BLIND RECRUITMENT
# 오픈채팅방
def solution(record):
    answer = []
    user = {}
    result = []

    for i in record:
        s = i.split(" ")
        length = len(s)
        command = s[0]
        uid = s[1]

        if length == 3:
            name = s[2]

        if s[0] == "Enter" or s[0] == "Change":
            save_user(user, uid, name)

        if s[0] == "Enter" or s[0] == "Leave":
            answer.append(make_string(s[0], uid))

    for word in answer:
        s = word.split("-")
        result.append(user[s[0]] + s[1])

    return result


def make_string(word, uid):
    if word == "Enter":
        return uid + "-님이 들어왔습니다."
    return uid + "-님이 나갔습니다."


def save_user(user, uid, nickname):
    user[uid] = nickname


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]

print(solution(record))
