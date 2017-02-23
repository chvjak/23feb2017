import lib




def solve(data):
    totals, video_sizes, endpoints, requests = data
    V, E, R, C, X = totals

    def get_best_request(c, leftover_capacity):
        max_score = 0
        best_request = None
        for r in requests:
            video_id, endpoint_id, request_number = r.values()

            ep = endpoints[endpoint_id]
            if c not in ep["servers"].keys():
                continue

            if leftover_capacity < video_sizes[video_id]:
                continue

            latency = ep["servers"][c]
            score = ((ep["latency"] - latency) * r["request_number"]) / video_sizes[video_id]

            if score > max_score:
                max_score = score
                best_request = r


        return best_request


    res = [None] * C
    loc = [X] * C   # leftover capacities


    distribute_count = 10000
    while len(requests) > 0 and distribute_count > 0:
         distributed = False
         for c in range(C):
            r = get_best_request(c, loc[c])
            if r is not None:
                distributed = True
                if res[c] is None:
                    res[c] = set()

                if r["video_id"] not in res[c]:
                    loc[c] -= video_sizes[r["video_id"]]

                    res[c].add(r["video_id"])

                requests.remove(r)
                distribute_count -= 1

         if not distributed:
            break


    return res

data = lib.read_data("videos_worth_spreading.in")  #<class 'list'>: [10000, 100, 100000, 100, 10000]
#data = lib.read_data("kittens.in")  #<class 'list'>: [10000, 100, 100000, 100, 10000]
#data = lib.read_data("trending_today.in")          #<class 'list'>: [10000, 100, 100000, 100, 50000]
#data = lib.read_data("me_at_the_zoo.in")            #<class 'list'>: [100, 10, 100, 10, 100]


solution = solve(data)

lib.write_data("output1.txt", solution)


