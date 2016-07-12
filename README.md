# InsightDataScienceCodingChallenge

**About environment/libraries:**  
The program median_degree.py runs under Python 3.5.1.  
Two libraries, json and time, were imported by the program to handle json data structure and time format.  
  
**Reading data from input file**  
The program includes exception handling to exclude the transactions with missing values in any field. In addition, incorrect time format or user names with empty strings or only spaces are also treated as missing values and excluded.  
  
**Explanation of the solution and data structure**  
A linked list is created to store all payment transactions within the 60-seconds window, with the order of actual transaction time. Each time a new transaction arrives, depending on its transaction time, it will be either ignored, or inserted into the right position in linked list. If a new node is added to the end of the list, which means a new maximum timestamp appears, then those nodes outside the 60-s window will be deleted from the beginning of the list.
To handle user relationship graph information, two dictionaries (hash tables) are used, with one for adjacency list (key: user pair tuple; value: number of transactions happened in the 60-s window), and the other one for degree of vertex (key: user name; value: degree of vertex). Each time a new node is added, the user pair information will be checked against the first dictionary. If transaction between the two users never happened, the user pair will be added to the dictionary with "redundancy" of 1, and the degree of vertex values for both users will be updated into the second dictionary; If transaction between these two users already exists, only the corresponding "redundancy" value in first dictionary needs to be increased by 1, and there is no need to update the second dictionary for degrees of vertex. When a node is removed from linked list, the process is opposite. If "redundancy" value for transaction between a pair of users is decreased to 0, we need to remove the pair from the first dictionary and update the degree of vertex for each user in the second dictionary. And when the degree of vertex for a user is dropped to 0, the user will be deleted from the second dictionary.  
Depending on actual time of each transaction, adding a payment node (and deleting old payment nodes accordingly) takes O(n) time for worst case, where n is the number of transactions in 60-s window. The calculation of median degree involves a sort process which takes O(nlogn) time for worst case, where n is the number of users in 60-s window. So overall, the processing time follows the longer one.
  
**Testing**
In addtion to the testing defined by the requirements, I have also included a python code unit_testing.py and a shell script named unit_testing.sh in insight_testsuite folder. The unit tests were done for important classes and methods in median_degree.py.  
