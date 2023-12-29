First try at doing a Chatroom. It was a good experience. I tried to do it in Python since is the language I'm more familiar with, but still, it wasn't an easy task. I had to learn sockets and relearn concurrency and parallelism. Structures to manage I/O blocking code.

A note on my understanding. Parallelism is a subset of concurrency. I'd say concurrency means executing things simultaneously, not necessarily at the same time. Parallelism is a way of doing this using the processor cores. It does run things at the same time and I believe is the only that really does things at the same time. Threading is another, the code uses threads (I thing that the OS manages) and changes between them really quickly that it seems as those are being done at the same time.

Async is another approach where threads are not used. Not sure how that works, but I think this won't work for sockets. I believe async works for external resources (calling an API) and not for something I/O blocking like input or checking a socket, but now than I'm writing this it may be more like of putting processes on the background. Again, not really now how that will work.

Just a brainstorm.
