#! /usr/bin/env python3
import sys
from dataclasses import dataclass
from typing import Optional
from collections import deque

@dataclass
class Node:
    val: Optional[int] = None
    left: Optional["Node"] = None
    right: Optional["Node"] = None

@dataclass
class Tree:
    root: Optional["Node"] = None
    def make_tree(self, nums):
        if not nums or nums[0] == 0:
            self.root = None
            return

        self.root = Node(nums[0])
        node_queue = deque([self.root])
        index_queue = deque([0])

        while node_queue:
            curr = node_queue.popleft()
            idx = index_queue.popleft()

            left_idx = 2 * idx + 1
            right_idx = 2 * idx + 2

            if left_idx < len(nums) and nums[left_idx] != 0:
                curr.left = Node(nums[left_idx])
                node_queue.append(curr.left)
                index_queue.append(left_idx)

            if right_idx < len(nums) and nums[right_idx] != 0:
                curr.right = Node(nums[right_idx])
                node_queue.append(curr.right)
                index_queue.append(right_idx)

    def print_tree(self):
        stack = [self.root]
        while stack:
            cur = stack.pop()
            print(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
    def find_target(self,target):
        res = []

        def dfs(node, path, total):
            if not node:
                return

            path.append(node.val)
            total += node.val
            if not node.left and not node.right:
                if total == target:
                    res.append(path[:])

            dfs(node.left, path, total)
            dfs(node.right, path, total)

            path.pop()  

        dfs(self.root, [], 0)
        res =sorted(res)
        # print(res)
        # res.sort()
        for item in res:
            print(f"{target}: {", ".join(map(str,item))}")
        if not res:
            print()



# t = Tree()
# t.make_tree([5, 4, 8, 11, 0, 13, 4, 7, 2, 0, 0, 0, 0, 5, 1])
# # t.print_tree()
# # print(t.root)
# t.find_target(22)

for line in sys.stdin:
    target = int(line.strip())
    nums = list(map(int,sys.stdin.readline().strip().split()))
    # print(target, nums)
    tree = Tree()
    tree.make_tree(nums)
    tree.find_target(target)





