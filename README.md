# Key-Value Store
A distributed key value store implementation which uses Paxos made simple by Leslie Lamport to reach consensus.
Here I am using dockers to setup a 3 node Paxos cluster which sits behind a proxy node.
Proxy node also acts as a Load balancer which takes incoming requests and forwards it to Paxos cluster in Round robin fashion.
The Key-Value store offers two operations GET and POST.

 # PAXOS
 There are three basic roles:
  * Proposers that propose a value for consensus.
  * Acceptors that choose the consensus value.
  * Learners that learn the consensus value.
  A single process may take on multiple roles.
  
 ## Failure Assumptions
 * Processes can only fail by Crashing.
 * Value Errors, Message omission errors are ignored.

  ## Steps:
  After cloning the repository, perform the below steps to start the Paxos cluster and Proxy server instance.

  * ```docker-compose up```
  * To set a key value pair
    ```curl -X POST "http://localhost:8081/" -d "{\"key1\":\"val1\"}"```
  * To get a key value pair 
    ```curl -X GET "http://localhost:8081/key=key1"```
  
 ## References
 [Paxos Made Simple by Leslie Lamport] (https://lamport.azurewebsites.net/pubs/paxos-simple.pdf)
 
