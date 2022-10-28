# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        lsout = []
        i1 = l1.val
        i2 = l2.val
        i3 = i1 + i2
        pst = str(i3)

        node = ListNode(i3 % 10, None)
        m = 0
        if i3 > 9:
            m = 1
        lsout.append(node)
        b1 = True
        b2 = True
        m = 0
        for i in range(0, 101):
            l1 = l1.next
            if l1 == None:
                i1 = 0
                b1 = False
            else:
                i1 = l1.val

            l2 = l2.next
            if l2 == None:
                i2 = 0
                b2 = False
            else:
                i2 = l2.val

            if not b1 and not b2:
                if m == 1:
                    nodecur = ListNode(1, None)
                    lsout[-1].next = nodecur
                    lsout.append(nodecur)
                    return lsout
                else:
                    return lsout

            i3 = i1 + i2 + m
            nodecur = ListNode(i3 % 10, None)
            lsout[-1].next = nodecur
            lsout.append(nodecur)
            if i3 > 9:
                m = 1
            continue

l13  = ListNode(2, None)
l12  = ListNode(1, l13)
l11  = ListNode(3, l12)
l1  = ListNode(1, l11)


l22  = ListNode(1, None)
l21  = ListNode(3, l22)
l2  = ListNode(1, l21)


solv = Solution()

rez = solv.addTwoNumbers(l1, l2)
print(rez)
