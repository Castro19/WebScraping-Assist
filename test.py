
course = {
    'receiving': {'courses':
                        [{'courseNumber': 'CHEM 110', 'courseTitle': 'World of Chemistry', 'courseUnits': '4.00'}],
                  'conjunctions': []},
    'sending': {'courses':
                        [{'courseNumber': 'CHEM 2A', 'courseTitle': 'General Chemistry I', 'courseUnits': '3.00'},
                         {'courseNumber': 'CHEM 2AL', 'courseTitle': 'General Chemistry I Laboratory', 'courseUnits': '2.00'},
                         {'courseNumber': 'CHEM 14', 'courseTitle': 'Fundamental Chemistry for Allied Health', 'courseUnits': '3.00'},
                         {'courseNumber': 'CHEM 14L', 'courseTitle': 'Fundamental Chemistry for Allied Health Laboratory', 'courseUnits': '1.00'}],
                'conjunctions':
                        ['AND', 'OR', 'AND']}
}

course2 = {'receiving': {'courses':
                            [{'courseNumber': 'BIO 150', 'courseTitle': 'Diversity and the History of Life', 'courseUnits': '4.00'},
                             {'courseNumber': 'BIO 161', 'courseTitle': 'Introduction to Cell and Molecular Biology', 'courseUnits': '4.00'}],
                        'conjunctions':
                            ['AND']},
            'sending': {'courses' :
                            [{'courseNumber': 'BIOL 2', 'courseTitle': 'Cell and Molecular Biology', 'courseUnits': '4.00'},
                             {'courseNumber': 'BIOL 6', 'courseTitle': 'Plant Biology and Ecology', 'courseUnits': '4.00'},
                             {'courseNumber': 'BIOL 4', 'courseTitle': 'Principles of Evolution and Zoology', 'courseUnits': '4.00'}],
                        'conjunctions':
                            ['AND', 'AND']}
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


a = {
        "conjunction": None,
        "courses": []
    }

# sending = course["sending"]

# print(sending)

# courses = sending["courses"]
# print(courses)
# conj = sending["conjunctions"]
# # print(conj)

# # for i, c in enumerate(courses):
# #     print(c["courseNumber"].replace(" ", ""))
# #     print(conj[i])

# a = [course["courseNumber"].replace(" ", "") for course in courses]

# print(a)

# # print(conj)
# for i, ele in enumerate(conj):
#     a.insert(len(conj) - i, ele)

# print(" ".join(a))
    
# print(a)


# for val in course.values():
#     print(val)



print(course)
# print(template)


for institution, val in course.items():
    courses = []
    has_and = False
    has_or = False
    courses.append(val["courses"][0])
    print(courses)
    if val["conjunctions"]:
        for i, conj in enumerate(val["conjunctions"]):
            if conj == "AND":
                has_and = True
                template[institution]["conjunction"] = "AND"
                if has_or:
                    pass
                else:
                    courses.append(val["courses"][i + 1])
            elif conj == "OR":
                has_or = True
                if has_and:
                    courses.append([val["courses"][i + 1]])
                template[institution]["conjunction"] = "OR"
        # print(courses)

    # else:
    #     template[institution]["conjunction"] = None
    # for k in val.keys():
    #     print(val[k])
    template[institution]["courses"] = courses
    print()

print(template)


for item in template["sending"]["courses"]:
    print(item)