import process_grades
import pytest


@pytest.mark.parametrize(
        "students, expected",
        [
            ([{'name': 'ana','grades':{90,90,90}}],['ana'])
        ]
)
def test_process_grades_passed(students,expected):
    result = process_grades.process_grades(students)
    assert result['passed'] == expected 



@pytest.mark.parametrize(
    "students, expected",
    [
        ([{'name': 'ana', 'grades': {60,60,60}}], 'ana is in recovery')
    ]
)
def test_process_grades_recovery(students, expected, capsys):
    process_grades.process_grades(students)

    captured = capsys.readouterr()

    assert expected in captured.out