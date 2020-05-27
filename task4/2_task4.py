import re
from mrjob.job import MRJob


class MRExtracting(MRJob):

# getting paragraphs
    def mapper(self, _, line):
        country = line.split("Introduction")[0]
        if (line.find("Natural resources") == -1) or (line.find("Land use") == -1):
            yield country, ''
        else:
            start = line.index("Natural resources")
            end = line.index("Land use")
            yield country, line[start + len("Natural resources"):end]

# deviding by words + _

    def reducer(self, res, country):
        countries = ''
        for i in country:
            countries += " " + i
        res1.write(res + "___________" + countries + "\n")
        yield res, countries





if __name__ == '__main__':
    res1 = open("resources.txt", "w+")
    MRExtracting.run()
