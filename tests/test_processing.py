import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "info_state, state_id, expected",
    [
(
      [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
      ],
      'EXECUTED',
      [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}]
    ),
(
      [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
      ],
      'CANCELED',
      [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
      ]
    ),
(
      [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"}
      ],
      'CANCELED',
      [
      ]
    )
    ]
)
def test_filter_by_state(info_state, state_id, expected):
    assert filter_by_state(info_state, state_id) == expected


@pytest.mark.parametrize(
    "info_list, revers_list, expected",
    [
(
      [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
      ],
      'date',
      [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
       {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
       {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}
       ]
       ),
(
      [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
      ],
      'date',
      [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}
      ]
    )
    ],
)
def test_sort_by_date(info_list, revers_list, expected):
    assert sort_by_date(info_list, revers_list) == expected
