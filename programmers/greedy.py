def solution(routes):
    answer = 0

    camera = -30001

    routes.sort(key = lambda x: x[1])

    for route in routes:
        print(camera, route[0])
        if camera < route[0]:
            answer += 1
            camera = route[1]

    return answer


(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))
