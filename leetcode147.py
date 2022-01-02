# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def insertionSortList(self, head):
        if head==None:
            return head
        #在开头建一个无穷小节点，保证所有节点都大于该节点，方便后面代码撰写
        res=ListNode(-float('inf'))
        res.next=head
        now=head
        cur=head.next
        while cur:
            #如果尾节点小于要判断的节点，则直接略过
            if cur.val>=now.val:
                cur,now=cur.next,cur
            else:
                pre=res
                #将尾节点的next指向下一个要判断的节点
                now.next=cur.next
                #循环到左小右大的位置
                while pre.next.val<cur.val:
                    pre=pre.next
                #将目标节点插入特定位置
                tmp=pre.next
                pre.next=cur
                cur.next=tmp
                #重新指向下一个要判断的节点，方便下一轮循环
                cur=now.next
        return res.next
if __name__ == "__main__":
    s = Solution()
    l = head = ListNode(None)
    for val in [4,2,1,3]:
        l.next = ListNode(val)
        l = l.next

    li = s.insertionSortList(head.next)
    while li:
        print(li.val)
        li = li.next