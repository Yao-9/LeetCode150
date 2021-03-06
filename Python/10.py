# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
  # @param head, a ListNode
  # @return a list node
  def detectCycle(self, head):
	fast = head
	slow = head
	isCycle = False
	while fast != None and fast.next != None:
		fast = fast.next.next
		slow = slow.next
		if fast == slow:
			isCycle = True
			break

	if not isCycle:
		return None

	slow = head
	while fast != slow:
		fast = fast.next
		slow = slow.next

	return slow
