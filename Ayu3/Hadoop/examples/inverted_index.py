from mrjob.job import MRJob
from mrjob.protocol import TextProtocol
import re

WORD_RE = re.compile(r"[\w']+")

class MRWordCountInvertedIndex(MRJob):
    OUTPUT_PROTOCOL = TextProtocol

    def mapper(self, _, line):
        # Parse the input line into words
        words = WORD_RE.findall(line)

        # Emit (word, (doc_id, 1)) for each word in the line
        for word in words:
            yield word.lower(), (self.options.jobconf['map_input_file'], 1)

    def combiner(self, word, counts):
        # Combine the counts for each word locally
        total_count = sum(count for _, count in counts)
        yield word, (list(set(doc_id for doc_id, _ in counts)), total_count)

    def reducer(self, word, counts):
        # Combine the counts globally and emit (word, (doc_id, total_count))
        total_count = sum(count for _, count in counts)
        doc_ids = [doc_id for doc_id, _ in counts]
        yield word, (doc_ids, total_count)

if __name__ == '__main__':
    MRWordCountInvertedIndex.run()

