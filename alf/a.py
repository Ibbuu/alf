def make_handler(large_buffer):
    cache_ref = large_buffer
    def handler(task):
        return process(task, cache_ref)
    return handler


