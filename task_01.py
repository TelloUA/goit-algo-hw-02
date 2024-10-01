import queue

q = queue.Queue()

request_number = 0;
def create_request_name():
    global request_number
    name = 'request_' + str(request_number)
    request_number += 1
    return name

def generate_request():
    request = create_request_name()
    q.put(request)

def process_request():
    if not q.empty():  
        processed = q.get()
        print(processed, 'was processed')
    else:
        print('Queue was empty')

def main():
    i = 0
    while i < 6:
        generate_request()
        process_request()
        process_request()
        i += 1

if __name__ == "__main__":
    main()