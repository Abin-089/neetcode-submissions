class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        result = []

        while curr:
            group = []

            for _ in range(k):
                if not curr:
                    break

                group.append(curr.val)
                curr = curr.next

            if len(group) == k:
                group.reverse()

            result.extend(group)

        res = ListNode(0)
        cur = res

        for node in result:
            cur.next = ListNode(node)
            cur = cur.next

        return res.next