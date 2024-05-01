course = {
    'receiving': {'courses':
                        [{'courseNumber': 'CHEM 110', 'courseTitle': 'World of Chemistry', 'courseUnits': '4.00'}],
                  'conjunctions': []},
    'sending': {'courses': [
                        {'courseNumber': 'CHEM 2A', 'courseTitle': 'General Chemistry I', 'courseUnits': '3.00'},
                        {'courseNumber': 'CHEM 2AL', 'courseTitle': 'General Chemistry I Laboratory', 'courseUnits': '2.00'},
                        {'courseNumber': 'CHEM 14', 'courseTitle': 'Fundamental Chemistry for Allied Health', 'courseUnits': '3.00'},
                        {'courseNumber': 'CHEM 14L', 'courseTitle': 'Fundamental Chemistry for Allied Health Laboratory', 'courseUnits': '1.00'}
                ],
                'conjunctions':
                        ['And', 'Or', 'And']}
}

{
  "receiving": {
        "conjunction": None,
        "courses": [
            {"courseNumber": "CHEM 110", "courseTitle": "World of Chemistry", "courseUnits": "4.00"}
        ]
    },

    "sending": {
        "conjunction": "OR",
        "courses": [
            {
                "conjunction": "AND",
                "courses": [
                    {"courseNumber": "CHEM 2A", "courseTitle": "General Chemistry I", "courseUnits": "3.00"},
                    {"courseNumber": "CHEM 2AL", "courseTitle": "General Chemistry I Laboratory", "courseUnits": "2.00"}
                ]
            },
            {
                "conjunction": "AND",
                "courses": [
                    {"courseNumber": "CHEM 14", "courseTitle": "Fundamental Chemistry for Allied Health", "units": "3.00"},
                    {"courseNumber": "CHEM 14L", "courseTitle": "Fundamental Chemistry for Allied Health Laboratory", "units": "1.00"}
                ]
            }
        ]
    }
}

template = {
    "receiving": {
        "conjunction": None,
        "courses": [
            {}
        ]
    },
  
    "sending": {
        "conjunction": None,
        "courses": [
            {}
        ]
    }
}

course2 = {'Receiving': {'Courses':
                            [{'Course Number': 'BIO 150', 'Course Title': 'Diversity and the History of Life', 'Units': '4.00'},
                             {'Course Number': 'BIO 161', 'Course Title': 'Introduction to Cell and Molecular Biology', 'Units': '4.00'}],
                        'Conjunctions':
                            ['And']},
            'Sending': {'Courses' :
                            [{'Course Number': 'BIOL 2', 'Course Title': 'Cell and Molecular Biology', 'Units': '4.00'},
                             {'Course Number': 'BIOL 6', 'Course Title': 'Plant Biology and Ecology', 'Units': '4.00'},
                             {'Course Number': 'BIOL 4', 'Course Title': 'Principles of Evolution and Zoology', 'Units': '4.00'}],
                        'Conjunctions':
                            ['And', 'And']}}





