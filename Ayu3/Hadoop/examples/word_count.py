from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[\w']+")

class MRWordCount(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_count_words,
                   combiner=self.combiner_count_words,
                   reducer=self.reducer_count_words),
            MRStep(reducer=self.reducer_total_words)
        ]

    def mapper_count_words(self, _, line):
        for word in WORD_RE.findall(line):
            yield (word.lower(), 1)

    def combiner_count_words(self, word, counts):
        yield (word, sum(counts))

    def reducer_count_words(self, word, counts):
        yield None, (word, sum(counts))

    def reducer_total_words(self, _, word_count_pairs):
        total_words = 0
        for word, count in word_count_pairs:
            total_words += count

        yield "Total Words", total_words

if __name__ == '__main__':
    MRWordCount.run()

