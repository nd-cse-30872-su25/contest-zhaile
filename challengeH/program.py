#!/usr/bin/env python3
import sys
from collections import defaultdict

def parse_input():
    lines = sys.stdin.readlines()
    if not lines:
        return None, None, None, None

    line_iter = iter(lines)
    num_families = int(next(line_iter).strip())
    family_lines = [next(line_iter).strip() for _ in range(num_families)]
    num_givers = int(next(line_iter).strip())
    givers = [next(line_iter).strip() for _ in range(num_givers)]

    parents_to_children = {}
    child_to_parents = {}
    spouses = {}

    for line in family_lines:
        if not line or ':' not in line:
            continue

        parents_str, children_str = line.split(':', 1)
        parents = tuple(sorted(parents_str.strip().split()))
        children = children_str.strip().split()

        parents_to_children[parents] = children
        # print(parents_to_children)

        for child in children:
            child_to_parents[child] = parents
        # print(child_to_parents)

        if len(parents) == 2:
            p1, p2 = parents
            spouses[p1] = p2
            spouses[p2] = p1

    return parents_to_children, child_to_parents, spouses, givers

def get_siblings(person, child_to_parents, parents_to_children):
    if person not in child_to_parents:
        return set()

    my_parents = child_to_parents[person]
    siblings = set()

    for parent in my_parents:
        for parent_pair, children in parents_to_children.items():
            if parent in parent_pair:
                siblings.update(children)

    siblings.discard(person)
    return siblings

def get_own_children(person, parents_to_children):
    children = set()
    for parent_pair, kids in parents_to_children.items():
        if person in parent_pair:
            children.update(kids)
    return children

def get_niblings(giver, spouses, child_to_parents, parents_to_children):
    all_siblings = set()
    all_siblings.update(get_siblings(giver, child_to_parents, parents_to_children))
    if giver in spouses:
        spouse = spouses[giver]
        all_siblings.update(get_siblings(spouse, child_to_parents, parents_to_children))
    nieces_and_nephews = set()
    for sibling in all_siblings:
        for parent_pair, kids in parents_to_children.items():
            if sibling in parent_pair:
                nieces_and_nephews.update(kids)
    nieces_and_nephews -= get_own_children(giver, parents_to_children)

    return sorted(nieces_and_nephews)

def solve_niblings_updated():
    parents_to_children, child_to_parents, spouses, givers = parse_input()
    if not givers:
        return

    for giver in givers:
        if not giver:
            continue

        niblings = get_niblings(giver, spouses, child_to_parents, parents_to_children)

        if not niblings:
            print(f"{giver} does not need to buy gifts")
        else:
            print(f"{giver} needs to buy gifts for: {', '.join(niblings)}")


solve_niblings_updated()
