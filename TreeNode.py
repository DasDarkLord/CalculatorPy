from dataclasses import dataclass


@dataclass
class TreeNode:
    type: str
    left: 'TreeNode' = None
    right: 'TreeNode' = None
    value: any = None
    arguments: list = None
