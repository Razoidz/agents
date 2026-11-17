import re

pattern = re.compile(r'\d{4}')
result = pattern.search("My PIN is ABDC")
print(result)

# def white_rook_can_capture(rook, chess_board):
#     collector = []
#     for square, piece in chess_board.items():
#         if piece[0] == 'a' and(square[0] == rook[0] or square[1]   == rook[1]):
#             collector.append(square)
#     return collector
# #print(white_rook_can_capture('d3', {'d7': 'bQ', 'd2': 'wB', 'f1': 'bP', 'a3': 'bN'}))
# print(white_rook_can_capture(
#     'a1',
#     {
#         'a5': 'aQ',
#         'b1': 'bP',
#         'c3': 'bN',
#         'h8': 'bK'
#     }
# ))

