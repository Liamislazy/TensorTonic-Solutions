class SimpleTokenizer:
    def __init__(self):
        self.word_to_id = {}
        self.id_to_word = {}
        self.vocab_size = 0
        self.pad_token = "<PAD>"
        self.unk_token = "<UNK>"
        self.bos_token = "<BOS>"
        self.eos_token = "<EOS>"

    def build_vocab(self, texts: list[str]) -> None:
        """
        Builds the vocabulary in place.
        """
        self.word_to_id[self.pad_token] = 0
        self.word_to_id[self.unk_token] = 1
        self.word_to_id[self.bos_token] = 2
        self.word_to_id[self.eos_token] = 3

        self.id_to_word[0] = self.pad_token
        self.id_to_word[1] = self.unk_token
        self.id_to_word[2] = self.bos_token
        self.id_to_word[3] = self.eos_token
        
        words = sorted({word for text in texts for word in text.lower().split()})
        
        for index, word in enumerate(words, start=4):
            self.word_to_id[word] = index
            self.id_to_word[index] = word
            
        self.vocab_size = len(self.word_to_id)

    def encode(self, text: str) -> list[int]:
        """
        Returns token IDs for the input text.
        """
        encoded_text = []
        words = [word.lower() for word in text.split()]
        for word in words:
            if word in self.word_to_id:
                encoded_text.append(self.word_to_id[word])
            else:
                encoded_text.append(1)
        return encoded_text

    def decode(self, ids: list[int]) -> str:
        """
        Returns the decoded, space-separated text.
        """
        decoded_text = " ".join(self.id_to_word.get(index, "<UNK>") for index in ids)
        return decoded_text