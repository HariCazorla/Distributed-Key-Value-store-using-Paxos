# key-store
A distributed key value store implementation which uses Simple Paxos to reach consensus.

Sample commands:

1. curl -X POST "http://localhost:8081/" -d "{\"k\":\"v\"}"