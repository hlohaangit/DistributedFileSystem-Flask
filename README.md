# Quick Start

## Design and Implementation

### File Identification

To avoid duplicate file names and confusion in fetching the right file, LocalDFS assigns a unique key (id) to each uploaded file. Clients must store the file-id to access the file.

### Machine Identification

In a cluster of multiple machines, it is important to identify each machine when allocating file partitions and searching for file partitions. LocalDFS uses a stable identifier, such as a unique machine-id, to address this issue. Each machine in the cluster stores its machine-id persistently, ensuring it remains unchanged even in case of failures. Additionally, LocalDFS maintains mapping relationships between IP addresses and machine-ids to handle changes in IP addresses.

### Hashing

LocalDFS uses hashing on file-ids to determine which machine to allocate a file to. It employs a consistent-hashing algorithm and builds a Hash Ring to facilitate this process. At startup, each machine in the cluster obtains the machine-ids of all other machines and constructs a complete mapping of IP addresses to machine-ids. The Hash Ring is then created based on the sorted machine-ids.

### Storing a File Workflow

The workflow for storing a file in LocalDFS is as follows:

1. The user provides a list of IPs (IP List) in the code, and multiple machines run the code, making all machines/nodes equivalent and aware of each other.
2. A client sends a request to store a file segment. A server (e.g., ip-1) receives the request, generates a file-id using a hash function, and returns the file-id to the client. The client must remember the file-id for future file access.
3. The server determines which machine to store the file by generating a hash-value using another hash function on the file-id and checking the Hash Ring.

## Fault Tolerance

Currently, LocalDFS does not provide strong fault tolerance by creating replicas for each file partition. However, users can implement their own fault-tolerant strategies, such as making multiple storage/query API calls using different hash functions.
