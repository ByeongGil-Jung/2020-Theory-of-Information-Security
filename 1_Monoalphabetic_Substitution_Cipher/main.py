from utils import Util


class MonoalphabeticSubstitutionCipher(object):

    CIPHER_TEXT_FILE_PATH = "./cipher_text.txt"
    PLAIN_TEXT_FILE_PATH = "./plain_text.txt"

    def __init__(self):
        self.cipher_text = ""
        self.plain_text = ""
        self.sbox = dict()

    def _get_n_word_count_list(self, text, n):
        n_word_list = list()
        text_list = list(text)

        for i in range(0, len(text_list) - n + 1):
            n_word_list.append("".join(text_list[i:i + n]))

        n_word_count_list = sorted(
            {word: n_word_list.count(word) for word in set(n_word_list)}.items(),
            key=lambda item: item[1],
            reverse=True
        )

        return n_word_count_list

    def decrypt(self):
        word_count_number_max = 15
        cipher_text = self.cipher_text
        plain_text = list(self.cipher_text)

        print("Decryption start")
        """
        Count 결과 :
        [('b', 116), ('n', 103), ('c', 92), ('g', 92), ('z', 90), ('y', 86), ('v', 68), ('i', 65), ('m', 59), ('p', 42),
         ('f', 41), ('x', 38), ('a', 26), ('o', 24), ('r', 23), ('h', 22), ('q', 20), ('j', 19), ('k', 18), ('s', 10), 
         ('d', 9), ('u', 5), ('l', 3), ('t', 2), ('e', 2), ('w', 1)]
        """

        cipher_text_word_count_lists = [self._get_n_word_count_list(text=cipher_text, n=n) for n in range(1, word_count_number_max + 1)]
        for idx, plain_text_word_count_list in enumerate(cipher_text_word_count_lists):
            print(f"Cipher text {idx + 1} word count :\n{plain_text_word_count_list}")

        sbox = {alphabet: alphabet for alphabet in set(cipher_text)}

        # Sbox
        sbox['b'] = 't' #
        sbox['n'] = 'e' #
        sbox['c'] = 'a' #
        sbox['g'] = 'n' #
        sbox['z'] = 'i' #
        sbox['y'] = 'o' #
        sbox['v'] = 's' #
        sbox['i'] = 'r' #
        sbox['m'] = 'c' #
        sbox['p'] = 'h' #

        sbox['f'] = 'l' #
        sbox['x'] = 'd' #
        sbox['a'] = 'u' #
        sbox['o'] = 'f' #
        sbox['r'] = 'b' #
        sbox['h'] = 'p' #
        sbox['q'] = 'm' #
        sbox['j'] = 'w' #
        sbox['k'] = 'y' #
        sbox['s'] = 'k' #

        sbox['d'] = 'g' #
        sbox['u'] = 'v' #
        sbox['l'] = 'z' #
        sbox['t'] = 'x' #
        sbox['e'] = 'j' #
        sbox['w'] = 'q' #

        is_alphabet_changed_list = [False for _ in range(len(cipher_text))]

        for idx, alphabet in enumerate(plain_text):
            if not is_alphabet_changed_list[idx]:

                plain_text[idx] = sbox[cipher_text[idx]]

                is_alphabet_changed_list[idx] = True

        self.sbox = sbox
        self.plain_text = "".join(plain_text)

        print("=======================================================================================================")
        print("Decryption Finished")

        plain_text_word_count_lists = [self._get_n_word_count_list(text=plain_text, n=n) for n in range(1, word_count_number_max + 1)]
        for idx, plain_text_word_count_list in enumerate(plain_text_word_count_lists):
            print(f"Plain text {idx + 1} word count :\n{plain_text_word_count_list}")


def main():
    msc = MonoalphabeticSubstitutionCipher()
    msc.cipher_text = Util.load(file_path=MonoalphabeticSubstitutionCipher.CIPHER_TEXT_FILE_PATH)
    msc.decrypt()

    cipher_text = msc.cipher_text
    plain_text = msc.plain_text

    print("=======================================================================================================")
    print(f"Cipher Text :\n{cipher_text}")
    print(f"Plain Text :\n{plain_text}")
    Util.save(file_path=MonoalphabeticSubstitutionCipher.PLAIN_TEXT_FILE_PATH, data=plain_text)


if __name__ == "__main__":
    main()
