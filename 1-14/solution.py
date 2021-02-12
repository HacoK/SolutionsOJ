import heapq

class LinkedNode:
    def __init__(self,val):
        self.val=val
        self.link=None
    def __lt__(self, other):
        if self.val<other.val:
            return True
        else:
            return False

def solve(K):
    headList = []
    for i in range(K):
        head = LinkedNode(matrix[i*K])
        cur_node = head
        for j in range(1,K):
            cur_node.link = LinkedNode(matrix[i*K+j])
            cur_node = cur_node.link
        headList.append(head)
    heapq.heapify(headList)
    while len(headList)>1:
        node = heapq.heappop(headList)
        if node.link:
            heapq.heappush(headList,node.link)
        result.append(node.val)
    left = heapq.heappop(headList)
    result.append(left.val)
    while left.link:
        left=left.link
        result.append(left.val)

if __name__=='__main__':
    test_cnt = int(input())
    for t in range(test_cnt):
        K = int(input())
        matrix = [int(x) for x in input().split()]
        result = []
        solve(K)
        print(' '.join(map(str,result)))