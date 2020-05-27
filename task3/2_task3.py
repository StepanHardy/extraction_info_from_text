import re
from mrjob.job import MRJob


class MRExtracting(MRJob):

# getting paragraphs
    def mapper(self, _, line):
        country = line.split("Introduction")[0]
        if (line.find("International organization") == -1) or (line.find("Diplomatic") == -1):
            yield country, ''
        else:
            start = line.index("International")
            end = line.index("Diplomatic")
            yield line[start + len("International organization participation"):end]

# deviding by words + _
    def reducer(self, country, orgs):
        organizations = ''

        for org in orgs:
            organizations += str(org)
        if (len(organizations) > 0):
            res1.write(country.lower() + str(organizations) + "\n")
            pattern = re.split("[,]", organizations)
            res1.write(country + "\n")
            for i in pattern:
                res1.write(str(i) + '_')


class MRWordCount(MRJob):

    def mapper(self, _, line):
        st = re.split(r'_', line)
        for word in st:
            yield word, 1

    def reducer(self, word, counts):
        res2.write(word + " " + str(sum(counts)) + '\n')


if __name__ == '__main__':
    res1 = open("list_of_org.txt", "w+")
    MRExtracting.run()
    res2 = open("org_countryCount.txt", "w+")
    MRWordCount.run()
