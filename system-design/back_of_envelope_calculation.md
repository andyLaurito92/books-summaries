# Back of the envelope Calculation, alias, Resource calculation

This concept means doing math: The main idea is just to do a quick estimate over the math on 
- Storage
- CPU usage
- Requests per second
- TCP connections

so we can track how many resources will we need for our system. This is the step where we do
some math to calculate concrete numbers on what will we need for our syste.
Think on CERN, when simulating network traffic to understand what type of devices will we need
for supporting the new ATLAS network.

## Standard numbers to remember

| Component                                        | Time (nanoseconds) 10^-9 seconds | Time (seconds) |
| L1 cache                                         | 0.9                              | 9 * 10^-10     |
| L2 cache                                         | 2.8                              |                |
| L3 cache                                         | 12.9                             |                |
| Main memory                                      | 100                              |                |
| Compress 1KB w/snzip                             | 3.000 (3 microseconds)           |                |
| Read 1MB sequentially from memory                | 9.000                            |                |
| Read 1 MB sequentially from SSD                  | 200.000                          | 0,0002         |
| Round trip within same datacenter                | 500.000                          |                |
| Read 1MB sequentially from SSD w/speed ~ 1GB/sec | 1.000.000 (1 millisecond)        | 0,001          |
| Disk seek                                        | 4.000.000 (4 milliseconds)       | 0,004          |
| Read 1MB from sequentially from disk             | 2.000.000 (2 milliseconds)       | 0,002          |
| Send packets SF -> NYC                           | 71.000.000 (71 milliseconds)     | 0,71           |

