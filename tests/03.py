test = {
  'name': 'Question 3',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> take_turn(2, 0, make_test_dice(4, 5, 1))
          872dbe4a4fe5d8451aa842c21194c866
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> take_turn(3, 0, make_test_dice(4, 6, 1))
          43d176e102c8d95338faf8791aa509b3
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> take_turn(0, 16)
          c42887e7b9ffe8fc26bb57b61329f916
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> take_turn(0, 47)
          872dbe4a4fe5d8451aa842c21194c866
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> take_turn(0, 7)
          43d176e102c8d95338faf8791aa509b3
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> take_turn(2, 0, make_test_dice(6))
          12
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> take_turn(9, 0, make_test_dice(4))
          36
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> take_turn(7, 0, make_test_dice(4))
          28
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> take_turn(8, 0, make_test_dice(5))
          40
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> hog.take_turn(5, 0) # Make sure you call roll_dice!
          Called roll dice!
          9002
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import hog
      >>> def roll_dice(num_rolls, dice):
      ...     print("Called roll dice!")
      ...     return 9002
      ...
      >>> hog.roll_dice, old_roll_dice = roll_dice, hog.roll_dice
      """,
      'teardown': r"""
      >>> hog.roll_dice = old_roll_dice
      """,
      'type': 'doctest'
    }
  ]
}
