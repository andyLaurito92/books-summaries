Protocol over TCP that creates long-lived connections. These are useful for chat, real feed applications. 

They were created around 2008. You can read more about webscoekts [here](https://websocket.org/guides/road-to-websockets/)

In this playground I will create a small websocket server/client using python


## SSE (server side events) vs webscokets

Server side events is a unidirectional chat, where the server pushes updates to the client, while websockets is a full-duplex 
communication (both client and server are continously sending events)

- It's also implemented over HTTP


## HTTP streaming

- The server keeps the HTTP connection open, and sends responses in chunks instead of sending everything at once
- There are 2 usual ways of implementing HTTP streaming:
	- Chunked Transfer Encoding (HTTP/1.1)
		- In order to implement HTTP streaming on the server side you need to set HTTP header `Transfer-Encoding: chunked`
	- SSE (high level protocol implemented over HTTP)
	


## Reference about this topic

[High performance browser networking book](https://hpbn.co/) -> covers all you need to now regarding the client-server web
development
