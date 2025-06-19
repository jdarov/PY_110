"""
P :
    Building blocks must be cubes (YxYxY)
    Built in layers
    Top layer is a single block
    One Block in Upper Layer must be supported by 4 blocks in lower layer
    A block in lower layer can support more than one block in an upper layer
    Can not leave gaps between blocks 

    Input - integer representing number of total available blocks
    output - integer representing total number of leftover blocks after structure is built

    explicit - top layer is a single block (how big are the blocks?)
        each layer below it will be 4 blocks or more (each upper MUST be supported by 4 lower)
        a lower block can carry more than one block (how many blocks can a lower block carry?)
    implicit: one layer holds one, two layers must hold at least 5 blocks (so 2 - 4 blocks leftover = x - 1)
        layers  []
                [][][][]
                [][][][][][][][][]
        layer number is directly related to number of blocks in that layer
        layer number**2 represents # of blocks in that layer 
E: 
    print(calculate_leftover_blocks(0) == 0)  # True
    print(calculate_leftover_blocks(1) == 0)  # True
    print(calculate_leftover_blocks(2) == 1)  # True
    print(calculate_leftover_blocks(4) == 3)  # True
    print(calculate_leftover_blocks(5) == 0)  # True
    print(calculate_leftover_blocks(6) == 1)  # True
    print(calculate_leftover_blocks(14) == 0) # True

    Test cases confirm that the number of blocks in each layer directly correlates
    Relationship between remaining blocks is sum(row1, row2, etc) - # bocks being used 
    We build all rows up to the final one before calculating leftover blocks

    leftover(7) == 2
    leftover(8) == 3
    leftover(9) == 4
    leftover(10) == 5
    leftover(11) == 6
    leftover(12) == 7
    leftover(13) == 8 

D :
    list? (integers) 
    integers 

A :
    take an integer (number of blocks)
    build our layers in the structure, starting at layer 0
    loop through that number building our structure with each layer as we go through 
    for every block used in a layer subtract those blocks from blocks remaining
    increment to next layer
    when we reach a point that we don't have enough blocks to continue (eg 8 blocks instead of 9 for layer 3) we
        stop and return that number of blocks remining
"""
def calculate_leftover_blocks(blocks):
    layer = 0

    while blocks >= layer**2:
        blocks -= layer**2
        layer += 1
    return blocks

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True