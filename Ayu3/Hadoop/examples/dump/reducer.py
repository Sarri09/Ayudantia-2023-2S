from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"[\w']+")

class MRWordCountInvertedIndex(MRJob):

    def mapper(self, _, line):
        doc_id = self.options.input_file.split('/')[-1]

        for word in WORD_RE.findall(line):
            # Emitir resultados del mapper
            print(f'Mapper: ({word.lower()}, ({doc_id}, 1))')
            yield (word.lower(), (doc_id, 1))

    def combiner(self, word, doc_counts):
    	total_count = sum(count for doc, count in doc_counts)
    
    	# Utilizar una lista de comprensión en lugar de un generador
    	result_list = [(doc, total_count) for doc, count in doc_counts]

    	# Emitir resultados del combiner
    	print(f'Combiner: ({word}, {result_list})')
    	yield (word, result_list)


    def reducer(self, word, doc_counts):
        inverted_index = {}
        for doc, count in doc_counts:
            inverted_index.setdefault(doc, []).append(count)
        
        # Emitir resultados del reducer
        print(f'Reducer: ({word}, {inverted_index})')
        yield (word, inverted_index)

if __name__ == '__main__':
    MRWordCountInvertedIndex.run()

