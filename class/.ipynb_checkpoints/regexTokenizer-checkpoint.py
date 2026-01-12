import regex as re
import pickle

SPLIT_PATTERN = r"""'(?i:[sdmt]|ll|ve|re)|[^\r\n\p{L}\p{N}]?+\p{L}+|\p{N}{1,2}| ?[^\s\p{L}\p{N}]++[\r\n]*|\s*[\r\n]|\s+(?!\S)|\s+"""

def get_pair(ids, counts):
    for pair in zip(ids, ids[1:]):
        counts[pair] = counts.get(pair, 0) + 1
    return counts

def merge(ids, pair, index):
    '''
    This function will iterate over ids and every time
    it sees a instance of pair, it will take that pair
    and instead put index , then it will return the list
    merge()
    list = [1,2, 3, 4, 1, 2]
    merge(list, (1,2). 257)
    list = [257, 3, 4, 257, 3]
    '''

    new_ids = []
    i = 0
    while i < len(ids):
        if i <len(ids) - 1 and  (ids[i], ids[i+1]) == pair:
            new_ids.append(index)
            i += 2
        else:
            new_ids.append(ids[i])
            i += 1
    return new_ids

class regexTokenizer:

    def __init__(self, vocab_size, pattern):
        
        self.vocab_size = vocab_size
        self.vocabulary = {i : bytes([i]) for i in range(256)}
        self.merges = {}
        self.pattern = re.compile(pattern)

    def train(self, text, verbose = False):
        # Encode the text
        # Iterate over text, self.vocab_size - 256 times
        # count all of the pairs in a dictionary
        # choose the pair with the highest frequency
        # merge that pair as a new token
        # add that token to the vocab
        # {256: byte_string}
        # add to self.merges = {byte_string: 256}
        
        assert self.vocab_size > 256
        number_merges = self.vocab_size - 256

        text_chunks = re.findall(self.pattern, text)
        encoded_chunks = [list(text_chunk.encode('utf-8')) for text_chunk in text_chunks]

        length_initial = sum([len(encoded_chunk) for encoded_chunk in encoded_chunks])

        for i in range(number_merges):
            pairs = {}
            for encoded_chunk in encoded_chunks:
                pairs = get_pair(encoded_chunk, pairs)

            pair = max(pairs, key = pairs.get)
            index = 256 + i
            encoded_chunks = [merge(encoded_chunk,pair,index) for encoded_chunk in encoded_chunks]
            self.merges[pair] = index
            self.vocabulary[index] = self.vocabulary[pair[0]] + self.vocabulary[pair[1]]
            print(sorted( [(v, k) for k,v in pairs.items()], reverse = True) [:10])

        if verbose:
            length_final = sum([len(encoded_chunk) for encoded_chunk in encoded_chunks])
            compression = length_initial/length_final
            print(length_initial, length_final)
            print(compression)

    def encode(self, text):

        text_chunks = re.findall(self.pattern, text)
        encoded_text = []

        for text_chunk in text_chunks:
            encoded_chunk = self.encode_chunk(text_chunk)
            encoded_text.extend(encoded_chunk)
        return encoded_text

    def encode_chunk(self, text):
        '''
        self.merges is important here
        
        we get text, and then we convert that text to byte strings, then to integers
        and then we iterate over the text until all pairs of
        merges that are possible under the trained tokenizer
        have been completed

        '''

        ids = list(text.encode('utf-8'))
        
        for pair, index in self.merges.items():
            ids = merge(ids, pair, index)

        return ids

    def decode(self, ids):
        '''
        decode gets ids 
        1. convert the ids to their byte strings
        2. convert the byte strings to strings via the vocabulary
        3. then return the decoded_text
        '''

        byte_strings = b''.join([bytes(self.vocabulary[i]) for i in ids])
        decoded_text =  byte_strings.decode('utf-8')
        return decoded_text
    
    def save(self, path):
        with open(path, "wb") as file:
            pickle.dump(
                {
                    "merges": self.merges,
                    "vocabulary": self.vocabulary,
                    "pattern": self.pattern
                },
                file
            )

    @classmethod
    def load(cls, path):
        tokenizer = cls(300, SPLIT_PATTERN)

        with open(path , "rb") as file:
            data = pickle.load(file)
            tokenizer.merges = data["merges"]
            tokenizer.vocabulary = data["vocabulary"]
            tokenizer.pattern = data["pattern"]
        return tokenizer


tokenizer = regexTokenizer(300, SPLIT_PATTERN)
text = "Ｕｎｉｃｏｄｅ! 🅤🅝🅘🅒🅞🅓🅔‽ 🇺‌🇳‌🇮‌🇨‌🇴‌🇩‌🇪! 😄 The very name strikes fear and awe into the hearts of programmers worldwide. We all know we ought to “support Unicode” in our software (whatever that means—like using wchar_t for all the strings, right?). But Unicode can be abstruse, and diving into the thousand-page Unicode Standard plus its dozens of supplementary annexes, reports, and notes can be more than a little intimidating. I don’t blame programmers for still finding the whole thing mysterious, even 30 years after Unicode’s inception."
tokenizer.train(text, True) 
tokenizer.save("tokenizer.pkl")

tokenizer_load = tokenizer.load("tokenizer.pkl")

print(tokenizer_load.decode(tokenizer_load.encode("are hello")))