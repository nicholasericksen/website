# SDK of Pure HTTP?

Whenever I try and integrate with a new system and leverage there API it always seems
I am faced with two choices; use pure HTTP requests or try there SDK for whatever specific language.
Over the years I have really become engrained with the idea that using pure HTTP is always the way to go.
And there are a few reasons for that.

When using a standard HTTP client library such as Python `requests` or  Go `net/http`, you get the exact
same experience accross every single application you are trying to integrate with.
With most REST based HTTP APIs building the request is fairly standard as well since they all use 
standard HTTP methods, JSON, URL parameters, etc. A little bit of understanding of how the basics of 
HTTP works under the hood and networking can go a long way to make ever intergration as seamless as possible.

Second it is usually the most up to date way of interfacing with the 3rd party application. No lag time between 
SDK development and the API itself. 

## Example
Recently I was trying out the Go Kubos RPC client listed [here](https://pkg.go.dev/github.com/ipfs/kubo/client/rpc).
For the life of me I couldn't see how to add a new file to an IPFS cluster.
To this day I still don't know if it is possible, but reach out if you know. It certainly isn't very obvious.
This HTTP client wraps itself around and around and around...
Going to the standard [docs](https://docs.ipfs.tech/reference/kubo/rpc/#getting-started) for the IPFS API showed the `Add`
command as the first listed entry.
No need for specialized documentation, I just had to go back to my old friend `net/http` and formulate the HTTP request.
They even provided a CURL command example which makes it super easy to reason about.
Don't get me started on POSTMan. That's for another time.

## Conclusion
So what are those silly wrappers really doing for us anyway?

Here is a bit of networking debugging tools in case it helps.
```
Ping. Telnet. Curl. TCPDump. Strace.
```

Using standards makes life a whole lot easier. That's probably why 
we create them in the first place.
