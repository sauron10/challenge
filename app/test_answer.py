import queens

CORRECT_ANSWER={
  1:1,
  2:0,
  3:0,
  4:2,
  5:10,
  6:4,
  7:40,
  8:92,
  9:352,
  10:724,
  11:2680,
  12:14200,
  13:73712,
  14:365596,
  # 15:2279184,
  # 16:14772512,
  # 17:95815104,
  # 18:666090624,
  # 19:4968057848,
  # 20:39029188884,
  # 21:314666222712,
  # 22:2691008701644,
  # 23:24233937684440,
  # 24:227514171973736,
  # 25:2207893435808352,
  # 26:22317699616364044,
  # 27:234907967154122528 
}

def test_number_of_answers()-> None:
  for key in CORRECT_ANSWER:
    print(f'N = {key}')
    answer = queens.main(key)
    assert answer == CORRECT_ANSWER[key]
    print()

# This are test of tools and probably would change, not exactly suitable for TDD 

# def test_diagonals():
#   arr = queens.getDiagonal(queens.Point(1,3),4)
#   arr1 = queens.getDiagonal(queens.Point(0,2),4)
#   assert arr == [str(queens.Point(0,2)),str(queens.Point(2,2)),str(queens.Point(3,1))]
#   assert arr1 == [str(queens.Point(2,0)),str(queens.Point(1,1)),str(queens.Point(1,3))]

# def test_rec_search():
#   assert queens.recursiveSearch(2,[[8,9,7,4,[1]],5])
   