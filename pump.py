import argparse
from redis_q import RedisQueue

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--param", required=True,
                        help="Parameter to pass into redis")
    parser.add_argument("--redishost", default="127.0.0.1",
                        help="Address at which the redis server can be reached")
    parser.add_argument("--redisport", default="6379",
                        help="Port on which redis is available")
    parser.add_argument("-i", "--input", action='store_true',
                        help='Send message to input queue')
    args = parser.parse_args()

    if args.input:
        redis_queue = RedisQueue(args.redishost, port=int(args.redisport), prefix='input')
    else:
        redis_queue = RedisQueue(args.redishost, port=int(args.redisport))
    redis_queue.connect()

    if args.param == 'None':
        redis_queue.put(None)
    else:
        redis_queue.put(int(args.param))
    print(f"Pushed {args.param} to Redis")
