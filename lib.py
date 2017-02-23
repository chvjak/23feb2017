
def read_data(file_name):
    f = open(file_name)

    V, E, R, C, X = [int(x) for x in f.readline().strip().split()]

    video_sizes = [int(x) for x in f.readline().strip().split()]

    endpoints = []
    for i in range(E):
        latency, cache_servers = [int(x) for x in f.readline().strip().split()]
        ep = {"latency":latency, "servers": []}
        for j in range(cache_servers):
            server_id, latency =  [int(x) for x in f.readline().strip().split()]
            ep["servers"].append({"id": server_id, "latency": latency})
        endpoints.append(ep)

    requests = []
    for k in range(R):
        video_id, endpoint_id, request_number =  [int(x) for x in f.readline().strip().split()]
        requests.append( {"video_id": video_id,  "endpoint_id" : endpoint_id, "request_number" :  request_number} )


    data = [video_sizes, endpoints, requests]

    return data


def write_data(file_name, data):
    f = open(file_name, "w")

    for line in data:
        f.write(line)

    f.close()