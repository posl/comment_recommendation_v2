def levelOrder(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        level_nodes = []
        for _ in range(level_size):
            node = queue.popleft()
            if node:
                level_nodes.append(node.val)
                # 子がいない場合にはNoneを追加する
                queue.append(node.left or None)
                queue.append(node.right or None)
            else:
                level_nodes.append(None)

        # 末尾のNoneを削除
        while level_nodes and level_nodes[-1] is None:
            level_nodes.pop()

        result.extend(level_nodes)
    return result