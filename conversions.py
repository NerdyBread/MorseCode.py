class Converter:
	def __init__(self, string: str):
		self.string = string
		self.chars = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ',':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', ' ': '/'}

	def to_english(self) -> str:
		#  TODO make faster
		#  Maybe use the same dictionary but flipped
		new = str()
		for section in self.string.split(' '):
			if section not in self.chars.values():
				new += '?'
			for letter, code in self.chars.items():
				if code == section:
					new += letter
		return new.lower()

	def to_morse(self) -> str:
		new = str()
		for char in self.string.upper():
			new += self.chars.get(char, '?') + ' '
		return new

	def __repr__(self) -> str:
		return f"class {self.__class__.__name__} --> {self.string}"

if __name__ == '__main__':
	new = Converter("- .... .. ... / .--. .-. --- .--- . -.-. - / .. ... / ... .... .. -")
	print(new.to_english())