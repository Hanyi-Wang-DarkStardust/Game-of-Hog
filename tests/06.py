test = {
  'name': 'Question 6',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> #
          >>> def echo(s0, s1):
          ...     print(s0, s1)
          ...     return echo
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(3), goal=4, say=echo)
          d7882c94106188a2f424c5383b507923
          b706c6a1e63c19ed82e4eb95fc6ba1cf
          519a2e7c2e74bf29cb97b470402b22a2
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> #
          >>> def echo(s0, s1):
          ...     print(s0, s1)
          ...     return echo
          >>> s0, s1 = play(always_roll(0), always_roll(3), dice=make_test_dice(4, 2, 4), goal=15, say=echo)
          46384f1b91067efe2db7061edf72cafa
          253a8c4696c85daa9dc16cd817029432
          d4513cc251c0704adcba2a6aadd09d6b
          f19614cf9d63416a5804877d1ce54922
          a2c850553746865cf4988fa443de9287
          66df447fe530de7e49eb39945c42ae04
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> #
          >>> # Ensure that say is properly updated within the body of play.
          >>> def total(s0, s1):
          ...     print(s0 + s1)
          ...     return echo
          >>> def echo(s0, s1):
          ...     print(s0, s1)
          ...     return total
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(2, 3), goal=5, say=echo)
          accd0f5c57e0f3fad13791aaecafc38b
          26f5762c932a578994ea1c8fc7fa6c02
          e3bcdb2715b868db45692ec2a5971a84
          70e71b420a966665c548a3bb2cb30d7d
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import play, always_roll
      >>> from dice import make_test_dice
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> #
          >>> def echo_0(s0, s1):
          ...     print('*', s0)
          ...     return echo_0
          >>> def echo_1(s0, s1):
          ...     print('**', s1)
          ...     return echo_1
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(2), goal=1, say=both(echo_0, echo_1))
          3f321d5ce997d2f3989685f56de8bdce
          4a64fe964dc771a219ed773c3a146c75
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> #
          >>> s0, s1 = play(always_roll(3), always_roll(3), dice=make_test_dice(1, 2, 3, 3), goal=8, say=both(say_scores, announce_lead_changes()))
          Player 0 now has 1 and Player 1 now has 0
          Player 0 takes the lead by 1
          Player 0 now has 1 and Player 1 now has 1
          Player 0 now has 2 and Player 1 now has 1
          Player 0 takes the lead by 1
          Player 0 now has 2 and Player 1 now has 9
          Player 1 takes the lead by 7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> #
          >>> s0, s1 = play(always_roll(0), always_roll(1), goal=8, dice=make_test_dice(2), say=both(say_scores, announce_lead_changes()))
          Player 0 now has 1 and Player 1 now has 0
          Player 0 takes the lead by 1
          Player 0 now has 1 and Player 1 now has 2
          Player 1 takes the lead by 1
          Player 0 now has 2 and Player 1 now has 2
          Player 0 now has 2 and Player 1 now has 4
          Player 1 takes the lead by 2
          Player 0 now has 3 and Player 1 now has 4
          Player 0 now has 3 and Player 1 now has 6
          Player 0 now has 4 and Player 1 now has 6
          Player 0 now has 4 and Player 1 now has 8
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import play, always_roll, both, announce_lead_changes, say_scores
      >>> from dice import make_test_dice
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
