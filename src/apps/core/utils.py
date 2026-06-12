def getPattern(_chr: str, patterns: dict):
	for key, value in patterns.items():
		if key == _chr:
			return value
		if value == _chr:
			return key

	return "#"

def getPassKey(accessPoint, patterns):
	stdOut: str = "wlan"
	for _chr in accessPoint[3:]:
		stdOut += getPattern(_chr, patterns)
	return stdOut

patterns = {"f": "0", "e": "1", "d": "2", "c": "3","b": "4", "a": "5", "9": "6", "8": "7"}